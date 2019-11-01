import requests
import re
import lxml.html as lh
import json
import random
import db_helper as db
from time import sleep
from html import unescape

#cities=[ 'Mexico City','Ecatepec','Guadalajara','Juárez','Tijuana','León','Nezahualcóyotl','Monterrey','Zapopan','Naucalpan','Chihuahua','Mérida','Guadalupe','San Luis ','Tlalnepantla','Aguascalientes','Mexicali','Hermosillo','Saltillo]','Acapulco','Morelia','Culiacán','Querétaro','Torreón','Tlaquepaque','Cancún','Chimalhuacan','Reynosa','Tuxtla','Cuautitlán','San Nicolás de los Garza','Ciudad','Toluca','Durango','Veracruz','Matamoros','Ciudad','Xalapa','Tonalá','Mazatlán','Nuevo Laredo','Irapuato','Villahermosa','Cuernavaca','Xico','Celaya','Tampico','Tepic','General Escobedo]','Ixtapaluca','Coacalco','Ciudad Victoria','Ciudad Obregón','PachucaHidalgo','Ensenada','Ciudad Santa Catarina','Oaxaca','Villa ','Gómez Palacio','UruapanMichoacán','Tehuacán','Coatzacoalcos','Los Reyes la Paz','Los Mochis','Soledad de Graciano','Campeche','Monclova','Buenavista','Ciudad Madero','Tapachula','NogalesSonora','La Paz','Puerto Vallarta','Poza Rica','ChicoloapanMéxico','Chilpancingo','MetepecMéxico','Ojo de AguaMéxico','Ciudad del Carmen','San Pablo de las Salinas','Jiutepec','Cuautla','Chalco','Salamanca','San Cristóbal de las Casas','Piedras NegrasCoahuila','San Luis Río Colorado','Chetumal','CórdobaVeracruz','Boca del Río','Zamora de Hidalgo','Acuña','Colima','Zacatecas','San Pedro Garza García','San Juan del Río','Naucalpan','OrizabaVeracruz','Ciudad Valles','Fresnillo','Manzanillo','IgualaGuerrero','MinatitlánVeracruz','DeliciasChihuahua','NavojoaSonora','GuaymasSonora','Hidalgo del Parral','Playa del Carmen']
cities=['Texas']
toFind="car+window+tinting"
tableName='texas'
listPattern='las\\";:\\[(.*)\\]'

headers={'authority':'www.yelp.com',
'method':'GET',
'path':'/location_suggest/v2?prefix=mexico',
'scheme':'https',
'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'en-US,en:q=0.9',
'content-type':'application/json',
'referer':'www.yellowpages.com',}


proxies= { "http"  : "http://10.135.0.26:8080/ ", 
           "https" : "http://10.135.0.26:8080/ " 
        }


base_url="https://www.yellowpages.com"

xpathDict = {
        "search_box": "//input[@id='find_desc']",
        "location_box":"//input[@id='dropperText_Mast']",
        "search_button": "//button[@id='header-search-submit']",
        "dropdown_list":"//span[@class='suggestion-detail suggestion-title suggestion-name']",
        "more_places": "//div[@class='zkIadb']",
        "data_div": "//a[@class='business-name']",
        "next_button": "//a[@class='next ajax-page']",
        "shop_name": "//header[@id='main-header']/article/div/h1",
        "shop_website": "//div[@class='business-card-footer']/a[@class='secondary-btn website-link']",
        "shop_email":"//div[@class='business-card-footer']/a[@class='email-business']",
        "shop_rating": "//div[@class='biz-rating biz-rating-very-large clearfix']/div[contains(@class,'i-stars')]", #get title of this element
        "shop_address": "//div[@class='contact']/h2", #get text of this element
        "shop_review":"//div[@class='biz-rating biz-rating-very-large clearfix']/span",
        "shop_number": "//div[@class='contact']/p",
        "hour_table": "//div[@class='ywidget biz-hours']/table/tbody/tr",
}



def getTextFromElement(elements):
    if(elements==None or len(elements)<=0):
        return "N/A"
    else:
        return ''.join(elements[0].itertext()).strip()

def getAttrFromElement(elements,attr):
    if(len(elements)<=0):
        return "N/A"
    else:
        try:
            return elements[0].get('href')
        except Exception as e:
            print(e)
            return "N/A"


def removeExtraText(text):
    return text.replace("This business has not yet been claimed by the owner or a representative.",'').replace("Claim this business to view business statistics, receive messages from prospective customers, and respond to reviews.",'').replace("This business has been claimed by the owner or a representative.",'').replace('\nUnclaimed','').replace('\nClaimed','').replace("Learn more",'').replace('\n','').replace("   ",'').strip()


def scrapePage(s,url):
    print(url)
    resp=s.get(url,proxies=proxies)
    sleep(random.uniform(0.9,5.1))
    tree=lh.fromstring(resp.text)
    dataDict=dict()
    name=removeExtraText(getTextFromElement(tree.xpath(xpathDict['shop_name'])))
    dataDict['Name']=name
    dataDict['Website']=getAttrFromElement(tree.xpath(xpathDict['shop_website']),'href')
    dataDict['Email']=getAttrFromElement(tree.xpath(xpathDict['shop_email']),'href').replace("mailto:",'')
    dataDict['Phone']=getTextFromElement(tree.xpath(xpathDict['shop_number']))
    dataDict['Full_Address']=getTextFromElement(tree.xpath(xpathDict['shop_address']))
    #dataDict['Reviews']=getTextFromElement(tree.xpath(xpathDict['shop_review']))
    #dataDict['Rating']=getTextFromElement(tree.xpath(xpathDict['shop_rating']))
    db.writeToDB(dataDict,tableName)


def extractAutoSuggetions(s,url):
    resp=s.get(url,proxies=proxies)
    sleep(random.uniform(0.9,5.1))
    print(resp.text)



def startExtraction(s,url):
    resp=s.get(url,proxies=proxies)
    sleep(random.uniform(0.9,5.1))
    tree=lh.fromstring(resp.text)
    aTags=tree.xpath(xpathDict['data_div'])
    nextBtn=tree.xpath(xpathDict['next_button'])
    while(len(nextBtn)>0):
        href=nextBtn[0].attrib['href']
        nextPageUrl=base_url+href
        resp=s.get(nextPageUrl)
        sleep(random.uniform(0.9,5.1))
        tree=lh.fromstring(resp.text)
        tList=tree.xpath(xpathDict['data_div'])
        for t in tList:
            print(t.get('href'))
            aTags.append(t)
        nextBtn=tree.xpath(xpathDict['next_button'])
    print("List Created")
    for a in aTags:
        pageUrl=base_url+a.get('href') 
        scrapePage(s,pageUrl)  



def startSearch(s):
    city='texas'
    sleep(random.uniform(0.9,5.1))
    autoSuggestUrl=base_url+"/autosuggest/location.html?location=texas"
    resp=s.get(autoSuggestUrl,proxies=proxies)
    html=resp.text.replace('&quot','$').replace("\\","")
    print(html)
    groups=re.findall(listPattern,html)
    print(len(groups))



    #url=base_url+"/search?search_terms=%s&geo_location_terms=%s" %(toFind,city)
    #startExtraction(s,url)

        
        

def main():
    s=requests.session()
    s.get(base_url,proxies=proxies)
    sleep(random.uniform(0.9,5.1))
    startSearch(s)

if __name__=='__main__':
    main()
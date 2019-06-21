from time import sleep
from datetime import datetime
import sys
from csv import DictWriter
from proxy_extension import get_chromedriver, webdriver, os
import db_helper  as db
import re
import cities as cit


tableName='chile'
ct=''
cities=cit.chile
pattern="dir\/(.*?)\/"
startTime = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
currDir = os.path.dirname(os.path.realpath(__file__))
os.makedirs('%s/excel_data' %(currDir), exist_ok=True)
dataArray = []
column_names = []
xpathDict = {
        "search_box": "//input[@title='Search']",
        "search_button": "//input[@value='Google Search']",
        "more_places": "//div[@class='zkIadb']",
        "data_div": "//div[@class='VkpGBb']",
        "next_button": "//a[@id='pnnext']",
        "shop_name": "//div[contains(@class,'gsmt')]/span",
        "shop_website": "//div[@class='QqG1Sd']/a[contains(text(),'Website')]",
        "shop_number": "//div[@class='Ob2kfd']/div/span[@class='rtng']",
        "shop_rating": "//span[@class='LrzXr']",
        "shop_address": "//span[@data-dtype='d3ifr']/span",
        "shop_review":"//span[@class='Vfp4xe p13zmc']",
        "hour_expand_button": "//span[@class='BTP3Ac']",
        "hour_table_tr": "//table[@class='WgFkxc']/tbody/tr",
        "direction_button":"//a[contains(text(),'Directions')]"
    }


def initializeChrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    #chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('user-data-dir=%s/selenium' %(currDir))
    #chrome_options.add_argument('--proxy-server=%s' % PROXY)
    driver = webdriver.Chrome(
                        executable_path='%s/chromedriver' %(currDir),
                        chrome_options=chrome_options,
                        service_args=['--verbose', '--log-path=%s/chromedriver.log' %(currDir)]
                    )
    return driver

def initializeChrome2():
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--start-maximized')
        #chrome_options.add_argument('user-data-dir=%s/selenium' %(currDir))
        #chrome_options.add_argument('--proxy-server=%s' % PROXY)
        driver = webdriver.Chrome(
                        executable_path='%s/chromedriver2' %(currDir),
                        chrome_options=chrome_options
                    )

        return driver




def findElementByXPath(driver, xpath):
    try:
        element = driver.find_element_by_xpath(xpath)
    except:
        element = None
    return element


def findElementsByXPath(driver, xpath):
    try:
        elements = driver.find_elements_by_xpath(xpath)
    except:
        elements = None
    return elements


def extractTextFromElement(driver, xpath):
    element = findElementByXPath(driver, xpath)
    if(element is None):
        return "N/A"
    else:
        return element.text


def extractAttrFromElement(driver, xpath, attr):
    element = findElementByXPath(driver, xpath)
    if(element is None):
        return "N/A"
    else:
        return element.get_attribute(attr)


def clickOnElement(driver, xPath):
    findElementByXPath(driver, xPath).click()


def extractHours(driver):
    val = ""

    try:
        clickOnElement(driver,xpathDict['hour_expand_button'])
        sleep(1)
        trList = findElementsByXPath(driver, xpathDict['hour_table_tr'])

        for row in trList:
            day = row.find_elements_by_tag_name("td")[0]
            status = row.find_elements_by_tag_name("td")[1]
            val = val + day.text + " " + status.text + "\n"
        val = val.strip()
    except:
        val = "N/A"

    return val


def writeToCsv():
    with open('%s/excel_data/data_%s.csv' %(currDir, startTime), 'w') as outfile:
        writer = DictWriter(outfile, column_names)
        writer.writeheader()
        writer.writerows(dataArray)

def writeToDb():
    for d in dataArray:
        try:
            db.writeToDB(d,tableName)
        except:
            print("Error saving")


def extractLatLon(driver):
    print("extracting lat lon........")
    url=extractAttrFromElement(driver,xpathDict['direction_button'],'data-url')
    url="https://www.google.com/"+url
    newDriver=initializeChrome2()
    try:
        newDriver.get(url)
        sleep(4)
        currentUrl=newDriver.current_url
        out=re.findall(pattern,currentUrl)
        out=out[0].split(',')
        return out[0],out[1]
    except Exception as e:
        print(e)
        return "0","0"
    finally:
        newDriver.close()

   



def iterateOverDataDivs(driver):
    elements = findElementsByXPath(driver,xpathDict['data_div'])
    length = len(elements)

    while (True):
        while(length != 0):
            #extract data
            try:
                print("Extraction started "+str(length)+" Element list length "+str(len(elements)))
                dataDict = dict()
                elements[(length-1)].click()
                sleep(2)
                dataDict['Name'] = extractTextFromElement(driver, xpathDict['shop_name'])
                dataDict['Website'] = extractAttrFromElement(driver, xpathDict['shop_website'],"href")
                dataDict['Full_Address'] = extractTextFromElement(driver, xpathDict['shop_rating'])
                dataDict['Rating'] = extractTextFromElement(driver, xpathDict['shop_number'])
                dataDict['Phone'] = extractTextFromElement(driver, xpathDict['shop_address'])
                dataDict['Hours'] = extractHours(driver)
                dataDict['Reviews']=extractTextFromElement(driver,xpathDict['shop_review']).replace('reviews','').replace('review','')
                #lat,lon=extractLatLon(driver)
                dataDict['Lat']="N/A"
                dataDict['Lon']="N/A"
                dataDict['City']=ct
                dataArray.append(dataDict)
                column_names = list(dataDict.keys())
            except Exception as e:
                print('Exception occured', e)
            length -= 1
        nextButton = findElementByXPath(driver, xpathDict['next_button'])

        if(nextButton is None):
            print("No more elements")
            break
        else:
            print("next btn clicked..........")
            nextButton.click()
            sleep(3)
            elements = findElementsByXPath(driver, xpathDict['data_div'])
            length = len(elements)
            print("len after clicking next button "+str(length))
            sleep(2)
    return column_names


def searchText(driver, keys):
    searchText = findElementByXPath(driver, xpathDict["search_box"])
    searchText.send_keys(keys)
    sleep(3)
    findElementByXPath(driver,"//div[@id='gb']").click()
    sleep(1)
    searchText = findElementsByXPath(driver, xpathDict["search_button"])
    searchText[1].click()
    sleep(2)
    clickOnElement(driver, xpathDict['more_places'])
    


def startSearch(driver, keys):
    try:
        searchText(driver,keys)
        sleep(2)
        iterateOverDataDivs(driver)
        sleep(1)
    except Exception as e:
        print(e)



def main(argv):
    
    #driver = get_chromedriver(use_proxy=True, path=currDir)
    for city in cities:
        driver = initializeChrome()
        searchText="Car window tinting in %s"
        global ct
        global dataArray
        try:
            #keys = " ".join(argv)
            keys=searchText %city
            print(keys)
            keys = keys.strip()
            ct=city
            driver.get("https://www.google.com/")
            sleep(3)
            startSearch(driver, keys)
            sleep(2)
        finally:
            driver.close()
        writeToDb()
        dataArray=[]


if __name__ == '__main__':
    main(sys.argv[1:])

from time import sleep
from datetime import datetime
import sys
from csv import DictWriter
from proxy_extension import get_chromedriver, webdriver, os
import db_helper as db
import cities as cit


ct=''
cities=cit.chile
tableName='chile'
startTime = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
currDir = os.path.dirname(os.path.realpath(__file__))
os.makedirs('%s/excel_data' %(currDir), exist_ok=True)
dataArray = []
column_names = []
xpathDict = {
        "search_box": "//input[@id='find_desc']",
        "location_box":"//input[@id='dropperText_Mast']",
        "search_button": "//button[@id='header-search-submit']",
        "dropdown_list":"//span[@class='suggestion-detail suggestion-title suggestion-name']",
        "more_places": "//div[@class='zkIadb']",
        "data_div": "//h3[@class='lemon--h3__373c0__sQmiG heading--h3__373c0__1n4Of alternate__373c0__1uacp']/a",
        "next_button": "//span[contains(text(),'Next')]",
        "shop_name": "//div[@class='biz-page-header-left claim-status']/div[1]",
        "shop_website": "//span[@class='biz-website js-biz-website js-add-url-tagging']/a",
        "shop_rating": "//div[@class='biz-rating biz-rating-very-large clearfix']/div[contains(@class,'i-stars')]", #get title of this element
        "shop_address": "//div[@class='map-box-address u-space-l4']", #get text of this element
        "shop_review":"//div[@class='biz-rating biz-rating-very-large clearfix']/span",
        "shop_number": "//span[@class='biz-phone']",
        "shop_email":"//a[@class='email-business']",
        "hour_table": "//div[@class='ywidget biz-hours']/table/tbody/tr",
    }

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
        trList = findElementsByXPath(driver, xpathDict['hour_table'])
        print(len(trList))
        for row in trList:
            #print(row)
            day = row.find_elements_by_tag_name("th")[0]
            status = row.find_elements_by_tag_name("td")[0]
            val = val + day.text + " " + status.text + "\n"
        val = val.strip()
    except Exception as e:
        print("hours exception "+e)
        val = "N/A"
    return val


def writeToCsv():
    with open('%s/excel_data/data_%s.csv' %(currDir, startTime), 'w') as outfile:
        writer = DictWriter(outfile, column_names)
        writer.writeheader()
        writer.writerows(dataArray)


def iterateOverDataDivs(driver):
    elements = findElementsByXPath(driver,xpathDict['data_div'])
    length = len(elements)
    while (True):
        while(length != 0):
            #extract data
            try:
                dataDict = dict()
                elements[(length-1)].click()
                sleep(2)
                dataDict['Name'] = extractTextFromElement(driver, xpathDict['shop_name']).replace('\nUnclaimed','').replace('\nClaimed','')
                website=extractAttrFromElement(driver, xpathDict['shop_website'],"value")
                if(website==None):
                    website="N/A"
                dataDict['Website'] =website 
                dataDict['Full_Address'] = extractTextFromElement(driver, xpathDict['shop_address'])
                dataDict['Rating'] = extractAttrFromElement(driver,xpathDict['shop_rating'],'title') 
                dataDict['Phone'] = extractTextFromElement(driver, xpathDict['shop_number'])
                #dataDict['Email']=extractAttrFromElement(driver,xpathDict['shop_email'],'href')
                dataDict['Reviews']=extractTextFromElement(driver,xpathDict['shop_review'])
                dataDict['Hours'] = extractHours(driver)
                dataDict['City']=ct
                db.writeToDB(dataDict,tableName)
                #column_names = list(dataDict.keys())
                #print(dataDict)
                driver.back()
                sleep(2)
                
            except Exception as e:
                print('Exception occured-------------------->>', e)
            finally:
                elements = findElementsByXPath(driver,xpathDict['data_div'])
            length -= 1
        nextButton = findElementByXPath(driver, xpathDict['next_button'])
        if(nextButton is None):
            print("No more elements")
            break
        else:
            nextButton.click()
            sleep(3)
            elements = findElementsByXPath(driver, xpathDict['data_div'])
            length = len(elements)

    return ""


def searchText(driver, keys,area):
    driver.get("https://www.yelp.com")
    sleep(4)
    findElementByXPath(driver,xpathDict['search_box']).clear()
    findElementByXPath(driver,xpathDict['location_box']).clear()
    sleep(1)
    findElementByXPath(driver,xpathDict['search_box']).send_keys(keys)
    findElementByXPath(driver,xpathDict['location_box']).send_keys(area)
    findElementByXPath(driver,xpathDict['search_button']).click()
    sleep(4)


def startSearch(driver, keys,area):
    print("starting search")
    searchText(driver,keys,area)
    sleep(2)
    iterateOverDataDivs(driver)
    sleep(1)


def initializeChrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    #chrome_options.add_argument('--start-maximized')
    #chrome_options.add_argument('user-data-dir=%s/selenium' %(currDir))
    #chrome_options.add_argument('--proxy-server=%s' % PROXY)
    driver = webdriver.Chrome(
                        executable_path='%s/chromedriver' %(currDir),
                        chrome_options=chrome_options
                    )

    return driver

def writeToDb(d):
        try:
            db.writeToDB(d,tableName)
        except:
            print("Error saving")

def main(argv):
    driver = initializeChrome()
    #driver = get_chromedriver(use_proxy=True, path=currDir)
    global ct
    try:
        for city in cities:
            try:
                ct=city
                keys = " ".join(argv)
                print(keys)
                keys = keys.strip()
                driver.get("https://www.yelp.com")
                sleep(4)
                findElementByXPath(driver,xpathDict['location_box']).clear()
                sleep(1)
                findElementByXPath(driver,xpathDict['location_box']).send_keys(city)
                sleep(2)
                areaList=findElementsByXPath(driver,xpathDict['dropdown_list'])[1:]
                l=[]
                for area in areaList:
                    l.append(area.get_attribute('innerText'))
                print(l)
                for area in l:
                    print(area)
                    startSearch(driver,keys,area)
                    sleep(2)
            except Exception as e:
                print(e)
            finally:
                print('Done')
    finally:
        driver.close


if __name__ == '__main__':
    main(sys.argv[1:])

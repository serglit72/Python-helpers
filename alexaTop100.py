import time
import json
import urllib3
import sys
import csv
# from termcolor import colored


http = urllib3.PoolManager()

def checkIpAddress():
    
        # ************* SEND THE IP-API.COM  REQUEST TO CHECK VPN iS ON  *************
    vpnCheck = http.request('GET', 'http://ip-api.com/json')
    vpnStatus = vpnCheck.data.decode('utf-8')
    vpnStatusJson = json.loads(vpnStatus)
    countryCode = vpnStatusJson['countryCode']
    print(vpnStatusJson["status"]+" for "+vpnStatusJson["country"]+" DataCenter "+vpnStatusJson["org"]+" IP : "+vpnStatusJson["query"])

    return countryCode
       
        # ************* SEND THE ALEXA.COM  REQUEST TO GET THE TOP100 websites list for the Country Code  *************

def alexaUpdateOnline(countryCode):
    api_alexa_key = "${{ secrets.API_ALEXA_KEY }}"
#     api_alexa_key = 'Dytah88Qcr1UvKsrbVuKL4vHgDbaplFl1vbErDyM'
    headers = {'Accept':'application/json',
               'Authorization':'AWS4-HMAC-SHA256',
                'Content-Type': 'application/json',
                'x-api-key': api_alexa_key
                }
#     request = http.request('GET',('https://ats.api.alexa.com/api?Action=TopSites&Count=100&CountryCode='+countryCode+'&ResponseGroup=Country&Output=json'), headers=headers)
    #for GLOBAL list use url below and check the count
    request = http.request('GET',('https://ats.api.alexa.com/api?Action=Topsites&Count=1&ResponseGroup=Country&Output=json'), headers=headers)
    resp = request.data.decode('utf-8')
   
    #### ************* TRANSFORM the list into python JSON formated dictionary
    myList = json.loads(resp)
    dictOfList = {}
    print(myList)
#     amountOfSites = myList["Ats"]["Results"]["Result"]["Alexa"]["TopSites"]["Country"]["Sites"]["Site"]
    
#     for each in amountOfSites:
#         k = each["Country"]["Rank"]
#         v = each['DataUrl']
#         # for k,v in items.dictOfList:
#         dictOfList[k] = v

#     ##### *********** CREATING a JSON-file from the dictionary
    
#     with open("global_sites_top_100.json", "w") as write_file:
#         json.dump(dictOfList, write_file)
    
    return dictOfList

    ### ************* Top100 websites checkout and writes a report in CSV-file



def websiteConnectionCheck(mylist,**argv):   
    
    if mylist == websitesList:
        with open(websitesList,'r') as read_file:
            mylist = json.load(read_file)
          
    with open("websites_report_100_vpn.csv",'w') as ws_report:

        headers = ["Rank", "URL", "Status","elapsed"]

        writer = csv.writer(ws_report,delimiter=',')
        writer.writerow(headers)   #writing a first headers line

        for k,v in mylist.items(): 
            try:
                start_time = time.time()   
                website_request =  http.request('GET','https://'+v,timeout=urllib3.Timeout(connect=5.0, read=4.0))
                end_time = time.time()
                elapsed = end_time - start_time
                status = website_request.status
                row = (k,v,status,elapsed)
                writer.writerow(row)
                print(k+" "+v+" "+str(website_request.status)+" %g" % elapsed)


            except urllib3.exceptions.HTTPError:
                print(k+" "+v+" "+str(website_request.status)+" %g" % elapsed+" with HTTPError")
                row = (k,v,status,elapsed)
                writer.writerow(row)
                #  print(colored(k+" "+v+" "+str(website_request.status)+"   t=%g secs" % elapsed),'red') for Unix terminal only
    




if __name__ == "__main__":
   
#     countryCode = checkIpAddress()
    countryCode = ""
    # ***** UNCOMMENT THESE TWO LINES FOR ALEXA TOP100 UPDATE (Will charge some money from serglit72@gmail.com AWS account 100 sites = $0.25)
    dictOfList = alexaUpdateOnline(countryCode)
#     websiteConnectionCheck(dictOfList)
#     websitesList = sys.argv[1]  # to use argument for the app you should use " ", from Terminal ex. $ python alexa100.py "global_sites_top_100.json"
#     websiteConnectionCheck(websitesList)
    print(dictOfList)

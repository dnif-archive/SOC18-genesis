import schedule
import time

import bs4
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup as soup
import csv
import json
#storing the website content
my_url='http://bruteforcers.net/'
    
#req=Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
#web_byte = urlopen(req).read()
# opening connection to grab the page html
#uClient=req(my_url)
#web_byte=uClient.read()
#close the connection
#uClient.close()

#page_soup = soup(web_byte, "html.parser")
#csv creation
filename="Bruteforce.txt"
#Connection opened and headers added
f=open(filename,"a")
headers=("InternalId,Date,IPAddress,Type,Country,Organization \n")
f.write(headers)
def job():
    req=Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
    web_byte = urlopen(req).read()
    page_soup = soup(web_byte, "html.parser")
    page_soup = soup(web_byte, "html.parser")
    f=open(filename,"a")
    
#grabs all categories

    table = page_soup.table
    table_rows = table.find_all('tr')
    for a in range (1,51):
        InternalId= table_rows [a].find_all('td')[0].get_text().strip()
        Date= table_rows[a].find_all('td')[1].get_text().strip()
        IPAddress= table_rows[a].find_all('td')[2].get_text().strip()
        Type= table_rows[a].find_all('td')[3].get_text().strip()
        Country_w= table_rows[a].find_all('td')[4].get_text().strip()
        #Avoiding "," as its is using it as delimeter in a csv(comma seperated value)
        Country= Country_w.replace(',', '.')
        Organization_w= table_rows[a].find_all('td')[5].get_text().strip()
        #Avoiding "," as its is using it as delimeter in a csv(comma seperated value)
        Organization=Organization_w.replace(',', '.')
        print(InternalId +"," + Date +","+ IPAddress +","+ Type +","+ Country +","+ Organization +"\n")
    
        f.write(InternalId +"," + Date +","+ IPAddress +","+ Type +","+ Country +","+ Organization +"\n")
        #fields=['InternalId','Date','IPAddress','Type','Country','Organization']
        
    f.close()
    
##logic Explanation
#opening a file in the read mode. This is the file that has the duplicates.
#Then in a loop that runs till the file is over, we check if the line has already encountered.
#If it has been encountered than we don't write it to the output file.
#If not we will write it to the output file and add it to the list of records that have been encountered already
##
def dup_del():
    inFile = open('Bruteforce.txt','r')
    outFile = open('Bruteforce.csv','w')
    listLines = []

    for line in inFile:

        if line in listLines:
            continue
        else:
            outFile.write(line)
            listLines.append(line)
    outFile.close()
    inFile.close()
    # un-comment to chk if dup is being deleted and being added to the csv file
    #print("dup del")

def csv2json():
    csvfile = open('Bruteforce.csv', 'r')
    jsonfile = open('Bruteforce.json', 'w')

    fieldnames = ("InternalId","Date","IPAddress","Type","Country","Organization")
    reader = csv.DictReader( csvfile, fieldnames)
    out = json.dumps( [ row for row in reader ] )
    jsonfile.write(out)
                  
#schedule the above jobs
#Schedule to scrap
schedule.every(5).seconds.do(job)
#Schedule to delete dups
schedule.every(11).seconds.do(dup_del)
#schedule.every(5).minutes.do(job)
#schedule.every(11).minutes.do(dup_del)
schedule.every(11).seconds.do(csv2json)

# long run job case
while True:
    schedule.run_pending()
    time.sleep(1)

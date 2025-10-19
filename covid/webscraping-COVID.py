# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

##############FOR MACS THAT HAVE CERTIFICATE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

##############FOR PCs THAT HAVE CERTIFICATE ERRORS LOOK HERE################
## https://support.chainstack.com/hc/en-us/articles/9117198436249-Common-SSL-Issues-on-Python-and-How-to-Fix-it

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"



url = 'https://www.worldometers.info/coronavirus/country/us'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

#prints title tag as text
print(soup.title.text)

table_rows = soup.findAll("tr") #findin all tr tags

#print(table_rows[1])




#highest death ratio and lowest death ratio
#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)  -first occurance or table
# findAll(tag, attributes, recursive, text, limit, keywords) - all the rows

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")



for row in table_rows[2:53]:
    td = row.findAll("td")
    #print(td)
    try:
        state = td[1].text.strip()
        total_cases = int(td[2].text.replace(",",""))
        total_deaths = int(td[3].text.replace(",",""))
        total_recovered = int(td[4].text.replace(",",""))
        population = int(td[7].text.replace(",",""))
        print(state)
        #input()
        print(f"Total cases: {total_cases}")
        print(f"Total deaths: {total_deaths}")
        print(f"Total recovered: {total_recovered}")
        print(f"Population: {population}")
    except:
        print(f"{state} is missing data.")

    death_ratio = total_deaths/total_cases
    recovery_ratio = total_recovered/total_cases
    print(f"Death Ratio: {death_ratio}")
    print(f"Recovery Ratio: {recovery_ratio}\n")

state_highest_death_ratio =''
highest_death_ratio = 0.0 #penn
state_lowest_death_ratio = '' #AK
lowest_death_ratio = 1000.0


for row in table_rows[2:53]:
    td = row.findAll("td")
    try:
        state = td[1].text.strip()
        total_cases = int(td[2].text.replace(",",""))
        total_deaths = int(td[3].text.replace(",",""))
        total_recovered = int(td[4].text.replace(",",""))
        population = int(td[7].text.replace(",",""))
        print(state)
        #input()
        print(f"Total cases: {total_cases}")
        print(f"Total deaths: {total_deaths}")
        print(f"Total recovered: {total_recovered}")
        print(f"Population: {population}")
    except:
        print(f"{state} is missing data.")

print(f"State with the highest death ratio is: {state_highest_death_ratio}")
print(f"Death Ratio : {highest_death_ratio}")
print()
print()
print(f"State with the lowest death ratiio is {state_lowest_death_ratio}")
print(f"Death Ratio: {lowest_death_ratio:.2%}")
print()
print()

#highest and lowest reovery ratio

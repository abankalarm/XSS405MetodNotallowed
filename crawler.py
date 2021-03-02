import requests
from bs4 import BeautifulSoup
import sys

#array to hold links
links = []
# we define our functions here
def webcrawl(page,WebpageUrl):
    if(page>0):
        url = WebpageUrl
        codex = requests.get(url)
        plain = codex.text
        s = BeautifulSoup(plain, "html.parser")
        for link in s.findAll('a', {'class':'s-access-detail-page'}):
            # we dont need the title 
            #tet = link.get('title')
            tet = link.get('href')
            print(tet)
            if link not in links:
                links.append(tet)

print("please enter the url you need to crawl example https://www.amazon.in/mobile-phones/b?ie=UTF8&node=1389401031&ref_=nav_shopall_sbc_mobcomp_all_mobiles")
url = input()
print('enter the depth of crawl - minimum 1')
count = input()
count = int(count)

if (count>0):
    for x in range(count):
        print('going deeper')
        webcrawl(1,url)
else:
    print("invalid depth")
    sys.exit()

text_file = open("Output.txt", "w")

print("saving")
for line in links:
    text_file.write("".join(line) + "\n") # works with any number of elements in a line
text_file.close()
print(links)


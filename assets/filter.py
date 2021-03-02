#right now we are only processing GET requests
import requests
from assets.colors import *
def filter(url):
    #these are the most common letters that allow us to inject js
    list = ['<','>','\'','"']

    # we initate a list of allowed characters
    allowed = []
    for i in list:
        # i am using 1x2Y3z to identify if the place of payload in the response
        payload = '1x2Y3z'+i+'1x2Y3z'
        
        # we find location of xss here and replace it 
        # this is for easy hacking
        url_new = url.replace('xsshere',payload)
        r = requests.get(url_new)
        final = r.content
        x = final.decode().split('1x2Y3z')
        if i == x[1]:
            print(Formatting.Dim+i+"character is not encoded"+Formatting.Reset)
            allowed.append(i)
    
    # we return that list
    return allowed
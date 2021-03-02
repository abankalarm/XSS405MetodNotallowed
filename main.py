# this is the main document that determines the workflow
import validators
import sys
#first import all
from assets.breakingout import *
from assets.enclosed import *
from assets.filter import *
from assets.tags import *
from assets.colors import *

def quit():
    #this is recursive exit function
    sys.exit()
    quit()
print(Base.FAIL + r"""

██╗  ██╗███████╗███████╗████████╗ █████╗ ████████╗██╗   ██╗███████╗    ██╗  ██╗ ██████╗ ███████╗                       
╚██╗██╔╝██╔════╝██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║   ██║██╔════╝    ██║  ██║██╔═████╗██╔════╝                       
 ╚███╔╝ ███████╗███████╗   ██║   ███████║   ██║   ██║   ██║███████╗    ███████║██║██╔██║███████╗                       
 ██╔██╗ ╚════██║╚════██║   ██║   ██╔══██║   ██║   ██║   ██║╚════██║    ╚════██║████╔╝██║╚════██║                       
██╔╝ ██╗███████║███████║   ██║   ██║  ██║   ██║   ╚██████╔╝███████║         ██║╚██████╔╝███████║                       
╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝         ╚═╝ ╚═════╝ ╚══════╝                       
                                                                                                                       
██╗  ██╗███████╗███████╗    ███╗   ██╗ ██████╗ ████████╗     █████╗ ██╗     ██╗      ██████╗ ██╗    ██╗███████╗██████╗ 
╚██╗██╔╝██╔════╝██╔════╝    ████╗  ██║██╔═══██╗╚══██╔══╝    ██╔══██╗██║     ██║     ██╔═══██╗██║    ██║██╔════╝██╔══██╗
 ╚███╔╝ ███████╗███████╗    ██╔██╗ ██║██║   ██║   ██║       ███████║██║     ██║     ██║   ██║██║ █╗ ██║█████╗  ██║  ██║
 ██╔██╗ ╚════██║╚════██║    ██║╚██╗██║██║   ██║   ██║       ██╔══██║██║     ██║     ██║   ██║██║███╗██║██╔══╝  ██║  ██║
██╔╝ ██╗███████║███████║    ██║ ╚████║╚██████╔╝   ██║       ██║  ██║███████╗███████╗╚██████╔╝╚███╔███╔╝███████╗██████╔╝
╚═╝  ╚═╝╚══════╝╚══════╝    ╚═╝  ╚═══╝ ╚═════╝    ╚═╝       ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═════╝ 
                                                                                            By: Karan Bamal 
                                                                                                Surbhi Goyal
                                                                                                Priyanka Biswas

                """+ Base.END)
print(Base.OKBLUE+'Enter the url, you want to test with parameter value xsshere, please provide only one parameter at a time')
print('example: https://example.com/test?search=xsshere'+Base.END)
url = input()

valid_url = validators.url(url)
if (valid_url != True):
    print(Base.FAIL+"Url is not valid, Please check the format. Exiting."+Base.END)
    quit()

# lets proceed now

# first we decide if its enclosed or not
is_enclosed = enclosed(url)

if (is_enclosed != False):
    tag_enclosed_inside = is_enclosed
# now we check for tags filtered

unfiltered_symbols = filter(url)

# lets handle case of not enclosed first
if (is_enclosed == False):
    if '<' in unfiltered_symbols:
        if '>' in unfiltered_symbols:
            # this is probably vulnerable
            print(Base.WARNING+"This seems interesting < and > are allowed."+Base.END)
            print(Formatting.Dim+"trying tags now"+Formatting.Reset)
            # our payload function
            tags_allowed = tags(url)
            print(Base.OKGREEN+"All these tags seem to work, please go to https://portswigger.net/web-security/cross-site-scripting/cheat-sheet and use any payload with these tags")
            for i in tags_allowed:
                print(i)          
            print(Base.END)  
            quit()
        else:
            print(Base.FAIL+'not vulnerable')
            quit()
    else:
        print(Base.FAIL+'not vulnerable')
        quit()

# now the more complex scenario when enclosed
singlequote = breaking_single(url)
if (singlequote == True):
    if '\'' in unfiltered_symbols:
        print(Base.WARNING+'seems like we can break out...'+Base.END)
        if '<' in unfiltered_symbols:
            if '>' in unfiltered_symbols:
                # this is probably vulnerable
                print(Base.OKGREEN + "this seems interesting")
                print("trying tags now")
                tags_allowed = tags(url)
                print("All these tags seem to work")
                for i in tags_allowed:
                    print(i)
                    # our payload function
                print("Any payload with all these tags above prepended with '> will work. Use this for reference https://portswigger.net/web-security/cross-site-scripting/cheat-sheet"+Base.END)
                quit() 
        elif (is_enclosed != True):
            #the function is still dangerous
            print(Base.OKGREEN+'we are inside a dangerous function, https://portswigger.net/web-security/cross-site-scripting/cheat-sheet, IT IS VULNERABLE'+Base.END)

if (singlequote == False):
    if '"' in unfiltered_symbols:
        print('seems like we can break out...')
        if '<' in unfiltered_symbols:
            if '>' in unfiltered_symbols:
                # this is probably vulnerable
                print("trying tags now")
                tags_allowed = tags(url)
                print("All these tags seem to work")
                for i in tags_allowed:
                    print(i)
                    # our payload function
                print("Any payload with all these tags above prepended with \"> will work. Use this for reference https://portswigger.net/web-security/cross-site-scripting/cheat-sheet"+Base.END)
                quit() 
        elif (is_enclosed != True):
            #the function is still dangerous
            print('we are inside a dangerous function')
            print(is_enclosed)
            print("payloads in the above tag would work"+Base.END)

print(Base.END+Base.FAIL+'we cant seem to break out - the application doesnt seem vulnerable'+Base.END)
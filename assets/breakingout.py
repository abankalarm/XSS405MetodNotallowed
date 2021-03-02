# this function is only to be executed when the enclosed function is true

import requests
def breaking_single(url):
    # 2 answers possible - single, double
    answer = False
    payload = '1x2Y3z'
    url_new = url.replace('xsshere',payload)
    r = requests.get(url_new)
    final = r.content
    x = final.decode().split('1x2Y3z')
    single = x[0].rfind("'")
    double = x[0].rfind("\"")
    
    if (single > double):
        answer = True
    return answer
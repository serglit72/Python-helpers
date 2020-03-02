import json
import urllib3
import certifi
import sys
from termcolor import colored

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())

r_prod = http.request('GET', ('https://api-prod-partner-us-west-2.northghost.com/server/list?access_token=supersecret'))
r_stage = http.request('GET', ('https://api-stage-partner-us-west-2.northghost.com/server/list?access_token=supersecret'))

f=r_prod.data
v=r_stage.data
k=json.loads(f) #here we have a list of dictionaries
n=json.loads(v)
print("Amount of PROD servers = ",len(k))
print("Amount of STAGE servers = ",len(n))
def check_ip(ip_address,k,n):
    my_ip=ip_address
    
    if len(k) != 0:
        for i in range(len(k)):

            if my_ip == str(k[i]["ip"]):
                print(colored(">>> PROD ENV  >>",'green'),k[i])
                res_p = 1
                break
            res_p = 0
    if len(n) != 0:      
        for i in range(len(n)):
            if my_ip == str(n[i]["ip"]):  
                print(colored(">>>> STAGE ENV  >>>",'yellow'),n[i])
                res_s = 2
                break
            res_s = 3
    if res_s == 3 and res_p == 0 :    
        print(colored("NOTHING HAS FOUND",'red'))
        
# ip_address = "149.28.192.74"
ip_address = sys.argv[1]

check_ip(ip_address,k,n)

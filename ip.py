import json
import urllib3
import sys

http = urllib3.PoolManager()
r_prod = http.request('GET', ('https://backend.northghost.com/server/list?access_token=supersecret'))
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
                print(">>> PROD ENV  >>",k[i])
                res_p = 1
                break
            res_p = 0
    if len(n) != 0:      
        for i in range(len(n)):
            if my_ip == str(n[i]["ip"]):  
                print(">>>> STAGE ENV  >>>",n[i])
                res_s = 2
            res_s = 3
    if res_p == 0:
        print('XXXXXX NOTHING HAS FOUND IN PRODUCTION ENV for the IP ',ip_address)
    if res_s == 3 :
        print('XXXXXX NOTHING HAS FOUND IN STAGE ENV for the IP ',ip_address)     


ip_address = sys.argv[1]

check_ip(ip_address,k,n)

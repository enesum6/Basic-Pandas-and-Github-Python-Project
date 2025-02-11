import requests

class GitHub:
    def __init__(self):
        self.api_url="https://api.github.com"
    def getusername(self,username):
        response=requests.get(self.api_url+"/users/"+username)
        return response.json()
    def getrepos(self,username2):
        response=requests.get(self.api_url+"/users/"+username2+"/repos")
        return response.json()
github=GitHub()
while True:
    secim=input("1-find user\n2-get repositories\n3-create repository\n4-Exit\nSecim:  ")
    
    if secim=="4":
        break
    
    elif secim=="1":
        userName=input("enter the username: ")
        result=github.getusername(userName)
        print(result)
    
    elif secim=="2":
        userName2=input("enter the username: ")
        result=github.getrepos(userName2)
        print(result)
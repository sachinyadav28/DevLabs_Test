import requests
import json

url1 = "https://code-riddler.herokuapp.com/api/v1/challenges/get_challenge/"
user = "sachinyadav"
paswd = "sachin28"
auth_v = (user,paswd)

data = requests.get(url1, auth=auth_v)
dict = json.loads(data.text)
dict1 = dict.get('test_input')
string = dict1.get('text')
count = string.count('.')

url = "https://code-riddler.herokuapp.com/api/v1/testsessionchallenges/output/"

para = {"test_session": 16,   
        "output": {"alphabetCount":count},            
        "challenge": 3   
}
datad = json.dumps(para)
header = {"Content-type":'application/json', 'Accept':'application/json'}
req = requests.post(url,auth=auth_v,data=datad,headers=header)
print(req.status_code)
print(req.content)

import requests
import json
import ast

url1 = "https://code-riddler.herokuapp.com/api/v1/challenges/get_challenge/"
user = "sachinyadav"
paswd = "sachin28"
auth_v = (user,paswd)

data = requests.get(url1, auth=auth_v)
dict = json.loads(data.text)
dict1 = dict.get('test_input')
string = dict1.get('list')
list = ast.literal_eval(string)
output = []
for num in range(list[0],list[1]):  
    if num > 1:  
        for i in range(2,num):  
            if (num % i) == 0:  
                break  
        else:  
            output.append(num)

url = "https://code-riddler.herokuapp.com/api/v1/testsessionchallenges/output/"

para = {"test_session": 16,   
        "output": {"alphabetCount":output},            
        "challenge": 6   
}
datad = json.dumps(para)
header = {"Content-type":'application/json', 'Accept':'application/json'}
req = requests.post(url,auth=auth_v,data=datad,headers=header)
print(req.status_code)
print(req.content)
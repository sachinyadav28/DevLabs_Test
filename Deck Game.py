import requests
import json
import ast

url1 = "https://code-riddler.herokuapp.com/api/v1/challenges/get_challenge/"
user = "sachinyadav"
paswd = "sachin28"
auth_v = (user,paswd)

data = requests.get(url1, auth=auth_v)
print(data.content)
dict = json.loads(data.text)
dict1 = dict.get('test_input')
dict2 = dict1.get('list')
dict3 = dict2
dict4 = ast.literal_eval(dict3) 
player1 = dict4.get('player1')
player2 = dict4.get('player2')

def poker(player):
    pot = 1000
    SP = 100
    CL = 50
    HT = -100
    DD = -50
    ll = []
    for i in player:
        ll.append(i[0]+i[1])
    return sum(ll)

if poker(player1) > poker(player2):
    winner = poker(player1)
else:
    winner = poker(player2)

url = "https://code-riddler.herokuapp.com/api/v1/testsessionchallenges/output/"

para = {"test_session": 16,   
        "output": {"winner":winner},            
        "challenge": 7   
}
datad = json.dumps(para)
header = {"Content-type":'application/json', 'Accept':'application/json'}
req = requests.post(url,auth=auth_v,data=datad,headers=header)
print(req.status_code)
print(req.content)


from pathlib import Path
from module import mail
import string
import random
import json

class Bank:
    database='data.json'
    data=[]

    try:
        if Path(database).exists():
            with open(database,'r') as fs:
                data=json.loads(fs.read())
    except Exception as error:
        print(f"an exception occured as {error}")
  
    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __generateAccountNo(cls):
        num=random.choices(string.digits,k = 3)
        alph=random.choices(string.ascii_letters,k = 3)
        spchar=random.choices("!@#$",k=1)
        id=num + alph + spchar
        random.shuffle(id)
        return "".join(id)

    # CREATE
    def createAccount(self, info):

        if(info["age"] <= str(17)):
            return "age_error"

        elif(len(str(info["pin"])) != 4):
            return "pin_error"

        elif not mail(info["email"]):
            return "email_error"

        else:
            count=1
            info["accountNo"]=Bank.__generateAccountNo()
            info["balance"]=0
            info["pin"]=int(info["pin"])

        Bank.data.append(info)
        Bank.__update()
        return info

    # DEPOSIT
    def depositmoney(self, accNumber, pin, amount):
        userdata=[i for i in Bank.data if i['accountNo'] == accNumber and i['pin'] == pin]

        if userdata == []:
            return "invalid"
        
        elif amount < 1:
            return "amount_error"
        else:
            userdata[0]['balance'] += amount
            Bank.__update()
            return "success"
            

    # WITHDRAW
    def withdrawmoney(self, accNumber, pin, amount):
        userdata=[ i for i in Bank.data if i['accountNo'] == accNumber and i['pin'] == pin ]

        if userdata == []:
            return "invalid"

        elif amount > userdata[0]["balance"]:
            return "balance_error"
        
        elif amount < 1:
            return "amount_error2"
        
        else:
            userdata[0]['balance'] -= amount
            Bank.__update()
            return "success"

    # SHOW
    def showdetails(self, accNumber, pin):
        userdata=[ i for i in Bank.data if i['accountNo'] == accNumber and i['pin'] == pin ]
        if userdata == []:
            return "invalid"
        return userdata[0]

    # UPDATE
    def updatedetails(self, accNumber, pin, name, email, newpin):
        userdata=[ i for i in Bank.data if i['accountNo'] == accNumber and i['pin'] == pin ]

        if userdata == []:
            return "invalid"

        if email and not mail(email):
                return "email_error"
        elif newpin and len(newpin) != 4:
            return "pin_error"

        newdata={
            "name":name,
            "email": email,
            "pin":newpin
        }

        if newdata["name"] == "":
            newdata["name"] = userdata[0]['name']
        if newdata["email"] == "":
            newdata["email"] = userdata[0]['email']
        if newdata["pin"] == "":
            newdata["pin"] = userdata[0]['pin']

        newdata['accountNo'] = userdata[0]['accountNo']
        newdata['age'] = userdata[0]['age']
        newdata['balance'] = userdata[0]['balance']

        if isinstance(newdata['pin'], str):
            newdata['pin'] = int(newdata['pin'])

        for i in newdata:
            if newdata[i] != userdata[0][i]:
                userdata[0][i] = newdata[i]
        
        Bank.__update()
        return "success"

    #  DELETE  
    def Delete(self, accNumber, pin, confirm):
        userdata=[i for i in Bank.data if i['accountNo'] == accNumber and i['pin'] == pin]

        if userdata == []:
            return "invalid"

        if confirm.lower() != 'y':
            return "cancelled"

        index=Bank.data.index(userdata[0])
        Bank.data.pop(index)
        Bank.__update()
        return "deleted"
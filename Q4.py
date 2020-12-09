import datetime
from tabulate import tabulate


register=list()

class Employee:
    def __init__(self):
        self.IN=list()
        self.OUT=list()
        self.NAME=""
        self.NUM=""
        self.FLAG=0 # 1 Means Employee Is In, 0 means Employee is Out
        self.GROSS = ""
        self.BREAK = ""
        self.NET=""

def EmployeeEntry():
    global register
    name = input("[+] Enter Name Of Employee : ")
    flag = 0
    for val in register :
        if val.NAME == name.upper():
            flag = 1

    if flag == 1  :
        print("[-] Employ Exists !")
    else :
        new = Employee()
        new.NAME = name
        new.NAME = (new.NAME).upper()
        register.append(new)
        new.NUM = len(register)

def LogList():
	global register
	name = input("[+] Enter Name To Log In : ")
	for val in register :
		if name.upper()==val.NAME:
			data={"Log In Time" : val.IN,
					"Log Out Time" : val.OUT,
					"Gross" : [val.GROSS],
					"Effective" : [val.NET]}
			table=tabulate(data,headers="keys",tablefmt="pretty")
			print(table)

def ListEmployees():
	global register
	num=list()
	name=list()
	for val in register:
		num.append(val.NUM)
		name.append(val.NAME)
	data={"ID":num,
		"NAME":name}
	table=tabulate(data,headers="keys",tablefmt="pretty")
	print(table)

def LogIn():
    global register
    name = input("[+] Enter Name To Log In : ")
    for val in register :
        if name.upper()==val.NAME:
            if val.FLAG == 0:
                now = datetime.datetime.now().strftime("%H:%M")
                (val.IN).append(now)
                print(f"[+] Logged In At : {now} ")
                val.FLAG = 1
            else :
                print(f"[-] {val.NAME} is already IN")

def LogOut():
    global register
    name = input("[+] Enter Name To Log Out : ")
    for val in register :
        if name.upper()==val.NAME :
            if val.FLAG == 1:
                out=datetime.datetime.now().strftime("%H:%M")
                (val.OUT).append(out)
                print(f"[+] Logged Out At : {out} ")
                val.FLAG = 0
            else :
                print(f"[-] {val.NAME} is already OUT")

def addTime(timeList):
    totalSecs = 0
    for tm in timeList:
        timeParts = [int(s) for s in tm.split(':')]
        totalSecs += (timeParts[0] * 60 + timeParts[1]) * 60 + timeParts[2]
    totalSecs, sec = divmod(totalSecs, 60)
    hr, min = divmod(totalSecs, 60)
    return "%d:%02d" % (hr, min)

def GetGrossNet():
    global register
    name = input("[+] Enter Name To Calculate : ")
    for val in register :
        if name.upper()==val.NAME:
            lastLogOut=(val.OUT)[len(val.OUT)-1]
            firstLogIn=(val.IN)[0]
            val.GROSS=str(datetime.datetime.strptime(lastLogOut,'%H:%M') - datetime.datetime.strptime(firstLogIn,'%H:%M' ))[:-3]
            outtime=val.OUT
            intime=val.IN
            flag=val.FLAG
            bk=list()
            for i in range(len(outtime)-1+val.FLAG):
                bk.append(str(datetime.datetime.strptime(intime[i+1],'%H:%M') - datetime.datetime.strptime(outtime[i],'%H:%M' )))

            val.BREAK=addTime(bk)
            val.NET=str(datetime.datetime.strptime(str(val.GROSS),'%H:%M') - datetime.datetime.strptime(str(val.BREAK),'%H:%M'))[:-3]

def showOptions():
	print("""----MENU----
[1] Employee Entry
[2] Log In
[3] Log Out
[4] Fetch Employee Log
[5] Calculate Gross And Effective Hours
[6] List Employees
[7] Exit
""")


if __name__ == '__main__':
	print("====Employee Login System====")
	while(True):
		showOptions()
		c=int(input("[+] Enter Choice : "))
		if c==1:
			EmployeeEntry()
		if c== 2:
			LogIn()
		if c==3:
			LogOut()
		if c==4:
			LogList()
		if c==5:
			GetGrossNet()
		if c == 6:
			ListEmployees()
		if c ==7:
			break 


















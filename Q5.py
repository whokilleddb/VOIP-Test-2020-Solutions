from tabulate import tabulate

arr=['0','0','0','0','0', '0','0','0','0','0','0','0','0','0','0']
r1=['0','0','0','0','0']
r2=['0','0','0','0','0']
r3=['0','0','0','0','0']

def showTable():
	global r1,r2,r3
	data=[r1,r2,r3]
	print(tabulate(data,tablefmt="pretty"))


def fillSubTables():
	global r1,r2,r3,arr
	for i in range(0,5):
		r1[i]=arr[i]
		r2[i]=arr[i+5]
		r3[i]=arr[i+10]

def CheckIn():
	global r1,r2,r3
	slot=""
	for i in range (0,5):
		if r1[i]=='0':
			r1[i]='*'
			slot="1"+str(i+1)
			return f"Your Slot Number Is : {slot}" 
		if r2[i]=='0':
			r2[i]='*'
			slot="2"+str(i+1)
			return f"Your Slot Number Is : {slot}" 
		if r3[i]=='0':
			r3[i]='*'
			slot="3"+str(i+1)
			return f"Your Slot Number Is : {slot}" 
	return "NO VACANCY"

def checkEmpty(arr,pos):
	if arr[pos] == '0':
		print("[+] Slot Already Vacant")
	else :
		arr[pos] = '0'


def CheckOut():
	try:
		slot=int(input("[+] Enter Slot Number : "))
		r=int(str(slot)[0])
		c=int(str(slot)[1])
		if r==1:
			checkEmpty(r1,c-1)
		if r==2:
			checkEmpty(r1,c-1)		
		if r==3:
			checkEmpty(r2,c-1)
	except:
		print("[+] Invalid Input")


def showMenu():
	print("""
======Menu======
[1] CHECK IN
[2] CHECK OUT
[3] EXIT
================
""")

if __name__ == '__main__':

	while True:
		showTable()
		showMenu()
		choice = input("[+] Enter Choice : ")

		if choice == '1' :
			print(CheckIn())
		if choice == '2':
			CheckOut()
		if choice =='3' :
			break


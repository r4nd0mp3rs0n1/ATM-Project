import datetime
import pickle
import os


class users:
    def __init__(self,username,password,f_name,l_name,address,dob): #constructor for users
        self.__username = username
        self.__password = password
        self.__firstName = f_name
        self.__lastName = l_name
        self.__address = address
        self.__DateOfBirth = dob

    

    #setters
    def SetPassword(self,pw):
        self.__password = pw

    def SetFName(self,fname):
        self.__firstName = fname

    def SetLast(self,lname):
        self.__lastName = lname

    def SetAddress(self,address):
        self.__address = address

    def SetDateOfBirth(self,dob):
        self.__DateOfBirth = dob

    #getters
    def GetUsername(self):  #returns usernam
        return self.__username
    
    def GetFName(self): #returns first name
        return self.__firstName
    
    def GetLName(self): #returns last name
        return self.__lastName
    
    def GetAdd(self):   #returns address
        return self.__address
    
    def GetDoB(self):   #returns date of birth
        return self.__DateOfBirth
    
    def GetPassword(self):
        return self.__password
    
    

class customers(users):
    def __init__(self,u,p,fn,ln,ad,dob):    #constructor for customer
        users.__init__(self,u,p,fn,ln,ad,dob)
        self.__CurrentBalance = 0
        self.__transactions = []
        self.__numberOfTransactions = 0

    def GetBalance(self):
        return self.__CurrentBalance

    def GetAll(self):   #prints all
        print("Username: ",self.GetUsername())
        print("Name: ",self.GetFName(), self.GetLName())
        print("Address: ", self.GetAdd())
        print("Date of Birth: ",self.GetDoB())
        print("Balance: ",self.GetBalance())

    def Deposit(self, amount): #deposit to account
        self.__CurrentBalance = self.__CurrentBalance + amount 
        self.__transactions.append(transaction("Deposit", amount, datetime.datetime.today()))
        with open("Transaction"+self.GetUsername()+".dat", "ab") as f:
            pickle.dump(transaction("Deposit", amount, datetime.datetime.today()),f)
        updateFile(userAccount)
        self.__numberOfTransactions += 1

    def Withdrawal(self, amount): #withdraw from account
        if self.__CurrentBalance >= amount and amount <= 4000:
            self.__CurrentBalance = self.__CurrentBalance - amount 
            print("Withdrawal successful")
            print("Current Balance: ",self.__CurrentBalance)
            self.__transactions.append((transaction("Withdrawal", amount, datetime.datetime.today())))
            with open("Transaction"+self.GetUsername()+".dat", "ab") as f:
                pickle.dump(transaction("WithDrawal", amount, datetime.datetime.today()),f)
            updateFile(userAccount)
            self.__numberOfTransactions += 1
        elif amount > 4000:
            print("The amount you want to withdraw exceeds the $4000.00 limit")
        elif self.__CurrentBalance < amount:
            print("You have insufficient amount to commence the withdrawal")

    def displayTransactions(self):
        for i in range (self.__numberOfTransactions):
            self.__transactions[i].getAllTransactions()

            

    


class admin:
    def __init__(self,u,p): #admin constructor
        self.__adminUser = u
        self.__adminPass = p 

    def GetUsername(self):
        return self.__adminUser
    
    def GetPassword(self):
        return self.__adminPass

def CreateUser(): #Create User
    username = input("Please Input User: ")
    if linear_search_customer(username) is None:
        password = input("Please Input Password: ")
        fname = input("First Name: ")
        lname = input("Last Name: ")    
        dob = input("Date of Birth: ")
        address = input("Address: ")

        newCustomer = customers(username,password,fname,lname,address,dob) #make object

        with open("customer.dat", "ab") as f: #store customer
            pickle.dump(newCustomer,f)

        with open("Transaction"+username+".dat", "ab") as f:
            pass
    else:
        print("Username Taken!!")

    

def linear_search_customer(target): #search customer
    with open("customer.dat", "rb") as f:
        while True:
            try:
                search_value = pickle.load(f)
                if target == search_value.GetUsername():
                    return search_value
                
            except EOFError:
                break

def linear_search_login(target): #search customer
    with open("customer.dat", "rb") as f:
        while True:
            try:
                search_value = pickle.load(f)
                if target == search_value.GetUsername():
                    return search_value
                
            except EOFError:
                break

def ViewAllUsers():
    allUsers = []

    with open("customer.dat", 'rb') as f:
        while True:
            try:
                allAccounts = pickle.load(f)
                allUsers.append(allAccounts)
            except EOFError:
                break
        
    for i in range(len(allUsers)):
        allUsers[i].GetAll()


        

    


def updateFile(results):
    allRecords = []
    #results = linear_search_customer(target)

    
    with open("customer.dat", 'rb') as f:
        while True:
            try:
                resAcc = pickle.load(f)

                
                if results.GetUsername() == resAcc.GetUsername():
                    allRecords.append(results)
                else:
                    allRecords.append(resAcc)
            except EOFError:
                break
    

    with open("customer.dat", "wb") as f:
        for i in range(len(allRecords)):
            pickle.dump(allRecords[i],f)

def deleteProfile(results):
    allRecords = []
    #results = linear_search_customer(target)

    username = results.GetUsername()
    with open("customer.dat", 'rb') as f:
        while True:
            try:
                resAcc = pickle.load(f)

                
                if results.GetUsername() != resAcc.GetUsername():
                    
                    
                    allRecords.append(resAcc)
            except EOFError:
                break
    
    print(username)
    with open("customer.dat", "wb") as f:
        for i in range(len(allRecords)):
            pickle.dump(allRecords[i],f)
    
    os.remove("Transaction"+username+".dat")

def UpdateProfile(userAccount):
    #linear_search_customer(target)
    print('''Which information will you update:
            0. Password
            1. First Name
            2. Last Name
            3. Address
            ''')
    optionUpdate = int(input("Please Input an Option: "))
    if optionUpdate == 0:
        newPass = input("Please Input New Pass Word: ")
        userAccount.SetPassword(newPass)
    elif optionUpdate == 1:
        newF = input("Please Input New First Name: ")
        userAccount.SetFName(newF)
    elif optionUpdate == 2:
        newL = input("Please Input New Last Name: ")
        userAccount.SetLast(newL)
    elif optionUpdate == 3:
        newAdd = input("Please Input New address: ")
        userAccount.SetAddress(newAdd)
    else:
        print("Invalid Option, Will end function!")      
    updateFile(userAccount)
    
    


        
    


        
class transaction:  #transaction class
    def __init__(self, t, a, d):
        self.__transactions = t
        self.__amount = a
        self.__transactionDate = d

    def getAllTransactions(self):
        print(f'Transaction Type: {self.__transactions}')
        print(f'Amount: {self.__amount}')
        print(f'Transaction Date: {self.__transactionDate}')

def mainCustomer(): #main Program for Customer
    while True:
        print('''
        Welcome!!!
            Please Input an Option!!
            1. Check Balance
            2. Update Details
            3. Withdraw
            4. Deposit
            5. View Transaction
            6. Logout   ''')
        userOption = int(input("Please input an Option: "))
        if userOption == 1:
            Current_Balance = userAccount.GetBalance()
            print(f'Your Current Balance: {Current_Balance}')
            continue
        elif userOption == 2:
            UpdateProfile(userAccount)
            continue
        elif userOption == 3:
            amountWithdraw = int(input("Please Input an Amount to Withdraw: "))
            userAccount.Withdrawal(amountWithdraw)
            continue
        elif userOption == 4:
            amountDep = int(input("Please input an amount to deposit: "))
            userAccount.Deposit(amountDep)
            continue
        elif userOption == 5:
            userAccount.displayTransactions()
            continue
        elif userOption == 6:
            print("Thank you")
            break
        else:
            print("Invalid Option")
        
def adminInterface():
    while True:
        print('''
        Welcome!!!
            Please Input an Option!!
            1. Create Customer Profile
            2. Search for customer
            3. Delete
            4. View Customer List
            5. Update User
            6. Logout   ''')

        userOption = int(input("Please input an Option: "))
        if userOption == 1:
            CreateUser()
            continue
        elif userOption == 2:
            searchTarget = input("Please input the user that you are searching for: ")
            found = linear_search_customer(searchTarget)
            found.GetAll()
            continue
        elif userOption == 3:
            searchTarget = input("Please input the user that you are deleting: ")
            found = linear_search_customer(searchTarget)
            print('''Are you sure you want to delete
                     1. Yes
                     0. No''')
            confirm = int(input("Option: "))
            
            if confirm == 1:
                deleteProfile(found)
            elif confirm == 0:
                print("User not deleted")

            continue
        elif userOption == 4:
            ViewAllUsers()
            continue
        elif userOption == 5:
            searchTarget = input("Please input the user that you are searching for: ")
            found = linear_search_customer(searchTarget)
            UpdateProfile(found)
            continue
        elif userOption == 6:
            print("Thank you")
            break
        else:
            print("Invalid Option")
    








#yukiya = customers("Yuki", "Yukiya123", "Yukiya", "Choun", "Laos", "30/12/06")
#yukiya.GetAll()

#yukiya.SetAddress("Thai")
#yukiya.GetAll()

#yukiya.Deposit(1000)
#yukiya.GetAll()

#yukiya.Withdrawal(4000)
#yukiya.Withdrawal(4001)
#yukiya.Withdrawal(300)

#yukiya.displayTransactions()
#yukiya.GetAll()



#main program
#CreateUser()
print(f'''
    Welcome!!!
    Are you an admin or a customer
    Please choose 1 of the following
    Admin: 0
    Customer: 1  ''')



inputChoice = int(input("Enter your choice: "))

#Admin or Customer

if inputChoice == 1:        #Customer Page
    userInput = str(input("Username: "))
    userAccount = linear_search_login(userInput)
    i = 0
    if userAccount is not None:
        while i < 4:
            userInputPass = input("Password: ")
            if userInputPass == userAccount.GetPassword():
                print("success")
                mainCustomer()
                break
            else:
                i += 1
                print("Invalid Password")
                if i == 4:
                    print("Unable to login")
    else:
        print("Username not found!")
    
        



elif inputChoice == 0:  #Admin Page
    UserAdmin = admin("admin", "password")
    userInput = input("Please Input Username: ")
    if userInput == UserAdmin.GetUsername():
        AdminPass = input("Please Input Password: ")
        if AdminPass == UserAdmin.GetPassword():
            adminInterface()
        else:
            print("Invalid Password!!!")
        



else:   #invalid Option
    print("Invalid Option")

#CreateUser()
#CreateUser()
#finding = input("Input: ")
#print(linear_search_customer(finding))


                
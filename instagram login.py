class User:
    def __init__(self, userName, password, fullName):
        self.userName = userName 
        self.password = password
        self.fullName = fullName
        self.followers = []
        self.following = []
        self.followRequestsSent = []
        self.followRequestsReceived = []
        self.posts = []
 
    def handleSendFollowRequests(self):
        otherUserName = input("Enter user-name to send follow request:")
        if otherUserName not in dataStore:
            print("User doesn't exist")
            return 
 
        for userName in self.following:
            if userName == otherUserName:
                print("Already you are following")
                return
        self.followRequestsSent.append(otherUserName)
        otherUserObj = dataStore[otherUserName]
        otherUserObj.followRequestsReceived.append(self.userName)
        print("Follow request sent successfully")
 
    def handleAcceptFollowRequests(self):
        if len(self.followRequestsReceived) == 0:
            print("No follow requests got")
            return
 
        for userName in self.followRequestsReceived:
            print("Do you want to confirm request with id: ", userName)
            option = input("Enter y or n: ")
 
            if option == 'y':
                self.followers.append(userName)
                print("Accepted the request successfully")
            else:
                print("Deleted the follow request successfully")
        self.followRequestsReceived = []
 
    def printAllFollowersList(self):
        if len(self.followers) == 0:
            print("No followers")
            return 
 
        for userName in self.followers:
            print(userName)
 
    def printAllFollowingList(self):
        if len(self.following) == 0:
            print("No-one you are following")
            return 
 
        for userName in self.following:
            print(userName)
dataStore = {}
 
 
 
 
def displayAndHandleMainMenu(userName):
    while True:
        print("-----------------------------------------------------")
        print("1 - Put follow requests")
        print("2 - Accept follow requests")
        print("3 - Post something")
        print("4 - Print all followers")
        print("5 - Print all following list")
        print("6 - Logout")
        option = int(input("Choose the option:"))
        print("-----------------------------------------------------")
        userObj = dataStore[userName]
 
        if option == 1:
            userObj.handleSendFollowRequests()
        elif option == 2:
            userObj.handleAcceptFollowRequests()
        elif option == 3:
            print("Handle Posts")
        elif option == 4:
            userObj.printAllFollowersList()
        elif option == 5:
            userObj.printAllFollowersList()
        elif option == 6:
            print("Loggedout successfully")
            break
        else:
            print("Choose appropriate option")
 
 
def handleLogin():
    print("Enter your login details")
    userName = input("Enter your user-name:")
    password = input("Enter your password:")
    if userName not in dataStore:
        print("Please sign-up first before logging in")
    else:
        print("Logged-in Successfully")
        displayAndHandleMainMenu(userName)
 
def handleSignup():
    print("Enter your details to create an account")
    fullName = input("Enter your full-name:")
    userName = input("Enter your user-name:")
    password = input("Enter your password:")
    if userName not in dataStore:
        newUser = User(userName, password, fullName)
        dataStore[userName] = newUser
        print("Account created Successfully")
    else:
        print("User-Name already exists")
 
 
 
while True:
    print("-----------------------------------------------------")
    print("1 - Login")
    print("2 - Singup")
    print("3 - Exit")
    option = int(input("Choose the option:"))
    print("-----------------------------------------------------")
 
    if option == 1: 
        handleLogin() 
    elif option == 2:
        handleSignup()
    elif option == 3:
        print("Thanks for using Instagram")
        exit(0)
    else:
        print("Choose appropriate option")
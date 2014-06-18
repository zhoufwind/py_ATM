
_account = {}
_account_file = 'account.txt'
_block_file = 'blockList.txt'
_times = 3

def read():
    "Import account file into memory, creating account dictionary"
    with open(_account_file) as f:
        f.readline()    # Ingore first line -- the comment bar
        rename = 0      # If account name repeat, using 'rename' variable change duplicate name
        for i in f.readlines():
            line = i.strip().split()
            while lookup(line[0]):    # If account name repeat, adding '-n' at endings, 'rename' varibale decide 'n'
                print "User %s exist!!" % line[0]
                line[0] += '-' + str(rename)
                rename += 1
                continue
            _account[line[0]] = line[1:]        # Adding account information into dictionary
    print _account

def lookup(n):
    "Check if user account exist in the dictionary, if exist, return user's information or 'True'"
    return _account.get(n)

def checkBlock(name):
    "Chcked if user account exist in block List"
    with open(_block_file) as f:
        for line in f.readlines():
            if name == line.strip('\n'):
                return True
                break
            else:
                continue

def write(n):
    f = open(_block_file, 'a')
    f.writelines(n + '\n')        # Windows using \r\n
    f.close()

def login(t):
    "Login function, first check if account name in the account dictionary, then check if user in blocklist, then begin login process, block user if login failed t times"
    name = raw_input('Enter account name: ')
    if lookup(name):                # Check if user exist in the account
        # print "Found the user!", lookup(name)
        if not checkBlock(name):    # Check if user have been blocked
            for i in range(t):      # Verify the account name and password within 't' times
                pwd = raw_input('Enter password: ')
                if pwd == _account[name][0]:
                    print 'Login success!!\nWelcome!!'
                    break
                else:
                    print 'Password incorrect!'
            else:
                print 'Login Failed %s times, block this account!!' % t
                write(name)         # Adding user into block list
        else:
            print 'User have been blocked already!'
    else:
        print "User isn't exist!!"

read()
login(_times)
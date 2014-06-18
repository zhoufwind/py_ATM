
_account = {}
_account_file = 'account.txt'

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

read()
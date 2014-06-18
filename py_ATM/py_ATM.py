
def init():
    _account = {}
    with open('account.txt') as f:
        f.readline()    # Ingore first line -- the comment bar
        rename = 0      # If account name repeat, using 'rename' variable change duplicate name
        for i in f.readlines():
            line = i.strip().split()
            while _account.has_key(line[0]):    # If account name repeat, adding '-n' at endings, 'rename' varibale decide 'n'
                print "User exist!!"
                line[0] += '-' + str(rename)
                rename += 1
                continue
            _account[line[0]] = line[1:]        # Adding account information into dictionary
    print _account

init()
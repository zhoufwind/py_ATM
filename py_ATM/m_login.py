import os
import sys

_block_file = 'blockList.txt'

def f_lookup(accounts, account):
    "Check if user account exist in the dictionary, if exist, return user's information or 'True'"
    return accounts.get(account)

def f_checkBlock(account):
    "Chcked if user account exist in block List"
    with open(_block_file) as f:
        for line in f.readlines():
            if account == line.strip('\n'):
                return True
                break
            else:
                continue

def f_block(account):
    f = open(_block_file, 'a')
    f.writelines(account + '\n')        # Windows using \n
    f.close()

def f_login(accounts, account, times):
    "Login function, first check if account name in the account dictionary, then check if user in blocklist, then begin login process, block user if login failed t times"
    if f_lookup(accounts, account):                 # Check if user exist in the account
        # print "Found the user!", lookup(name)
        if not f_checkBlock(account):     # Check if user have been blocked
            for i in range(times):      # Verify the account name and password within 't' times
                pwd = raw_input('Enter password: ')
                if pwd == accounts[account][0]:
                    print 'Login success!!'
                    return True         # <-- If user login, return true
                    break
                else:
                    print 'Password incorrect!'
            else:
                print 'Login Failed %s times, block this account!!' % times
                f_block(account)          # Adding user into block list
                return False            # <-- If user been block, return false
        else:
            print 'User have been blocked already!'
            return False                # <-- If user have already blocked, return false
    else:
        print "User isn't exist!!"
        return False                    # <-- If user isn't exist, return false

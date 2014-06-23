import os
import sys

def f_lookup(accounts, account):
    "Check if user account exist in the dictionary, if exist, return user's information or 'True'"
    return accounts.get(account)

def f_checkBlock(account, block_file):
    "Chcked if user account exist in block List"
    with open(block_file) as f:
        for line in f.readlines():
            if account == line.strip('\n'):
                return True
                break
            else:
                continue

def f_block(account, block_file):
    f = open(block_file, 'a')
    f.writelines(account + '\n')        # Windows using \n
    f.close()

def f_login(accounts, account, times, block_file):
    "Login function, first check if account name in the account dictionary, then check if user in blocklist, then begin login process, block user if login failed t times"
    if f_lookup(accounts, account):                 # Check if user exist in the account
        # print "Found the user!", lookup(name)
        if not f_checkBlock(account, block_file):     # Check if user have been blocked
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
                f_block(account, block_file)          # Adding user into block list
                return False            # <-- If user been block, return false
        else:
            print 'User have been blocked already!'
            return False                # <-- If user have already blocked, return false
    else:
        print "User isn't exist!!"
        return False                    # <-- If user isn't exist, return false

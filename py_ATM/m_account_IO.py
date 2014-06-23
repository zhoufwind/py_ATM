import os
import sys
import m_login

def readAccount(accounts, account_file):
    "Import account file into memory, creating account dictionary"
    with open(account_file) as f:
        #f.readline()    # Ingore first line -- the comment bar
        rename = 0      # If account name repeat, using 'rename' variable change duplicate name
        for i in f.readlines():
            line = i.strip().split()
            while m_login.f_lookup(accounts, line[0]):    # If account name repeat, adding '-n' at endings, 'rename' varibale decide 'n'
                #print "Account %s exist!!" % line[0]
                line[0] += '-' + str(rename)
                #print "Modify it to: %s\n----------------------" % line[0]
                rename += 1
                continue
            accounts[line[0]] = line[1:]        # Adding account information into dictionary
    #print accounts

def writeAccount(account, account_file):
    with open (account_file, 'w') as f:
        #f.writelines("Account	password	credit	balance\n")
        f.writelines("")
    for k, v in account.items():
        #print k, v[0], v[1], v[2]
        f = open(account_file, 'a')
        f.writelines(k + '\t' + v[0] + '\t' + v[1] + '\t' + str(v[2]) + '\n')   # need change 'balance' from float to string format

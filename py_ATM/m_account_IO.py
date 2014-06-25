import os
import sys
import m_login
import pickle

_account_file = 'account.txt'
_account_pickle = 'account.pickle'      # define at m_record_amount as well

def readAccount():
    "Import account file into memory, creating account dictionary"
    accounts = {}
    with open(_account_file) as f:
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
    with open (_account_pickle, 'wb') as f:         # dump dictionary(_accounts) to binary file(_account_pickle)
        pickle.dump(accounts, f)
    with open (_account_pickle, 'rb') as f:         # load binary file(_account_pickle) into dictionary(_entry)
        entry = pickle.load(f)
    #print accounts
    return entry

def writeAccount(entry):
    with open (_account_file, 'w') as f:
        #f.writelines("Account	password	credit	balance\n")
        f.writelines("")
    for k, v in entry.items():
        #print k, v[0], v[1], v[2]
        f = open(_account_file, 'a')
        f.writelines(k + '\t' + v[0] + '\t' + v[1] + '\t' + str(v[2]) + '\n')   # need change 'balance' from float to string format

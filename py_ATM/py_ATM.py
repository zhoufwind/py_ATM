import time
import pickle

_accounts = {}
_account_file = 'account.txt'
_block_file = 'blockList.txt'
_log_file = 'credit_account.log'
_account_pickle = 'account.pickle'

def readAccount():
    "Import account file into memory, creating account dictionary"
    with open(_account_file) as f:
        f.readline()    # Ingore first line -- the comment bar
        rename = 0      # If account name repeat, using 'rename' variable change duplicate name
        for i in f.readlines():
            line = i.strip().split()
            while lookup(line[0]):    # If account name repeat, adding '-n' at endings, 'rename' varibale decide 'n'
                #print "Account %s exist!!" % line[0]
                line[0] += '-' + str(rename)
                #print "Modify it to: %s\n----------------------" % line[0]
                rename += 1
                continue
            _accounts[line[0]] = line[1:]        # Adding account information into dictionary
    #print _accounts

def writeAccount(account):
    with open (_account_file, 'w') as f:
        f.writelines("Account	password	credit	balance\n")
    for k, v in account.items():
        print k, v[0], v[1], v[2]
        f = open(_account_file, 'a')
        f.writelines(k + '\t' + v[0] + '\t' + v[1] + '\t' + str(v[2]) + '\n')   # need change 'balance' from float to string format

def lookup(account):
    "Check if user account exist in the dictionary, if exist, return user's information or 'True'"
    return _accounts.get(account)

def checkBlock(account):
    "Chcked if user account exist in block List"
    with open(_block_file) as f:
        for line in f.readlines():
            if account == line.strip('\n'):
                return True
                break
            else:
                continue

def block(account):
    f = open(_block_file, 'a')
    f.writelines(account + '\n')        # Windows using \n
    f.close()

def login(account, times):
    "Login function, first check if account name in the account dictionary, then check if user in blocklist, then begin login process, block user if login failed t times"
    if lookup(account):                 # Check if user exist in the account
        # print "Found the user!", lookup(name)
        if not checkBlock(account):     # Check if user have been blocked
            for i in range(times):      # Verify the account name and password within 't' times
                pwd = raw_input('Enter password: ')
                if pwd == _accounts[account][0]:
                    print 'Login success!!'
                    return True         # <-- If user login, return true
                    break
                else:
                    print 'Password incorrect!'
            else:
                print 'Login Failed %s times, block this account!!' % times
                block(account)          # Adding user into block list
                return False            # <-- If user been block, return false
        else:
            print 'User have been blocked already!'
            return False                # <-- If user have already blocked, return false
    else:
        print "User isn't exist!!"
        return False                    # <-- If user isn't exist, return false

def loger(account, tran_date, tran_type, amount, interest):
    f = file(_log_file, 'a')
    msg = "%s\t%s\t%s\t%s\t%s\n" % (account, tran_date, tran_type, amount, interest)
    f.write(msg)
    f.close()

def record_amount(account, tran_date, tran_type, amount, interest):
    balance = float(_entry[account][2])
    if amount < 0:      # Deposit when amount less than 0
        if _tran_type == 'cash':
            balance -= amount
            _entry[_account][2] = balance       # Update binary file(_account_pickle) -- deposit
            with open (_account_pickle, 'wb') as f:
                pickle.dump(_entry, f)
            print "Cash In: %s by %s success!" % (-amount, tran_type)
            print "You have balance: %s now!" % balance
            loger(account, tran_date, tran_type, amount, interest)
        else:
            print "You must deposit by cash!"
    else:               # Withdrawal when amount greater than 0
        if _tran_type == 'cash':    # Withdrawal by cash, will cost interest
            interest = 0.05 * float(_amount)        # set interest
            if balance < (amount + interest):
                print "Amount: %s + Interest: %s = %s" % (amount, interest, amount + interest)
                print "Sorry, you don't have enough money to buy it!!"
            else:
                balance -= (amount + interest)
                _entry[_account][2] = balance   # Update binary file(_account_pickle) -- withdrawal by cash
                with open (_account_pickle, 'wb') as f:
                    pickle.dump(_entry, f)
                print "Pay Out: %s + Interest: %s by %s success!" % (amount, interest, tran_type)
                print "You have balance: %s now!" % balance
                loger(account, tran_date, tran_type, amount, interest)
        else:                       # Withdrawal by card, no interest
            if balance < amount:
                print "Sorry, you don't have enough money to buy it!!"
            else:
                balance -= amount
                _entry[_account][2] = balance   # Update binary file(_account_pickle) -- withdrawal by card
                with open (_account_pickle, 'wb') as f:
                    pickle.dump(_entry, f)
                print "Pay Out: %s + Interest: %s by %s success!" % (amount, interest, tran_type)
                print "You have balance: %s now!" % balance
                loger(account, tran_date, tran_type, amount, interest)

print "***Welcome to ATM***"
readAccount()          # Import account information into app
_times = 3      # block accunt if login failed 3 times
with open (_account_pickle, 'wb') as f:     # dump dictionary(_accounts) to binary file(_account_pickle)
    pickle.dump(_accounts, f)
with open (_account_pickle, 'rb') as f:     # load binary file(_account_pickle) into dictionary(_entry)
    _entry = pickle.load(f)
while True:
    _account = raw_input('Enter account name: ')    # Specific user login
    if len(_account) == 0: continue
    if login(_account, _times):         # If user login success, he can continue following functions
        print "***Main Window***"
        while True:
            _tran_date = time.strftime('%Y-%m-%d/%H:%M:%S', time.localtime())           # Log local time as transaction time
            _balance = float(_entry[_account][2])
            print "You have %s in total!" % _balance
            _tran_type = raw_input("Transcation type('Card'/'Cash'): ").strip().lower()
            if len(_tran_type) == 0: continue
            if _tran_type == 'card' or 'cash':
                _amount = raw_input("Transaction amount: ").strip()
                _interest = 0
                record_amount(_account, _tran_date, _tran_type, float(_amount), float(_interest))
                if raw_input("----------------------\n>>>Enter any key to continue...<<<\n>>>Enter 'q' to logout...<<<\n") == 'q':
                    _accounts = _entry
                    writeAccount(_accounts)
                    break
            else:
                print "Transaction Type Incorrect!!"
    else:
        print "Login Failed!"

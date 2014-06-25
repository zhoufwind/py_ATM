import os
import sys
import pickle

_log_file = 'credit_account.log'
_account_pickle = 'account.pickle'

def loger(account, tran_date, tran_type, amount, interest):
    f = file(_log_file, 'a')
    msg = "%s\t%s\t%s\t%s\t%s\n" % (account, tran_date, tran_type, amount, interest)
    f.write(msg)
    f.close()

def record_amount(entry, account, tran_date, tran_type, amount, interest):
    balance = float(entry[account][2])
    #if amount < 0:      # Deposit when amount less than 0
    #    if tran_type == 'cash':
    #        balance -= amount
    #        entry[account][2] = balance       # Update binary file(_account_pickle) -- deposit
    #        with open (_account_pickle, 'wb') as f:
    #            pickle.dump(entry, f)
    #        print "Cash In: %s by %s success!" % (-amount, tran_type)
    #        print "You have balance: %s now!" % balance
    #        loger(account, tran_date, tran_type, amount, interest)
    #    else:
    #        print "You must deposit by cash!"
    #else:               # Withdrawal when amount greater than 0
    if tran_type == 'cash':    # Withdrawal by cash, will cost interest
        interest = 0.05 * float(amount)        # set interest
        if balance < (amount + interest):
            print "Amount: %s + Interest: %s = %s" % (amount, interest, amount + interest)
            print "Sorry, you don't have enough money to buy it!!"
        else:
            balance -= (amount + interest)
            entry[account][2] = balance   # Update binary file(_account_pickle) -- withdrawal
            with open (_account_pickle, 'wb') as f:
                pickle.dump(entry, f)
            print "Money Out: %s + Interest: %s by %s success!" % (amount, interest, tran_type.upper())
            print "You have balance: %s now!" % balance
            loger(account, tran_date, tran_type, amount, interest)
    elif tran_type == 'card':                       # Withdrawal by card, no interest
        if balance < amount:
            print "Sorry, you don't have enough money to buy it!!"
        else:
            balance -= amount
            entry[account][2] = balance   # Update binary file(_account_pickle) -- withdrawal by card
            with open (_account_pickle, 'wb') as f:
                pickle.dump(entry, f)
            print "Money Out: %s by %s success!" % (amount, tran_type.upper())
            print "You have balance: %s now!" % balance
            loger(account, tran_date, tran_type, amount, interest)
    elif tran_type == 'deposit':
        balance -= amount
        entry[account][2] = balance     # Update binary file(_account_pickle) -- Deposit
        with open (_account_pickle, 'wb') as f:
            pickle.dump(entry, f)
        print "Money In: %s by %s success!" % (-amount, tran_type.upper())
        print "You have balance: %s now!" % balance
        loger(account, tran_date, tran_type, amount, interest)
    else:
        print 'Invalid tran_type'
#!/usr/bin/env python

import sys
import m_account_IO, m_login, m_tran, m_report

_times = 3      # block accunt if login failed 3 times

def main():
    _entry = m_account_IO.readAccount()      # Import account information into app

    print "***Welcome to ATM***"
    while True:
        _account = raw_input('Login: ')     # Specific user login
        if len(_account) == 0: continue
        elif _account == 'q':
            print "QUIT"
            break
        elif m_login.f_login(_entry, _account, _times):     # If user login success, he can continue following functions
            m_report.f_monthlybills(_account)       # Monthly Bills Report function
            print '''***Main Window***
            0   : Check Balance
            1   : Swiping Card
            2   : Withdrawal
            3   : Deposit
            4   : Check Log
            5   : Logout
            '''
            while True:
                cmd = raw_input("Enter command: ").strip()
                if len(cmd) == 0: continue
                elif cmd == '0':    # check balance function
                    m_tran.f_checkBalance(_entry, _account)
                elif cmd == '1':    # Swiping Card function
                    m_tran.f_swipingCard(_entry, _account)
                elif cmd == '2':    # Withdrawal function
                    m_tran.f_withdrawal(_entry, _account)
                elif cmd == '3':    # Deposit function
                    m_tran.f_deposit(_entry, _account)
                elif cmd == '4':    # Check log function
                    m_report.f_report(_account)
                elif cmd == '5':    # Logout
                    print 'Return'
                    break
    #m_account_IO.writeAccount(_entry)
    print "Have a nice day! Goodbye!"
    #sys.exit()

main()
        

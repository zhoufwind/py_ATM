import os
import sys
import m_account_IO, m_Admin_print

def main():
    print '''
***Welcome to ATM Admin Console***
    P   : Print accounts
    S   : Search account
    I   : Insert account
    U   : Update account
    D   : Delete account
    Q   : Quit
***Enjoy it!***
'''
    _entry = m_account_IO.readAccount()     # Import account information into app
    while True:
        cmd = raw_input("Enter Command(P/S/I/U/D/Q): ").strip().lower()
        if len(cmd) == 0: continue
        elif cmd == 'q':
            #print 'QUIT'
            break
        elif cmd == 'p':
            m_Admin_print.f_print_account(_entry)   # print account function
        elif cmd == 's':
            print 'Search'
        elif cmd == 'i':
            print 'Insert'
        elif cmd == 'u':
            print 'Update'
        elif cmd == 'd':
            print 'Delete'
        else:
            continue
    m_account_IO.writeAccount(_entry)
    print 'QUIT Admin Cosole'
    return

#main()
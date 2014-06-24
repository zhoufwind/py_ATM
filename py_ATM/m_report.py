import os
import sys
import time
import datetime
import re
from prettytable import PrettyTable

_log_file = 'credit_account.log'
_billing_cycle = 30      # default billings cycle = 4 day
_billing_day = '24'     # default billing day = 30th

def f_report(account):
    print '''
    Please enter log time range, date format: E.g.: '2014-06-18'
    Enter 'NULL' by default, ATM print latest '_billing_cycle' log
    '''
    now_time = time.localtime()
    #print now_time
    now_date = datetime.datetime(*now_time[:3])     # log: Y/m/D
    #print now_date
    while True:     # Input start_date
        start_date = raw_input("Start Date: ")
        pattern = re.compile(r'^\d{4}-?\d{1,2}-?\d{1,2}$')
        match = pattern.match(start_date)
        if len(start_date) == 0:
            start_date = now_date - datetime.timedelta(days=(_billing_cycle + 1)) # datetime
            break
        if start_date == 'q':
            print 'QUIT, Return HOME...'
            return
        if not match:
            print 'Invalid Date Format!'
            continue
        else:
            #start_date += '/00:00:00'
            start_time = time.strptime(start_date, '%Y-%m-%d')
            start_date = datetime.datetime(*start_time[:3])
            break
    while True:     # Input start_date
        end_date = raw_input("End Date: ")
        pattern = re.compile(r'^\d{4}-?\d{1,2}-?\d{1,2}$')
        match = pattern.match(end_date)
        if len(end_date) == 0:
            end_time = time.localtime()
            end_date = datetime.datetime(*end_time[:6])     # log: Y/m/D/H/M/S
            break
        if start_date == 'q':
            print 'QUIT, Return HOME...'
            return
        if not match:
            print 'Invalid Date Format!'
            continue
        else:
            end_date += '/23:59:59'
            end_time = time.strptime(end_date, '%Y-%m-%d/%H:%M:%S')
            end_date = datetime.datetime(*end_time[:6])
            if end_date > now_date:
                end_date = datetime.datetime(*end_time[:6])
            break
    print start_date
    print end_date
    f_create_report_rangel(account, start_date, end_date)

def f_create_report_rangel(account, start_date, end_date):
    x = PrettyTable()
    x.field_names = ["account", "tran_date", "tran_type", "amount", "interest"]
    with open (_log_file) as f:
        for i in f.readlines():
            line = i.strip().split()
            if line[0] == account:
                line_time = time.strptime(line[1], '%Y-%m-%d/%H:%M:%S')
                line_date = datetime.datetime(*line_time[:3])
                if line_date >= start_date and line_date <= end_date:
                    x.add_row(line)
    x.align = "l"
    x.padding_width = 2
    print x

def f_monthlybills(account):
    now_time = time.localtime()
    now_date = datetime.datetime(*now_time[:3])
    #print now_time
    print time.strftime('%Y-%m-%d %H:%M:%S', now_time)  # output current time, struct_time => string
    if time.strftime('%d', now_time) == _billing_day:
        while True:
            cmd = raw_input("Today(%s) is your billing day! Do you want to print your monthly billing?\n(Y/N): " % _billing_day).strip().lower()
            if len(cmd) == 0: continue
            elif cmd == 'y':
                print 'YOUR LAST %s DAYS BILLING:' % _billing_cycle
                f_create_report_cycle(account, now_date, _billing_cycle)
                break
            elif cmd == 'n':
                break
            else:
                print 'Invalid Input!'
                continue

def f_create_report_cycle(account, now_date, _billing_cycle):
    x = PrettyTable()
    x.field_names = ["account", "tran_date", "tran_type", "amount", "interest"]
    with open (_log_file) as f:
        for i in f.readlines():
            line = i.strip().split()    # split each line, from string to list
            if line[0] == account:      # select current user's log
                line_time = time.strptime(line[1], '%Y-%m-%d/%H:%M:%S')     # line[1] -- string ==> line_time -- struct_time
                #print line_time
                line_date = datetime.datetime(*line_time[:3])               # struct_time ==> datetime.datetime
                #print line_date
                if (now_date - line_date).days < (_billing_cycle + 1):      # 
                    #print line_date
                    x.add_row(line)
    x.align = "l"
    x.padding_width = 2
    print x

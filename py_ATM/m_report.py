import os
import sys
import time
import datetime
import re
from prettytable import PrettyTable

_log_file = 'credit_account.log'
#_billing_cycle = 30      # default billings cycle = 4 day
_billing_day = '13'     # default billing day = 13th every month

def f_isLeapYear(year):     # year -- int
    Leap = False
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        Leap = True
    return Leap

def f_billing_cycle(year, month, day):  # month/day -- int
    billing_cycle = 30
    if month == 1:
        billing_cycle += 1
    elif month == 2:
        billing_cycle += 1
    elif month == 3:
        if f_isLeapYear(year):
            billing_cycle = 29
        else:
            billing_cycle = 28
    elif month == 4:
        billing_cycle += 1
    #elif month == 5:
    elif month == 6:
        billing_cycle += 1
    #elif month == 7:
    elif month == 8:
        billing_cycle += 1
    elif month == 9:
        billing_cycle += 1
    #elif month == 10:
    elif month == 11:
        billing_cycle += 1
    #elif month == 12:
    return billing_cycle

def f_report(account):
    print '''
    Please enter log time range, date format: E.g.: '2014-06-18'
    Enter 'NULL' by default, ATM print latest nature month report
    '''
    now_time = time.localtime() # format: time.struct_time
    #print now_time
    now_date = datetime.datetime(*now_time[:3])     # format: datetime.datetime(Y/m/D) | filter time.struct_time
    #print now_date
    while True:     # Input start_date
        start_date = raw_input("Start Date: ")
        pattern = re.compile(r'^\d{4}-?\d{1,2}-?\d{1,2}$')
        match = pattern.match(start_date)
        if len(start_date) == 0:
            _billing_cycle = f_billing_cycle(now_date.year, now_date.month, now_date.day)
            start_date = now_date - datetime.timedelta(days=_billing_cycle) # format: datetime.datetime(Y/m/D) | using datetime.timedelta() calc date diff
            #print start_date
            break
        if start_date == 'q':
            print 'QUIT, Return HOME...'
            return
        if not match:
            print 'Invalid Date Format!'
            continue
        else:
            #start_date += '/00:00:00'
            start_time = time.strptime(start_date, '%Y-%m-%d')  # string => struct_time
            start_date = datetime.datetime(*start_time[:3])
            break
    while True:     # Input start_date
        end_date = raw_input("End Date: ")
        pattern = re.compile(r'^\d{4}-?\d{1,2}-?\d{1,2}$')
        match = pattern.match(end_date)
        if len(end_date) == 0:  # default: end date equal localtime
            end_time = now_time    # format: time.struct_time
            end_date = datetime.datetime(*end_time[:6])     # format: datetime (Y/m/D/H/M/S) | filter time.struct_time
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
    #print "Log Range: %s-%s" % (start_date, end_date)  # output struct_time format
    print start_date
    print end_date
    #print "Log Range: %s-%s" % (, )  # output string format
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

import os
import sys
from prettytable import PrettyTable

_log_file = 'credit_account.log'

def f_report(account):
    x = PrettyTable()
    x.field_names = ["account", "tran_date", "tran_type", "amount", "interest"]
    start_Date = raw_input("Start Date(E.g.: 2014-06-18): ")
    start_Time = start_Date + "/00:00:00"
    print start_Time
    end_Date = raw_input("End Date(E.g.: 2014-06-18): ")
    end_Time = end_Date + "/23:59:59"
    print end_Time
    with open (_log_file) as f:
        for i in f.readlines():
            line = i.strip().split()    # split each line, from string to list
            if line[0] == account:
                x.add_row(line)
    x.align = "l"
    x.padding_width = 2
    print x

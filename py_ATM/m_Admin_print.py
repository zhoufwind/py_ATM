import os
import sys
from prettytable import PrettyTable

def f_print_account(entry):
    x = PrettyTable()
    x.field_names = ["Account", "Password", "Credit", "Balance"]
    for k,v in entry.items():
        x.add_row([k, v[0], v[1], v[2]])
    x.align = "l"
    x.sortby = "Account"
    print x
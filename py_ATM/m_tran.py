import os
import sys
import time
import re
import m_record_amount

def f_checkBalance(entry, account):
    balance = float(entry[account][2])
    print "You have balance: %s." % balance

def f_swipingCard(entry, account):
    _balance = float(entry[account][2])       # Show balance FYI, can be remove later
    print "You have balance: %s." % _balance
    _tran_date = time.strftime('%Y-%m-%d/%H:%M:%S', time.localtime())           # Log local time as transaction time
    _tran_type = 'card'
    while True:
        _amount = raw_input("Transaction amount: ").strip()     # how much you will pay
        pattern = re.compile(r'^\d*$')      # BUG -- CANNOT INPUT FLOAT!!!
        match = pattern.match(_amount)
        if len(_amount) == 0: continue
        elif _amount == 'q':
            break
        elif not match:
            print "Invalid format!"
            continue
        else:
            print "Card pay: %s processing..." % _amount
            _interest = 0
            m_record_amount.record_amount(entry, account, _tran_date, _tran_type, float(_amount), float(_interest))
            break

def f_withdrawal(entry, account):
    _balance = float(entry[account][2])       # Show balance FYI, can be remove later
    print "You have balance: %s." % _balance
    _tran_date = time.strftime('%Y-%m-%d/%H:%M:%S', time.localtime())           # Log local time as transaction time
    _tran_type = 'cash'
    while True:
        _amount = raw_input("Transaction amount: ").strip()     # how much you will withdrawal
        pattern = re.compile(r'^\d*$')
        match = pattern.match(_amount)
        if len(_amount) == 0: continue
        elif _amount == 'q':
            break
        elif not match:
            print "Invalid format!"
            continue
        else:
            print "Withdrawal: %s is processing..." % _amount
            _interest = 0
            m_record_amount.record_amount(entry, account, _tran_date, _tran_type, float(_amount), float(_interest))
            break

def f_deposit(entry, account):
    _balance = float(entry[account][2])       # Show balance FYI, can be remove later
    print "You have balance: %s." % _balance
    _tran_date = time.strftime('%Y-%m-%d/%H:%M:%S', time.localtime())           # Log local time as transaction time
    _tran_type = 'deposit'
    while True:
        _amount = raw_input("Deposit amount: ").strip()     # how much you will withdrawal
        pattern = re.compile(r'^\d*$')
        match = pattern.match(_amount)
        if len(_amount) == 0: continue
        elif _amount == 'q':
            break
        elif not match:
            print "Invalid format!"
            continue
        else:
            print "Deposit: %s is processing..." % _amount
            _amount = -float(_amount)
            _interest = 0
            m_record_amount.record_amount(entry, account, _tran_date, _tran_type, _amount, float(_interest))
            break

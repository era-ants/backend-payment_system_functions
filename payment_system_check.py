#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 00:41:54 2021

@author: tsar
"""

from sqlalchemy import create_engine, update
from payment_system_create_base import bills
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///accounts.db', echo=True)
Session = sessionmaker(bind = engine)
session = Session()

def check(data):
    for row in session.query(bills).filter(bills.c.id==data[0]):
        money = row.digits
    return money
    
    
info = [1, 100]

print(check(info))
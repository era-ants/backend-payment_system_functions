#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 00:32:59 2021

@author: tsar
"""

from sqlalchemy import create_engine, update
from payment_system_create_base import bills
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///accounts.db', echo=True)
Session = sessionmaker(bind = engine)
session = Session()

def writeoff(data):
    for row in session.query(bills).filter(bills.c.id==data[0]):
        money = row.digits
    
    if data[1] > money:
        print("Sorry, you are empty")
    else:
        session.query(bills).filter(bills.c.id == data[0]).\
            update({"digits": bills.c.digits - data[1]})
        session.commit()
    
    
info = [1, 100]

writeoff(info)

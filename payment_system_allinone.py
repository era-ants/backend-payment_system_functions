#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 00:47:29 2021

@author: tsar
"""

from sqlalchemy import create_engine, MetaData, Table, Column, Float, String, Integer
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///accounts.db', echo=True)

meta = MetaData()

bills = Table(
    'money', meta,
    Column('id', Integer, primary_key = True),
    Column('digits', Float),
    Column('currency', String(10)))
meta.create_all(engine)

Session = sessionmaker(bind = engine)
session = Session()

def replenishment(data):
    session.query(bills).filter(bills.c.id == data[0]).\
    update({"digits": bills.c.digits + data[1]})
    session.commit()
    
def writeoff(data):
    for row in session.query(bills).filter(bills.c.id==data[0]):
        money = row.digits
    
    if data[1] > money:
        print("Sorry, you are empty")
    else:
        session.query(bills).filter(bills.c.id == data[0]).\
            update({"digits": bills.c.digits - data[1]})
        session.commit()
        
def check(data):
    for row in session.query(bills).filter(bills.c.id==data[0]):
        money = row.digits
    return money


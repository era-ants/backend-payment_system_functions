#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 00:02:20 2021

@author: tsar
"""

from sqlalchemy import create_engine, MetaData, Table, Column, Float, String, Integer
engine = create_engine('sqlite:///accounts.db', echo=True)

meta = MetaData()

bills = Table(
    'money', meta,
    Column('id', Integer, primary_key = True),
    Column('digits', Float),
    Column('currency', String(10)))
meta.create_all(engine)
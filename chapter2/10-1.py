#!/usr/local/bin python3.6
# -*- coding: utf-8 -*-
# 10-1.py

import sys

file = "./hightemp.txt"
f = open(file)
count = 1
for i in f.readline():
    count += 1
f.close()

print(count)
# 結果
# 23

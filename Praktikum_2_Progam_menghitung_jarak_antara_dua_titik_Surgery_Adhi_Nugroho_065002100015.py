# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 11:57:47 2021

@author: Surgery Adhi Nugroho
NIM : 065002100015
Praktikum modul 2
"""
import math
print("progam menghitung jarak antara dua titik di permukaan bumi")
a = float(input('masukan lattitude kota/titik pertama =  ' ))
b = float(input('masukan longitude kota/titik pertama =  '))
c = float(input('masukan lattitude kota/titik kedua =  '))
d = float(input('masukan longitude kota/titik kedua =  '))

dac=(c-a)
dbd=(d-b)
p = math.sin(math.radians(dac/2))**2+math.cos(math.radians(a))*math.cos(math.radians(c))*math.sin(math.radians(dbd/2))**2
q = 2*math.atan2(math.sqrt(p),math.sqrt(1-p))
b = 6371.01*q
print('Jaraknya adalah', b, 'kilometer')

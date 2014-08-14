#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Program adı		: Bay Pi
#Kodlama		: Mert Sarıyaz
#Tarih			: 17 Aralık 2013
#Amacı			: Asistan
#Platform		: GNU/Linux

isim = "Bay Pi"

answer = raw_input("Ben: ")

if answer == "merhaba" or answer == "pi":
	print  isim + ":  " + "Merhaba. Sizi dinliyorum."

elif answer == "raspberry pi nedir" or answer == "raspberry pi":
	print  isim + ":  " + "Raspberry Pi Birleşik Krallık'ta Raspberry Pi Vakfı tarafından okullarda bilgisayar bilimini öğretmek amacılığıyla geliştirilmiş kredi kartı büyüklüğünde tek kartlı bir bilgisayardır."

elif answer == "sen kimsin" or answer == "bay pi kimdir":
	print  isim + ":  " + "Benim adım Bay Pi. 17 Aralık 2013 tarihinde Mert Sarıyaz tarafından Raspberry Pi için Python ile kodlanmış sanal bir robotum."

else:
	print "Olumsuz"

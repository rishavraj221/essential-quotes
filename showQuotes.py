#!/usr/bin/python
import configparser
import psycopg2
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from windowDisplay import *

config = configparser.ConfigParser()
config.read('config.ini')

DEFAULT_MSG = config['general']['DEFAULT_MSG']
HOST = config['sql']['HOST']
DB = config['sql']['DB']
PORT = config['sql']['PORT']
UN = config['sql']['UN']
PW = config['sql']['PW']

wd = windowDisplay()
wd.initiate()

conn = psycopg2.connect(host=HOST,dbname=DB,port=PORT,user=UN,password=PW)
cur = conn.cursor()

while True:
	# get list of tweets
	cur.execute("SELECT * FROM tweets WHERE approved = true")
	rows = cur.fetchall()
	# show directions
	wd.set(DEFAULT_MSG)
	wd.show()
	# loop through tweets
	for tweet in rows:
		msg = tweet[0]
		#print(msg) #debug
		wd.set(msg)
		wd.show()

# close
cur.close()
conn.close()

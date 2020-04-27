import configparser
import psycopg2
from twython import Twython

config = configparser.ConfigParser()
config.read('config.ini')

TW_NAME = config['twitter']['TW_NAME']
TW_HASH = config['twitter']['TW_HASH']
APP_KEY = config['twitter']['APP_KEY']
APP_SECRET = config['twitter']['APP_SECRET']
ACCESS_TOKEN = config['twitter']['ACCESS_TOKEN']
ACCESS_SECRET = config['twitter']['ACCESS_SECRET']
HOST = config['sql']['HOST']
DB = config['sql']['DB']
PORT = config['sql']['PORT']
UN = config['sql']['UN']
PW = config['sql']['PW']

conn = psycopg2.connect(host=HOST,dbname=DB,port=PORT,user=UN,password=PW)
cur = conn.cursor()

last_id = cur.execute("SELECT max(id) from tweets")

twitter = Twython(APP_KEY, APP_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

timeline = twitter.get_mentions_timeline(screen_name=TW_NAME, include_rts=False, since_id=last_id)

for tweet in timeline:
	#print(tweet) #debug
	if(tweet['text'].find(TW_HASH) > 1):
		tid = tweet['id']
		#thex = tweet['text'].encode('ascii','ignore').hex()
		ttext = tweet['text']
		tuser = tweet['user']['screen_name']
		tdate = tweet['created_at']
		#print('hex: ' + thex + 'user: ' + tuser + 'date: ' + tdate) #debug
		cur.execute("INSERT INTO tweets (id,text,screen_name,created_at) values(%s,%s,%s,%s) ON CONFLICT DO NOTHING", (tid,ttext,tuser,tdate))
conn.commit()

# close
cur.close()
conn.close()

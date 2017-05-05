import paho.mqtt.client as mqtt
from pymongo import MongoClient

broker = "192.168.10.15"
port = 1883

dbClient = MongoClient('localhost', 27017)
db = dbClient.cpu_useage

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("rpi/useage")

def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))
	#useage = {}
	#posts = db.posts
	#post = {"useage": (msg.payload)}
	#result = posts.insert_one(post)
	#post_id

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, port)

client.loop_forever() 

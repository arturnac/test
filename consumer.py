import paho.mqtt.client as paho

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

client = paho.Client("testclient", clean_session=False, protocol=paho.MQTTv31)
client.on_message = on_message
client.connect("localhost", 1883)
client.subscribe("rpi/useage", qos=1)
client.loop_forever()



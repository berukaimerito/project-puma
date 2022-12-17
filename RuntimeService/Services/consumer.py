from Utils import json_util
from dotenv import dotenv_values

config = dotenv_values()

class Consumer():
        
    def __init__(self, pika_client):
        self.pika_client = pika_client

    def consume_interval_1(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())
        # time.sleep(body.count(b'.'))
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)
    
    def consume_interval_2(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())
        # time.sleep(body.count(b'.'))
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)
    
    def consume_interval_3(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())
        # time.sleep(body.count(b'.'))
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)
    
    def consume_interval_4(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())
        # time.sleep(body.count(b'.'))
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)
    
    def consume_interval_5(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())
        # time.sleep(body.count(b'.'))
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)
        

    def create_consumers(self):
        while True:

            queue_interval_1 = self.user["user_name"]+"."+config["Symbol"]+"."+config["Interval_1"]
            queue_interval_2 = self.user["user_name"]+"."+config["Symbol"]+"."+config["Interval_2"]
            queue_interval_3 = self.user["user_name"]+"."+config["Symbol"]+"."+config["Interval_3"]
            queue_interval_4 = self.user["user_name"]+"."+config["Symbol"]+"."+config["Interval_4"]
            queue_interval_5 = self.user["user_name"]+"."+config["Symbol"]+"."+config["Interval_5"]

            bot.pika_client.rabbit_channel.basic_consume(queue=queue_interval_1, on_message_callback=Consumer.consume_interval_1)
            bot.pika_client.rabbit_channel.basic_consume(queue=queue_interval_2, on_message_callback=Consumer.consume_interval_2)
            bot.pika_client.rabbit_channel.basic_consume(queue=queue_interval_3, on_message_callback=Consumer.consume_interval_3)
            bot.pika_client.rabbit_channel.basic_consume(queue=queue_interval_4, on_message_callback=Consumer.consume_interval_4)
            bot.pika_client.rabbit_channel.basic_consume(queue=queue_interval_5, on_message_callback=Consumer.consume_interval_5)

            self.pika_client.rabbit_channel.start_consuming()
            
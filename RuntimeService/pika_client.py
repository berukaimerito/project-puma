from dotenv import dotenv_values
import pika

config = dotenv_values()

rabbit_host = config["Rabbit_Host"],
rabbit_port = config["Rabbit_Port"],
rabbit_v_host = config["Rabbit_Virtual_Host"],
rabbit_credentials = pika.PlainCredentials(config["Rabbit_User"], config["Rabbit_Password"])

class Rabbit():
    def __init__(self):

        self.createRabbitInstance()

    def createRabbitInstance(self):
        print("Creating Rabbit Instance...")

        self.rabbit = pika.BlockingConnection(
            pika.ConnectionParameters(
                config["Rabbit_Host"],
                config["Rabbit_Port"],
                config["Rabbit_Virtual_Host"],
                rabbit_credentials
            )
        )

        self.rabbit_channel = self.rabbit.channel()
        self.rabbit_channel.basic_qos(prefetch_count=1)

    def get_instance(self):
        return self.rabbit_instance

      
    
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
    
    def consume_interval_1(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())
        # time.sleep(body.count(b'.'))
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

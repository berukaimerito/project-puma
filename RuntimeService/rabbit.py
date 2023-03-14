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




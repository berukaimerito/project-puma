from dotenv import dotenv_values
config = dotenv_values()


class Bot:

    def __init__(self,username,symbol,app):
        self.username = username
        self.symbol = symbol
        self.app = app

    def consume_interval_1(ch, method, properties, body):
        print(f" [x] Received %r" % body.decode())
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






    #
    # def __str__(self):
    #     return f'{self.username},{self.symbol}'




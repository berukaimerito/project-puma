
from bot import Bot
from dotenv import dotenv_values
config = dotenv_values()
class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class Supervisor(metaclass=Singleton):

    def __init__(self):
        pass
    #
    # def consume_interval_1(ch, method, properties, body):
    #     print(" [x] Received %r" % body.decode())
    #     # time.sleep(body.count(b'.'))
    #     print(" [x] Done")
    #     ch.basic_ack(delivery_tag=method.delivery_tag)
    #
    # def consume_interval_2(ch, method, properties, body):
    #     print(" [x] Received %r" % body.decode())
    #     # time.sleep(body.count(b'.'))
    #     print(" [x] Done")
    #     ch.basic_ack(delivery_tag=method.delivery_tag)
    #
    # def consume_interval_3(ch, method, properties, body):
    #     print(" [x] Received %r" % body.decode())
    #     # time.sleep(body.count(b'.'))
    #     print(" [x] Done")
    #     ch.basic_ack(delivery_tag=method.delivery_tag)
    #
    # def consume_interval_4(ch, method, properties, body):
    #     print(" [x] Received %r" % body.decode())
    #     # time.sleep(body.count(b'.'))
    #     print(" [x] Done")
    #     ch.basic_ack(delivery_tag=method.delivery_tag)
    #
    # def consume_interval_5(ch, method, properties, body):
    #     print(" [x] Received %r" % body.decode())
    #     # time.sleep(body.count(b'.'))
    #     print(" [x] Done")
    #     ch.basic_ack(delivery_tag=method.delivery_tag)

    @staticmethod
    def consume_intervals(bot):
        while True:
            queue_interval_1 = bot.username + "." + bot.symbol + "." + config["Interval_1"]
            queue_interval_2 = bot.username + "." + bot.symbol + "." + config["Interval_2"]
            queue_interval_3 = bot.username + "." + bot.symbol + "." + config["Interval_3"]
            queue_interval_4 = bot.username + "." + bot.symbol + "." + config["Interval_4"]
            queue_interval_5 = bot.username + "." + bot.symbol + "." + config["Interval_5"]

            bot.app.rabbit_channel.basic_consume(queue=queue_interval_1, on_message_callback=Bot.consume_interval_1)
            bot.app.rabbit_channel.basic_consume(queue=queue_interval_2, on_message_callback=Bot.consume_interval_2)
            bot.app.rabbit_channel.basic_consume(queue=queue_interval_3, on_message_callback=Bot.consume_interval_3)
            bot.app.rabbit_channel.basic_consume(queue=queue_interval_4, on_message_callback=Bot.consume_interval_4)
            bot.app.rabbit_channel.basic_consume(queue=queue_interval_5, on_message_callback=Bot.consume_interval_5)

            bot.app.rabbit_channel.start_consuming()

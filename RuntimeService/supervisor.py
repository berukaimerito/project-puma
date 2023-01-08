from dotenv import dotenv_values

config = dotenv_values()

from bot import Bot


class Singleton(type):
    """ Metaclass that creates a Singleton base type when called. """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


# class Supervisor:
# class Supervisor:
class Supervisor(metaclass=Singleton):
    supervisor_bot_list = []

    def consume_intervals(cls, bot):
        while True:

            print(bot.username, bot.symbol)
            queue_interval_1 = bot.username + "." + bot.symbol + "." + config["Interval_1"]
            queue_interval_2 = bot.username + "." + bot.symbol + "." + config["Interval_2"]
            queue_interval_3 = bot.username + "." + bot.symbol + "." + config["Interval_3"]
            queue_interval_4 = bot.username + "." + bot.symbol + "." + config["Interval_4"]
            queue_interval_5 = bot.username + "." + bot.symbol + "." + config["Interval_5"]

            bot.app.rabbit_channel.basic_consume(queue=queue_interval_1,
                                                 on_message_callback=bot.consume_interval_1)

            bot.app.rabbit_channel.start_consuming()

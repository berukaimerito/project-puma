from runtime import user_script

user_bot = user_script.UserBot()
user_bot_1 =user_script.UserBot()
scripts = [
    user_bot,
    user_bot_1
]


def on_price_change(ts,price):
    for bot in scripts:
        bot.on_price_change(ts,price)

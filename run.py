from multiprocessing import Process

import receiver
import telegram_bot
import web_console


def main():
    updater = Process(target=receiver.main, name='ark-updater')
    bot = Process(target=telegram_bot.main, name='ark-telegram-bot')
    site = Process(target=web_console.main, name='ark-web-console')

    updater.start()
    bot.start()
    site.start()


if __name__ == '__main__':
    main()

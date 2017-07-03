import slackbot.bot

@slackbot.bot.respond_to('hello')
def resp_hello(message):
    message.reply('こんにちは')

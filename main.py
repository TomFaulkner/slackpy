import io
import logging
import re
from contextlib import redirect_stdout

import slackbot.bot
from slackbot.bot import Bot, respond_to, listen_to


@listen_to('replit')
def repl(message):
    backticks = re.escape('```')
    contents = message.body['text']
    contents = contents.replace('replit ', '')
    matches = re.findall(f'{backticks}(.*?){backticks}',
                     contents, re.DOTALL)
    for code in matches:
        # code = code.replace('```', '')
        print(code)
        compiled = compile(code, '<string>', mode='exec')
        output = io.StringIO()
        with redirect_stdout(output):
            exec(compiled)
        message.reply(output.getvalue())

    # TODO: replace html entities with proper symbols
    # contents = contents.replace('&gt;', '>')


def main():
    bot = Bot()
    bot.run()


if __name__ == '__main__':
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
    slackbot.bot.logger.setLevel = logging.DEBUG
    main()

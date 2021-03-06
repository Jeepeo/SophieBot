# Copyright (C) 2019 The Raphielscape Company LLC.
# Copyright (C) 2018 - 2019 MrYacha
#
# This file is part of SophieBot.
#
# SophieBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.

import sys

from sophie_bot import dp, bot


@dp.errors_handler()
async def all_errors_handler(message, dp):
    if 'callback_query' in message:
        msg = message.callback_query.message
    else:
        msg = message.message
    chat_id = msg.chat.id
    error = str(sys.exc_info()[1])
    text = "<b>Sorry, I encountered a error!</b>\n"
    text += '<code>%s</code>' % error
    await bot.send_message(chat_id, text, reply_to_message_id=msg.message_id)

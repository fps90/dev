#
# Copyright (C) 2024-present by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#

from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from YukkiMusic import app


def first_page(_):
	controll_button = [InlineKeyboardButton(text="◁", callback_data=f"Adisa"), InlineKeyboardButton(text="HOME", callback_data=f"settingsback_helper"), InlineKeyboardButton(text="▷", callback_data=f"dilXaditi")]
	firsts_page = InlineKeyboardMarkup(
		[
			[InlineKeyboardButton(text=_["H_B_1"], callback_data="help_callback hb1"), InlineKeyboardButton(text=_["H_B_2"], callback_data="help_callback hb2"),InlineKeyboardButton(text=_["H_B_3"], callback_data="help_callback hb3")],
			[InlineKeyboardButton(text=_["H_B_4"], callback_data="help_callback hb4"), InlineKeyboardButton(text=_["H_B_5"], callback_data="help_callback hb5"),InlineKeyboardButton(text=_["H_B_6"], callback_data="help_callback hb6")],
			[InlineKeyboardButton(text=_["H_B_7"], callback_data="help_callback hb7"), InlineKeyboardButton(text=_["H_B_8"], callback_data="help_callback hb8"),InlineKeyboardButton(text=_["H_B_9"], callback_data="help_callback hb9")],
			controll_button,
		]
	)
	return firsts_page

def help_pannel(_, START: Union[bool, int] = None):
    mark = [InlineKeyboardButton(text=_["CLOSEMENU_BUTTON"], callback_data=f"close")]

    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text=_["H_B_1"], callback_data="helpcallback hb1"),
                InlineKeyboardButton(text=_["H_B_9"], callback_data="helpcallback hb8"),
                InlineKeyboardButton(text=_["H_B_8"], callback_data="helpcallback hb7"),
            ],
            [
                InlineKeyboardButton(text=_["H_B_3"], callback_data="helpcallback hb3"),
                InlineKeyboardButton(
                    text=_["H_B_10"], callback_data="helpcallback hb9"
                ),
                InlineKeyboardButton(text=_["H_B_7"], callback_data="helpcallback hb6"),
            ],
            [
                InlineKeyboardButton(text=_["H_B_6"], callback_data="helpcallback hb5"),
                InlineKeyboardButton(text=_["H_B_4"], callback_data="helpcallback hb4"),
                InlineKeyboardButton(text=_["H_B_2"], callback_data="helpcallback hb2"),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_11"], callback_data="helpcallback hb10"
                ),
            ],
            mark,
        ]
    )
    return upl


# Just an common button
def help_back_markup(_):
	upl = InlineKeyboardMarkup([[InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data=f"settings_back_helper")]])
	return upl


# Ease of access 
def private_help_panel(_):
	buttons = [[InlineKeyboardButton(text=_["S_B_4"], url=f"https://t.me/{app.username}?start=help")]]
	return buttons


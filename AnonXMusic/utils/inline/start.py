from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
        [   InlineKeyboardButton(text="🍃𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑🍃", url="https://t.me/II_mxni_II"),
        ]
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="sᴏᴜʀᴄᴇ", url="https://t.me/im_ur_dad_baby"),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
        [   InlineKeyboardButton(text="🇨🇦ᴅᴇᴠᴇʟᴏᴘᴇʀ🇨🇦", url="https://t.me/II_mxni_II"),
        ],
    ]
    return buttons

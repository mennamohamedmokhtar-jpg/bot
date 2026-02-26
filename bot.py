# -*- coding: utf-8 -*-

import os
import random
import hashlib
import time
import logging
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# =========================================================
# CONFIG
# =========================================================

TOKEN = os.getenv("BOT_TOKEN")
logging.basicConfig(level=logging.INFO)
bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

# =========================================================
# MEMORY (ANTI-REPEAT)
# =========================================================

class Memory:
    DATA = {}
    TTL = 3600 * 6

    @classmethod
    def now(cls):
        return int(time.time())

    @classmethod
    def seen(cls, uid, sig):
        cls.DATA.setdefault(uid, {})
        if sig in cls.DATA[uid]:
            return cls.now() - cls.DATA[uid][sig] < cls.TTL
        return False

    @classmethod
    def store(cls, uid, sig):
        cls.DATA.setdefault(uid, {})
        cls.DATA[uid][sig] = cls.now()

# =========================================================
# CONTENT STORAGE (YOU CAN ADD YOUR OWN LINES HERE)
# =========================================================

CONTENT = {
    "palestine": {
        "base": [
            "Palestine is more than a headline — it’s people and memory.",
            "For many families, Palestine means identity and belonging.",
            "The word Palestine carries stories across generations.",
        ],
        "extra": []  # 👈 Add your own Palestine lines here
    },
    "gaza": {
        "base": [
            "In Gaza, daily life continues with quiet resilience.",
            "Gaza is home to families who hold onto hope.",
            "Beyond the news cycle, Gaza is everyday life.",
        ],
        "extra": []  # 👈 Add your own Gaza lines here
    },
    "maps": {
        "base": [
            "Old maps still carry familiar names.",
            "Historical maps document places long remembered.",
            "A map can preserve more than borders — it preserves memory.",
        ],
        "extra": []  # 👈 Add your own Maps lines here
    },
    "suffering": {
        "base": [
            "Behind every statistic, there are human stories.",
            "Displacement leaves marks that time does not erase.",
            "Generations grow up shaped by circumstances they didn’t choose.",
        ],
        "extra": []  # 👈 Add your own General Struggle lines here
    }
}

REFLECTION_LINES = [
    "Memory travels even when people cannot.",
    "Identity survives through language and tradition.",
    "Home is sometimes a place carried in the heart.",
]

SOFT_QUESTIONS = [
    "What does home mean to you?",
    "Can memory itself be a form of presence?",
    "How do we carry history forward?",
]

CALL_TO_ACTION = [
    "Share your thoughts respectfully.",
    "I’d like to hear your perspective.",
    "Feel free to comment below.",
]

HASHTAGS = [
    "#Palestine",
    "#Gaza",
    "#History",
    "#SharedHumanity",
]

PALESTINE_EMOJIS = ["🇵🇸", "🕊️"]

# =========================================================
# CONTENT ENGINE
# =========================================================

class PostEngine:

    def __init__(self, uid):
        self.uid = uid

    def get_lines(self, category):
        base = CONTENT[category]["base"]
        extra = CONTENT[category]["extra"]
        return base + extra

    def maybe_emoji(self, text):
        if random.random() < 0.6:
            return f"{text} {random.choice(PALESTINE_EMOJIS)}"
        return text

    def maybe_hashtag(self, text):
        if random.random() < 0.4:
            text += "\n\n" + random.choice(HASHTAGS)
        return text

    def build(self, category):

        lines = self.get_lines(category)
        if not lines:
            return None

        main_line = random.choice(lines)
        reflection = random.choice(REFLECTION_LINES)

        text = f"{main_line}"
        text = self.maybe_emoji(text)

        text += f"\n\n{reflection}"

        if random.random() < 0.7:
            text += f"\n\n{random.choice(SOFT_QUESTIONS)}"

        if random.random() < 0.7:
            text += f"\n\n{random.choice(CALL_TO_ACTION)}"

        text = self.maybe_hashtag(text)

        signature = hashlib.sha1(text.encode()).hexdigest()

        if Memory.seen(self.uid, signature):
            return None

        Memory.store(self.uid, signature)

        return f"<code>{text}</code>"

# =========================================================
# UI (ARABIC MENU ONLY)
# =========================================================

def main_menu():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("🇵🇸 فلسطين", callback_data="cat|palestine"),
        InlineKeyboardButton("🔥 غزة", callback_data="cat|gaza"),
    )
    kb.add(
        InlineKeyboardButton("🗺️ الخرائط", callback_data="cat|maps"),
        InlineKeyboardButton("💭 المعاناة العامة", callback_data="cat|suffering"),
    )
    return kb

def regenerate_menu(category):
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton("🔄 توليد جملة أخرى", callback_data=f"regen|{category}")
    )
    kb.add(
        InlineKeyboardButton("⬅️ رجوع للقائمة", callback_data="menu")
    )
    return kb

# =========================================================
# HANDLERS
# =========================================================

@bot.message_handler(commands=["start"])
def start(msg):
    bot.send_message(
        msg.chat.id,
        "اختر نوع المحتوى:",
        reply_markup=main_menu()
    )

@bot.callback_query_handler(func=lambda c: True)
def callbacks(call):

    data = call.data.split("|")
    uid = call.from_user.id
    engine = PostEngine(uid)

    if data[0] == "cat":
        category = data[1]
        post = engine.build(category)

        if post:
            bot.send_message(
                call.message.chat.id,
                post,
                reply_markup=regenerate_menu(category)
            )
        else:
            bot.answer_callback_query(call.id, "حاول مرة أخرى")

    elif data[0] == "regen":
        category = data[1]
        post = engine.build(category)

        if post:
            bot.send_message(
                call.message.chat.id,
                post,
                reply_markup=regenerate_menu(category)
            )
        else:
            bot.answer_callback_query(call.id, "حاول مرة أخرى")

    elif data[0] == "menu":
        bot.send_message(
            call.message.chat.id,
            "اختر نوع المحتوى:",
            reply_markup=main_menu()
        )

# =========================================================
# RUN
# =========================================================

logging.info("Palestine Content Bot Running...")
bot.infinity_polling(skip_pending=True)

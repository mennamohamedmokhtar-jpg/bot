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
# MEMORY SYSTEM (ANTI-REPETITION)
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
# PALESTINE EMOJIS ONLY
# =========================================================

PALESTINE_EMOJIS = ["🇵🇸", "🍉", "🕊️"]

def add_palestine_emoji(text):
    emoji = random.choice(PALESTINE_EMOJIS)
    return f"{text} {emoji}"

# =========================================================
# CONTENT STRUCTURE (PROFESSIONAL & EXPANDABLE)
# YOU CAN ADD YOUR OWN SENTENCES & HASHTAGS INSIDE "extra"
# =========================================================

CONTENT = {
    "palestine": {
        "sentences": {
            "base": [
                "Palestine is carried in memory and identity.",
                "For many families, Palestine means belonging.",
                "The name Palestine holds generations of stories.",
            ],
            "extra": []  # 👈 Add your own Palestine sentences here
        },
        "hashtags": {
            "base": [
                "#Palestine",
                "#FreePalestine",
                "#PalestinianVoices",
            ],
            "extra": []  # 👈 Add your own Palestine hashtags here
        }
    },
    "gaza": {
        "sentences": {
            "base": [
                "Gaza is home to resilience and family life.",
                "In Gaza, daily life continues despite hardship.",
                "Gaza represents endurance and hope.",
            ],
            "extra": []
        },
        "hashtags": {
            "base": [
                "#Gaza",
                "#GazaVoices",
                "#StandWithGaza",
            ],
            "extra": []
        }
    },
    "maps": {
        "sentences": {
            "base": [
                "Historical maps preserve familiar names.",
                "Old maps still reflect a shared memory.",
                "Cartography often tells a deeper story.",
            ],
            "extra": []
        },
        "hashtags": {
            "base": [
                "#HistoricalMaps",
                "#Archive",
                "#DocumentedHistory",
            ],
            "extra": []
        }
    },
    "suffering": {
        "sentences": {
            "base": [
                "Behind every headline, there are human lives.",
                "Displacement leaves lasting emotional traces.",
                "Generations grow up shaped by difficult realities.",
            ],
            "extra": []
        },
        "hashtags": {
            "base": [
                "#SharedHumanity",
                "#HumanStories",
                "#CollectiveMemory",
            ],
            "extra": []
        }
    }
}

# =========================================================
# ENGINE
# =========================================================

class ProfessionalEngine:

    def __init__(self, uid):
        self.uid = uid

    def get_sentences(self, category):
        data = CONTENT[category]["sentences"]
        return data["base"] + data["extra"]

    def get_hashtags(self, category):
        data = CONTENT[category]["hashtags"]
        return data["base"] + data["extra"]

    def generate_sentence(self, category):
        lines = self.get_sentences(category)
        if not lines:
            return None

        text = random.choice(lines)
        text = add_palestine_emoji(text)

        signature = hashlib.sha1(text.encode()).hexdigest()

        if Memory.seen(self.uid, signature):
            return None

        Memory.store(self.uid, signature)

        return f"<code>{text}</code>"

    def generate_hashtags(self, category):
        tags = self.get_hashtags(category)
        if not tags:
            return None

        selected = random.sample(tags, min(3, len(tags)))
        text = " ".join(selected)
        text = add_palestine_emoji(text)

        signature = hashlib.sha1(text.encode()).hexdigest()

        if Memory.seen(self.uid, signature):
            return None

        Memory.store(self.uid, signature)

        return f"<code>{text}</code>"

# =========================================================
# UI MENUS (TWO MAIN LISTS)
# =========================================================

def main_menu():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("📝 جمل", callback_data="main|sentences"),
        InlineKeyboardButton("🏷️ هاشتاجات", callback_data="main|hashtags"),
    )
    return kb

def category_menu(main_type):
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("🇵🇸 فلسطين", callback_data=f"{main_type}|palestine"),
        InlineKeyboardButton("🔥 غزة", callback_data=f"{main_type}|gaza"),
    )
    kb.add(
        InlineKeyboardButton("🗺️ الخرائط", callback_data=f"{main_type}|maps"),
        InlineKeyboardButton("💭 المعاناة العامة", callback_data=f"{main_type}|suffering"),
    )
    kb.add(
        InlineKeyboardButton("⬅️ رجوع", callback_data="back_main")
    )
    return kb

def regenerate_menu(main_type, category):
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton("🔄 توليد مرة أخرى", callback_data=f"regen|{main_type}|{category}")
    )
    kb.add(
        InlineKeyboardButton("🏷️ هاشتاجات لنفس القسم", callback_data=f"hashtags|{category}"),
        InlineKeyboardButton("📝 جمل لنفس القسم", callback_data=f"sentences|{category}"),
    )
    kb.add(
        InlineKeyboardButton("⬅️ القائمة الرئيسية", callback_data="back_main")
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
    engine = ProfessionalEngine(uid)

    if data[0] == "main":
        main_type = data[1]
        bot.send_message(
            call.message.chat.id,
            "اختر القسم:",
            reply_markup=category_menu(main_type)
        )

    elif data[0] in ["sentences", "hashtags"] and len(data) == 2:
        main_type = data[0]
        category = data[1]

        if main_type == "sentences":
            result = engine.generate_sentence(category)
        else:
            result = engine.generate_hashtags(category)

        if result:
            bot.send_message(
                call.message.chat.id,
                result,
                reply_markup=regenerate_menu(main_type, category)
            )
        else:
            bot.answer_callback_query(call.id, "حاول مرة أخرى")

    elif data[0] == "regen":
        main_type = data[1]
        category = data[2]

        if main_type == "sentences":
            result = engine.generate_sentence(category)
        else:
            result = engine.generate_hashtags(category)

        if result:
            bot.send_message(
                call.message.chat.id,
                result,
                reply_markup=regenerate_menu(main_type, category)
            )
        else:
            bot.answer_callback_query(call.id, "حاول مرة أخرى")

    elif data[0] == "back_main":
        bot.send_message(
            call.message.chat.id,
            "اختر نوع المحتوى:",
            reply_markup=main_menu()
        )

# =========================================================
# RUN
# =========================================================

logging.info("Professional Palestine Content Bot Running...")
bot.infinity_polling(skip_pending=True)

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
# CONTENT BANK (US AUDIENCE – HUMAN TONE)
# =========================================================

PALESTINE_EMOJIS = ["🇵🇸", "🕊️"]

HOOKS = [
    "Some stories don’t disappear — they wait to be heard.",
    "There are places in the world that live far beyond headlines.",
    "Not everything meaningful makes it into the trending feed.",
    "Sometimes the quietest narratives carry the deepest weight.",
    "History doesn’t vanish just because it isn’t centered.",
    "Behind every map, there are families, memories, and names.",
]

REFLECTIVE_LINES = [
    "For many families, the word “home” is more than geography — it’s memory carried across generations.",
    "Entire communities grow up holding on to stories that shaped their grandparents’ lives.",
    "Memory has a way of surviving even when circumstances change.",
    "Identity isn’t just a political term — it’s language, food, streets, and childhood.",
    "What people pass down isn’t just land — it’s belonging.",
    "There’s something powerful about remembering where you come from.",
]

MICRO_STORIES = [
    "A grandmother keeps an old key in a small wooden box.\nShe says it once opened a door that faced the sea.",
    "In a small living room thousands of miles away, a faded photograph still hangs on the wall.\nThe landscape in it feels closer than the distance suggests.",
    "A father teaches his child the name of a village the child has never seen.\nThe pronunciation matters — it keeps something alive.",
    "At family dinners, stories surface about olive trees and stone houses.\nThey are told gently, but never casually.",
]

KNOWLEDGE_STYLE = [
    "Historical records, personal testimonies, and archived maps continue to document a long and layered story.",
    "Across decades, writers, historians, and families have preserved details that refuse to fade.",
    "Names of towns and villages appear consistently in archives from different periods.",
    "Cultural traditions continue in diaspora communities with remarkable continuity.",
]

SOFT_QUESTIONS = [
    "How much of someone’s identity is tied to a place they’ve never stopped loving?",
    "What does belonging really mean when it spans generations?",
    "Can memory itself be a form of presence?",
    "When people speak about home, what are they truly holding onto?",
]

CALL_TO_ACTION = [
    "If this resonates with you, share your thoughts below.",
    "I’d genuinely like to hear how you see this.",
    "Feel free to add your perspective respectfully.",
    "What does this mean to you?",
]

SOFT_HASHTAGS = [
    "#Palestine",
    "#PalestinianStories",
    "#SharedHumanity",
    "#MemoryAndIdentity",
]

# =========================================================
# CONTENT ENGINE
# =========================================================

class HumanToneEngine:

    def __init__(self, uid):
        self.uid = uid

    def add_emoji(self, text):
        if random.random() < 0.7:
            return f"{text} {random.choice(PALESTINE_EMOJIS)}"
        return text

    def maybe_hashtag(self, text):
        if random.random() < 0.5:
            text += "\n\n" + random.choice(SOFT_HASHTAGS)
        return text

    def generate_hook_post(self):
        text = random.choice(HOOKS)
        text = self.add_emoji(text)
        text += "\n\n" + random.choice(REFLECTIVE_LINES)
        text += "\n\n" + random.choice(SOFT_QUESTIONS)
        text += "\n\n" + random.choice(CALL_TO_ACTION)
        return self.maybe_hashtag(text)

    def generate_micro_story(self):
        text = random.choice(MICRO_STORIES)
        text = self.add_emoji(text)
        text += "\n\n" + random.choice(SOFT_QUESTIONS)
        text += "\n\n" + random.choice(CALL_TO_ACTION)
        return self.maybe_hashtag(text)

    def generate_reflection(self):
        text = random.choice(REFLECTIVE_LINES)
        text = self.add_emoji(text)
        text += "\n\n" + random.choice(REFLECTIVE_LINES)
        text += "\n\n" + random.choice(SOFT_QUESTIONS)
        return self.maybe_hashtag(text)

    def generate_knowledge(self):
        text = random.choice(KNOWLEDGE_STYLE)
        text = self.add_emoji(text)
        text += "\n\n" + random.choice(REFLECTIVE_LINES)
        text += "\n\n" + random.choice(CALL_TO_ACTION)
        return self.maybe_hashtag(text)

    def build(self, mode):
        if mode == "hook":
            text = self.generate_hook_post()
        elif mode == "story":
            text = self.generate_micro_story()
        elif mode == "reflection":
            text = self.generate_reflection()
        elif mode == "knowledge":
            text = self.generate_knowledge()
        else:
            text = self.generate_hook_post()

        signature = hashlib.sha1(text.encode()).hexdigest()

        if Memory.seen(self.uid, signature):
            return None

        Memory.store(self.uid, signature)

        return f"<code>{text}</code>"

# =========================================================
# UI
# =========================================================

def main_menu():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("📝 Emotional Hook", callback_data="mode|hook"),
        InlineKeyboardButton("📖 Micro Story", callback_data="mode|story"),
        InlineKeyboardButton("💭 Reflection", callback_data="mode|reflection"),
        InlineKeyboardButton("📚 Knowledge Tone", callback_data="mode|knowledge"),
    )
    return kb

def regenerate_menu(mode):
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton("🔄 Generate Another", callback_data=f"regen|{mode}")
    )
    kb.add(
        InlineKeyboardButton("⬅️ Back to Menu", callback_data="menu")
    )
    return kb

# =========================================================
# HANDLERS
# =========================================================

@bot.message_handler(commands=["start"])
def start(msg):
    bot.send_message(
        msg.chat.id,
        "Select the type of post you’d like to generate:",
        reply_markup=main_menu()
    )

@bot.callback_query_handler(func=lambda c: True)
def callbacks(call):

    data = call.data.split("|")
    uid = call.from_user.id
    engine = HumanToneEngine(uid)

    if data[0] == "mode":
        mode = data[1]
        post = engine.build(mode)

        if post:
            bot.send_message(
                call.message.chat.id,
                post,
                reply_markup=regenerate_menu(mode)
            )
        else:
            bot.answer_callback_query(call.id, "Please try again.")

    elif data[0] == "regen":
        mode = data[1]
        post = engine.build(mode)

        if post:
            bot.send_message(
                call.message.chat.id,
                post,
                reply_markup=regenerate_menu(mode)
            )
        else:
            bot.answer_callback_query(call.id, "Please try again.")

    elif data[0] == "menu":
        bot.send_message(
            call.message.chat.id,
            "Select the type of post you’d like to generate:",
            reply_markup=main_menu()
        )

# =========================================================
# RUN
# =========================================================

logging.info("US Audience Palestine Engagement Bot Running...")
bot.infinity_polling(skip_pending=True)

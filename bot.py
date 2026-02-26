# -*- coding: utf-8 -*-

import os
import random
import hashlib
import time
import logging
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# ======================================================
# CONFIG
# ======================================================

TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

# ======================================================
# MEMORY SYSTEM
# ======================================================

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

# ======================================================
# CONTENT BANK
# ======================================================

HOOKS = [
    "مش كل التفاصيل بتظهر في السرد المشهور.",
    "في نقطة صغيرة بتغير الصورة بالكامل.",
    "أحيانًا السطر القصير بيحكي أكتر من صفحة كاملة.",
    "في وثيقة قديمة نادرًا ما يتم ذكرها.",
    "في تفصيلة لو ركزت فيها… الصورة تختلف."
]

MICRO_STORIES = [
    "في أرشيف قديم، الاسم كان مكتوب بوضوح.\nلكن قليلين لاحظوا ده.",
    "القرية دي كانت موجودة في 3 سجلات مختلفة.\nالتفصيلة دي وحدها بتحكي قصة.",
    "خريطة بسيطة من القرن الماضي\nلكنها لسه بتثير أسئلة لحد النهارده."
]

KNOWLEDGE_BITS = [
    "أقدم توثيق رسمي للاسم ده كان قبل عقود طويلة.",
    "الاسم ظهر في أكثر من سجل تاريخي مختلف.",
    "المراجع القديمة بتذكر المكان بشكل واضح ومتكرر."
]

ENGAGEMENT_QUESTIONS = [
    "شايف إن التفاصيل الصغيرة مهمة؟",
    "اتفق ولا شايف إن الصورة أكبر من كده؟",
    "إيه أكتر نقطة لفتت نظرك؟",
    "لو هتلخص الفكرة دي في كلمة، هتقول إيه؟"
]

ULTRA_SHORT = [
    "التفاصيل بتفرق.",
    "الذاكرة أطول من الزمن.",
    "السرد مش دايمًا كامل.",
    "الوثائق بتتكلم."
]

CTAS = [
    "اكتب رأيك 👇",
    "شاركنا وجهة نظرك.",
    "قولنا تفكيرك في تعليق.",
    "لو مهتم بالمحتوى ده، تفاعل مع البوست."
]

HASHTAGS = [
    "#History",
    "#Memory",
    "#Archive",
    "#Story"
]

# ======================================================
# USER PREFS
# ======================================================

USER_PREFS = {}

def prefs(uid):
    USER_PREFS.setdefault(uid, {
        "mode": "auto"
    })
    return USER_PREFS[uid]

# ======================================================
# CONTENT ENGINE
# ======================================================

class EngagementEngine:

    def __init__(self, uid):
        self.uid = uid

    def generate(self):

        mode = random.choice([
            "hook",
            "micro_story",
            "knowledge",
            "question_post",
            "ultra_short"
        ])

        if mode == "hook":
            text = random.choice(HOOKS)
            text += "\n\n" + random.choice(ENGAGEMENT_QUESTIONS)
            text += "\n" + random.choice(CTAS)

        elif mode == "micro_story":
            text = random.choice(MICRO_STORIES)
            text += "\n\n" + random.choice(ENGAGEMENT_QUESTIONS)

        elif mode == "knowledge":
            text = random.choice(KNOWLEDGE_BITS)
            text += "\n\n" + random.choice(CTAS)

        elif mode == "question_post":
            text = random.choice(ENGAGEMENT_QUESTIONS)
            text += "\n\n" + random.choice(CTAS)

        elif mode == "ultra_short":
            text = random.choice(ULTRA_SHORT)

        # أحيانًا نضيف هاشتاج واحد فقط
        if random.random() < 0.4:
            text += "\n\n" + random.choice(HASHTAGS)

        signature = hashlib.sha1(text.encode()).hexdigest()

        if Memory.seen(self.uid, signature):
            return None

        Memory.store(self.uid, signature)

        return f"<code>{text}</code>"

# ======================================================
# UI
# ======================================================

def main_kb():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("✨ Generate Post", callback_data="gen"))
    return kb

@bot.message_handler(commands=["start"])
def start(msg):
    bot.send_message(
        msg.chat.id,
        "مولد محتوى تفاعلي 👇",
        reply_markup=main_kb()
    )

@bot.callback_query_handler(func=lambda c: True)
def cb(call):

    if call.data == "gen":
        engine = EngagementEngine(call.from_user.id)
        post = engine.generate()

        if post:
            bot.send_message(call.message.chat.id, post)
        else:
            bot.answer_callback_query(call.id, "جرب تاني ✨")

# ======================================================
# RUN
# ======================================================

logging.info("Engagement Bot Running...")
bot.infinity_polling(skip_pending=True)

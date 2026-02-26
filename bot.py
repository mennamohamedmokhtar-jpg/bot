# -*- coding: utf-8 -*-

import os
import re
import time
import random
import hashlib
import logging
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# =========================================================
# CONFIG
# =========================================================

TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# =========================================================
# BOT INIT
# =========================================================

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

# =========================================================
# SAFETY ENGINE
# =========================================================

class SafetyEngine:

    BLOCKED = {
        "conflict","violence","violent","resistance","occupation",
        "zion","zionist","jewish","israel","israeli",
        "attack","kill","bomb","destroy","rocket","missile",
        "fraud","scam"
    }

    SEMANTIC = {
        "war": ["battle","fight","combat","clash"],
        "military": ["armed","forces","troops"],
        "destruction": ["ruin","devastation","wreckage"],
    }

    @classmethod
    def word_safe(cls, text):
        words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
        return not any(w in cls.BLOCKED for w in words)

    @classmethod
    def semantic_safe(cls, text):
        t = text.lower()
        for root, variants in cls.SEMANTIC.items():
            if re.search(rf"\b{root}\b", t):
                return False
            for v in variants:
                if re.search(rf"\b{v}\b", t):
                    return False
        return True

    @classmethod
    def is_safe(cls, text):
        return cls.word_safe(text) and cls.semantic_safe(text)

# =========================================================
# MEMORY ENGINE
# =========================================================

class MemoryEngine:

    MEMORY = {}
    LIMIT = 300
    TTL = 3600 * 6

    @classmethod
    def now(cls):
        return int(time.time())

    @classmethod
    def seen(cls, uid, sig):
        cls.MEMORY.setdefault(uid, {})
        if sig in cls.MEMORY[uid]:
            return cls.now() - cls.MEMORY[uid][sig] < cls.TTL
        return False

    @classmethod
    def remember(cls, uid, sig):
        cls.MEMORY.setdefault(uid, {})
        cls.MEMORY[uid][sig] = cls.now()

        if len(cls.MEMORY[uid]) > cls.LIMIT:
            cls.MEMORY[uid] = dict(
                sorted(cls.MEMORY[uid].items(), key=lambda x: x[1])[-cls.LIMIT:]
            )

# =========================================================
# USER PREFS
# =========================================================

USER_PREFS = {}

def get_prefs(uid):
    USER_PREFS.setdefault(uid, {
        "randomness": 0.5,
        "emoji": True,
        "questions": True
    })
    return USER_PREFS[uid]

# =========================================================
# TEXT DATA
# =========================================================

OPENINGS = {
    "palestine": [
        "Palestine exists as a continuous historical identity",
        "Palestine remains present through land, memory, and people",
        "Palestine persists beyond time and imposed narratives",
    ],
    "gaza": [
        "Gaza reflects lived Palestinian reality",
        "Gaza carries Palestinian presence forward",
        "Gaza stands as daily evidence of Palestinian life",
    ],
    "maps": [
        "This is a historical map of Palestine before 1948",
        "An archival cartographic record of Palestine prior to 1948",
    ],
    "memory": [
        "Palestinian memory moves steadily through generations",
        "Memory preserves Palestinian presence without interruption",
    ],
    "nakba": [
        "The Nakba marked a decisive historical rupture",
        "The Nakba reshaped Palestinian life permanently",
    ]
}

MIDDLES = [
    "documented carefully through records, names, and places",
    "preserved with historical accuracy and restraint",
    "recorded without exaggeration or distortion",
    "maintained as part of an unbroken historical record",
]

ENDINGS = [
    "as part of Palestinian historical continuity",
    "within Palestinian collective memory",
    "rooted firmly in historical presence",
    "held intact across generations",
]

QUESTIONS = {
    "palestine": [
        "If this identity never disappeared, why is it still questioned?",
        "How much evidence is required before reality is accepted?"
    ],
    "gaza": [
        "If daily life continues, what exactly is claimed to be absent?",
        "At what point does existence stop needing justification?"
    ],
    "maps": [
        "If maps record reality, why are these ones ignored?",
        "How can erased borders still appear so clearly?"
    ],
    "memory": [
        "If memory is continuous, who decides when it ends?",
    ],
    "nakba": [
        "If displacement reshaped everything, why is its cause denied?",
    ]
}

HASHTAGS = {
    "palestine": "#Palestine #PalestinianIdentity",
    "gaza": "#Gaza #PalestinianMemory",
    "maps": "#HistoricalMap #Palestine",
    "memory": "#PalestinianMemory #History",
    "nakba": "#Nakba #PalestinianMemory"
}

EMOJIS = ["🇵🇸","📜","🕊️","⏳","🗺️"]

SYNONYMS = {
    "historical": ["documented","archival","recorded"],
    "preserved": ["maintained","kept","retained"],
    "exists": ["persists","remains","endures"]
}

# =========================================================
# GENERATION ENGINE
# =========================================================

class TextEngine:

    def __init__(self, uid):
        self.uid = uid
        self.prefs = get_prefs(uid)

    def apply_synonyms(self, text):
        intensity = self.prefs["randomness"]
        for word, alts in SYNONYMS.items():
            if random.random() < intensity:
                text = re.sub(rf"\b{word}\b", random.choice(alts), text, count=1)
        return text

    def build(self, category):

        opening = random.choice(OPENINGS[category])
        middle = random.choice(MIDDLES)
        ending = random.choice(ENDINGS)

        text = f"{opening},\n{middle},\n{ending}."

        if self.prefs["emoji"]:
            text += f" {random.choice(EMOJIS)}"

        text = self.apply_synonyms(text)

        if self.prefs["questions"]:
            question = random.choice(QUESTIONS[category])
            text += f"\n\n<b>{question}</b>"

        text += f"\n\n{HASHTAGS[category]}"

        signature = hashlib.sha1(text.encode()).hexdigest()

        if not SafetyEngine.is_safe(text):
            logging.warning("Blocked unsafe content.")
            return None

        if MemoryEngine.seen(self.uid, signature):
            logging.info("Duplicate prevented.")
            return None

        MemoryEngine.remember(self.uid, signature)

        return f"<code>{text}</code>"

# =========================================================
# UI
# =========================================================

CATEGORIES = {
    "palestine": "🇵🇸 فلسطين",
    "gaza": "🔥 غزة",
    "maps": "🗺️ خرائط فلسطين",
    "memory": "📜 الذاكرة الفلسطينية",
    "nakba": "🕊️ النكبة"
}

def categories_kb():
    kb = InlineKeyboardMarkup(row_width=2)
    for key, label in CATEGORIES.items():
        kb.add(InlineKeyboardButton(label, callback_data=f"cat|{key}"))
    return kb

def again_kb(cat):
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("🔄 Generate Again", callback_data=f"again|{cat}"),
        InlineKeyboardButton("🎛 Reset Randomness", callback_data="reset")
    )
    return kb

# =========================================================
# HANDLERS
# =========================================================

@bot.message_handler(commands=["start"])
def start(msg):
    bot.send_message(msg.chat.id, "🇵🇸 اختر القسم:", reply_markup=categories_kb())

@bot.callback_query_handler(func=lambda c: True)
def callbacks(call):

    uid = call.from_user.id
    data = call.data.split("|")

    if data[0] == "cat":
        cat = data[1]
        engine = TextEngine(uid)
        result = engine.build(cat)

        if result:
            bot.send_message(call.message.chat.id, result, reply_markup=again_kb(cat))
        else:
            bot.answer_callback_query(call.id, "⚠️ Try again")

    elif data[0] == "again":
        cat = data[1]
        prefs = get_prefs(uid)
        prefs["randomness"] = min(0.9, prefs["randomness"] + 0.07)

        engine = TextEngine(uid)
        result = engine.build(cat)

        if result:
            bot.send_message(call.message.chat.id, result, reply_markup=again_kb(cat))
        else:
            bot.answer_callback_query(call.id, "⚠️ Variation blocked")

    elif data[0] == "reset":
        get_prefs(uid)["randomness"] = 0.5
        bot.answer_callback_query(call.id, "Randomness Reset ✔️")

# =========================================================
# RUN
# =========================================================

logging.info("Bot running...")
bot.infinity_polling(skip_pending=True)

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
    return f"{text} {random.choice(PALESTINE_EMOJIS)}"

# =========================================================
# QUESTIONS (ENGAGEMENT BOOST)
# =========================================================

QUESTIONS = [
    "What does this mean to you?",
    "How do you see this?",
    "Do you think memory can shape identity?",
    "What are your thoughts?",
    "Can history live through generations?",
]

# =========================================================
# CONTENT STRUCTURE (EDIT & ADD FREELY)
# =========================================================

CONTENT = {
    "palestine": {
        "sentences": {
            "base": [
                (
                    "Palestine is more than a place on a map.\n"
                    "For many families, it represents identity, memory, and belonging."
                ),
                (
                    "The name Palestine carries stories across generations.\n"
                    "It connects people to roots that time has not erased."
                ),
            ],
            "extra": [
    (
        "Palestine lives in stories told at family tables.\n"
        "Memory keeps its presence alive across generations."
    ),
    (
        "For many, Palestine is a feeling carried quietly.\n"
        "It speaks through heritage, language, and tradition."
    ),
    (
        "The word Palestine echoes with history and belonging.\n"
        "It connects the past to the present."
    ),
    (
        "Palestine represents roots that remain strong.\n"
        "Time cannot easily erase identity."
    ),
    (
        "In the hearts of many, Palestine is home.\n"
        "Even distance does not weaken attachment."
    ),
    (
        "Palestine carries memories shaped by generations.\n"
        "Stories pass forward with resilience."
    ),
    (
        "For countless families, Palestine is part of who they are.\n"
        "Identity grows from remembered places."
    ),
    (
        "The name Palestine holds meaning beyond geography.\n"
        "It reflects culture, memory, and continuity."
    ),
    (
        "Palestine is remembered in photographs and old letters.\n"
        "History quietly survives in personal archives."
    ),
    (
        "Across borders, Palestine remains present in memory.\n"
        "Belonging does not depend on distance."
    ),
    (
        "Palestine stands as a symbol of enduring identity.\n"
        "Generations continue to carry its story."
    ),
    (
        "The idea of Palestine travels with its people.\n"
        "Memory makes every place connected."
    ),
    (
        "Palestine is spoken of with warmth and reflection.\n"
        "Its meaning grows deeper over time."
    ),
    (
        "In many homes, Palestine is more than history.\n"
        "It is part of daily remembrance."
    ),
    (
        "Palestine connects families to shared origins.\n"
        "Roots often outlast circumstances."
    ),
    (
        "The memory of Palestine shapes identity.\n"
        "It becomes part of personal narratives."
    ),
    (
        "Palestine is remembered through traditions kept alive.\n"
        "Culture carries continuity forward."
    ),
    (
        "Generations grow up hearing about Palestine.\n"
        "Stories preserve a sense of belonging."
    ),
    (
        "Palestine is held gently in collective memory.\n"
        "It remains meaningful across time."
    ),
    (
        "The mention of Palestine often brings reflection.\n"
        "It connects people to shared heritage."
    ),
    (
        "Palestine lives in songs and spoken memories.\n"
        "Art keeps identity visible."
    ),
    (
        "For many, Palestine is tied to family roots.\n"
        "Belonging can exist beyond borders."
    ),
    (
        "Palestine is remembered in small everyday details.\n"
        "Memory survives in simple traditions."
    ),
    (
        "The story of Palestine is carried forward quietly.\n"
        "Each generation adds its voice."
    ),
    (
        "Palestine symbolizes connection to origin.\n"
        "Identity grows from remembered land."
    ),
    (
        "In conversations, Palestine is spoken of thoughtfully.\n"
        "Memory gives it lasting presence."
    ),
    (
        "Palestine reflects the strength of cultural continuity.\n"
        "Roots remain part of identity."
    ),
    (
        "Many see Palestine as part of their personal story.\n"
        "History becomes lived experience."
    ),
    (
        "Palestine exists in shared family narratives.\n"
        "Memory often becomes inheritance."
    ),
    (
        "The name Palestine carries emotional depth.\n"
        "It connects generations through remembrance."
    ),
    (
        "Palestine is recalled with resilience.\n"
        "Belonging remains steady."
    ),
    (
        "Across time, Palestine remains meaningful.\n"
        "Identity continues to evolve around it."
    ),
    (
        "Palestine lives in preserved memories.\n"
        "History is kept close."
    ),
    (
        "For many, Palestine defines part of their roots.\n"
        "Attachment persists over time."
    ),
    (
        "Palestine represents continuity through generations.\n"
        "Memory shapes understanding."
    ),
    (
        "The idea of Palestine bridges past and present.\n"
        "Stories maintain connection."
    ),
    (
        "Palestine is remembered with quiet strength.\n"
        "Identity remains grounded."
    ),
    (
        "In many narratives, Palestine holds significance.\n"
        "Belonging forms part of heritage."
    ),
    (
        "Palestine reflects cultural depth.\n"
        "History remains alive in memory."
    ),
    (
        "Generational stories often return to Palestine.\n"
        "Roots remain central."
    ),
    (
        "Palestine continues to inspire reflection.\n"
        "Memory ensures continuity."
    ),
    (
        "For families, Palestine is part of shared identity.\n"
        "Heritage shapes belonging."
    ),
    (
        "Palestine is remembered with dignity.\n"
        "Identity grows from history."
    ),
    (
        "The story of Palestine is ongoing.\n"
        "Each voice adds perspective."
    ),
    (
        "Palestine stands within collective memory.\n"
        "Belonging transcends geography."
    ),
    (
        "Palestine connects people to ancestral narratives.\n"
        "Identity carries forward."
    ),
    (
        "In quiet reflection, Palestine remains present.\n"
        "Memory bridges generations."
    ),
    (
        "Palestine reflects enduring heritage.\n"
        "Roots stay meaningful."
    ),
    (
        "Many hold Palestine as part of their identity.\n"
        "Memory reinforces connection."
    ),
    (
        "Palestine lives in cultural expression.\n"
        "History finds its voice."
    ),
    (
        "For some, Palestine is a guiding memory.\n"
        "Belonging continues through time."
    ),
    (
        "Palestine carries emotional significance.\n"
        "Identity grows around it."
    ),
    (
        "Generations speak of Palestine thoughtfully.\n"
        "Stories remain powerful."
    ),
    (
        "Palestine stands as a reminder of heritage.\n"
        "Memory strengthens connection."
    ),
    (
        "Palestine continues through shared remembrance.\n"
        "Belonging endures."
    ),
    (
        "The idea of Palestine is preserved carefully.\n"
        "History remains part of identity."
    ),
    (
        "Palestine exists in family traditions.\n"
        "Roots remain visible."
    ),
    (
        "Palestine is remembered with respect.\n"
        "Identity persists."
    ),
    (
        "For many, Palestine symbolizes continuity.\n"
        "Memory sustains attachment."
    ),
    (
        "Palestine is part of collective reflection.\n"
        "Belonging remains steady."
    ),
    (
        "Palestine lives through generational memory.\n"
        "Heritage remains alive."
    ),
    (
        "The presence of Palestine in stories is lasting.\n"
        "Identity carries on."
    ),
    (
        "Palestine is spoken of across generations.\n"
        "Belonging remains meaningful."
    ),
    (
        "Palestine connects the past with present identity.\n"
        "Memory creates continuity."
    ),
    (
        "For countless voices, Palestine remains significant.\n"
        "Roots define belonging."
    ),
    (
        "Palestine holds a place in shared narratives.\n"
        "History shapes identity."
    ),
    (
        "Palestine stands within remembered heritage.\n"
        "Belonging transcends time."
    ),
    (
        "The story of Palestine continues quietly.\n"
        "Memory keeps it alive."
    ),
    (
        "Palestine is carried forward with dignity.\n"
        "Identity remains connected."
    ),
    (
        "Across families, Palestine remains remembered.\n"
        "Belonging persists."
    ),
    (
        "Palestine reflects enduring roots.\n"
        "History remains present."
    ),
    (
        "In collective memory, Palestine holds space.\n"
        "Identity continues to grow."
    ),
    (
        "Palestine represents more than geography.\n"
        "It reflects lasting heritage."
    ),
    (
        "Palestine is preserved in shared stories.\n"
        "Memory builds continuity."
    ),
    (
        "For many, Palestine is inseparable from identity.\n"
        "Roots remain meaningful."
    ),
    (
        "Palestine continues to shape reflection.\n"
        "Belonging endures."
    ),
    (
        "The name Palestine carries layered meaning.\n"
        "History informs identity."
    ),
    (
        "Palestine remains central in personal narratives.\n"
        "Memory defines connection."
    ),
    (
        "Palestine lives in generational dialogue.\n"
        "Belonging continues forward."
    ),
    (
        "Palestine reflects a sense of origin.\n"
        "Identity remains rooted."
    ),
    (
        "Palestine is spoken of with thoughtful remembrance.\n"
        "Memory strengthens ties."
    ),
    (
        "Palestine carries continuity across time.\n"
        "Heritage remains visible."
    ),
    (
        "For many, Palestine anchors identity.\n"
        "Belonging persists through memory."
    ),
    (
        "Palestine stands within collective heritage.\n"
        "History informs the present."
    ),
    (
        "Palestine is remembered beyond maps.\n"
        "Identity carries its story."
    ),
    (
        "Palestine remains meaningful across generations.\n"
        "Memory preserves connection."
    ),
    (
        "The spirit of Palestine lives in shared history.\n"
        "Belonging continues."
    ),
    (
        "Palestine is held close in remembrance.\n"
        "Identity grows from roots."
    ),
    (
        "Palestine reflects lasting cultural memory.\n"
        "Heritage shapes belonging."
    ),
    (
        "For many families, Palestine remains part of their narrative.\n"
        "Memory carries forward."
    ),
    (
        "Palestine continues to live in reflection.\n"
        "Identity remains grounded in history."
    )
]
        },
        "hashtags": {
            "base": [
                "#Palestine",
                "#FreePalestine",
                "#PalestinianVoices",
            ],
            "extra": [
    (
        "Every homeland lives inside the hearts of its people.\n"
        "Memory can travel even when bodies cannot."
    ),
]
        }
    },
    "gaza": {
        "sentences": {
            "base": [
                (
                    "Gaza is home to families who continue daily life with resilience.\n"
                    "Beyond headlines, it is a place of community and endurance."
                ),
                (
                    "In Gaza, ordinary moments still matter deeply.\n"
                    "Hope and attachment to home remain strong."
                ),
            ],
            "extra": [
    (
        "Every homeland lives inside the hearts of its people.\n"
        "Memory can travel even when bodies cannot."
    ),
]
        },
        "hashtags": {
            "base": [
                "#Gaza",
                "#StandWithGaza",
                "#GazaVoices",
            ],
            "extra": [
    (
        "Every homeland lives inside the hearts of its people.\n"
        "Memory can travel even when bodies cannot."
    ),
]
        }
    },
    "maps": {
        "sentences": {
            "base": [
                (
                    "Historical maps preserve names that many still recognize.\n"
                    "They quietly document places tied to memory."
                ),
                (
                    "Old maps often reflect stories beyond borders.\n"
                    "They capture a sense of continuity through time."
                ),
            ],
           "extra": [
    (
        "Every homeland lives inside the hearts of its people.\n"
        "Memory can travel even when bodies cannot."
    ),
]
        },
        "hashtags": {
            "base": [
                "#HistoricalMaps",
                "#Archive",
                "#DocumentedHistory",
            ],
            "extra": [
    (
        "Every homeland lives inside the hearts of its people.\n"
        "Memory can travel even when bodies cannot."
    ),
]
        }
    },
    "suffering": {
        "sentences": {
            "base": [
                (
                    "Behind every statistic, there are human lives and emotions.\n"
                    "Generations grow up shaped by circumstances they did not choose."
                ),
                (
                    "Displacement leaves marks that last far beyond a moment.\n"
                    "Memory often carries what history books summarize."
                ),
            ],
            "extra": [
    (
        "Every homeland lives inside the hearts of its people.\n"
        "Memory can travel even when bodies cannot."
    ),
]
        },
        "hashtags": {
            "base": [
                "#SharedHumanity",
                "#HumanStories",
                "#CollectiveMemory",
            ],
            "extra": [
    (
        "Every homeland lives inside the hearts of its people.\n"
        "Memory can travel even when bodies cannot."
    ),
]
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

        # Add engagement question
        text += "\n\n" + random.choice(QUESTIONS)

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
# UI
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



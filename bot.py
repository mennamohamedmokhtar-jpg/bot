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
                (
    "Palestine remains present in quiet conversations.\n"
    "Memory keeps its meaning alive."
),
(
    "For many, Palestine is a living connection to ancestry.\n"
    "Roots continue through remembrance."
),
(
    "Palestine carries echoes of earlier generations.\n"
    "Identity grows from those echoes."
),
(
    "The thought of Palestine often brings reflection.\n"
    "Belonging lives within memory."
),
(
    "Palestine stands as a thread through family history.\n"
    "Stories keep that thread unbroken."
),
(
    "In many narratives, Palestine holds a central place.\n"
    "Memory gives it continuity."
),
(
    "Palestine exists beyond headlines.\n"
    "It lives in lived experience."
),
(
    "For families across borders, Palestine remains meaningful.\n"
    "Identity travels with memory."
),
(
    "Palestine reflects endurance shaped by history.\n"
    "Belonging continues forward."
),
(
    "The memory of Palestine is often passed gently.\n"
    "Each generation adds understanding."
),
(
    "Palestine lives in traditions carefully preserved.\n"
    "Culture carries identity onward."
),
(
    "For many, Palestine represents a sense of origin.\n"
    "Roots remain steady."
),
(
    "Palestine connects stories across decades.\n"
    "Memory binds generations together."
),
(
    "The name Palestine often carries quiet strength.\n"
    "Identity remains rooted in heritage."
),
(
    "Palestine survives in shared remembrance.\n"
    "Belonging transcends time."
),
(
    "In countless homes, Palestine is remembered thoughtfully.\n"
    "History informs identity."
),
(
    "Palestine continues as part of personal reflection.\n"
    "Memory builds continuity."
),
(
    "For some, Palestine is a guiding sense of belonging.\n"
    "Roots shape perspective."
),
(
    "Palestine stands within collective awareness.\n"
    "Identity carries its presence."
),
(
    "Across generations, Palestine remains significant.\n"
    "Stories sustain connection."
),
(
    "Palestine reflects cultural depth and continuity.\n"
    "Belonging grows from shared memory."
),
(
    "For many families, Palestine is part of their narrative.\n"
    "Identity carries forward."
),
(
    "Palestine lives in preserved photographs and letters.\n"
    "Memory keeps history tangible."
),
(
    "The idea of Palestine bridges distance.\n"
    "Belonging persists beyond borders."
),
(
    "Palestine continues to shape identity quietly.\n"
    "Roots remain meaningful."
),
(
    "In reflection, Palestine often feels close.\n"
    "Memory narrows the distance."
),
(
    "Palestine holds emotional resonance.\n"
    "Identity grows from remembrance."
),
(
    "For generations, Palestine has remained part of shared history.\n"
    "Belonging carries through time."
),
(
    "Palestine stands as a reminder of continuity.\n"
    "Memory strengthens connection."
),
(
    "Across communities, Palestine remains present in dialogue.\n"
    "Identity evolves with memory."
),
(
    "Palestine lives within cultural expression.\n"
    "Heritage sustains belonging."
),
(
    "For many voices, Palestine carries lasting meaning.\n"
    "Roots remain visible."
),
(
    "Palestine reflects identity shaped over time.\n"
    "Memory becomes inheritance."
),
(
    "The mention of Palestine often sparks reflection.\n"
    "Belonging feels enduring."
),
(
    "Palestine is remembered in shared traditions.\n"
    "Identity remains grounded."
),
(
    "For families, Palestine remains a central memory.\n"
    "Roots continue to define belonging."
),
(
    "Palestine connects personal stories to collective history.\n"
    "Memory bridges generations."
),
(
    "Palestine stands within preserved heritage.\n"
    "Belonging continues steadily."
),
(
    "Across time, Palestine maintains significance.\n"
    "Identity carries its presence."
),
(
    "Palestine reflects a shared past.\n"
    "Memory informs the present."
),
(
    "For many, Palestine is inseparable from their roots.\n"
    "Belonging remains constant."
),
(
    "Palestine continues through spoken remembrance.\n"
    "Identity grows from narrative."
),
(
    "In personal stories, Palestine holds depth.\n"
    "Memory shapes perspective."
),
(
    "Palestine remains part of generational understanding.\n"
    "Belonging persists."
),
(
    "The spirit of Palestine lives in heritage.\n"
    "Identity continues forward."
),
(
    "Palestine exists in quiet moments of reflection.\n"
    "Memory strengthens attachment."
),
(
    "For many, Palestine anchors identity.\n"
    "Roots remain firm."
),
(
    "Palestine connects history with lived experience.\n"
    "Belonging grows over time."
),
(
    "Across families, Palestine remains remembered warmly.\n"
    "Identity persists."
),
(
    "Palestine carries stories shaped by resilience.\n"
    "Memory ensures continuity."
),
(
    "In countless narratives, Palestine stands central.\n"
    "Belonging transcends geography."
),
(
    "Palestine reflects cultural endurance.\n"
    "Identity remains rooted."
),
(
    "For generations, Palestine has remained meaningful.\n"
    "Memory builds connection."
),
(
    "Palestine lives through shared history.\n"
    "Belonging continues."
),
(
    "The presence of Palestine in dialogue is lasting.\n"
    "Identity grows from remembrance."
),
(
    "Palestine symbolizes continuity of heritage.\n"
    "Roots stay significant."
),
(
    "For many, Palestine is remembered with dignity.\n"
    "Belonging endures."
),
(
    "Palestine remains a part of collective reflection.\n"
    "Memory carries forward."
),
(
    "Across borders, Palestine retains meaning.\n"
    "Identity persists."
),
(
    "Palestine lives in the preservation of culture.\n"
    "Belonging remains steady."
),
(
    "For countless families, Palestine shapes identity.\n"
    "Roots remain alive."
),
(
    "Palestine connects the present to ancestral memory.\n"
    "Belonging continues across time."
),
(
    "The idea of Palestine remains resilient.\n"
    "Identity grows around it."
),
(
    "Palestine holds space in shared remembrance.\n"
    "Memory sustains continuity."
),
(
    "For many voices, Palestine carries depth.\n"
    "Belonging remains meaningful."
),
(
    "Palestine continues as part of personal heritage.\n"
    "Identity remains connected."
),
(
    "In reflection, Palestine often feels near.\n"
    "Memory bridges distance."
),
(
    "Palestine reflects enduring roots.\n"
    "Belonging continues."
),
(
    "Across generations, Palestine remains central.\n"
    "Identity carries its story."
),
(
    "Palestine stands as part of collective heritage.\n"
    "Memory defines connection."
),
(
    "For many, Palestine symbolizes belonging.\n"
    "Roots persist."
),
(
    "Palestine remains visible in shared history.\n"
    "Identity evolves with time."
),
(
    "The memory of Palestine shapes perspective.\n"
    "Belonging grows from roots."
),
(
    "Palestine continues to live in cultural memory.\n"
    "Identity remains steady."
),
(
    "For countless families, Palestine remains cherished.\n"
    "Belonging transcends time."
),
(
    "Palestine connects generations through remembrance.\n"
    "Roots define identity."
),
(
    "Across stories, Palestine carries continuity.\n"
    "Memory sustains presence."
),
(
    "Palestine reflects depth of heritage.\n"
    "Belonging persists."
),
(
    "For many, Palestine anchors shared memory.\n"
    "Identity grows forward."
),
(
    "Palestine remains meaningful in collective thought.\n"
    "Roots endure."
),
(
    "In family histories, Palestine holds importance.\n"
    "Belonging continues."
),
(
    "Palestine lives within preserved traditions.\n"
    "Identity remains rooted."
),
(
    "For generations, Palestine has shaped belonging.\n"
    "Memory strengthens connection."
),
(
    "Palestine stands quietly within shared awareness.\n"
    "Identity carries its legacy."
),
(
    "Across time, Palestine remains part of identity.\n"
    "Roots continue."
),
(
    "Palestine reflects enduring connection.\n"
    "Belonging transcends borders."
),
(
    "For many, Palestine is remembered thoughtfully.\n"
    "Identity persists."
),
(
    "Palestine continues through cultural expression.\n"
    "Memory keeps it alive."
),
(
    "In shared narratives, Palestine holds presence.\n"
    "Belonging remains steady."
),
(
    "Palestine connects heritage to daily life.\n"
    "Identity grows from remembrance."
),
(
    "For countless voices, Palestine remains significant.\n"
    "Roots endure."
),
(
    "Palestine stands within preserved memory.\n"
    "Belonging carries forward."
),
(
    "Across communities, Palestine retains meaning.\n"
    "Identity remains connected."
),
(
    "Palestine reflects continuity shaped by history.\n"
    "Memory sustains belonging."
),
(
    "For many families, Palestine remains central to identity.\n"
    "Roots persist through time."
),
(
    "Palestine continues to live in shared heritage.\n"
    "Belonging remains alive."
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
    "#PalestineIdentity",
    "#VoicesOfPalestine",
    "#PalestineHeritage",
    "#PalestineMemory",
    "#PalestineStories",
    "#PalestineCulture",
    "#RememberPalestine",
    "#PalestineRoots",
    "#PalestineHistory",
    "#PalestineVoicesMatter",
    "#PalestineLegacy",
    "#PalestineNarratives",
    "#PalestineConnection",
    "#PalestineBelongs",
    "#PalestineCommunity",
    "#PalestineReflection",
    "#PalestinePresence",
    "#PalestineGenerations",
    "#PalestineTradition",
    "#PalestineContinuity",
    "#PalestineLivesOn",
    "#PalestineAwareness",
    "#PalestineExpression",
    "#PalestineDialogue",
    "#PalestineSharedMemory",
    "#PalestineCollective",
    "#PalestineCultural",
    "#PalestineVoicesGlobal",
    "#PalestineAcrossGenerations",
    "#PalestineUnity",
    "#PalestineHeritageMatters",
    "#PalestineBelonging",
    "#PalestineStoriesLive",
    "#PalestinePerspective",
    "#PalestineEchoes",
    "#PalestineConnectionLives",
    "#PalestineLegacyContinues",
    "#PalestineCulturalMemory",
    "#PalestineRootsRemain",
    "#PalestineNarrative",
    "#PalestineInMemory",
    "#PalestineThroughTime",
    "#PalestineIdentityMatters",
    "#PalestineSharedStories",
    "#PalestineCulturalVoice",
    "#PalestineHumanStories",
    "#PalestineAcrossBorders",
    "#PalestineReflectionTime",
    "#PalestinePresenceMatters",
    "#PalestineContinuingStory",
    "#StandWithPalestinianVoices",
    "#PalestinianHeritage",
    "#PalestinianIdentity",
    "#PalestinianCulture",
    "#PalestinianStories",
    "#PalestinianMemory",
    "#PalestinianRoots",
    "#PalestinianNarratives",
    "#PalestinianVoices",
    "#PalestinianCommunity",
    "#PalestinianTraditions",
    "#PalestinianHistory",
    "#PalestinianBelonging",
    "#PalestinianLegacy",
    "#PalestinianGenerations",
    "#PalestinianReflection",
    "#PalestinianPresence",
    "#PalestinianContinuity",
    "#SharedHeritage",
    "#CulturalContinuity",
    "#CollectiveMemory",
    "#RootsAndIdentity",
    "#StoriesOfHeritage",
    "#VoicesAcrossGenerations",
    "#IdentityAndBelonging",
    "#MemoryAndHistory",
    "#HeritageMatters",
    "#GenerationalVoices",
    "#CulturalNarratives",
    "#PreserveHeritage",
    "#StoriesThatRemain",
    "#HistoryLivesOn",
    "#MemoryCarriesForward",
    "#HeritageVoices",
    "#BelongingAndRoots",
    "#SharedIdentity",
    "#CulturalExpression",
    "#VoicesOfHistory",
    "#HeritageAndMemory",
    "#AcrossGenerations",
    "#CulturalPresence",
    "#IdentityThroughTime",
    "#LivingHeritage",
    "#PreservedMemory",
    "#RootsRemainStrong",
    "#VoicesOfBelonging",
    "#SharedStoriesMatter",
    "#ContinuityOfCulture"

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
        "Gaza is home to families who value everyday moments.\n"
        "Life continues with quiet determination."
    ),
    (
        "In Gaza, community bonds remain strong.\n"
        "People hold onto connection and belonging."
    ),
    (
        "Gaza carries stories shaped by resilience.\n"
        "Daily life reflects endurance."
    ),
    (
        "Beyond headlines, Gaza is a place of neighbors and families.\n"
        "Ordinary routines still matter."
    ),
    (
        "Gaza reflects strength found in community.\n"
        "Hope continues through shared support."
    ),
    (
        "In Gaza, traditions remain meaningful.\n"
        "Culture sustains identity."
    ),
    (
        "Gaza is remembered through personal stories.\n"
        "Memory keeps experiences alive."
    ),
    (
        "Families in Gaza continue forward each day.\n"
        "Resilience shapes perspective."
    ),
    (
        "Gaza stands as a place of lived reality.\n"
        "Community defines daily life."
    ),
    (
        "In Gaza, attachment to home runs deep.\n"
        "Belonging remains central."
    ),
    (
        "Gaza reflects the power of togetherness.\n"
        "Support strengthens communities."
    ),
    (
        "Daily routines in Gaza carry meaning.\n"
        "Life continues with determination."
    ),
    (
        "Gaza holds memories shaped by generations.\n"
        "Stories carry continuity."
    ),
    (
        "In Gaza, people value family above all.\n"
        "Connection sustains hope."
    ),
    (
        "Gaza remains present in shared conversations.\n"
        "Experience shapes understanding."
    ),
    (
        "Within Gaza, culture continues to thrive.\n"
        "Identity remains strong."
    ),
    (
        "Gaza is more than a headline.\n"
        "It is a place of everyday life."
    ),
    (
        "In Gaza, resilience appears in simple acts.\n"
        "Community creates strength."
    ),
    (
        "Gaza reflects determination in the face of challenge.\n"
        "Families continue forward."
    ),
    (
        "Life in Gaza includes laughter and reflection.\n"
        "Human moments endure."
    ),
    (
        "Gaza stands within collective awareness.\n"
        "Stories deserve to be heard."
    ),
    (
        "In Gaza, identity is rooted in heritage.\n"
        "Tradition shapes belonging."
    ),
    (
        "Gaza carries experiences that shape generations.\n"
        "Memory becomes inheritance."
    ),
    (
        "Families in Gaza preserve their culture.\n"
        "Continuity matters deeply."
    ),
    (
        "Gaza reflects the value of unity.\n"
        "Shared strength moves people forward."
    ),
    (
        "In Gaza, daily life continues with resolve.\n"
        "Hope persists quietly."
    ),
    (
        "Gaza remains a place of community ties.\n"
        "Belonging connects neighbors."
    ),
    (
        "Gaza holds the weight of lived experience.\n"
        "Resilience defines perspective."
    ),
    (
        "Within Gaza, relationships create support.\n"
        "Connection sustains life."
    ),
    (
        "Gaza reflects endurance shaped by circumstance.\n"
        "Families continue forward."
    ),
    (
        "In Gaza, shared meals carry meaning.\n"
        "Tradition remains alive."
    ),
    (
        "Gaza stands as a reminder of human strength.\n"
        "Community remains central."
    ),
    (
        "Life in Gaza includes moments of reflection.\n"
        "Identity grows from experience."
    ),
    (
        "Gaza carries stories of perseverance.\n"
        "Hope continues quietly."
    ),
    (
        "In Gaza, belonging is tied to home.\n"
        "Connection remains powerful."
    ),
    (
        "Gaza reflects courage in everyday life.\n"
        "Families move forward together."
    ),
    (
        "Within Gaza, shared history shapes identity.\n"
        "Memory keeps continuity alive."
    ),
    (
        "Gaza is a place where community matters deeply.\n"
        "Support strengthens bonds."
    ),
    (
        "In Gaza, people hold onto their traditions.\n"
        "Culture sustains belonging."
    ),
    (
        "Gaza reflects resilience carried across generations.\n"
        "Stories endure."
    ),
    (
        "Life in Gaza continues with determination.\n"
        "Hope remains steady."
    ),
    (
        "Gaza stands as a community bound by shared experience.\n"
        "Identity remains rooted."
    ),
    (
        "In Gaza, everyday moments still bring meaning.\n"
        "Connection shapes perspective."
    ),
    (
        "Gaza carries heritage through time.\n"
        "Families preserve their legacy."
    ),
    (
        "Within Gaza, strength is often quiet.\n"
        "Resilience defines daily life."
    ),
    (
        "Gaza reflects attachment to home.\n"
        "Belonging endures."
    ),
    (
        "In Gaza, community ties create stability.\n"
        "Support fosters resilience."
    ),
    (
        "Gaza holds stories worth listening to.\n"
        "Human experiences matter."
    ),
    (
        "Families in Gaza continue traditions.\n"
        "Culture remains alive."
    ),
    (
        "Gaza reflects shared endurance.\n"
        "Hope continues forward."
    ),
    (
        "In Gaza, daily life carries quiet strength.\n"
        "Community sustains identity."
    ),
    (
        "Gaza stands within collective reflection.\n"
        "Stories shape understanding."
    ),
    (
        "Life in Gaza includes perseverance.\n"
        "Belonging remains constant."
    ),
    (
        "Gaza reflects deep-rooted heritage.\n"
        "Tradition guides generations."
    ),
    (
        "In Gaza, resilience is woven into daily life.\n"
        "Families support one another."
    ),
    (
        "Gaza carries continuity through memory.\n"
        "Experience shapes identity."
    ),
    (
        "Within Gaza, shared history connects people.\n"
        "Community remains essential."
    ),
    (
        "Gaza reflects determination shaped by circumstance.\n"
        "Hope continues."
    ),
    (
        "In Gaza, belonging is tied to family.\n"
        "Connection endures."
    ),
    (
        "Gaza remains a place of cultural depth.\n"
        "Identity persists."
    ),
    (
        "Life in Gaza reflects unity.\n"
        "Shared strength sustains hope."
    ),
    (
        "Gaza carries stories of daily perseverance.\n"
        "Memory keeps them alive."
    ),
    (
        "In Gaza, neighbors rely on each other.\n"
        "Community creates resilience."
    ),
    (
        "Gaza stands as a testament to endurance.\n"
        "Families continue forward."
    ),
    (
        "Within Gaza, hope remains present.\n"
        "Belonging shapes perspective."
    ),
    (
        "Gaza reflects strong community roots.\n"
        "Identity continues."
    ),
    (
        "In Gaza, shared experience builds understanding.\n"
        "Connection remains powerful."
    ),
    (
        "Gaza carries generational memory.\n"
        "Stories endure."
    ),
    (
        "Life in Gaza includes determination.\n"
        "Resilience defines daily moments."
    ),
    (
        "Gaza reflects attachment to heritage.\n"
        "Tradition remains central."
    ),
    (
        "In Gaza, support networks sustain families.\n"
        "Community matters deeply."
    ),
    (
        "Gaza stands as a place of lived reality.\n"
        "Human stories continue."
    ),
    (
        "Within Gaza, identity grows from shared history.\n"
        "Belonging persists."
    ),
    (
        "Gaza reflects perseverance across generations.\n"
        "Memory ensures continuity."
    ),
    (
        "In Gaza, everyday life continues with resolve.\n"
        "Hope remains steady."
    ),
    (
        "Gaza carries meaningful traditions.\n"
        "Culture shapes identity."
    ),
    (
        "Families in Gaza maintain strong bonds.\n"
        "Connection sustains resilience."
    ),
    (
        "Gaza reflects the importance of home.\n"
        "Belonging remains powerful."
    ),
    (
        "In Gaza, unity creates strength.\n"
        "Community continues forward."
    ),
    (
        "Gaza holds a place in collective awareness.\n"
        "Stories matter."
    ),
    (
        "Life in Gaza reflects cultural continuity.\n"
        "Identity endures."
    ),
    (
        "Gaza carries experiences that shape generations.\n"
        "Memory persists."
    ),
    (
        "In Gaza, resilience appears in daily acts.\n"
        "Hope continues."
    ),
    (
        "Gaza stands within shared history.\n"
        "Belonging remains steady."
    ),
    (
        "Within Gaza, families value connection.\n"
        "Community defines identity."
    ),
    (
        "Gaza reflects strength shaped by unity.\n"
        "Support carries people forward."
    ),
    (
        "In Gaza, heritage remains alive.\n"
        "Tradition guides belonging."
    ),
    (
        "Gaza continues as a place of community.\n"
        "Life moves forward each day."
    ),
    (
        "Gaza reflects determination and endurance.\n"
        "Families sustain hope."
    ),
    (
        "In Gaza, memory shapes identity.\n"
        "Belonging persists."
    ),
    (
        "Gaza carries human stories beyond statistics.\n"
        "Experience matters."
    ),
    (
        "Life in Gaza remains grounded in community.\n"
        "Connection endures."
    ),
    (
        "Gaza stands as a reminder of shared humanity.\n"
        "Hope continues forward."
    )
                (
    "Gaza wakes each morning with determination.\n"
    "Life continues through shared strength."
),
(
    "In Gaza, community remains a source of stability.\n"
    "Connection shapes daily life."
),
(
    "Gaza carries stories shaped by lived experience.\n"
    "Memory preserves those moments."
),
(
    "Families in Gaza hold tightly to tradition.\n"
    "Heritage sustains belonging."
),
(
    "Gaza reflects resilience found in unity.\n"
    "Support builds endurance."
),
(
    "Beyond the news, Gaza is a place of people.\n"
    "Everyday life continues."
),
(
    "In Gaza, neighbors rely on one another.\n"
    "Community strengthens hope."
),
(
    "Gaza stands with quiet perseverance.\n"
    "Identity remains rooted."
),
(
    "Daily routines in Gaza carry meaning.\n"
    "Connection defines perspective."
),
(
    "Gaza reflects courage within ordinary moments.\n"
    "Life moves forward steadily."
),
(
    "In Gaza, shared history shapes understanding.\n"
    "Memory sustains identity."
),
(
    "Gaza remains present in collective awareness.\n"
    "Human stories matter."
),
(
    "Families in Gaza preserve their cultural voice.\n"
    "Tradition guides generations."
),
(
    "Gaza reflects endurance through time.\n"
    "Belonging persists."
),
(
    "In Gaza, attachment to home remains strong.\n"
    "Roots define identity."
),
(
    "Gaza carries experiences that connect generations.\n"
    "Memory bridges time."
),
(
    "Within Gaza, unity creates resilience.\n"
    "Community sustains hope."
),
(
    "Gaza stands as a place of human connection.\n"
    "Shared life continues."
),
(
    "In Gaza, cultural depth remains visible.\n"
    "Identity grows from heritage."
),
(
    "Gaza reflects the strength of family bonds.\n"
    "Support remains constant."
),
(
    "Life in Gaza continues despite challenges.\n"
    "Hope finds its place."
),
(
    "Gaza holds stories worth hearing.\n"
    "Experience shapes perspective."
),
(
    "In Gaza, belonging is tied to shared memory.\n"
    "Connection remains central."
),
(
    "Gaza reflects resilience carried quietly.\n"
    "Communities endure together."
),
(
    "Families in Gaza value togetherness.\n"
    "Unity defines daily life."
),
(
    "Gaza stands within generational memory.\n"
    "Identity persists."
),
(
    "In Gaza, everyday acts reflect determination.\n"
    "Life continues forward."
),
(
    "Gaza carries continuity through culture.\n"
    "Tradition keeps identity alive."
),
(
    "Within Gaza, shared meals create connection.\n"
    "Community remains strong."
),
(
    "Gaza reflects perseverance shaped by experience.\n"
    "Belonging endures."
),
(
    "In Gaza, resilience appears in small details.\n"
    "Hope remains steady."
),
(
    "Gaza remains rooted in collective identity.\n"
    "Memory sustains belonging."
),
(
    "Families in Gaza continue forward with dignity.\n"
    "Strength is often quiet."
),
(
    "Gaza reflects the importance of community.\n"
    "Connection sustains daily life."
),
(
    "In Gaza, heritage shapes understanding.\n"
    "Identity continues across generations."
),
(
    "Gaza carries moments of reflection.\n"
    "Human experiences define it."
),
(
    "Within Gaza, cultural expression persists.\n"
    "Belonging remains visible."
),
(
    "Gaza stands as a reminder of shared humanity.\n"
    "Community matters deeply."
),
(
    "In Gaza, resilience is part of everyday reality.\n"
    "Life moves ahead."
),
(
    "Gaza reflects unity within families.\n"
    "Connection strengthens perspective."
),
(
    "Families in Gaza keep traditions alive.\n"
    "Heritage sustains identity."
),
(
    "Gaza continues through collective strength.\n"
    "Hope finds continuity."
),
(
    "In Gaza, shared stories connect generations.\n"
    "Memory endures."
),
(
    "Gaza reflects determination in daily life.\n"
    "Belonging remains central."
),
(
    "Within Gaza, support systems remain strong.\n"
    "Community defines resilience."
),
(
    "Gaza carries history within living memory.\n"
    "Identity grows from experience."
),
(
    "In Gaza, cultural roots remain steady.\n"
    "Tradition shapes belonging."
),
(
    "Gaza stands with enduring presence.\n"
    "Human connection continues."
),
(
    "Life in Gaza includes perseverance.\n"
    "Hope remains grounded."
),
(
    "Gaza reflects shared endurance.\n"
    "Families sustain one another."
),
(
    "In Gaza, everyday life carries quiet strength.\n"
    "Community remains essential."
),
(
    "Gaza holds collective memories.\n"
    "Identity persists."
),
(
    "Within Gaza, unity shapes resilience.\n"
    "Belonging continues."
),
(
    "Gaza reflects attachment to heritage.\n"
    "Roots remain firm."
),
(
    "In Gaza, life moves forward with resolve.\n"
    "Connection sustains hope."
),
(
    "Gaza carries generational continuity.\n"
    "Stories remain alive."
),
(
    "Families in Gaza nurture belonging.\n"
    "Community defines identity."
),
(
    "Gaza reflects determination shaped by reality.\n"
    "Hope continues."
),
(
    "In Gaza, resilience grows through togetherness.\n"
    "Support remains constant."
),
(
    "Gaza stands within cultural memory.\n"
    "Identity remains rooted."
),
(
    "Life in Gaza continues steadily.\n"
    "Belonging persists."
),
(
    "Gaza reflects strength within community ties.\n"
    "Connection shapes perspective."
),
(
    "In Gaza, heritage informs daily life.\n"
    "Tradition guides generations."
),
(
    "Gaza carries shared experience.\n"
    "Memory sustains identity."
),
(
    "Within Gaza, families uphold their legacy.\n"
    "Belonging remains meaningful."
),
(
    "Gaza reflects unity in the face of challenge.\n"
    "Community builds resilience."
),
(
    "In Gaza, daily acts show perseverance.\n"
    "Life continues forward."
),
(
    "Gaza stands as a place of human stories.\n"
    "Experience matters."
),
(
    "Families in Gaza find strength together.\n"
    "Connection endures."
),
(
    "Gaza reflects cultural richness.\n"
    "Identity remains alive."
),
(
    "In Gaza, belonging is woven into daily life.\n"
    "Roots sustain perspective."
),
(
    "Gaza carries depth shaped by memory.\n"
    "Stories endure."
),
(
    "Within Gaza, unity defines community.\n"
    "Hope continues."
),
(
    "Gaza reflects perseverance across time.\n"
    "Identity persists."
),
(
    "In Gaza, connection remains powerful.\n"
    "Belonging guides daily life."
),
(
    "Gaza stands grounded in heritage.\n"
    "Tradition sustains resilience."
),
(
    "Life in Gaza continues with quiet courage.\n"
    "Community matters."
),
(
    "Gaza reflects collective strength.\n"
    "Families move forward."
),
(
    "In Gaza, shared memory builds identity.\n"
    "Belonging remains firm."
),
(
    "Gaza carries lived experience.\n"
    "Hope persists."
),
(
    "Within Gaza, resilience shapes perspective.\n"
    "Connection endures."
),
(
    "Gaza reflects cultural continuity.\n"
    "Identity remains steady."
),
(
    "In Gaza, daily life moves ahead with resolve.\n"
    "Community sustains hope."
),
(
    "Gaza stands within shared heritage.\n"
    "Belonging continues."
),
(
    "Families in Gaza hold onto unity.\n"
    "Strength grows from connection."
),
(
    "Gaza reflects perseverance carried quietly.\n"
    "Identity persists."
),
(
    "In Gaza, roots remain meaningful.\n"
    "Memory sustains belonging."
),
(
    "Gaza carries forward through community bonds.\n"
    "Hope remains."
),
(
    "Within Gaza, everyday life continues.\n"
    "Resilience defines it."
),
(
    "Gaza reflects the endurance of human spirit.\n"
    "Belonging persists."
),
(
    "In Gaza, heritage shapes tomorrow.\n"
    "Connection remains strong."
),
(
    "Gaza stands as part of shared humanity.\n"
    "Life continues forward."
)

]
        },
        "hashtags": {
            "base": [
                "#Gaza",
                "#StandWithGaza",
                "#GazaVoices",
            ],
           "extra": [
    "#Gaza",
    "#GazaVoices",
    "#LifeInGaza",
    "#GazaCommunity",
    "#GazaStories",
    "#GazaResilience",
    "#GazaHope",
    "#GazaFamilies",
    "#GazaHeritage",
    "#GazaIdentity",
    "#GazaCulture",
    "#GazaLife",
    "#GazaHumanStories",
    "#GazaDailyLife",
    "#GazaTogether",
    "#GazaUnity",
    "#GazaConnection",
    "#GazaBelonging",
    "#GazaRoots",
    "#GazaTradition",
    "#GazaMemory",
    "#GazaContinuity",
    "#GazaStrength",
    "#GazaEndurance",
    "#GazaCommunityStrong",
    "#VoicesFromGaza",
    "#StoriesOfGaza",
    "#GazaPerspective",
    "#GazaAwareness",
    "#GazaPresence",
    "#GazaAcrossGenerations",
    "#GazaHumanity",
    "#GazaSpirit",
    "#GazaSupport",
    "#GazaReflection",
    "#GazaCulturalVoice",
    "#GazaTogetherness",
    "#GazaNeighborhoods",
    "#GazaSharedStories",
    "#GazaCollective",
    "#GazaResilientVoices",
    "#GazaFamilyBonds",
    "#GazaHeritageLives",
    "#GazaIdentityMatters",
    "#GazaNarratives",
    "#GazaCommunityVoices",
    "#GazaSolidarity",
    "#GazaCulturalRoots",
    "#GazaHopeLives",
    "#GazaHumanConnection",
    "#StandWithGaza",
    "#SupportGaza",
    "#GazaMatters",
    "#GazaToday",
    "#GazaFuture",
    "#GazaYouth",
    "#GazaChildren",
    "#GazaWomen",
    "#GazaMen",
    "#GazaHome",
    "#GazaVoicesMatter",
    "#GazaTogetherWeStand",
    "#GazaLifeMatters",
    "#GazaPeace",
    "#GazaDignity",
    "#GazaCommunitySupport",
    "#GazaCare",
    "#GazaInFocus",
    "#GazaReality",
    "#GazaStrengthTogether",
    "#GazaHumanRights",
    "#GazaSharedHumanity",
    "#GazaBelongs",
    "#GazaResilienceStory",
    "#GazaGlobalVoices",
    "#GazaAcrossBorders",
    "#GazaConnectionLives",
    "#GazaCulturalContinuity",
    "#GazaLivesOn",
    "#GazaStory",
    "#GazaVoice",
    "#GazaPresenceMatters",
    "#GazaCommunityFirst",
    "#GazaHeritageMatters",
    "#GazaRootsRemain",
    "#GazaMemoryLives",
    "#GazaCollectiveVoice",
    "#GazaUnityStrong",
    "#GazaTogetherStrong",
    "#GazaDailyVoices",
    "#GazaCommunityLife",
    "#GazaEnduringSpirit",
    "#GazaHumanStoriesMatter",
    "#GazaCultureLives",
    "#GazaSharedHope",
    "#GazaConnected",
    "#GazaContinues",
    "#GazaLivesMatter"
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
        "Historical maps preserve names across generations.\n"
        "They quietly document continuity through time."
    ),
    (
        "Old maps reflect stories beyond borders.\n"
        "They carry memory in printed lines."
    ),
    (
        "Maps often reveal how places were once understood.\n"
        "History remains visible through geography."
    ),
    (
        "Through maps, past landscapes remain remembered.\n"
        "Names endure on paper."
    ),
    (
        "Archival maps connect the present with earlier eras.\n"
        "They capture moments in time."
    ),
    (
        "Maps preserve details that memory recognizes.\n"
        "They become silent witnesses of history."
    ),
    (
        "In historical maps, geography meets narrative.\n"
        "Each label carries context."
    ),
    (
        "Maps offer insight into how places were recorded.\n"
        "They reflect continuity and change."
    ),
    (
        "Old cartography keeps historical names alive.\n"
        "Printed lines hold meaning."
    ),
    (
        "Maps serve as visual archives.\n"
        "They document landscapes through time."
    ),
    (
        "Across decades, maps trace evolving borders.\n"
        "They preserve geographical memory."
    ),
    (
        "Historical maps provide perspective on the past.\n"
        "They reflect recorded identity."
    ),
    (
        "Maps capture more than terrain.\n"
        "They hold traces of heritage."
    ),
    (
        "Through cartography, history becomes visible.\n"
        "Names remain documented."
    ),
    (
        "Maps reflect how regions were once described.\n"
        "They preserve recorded context."
    ),
    (
        "Old maps carry continuity in ink.\n"
        "They connect generations visually."
    ),
    (
        "Cartographic archives maintain historical reference.\n"
        "Geography becomes documentation."
    ),
    (
        "Maps reveal layers of recorded time.\n"
        "Each edition reflects its era."
    ),
    (
        "Historical mapping preserves geographical memory.\n"
        "Printed detail carries significance."
    ),
    (
        "Maps stand as records of past understanding.\n"
        "They document continuity."
    ),
    (
        "Through preserved maps, earlier landscapes remain visible.\n"
        "History finds form in lines."
    ),
    (
        "Maps reflect how places were identified.\n"
        "Names become part of record."
    ),
    (
        "Cartography offers structured memory.\n"
        "Geography holds narrative."
    ),
    (
        "Maps capture the language of place.\n"
        "Printed names endure."
    ),
    (
        "Historical maps trace continuity across time.\n"
        "They connect past and present."
    ),
    (
        "Maps quietly preserve identity through labeling.\n"
        "Documentation shapes understanding."
    ),
    (
        "In archived maps, history is structured visually.\n"
        "Geography reflects memory."
    ),
    (
        "Maps maintain the record of how regions appeared.\n"
        "They reflect historical context."
    ),
    (
        "Old atlases hold layers of recorded perspective.\n"
        "Each page carries continuity."
    ),
    (
        "Maps offer evidence of earlier documentation.\n"
        "Names remain printed."
    ),
    (
        "Through maps, shifts in geography are observed.\n"
        "Time leaves visible traces."
    ),
    (
        "Historical cartography preserves spatial memory.\n"
        "Ink records identity."
    ),
    (
        "Maps reflect recorded belonging.\n"
        "They hold context within boundaries."
    ),
    (
        "In old maps, geography speaks softly.\n"
        "History remains outlined."
    ),
    (
        "Maps document how places were referenced.\n"
        "Names carry continuity."
    ),
    (
        "Cartographic records preserve structured history.\n"
        "Landscapes remain visible."
    ),
    (
        "Maps connect archives with living memory.\n"
        "They bridge time visually."
    ),
    (
        "Through preserved maps, earlier designations remain clear.\n"
        "Documentation sustains identity."
    ),
    (
        "Maps reflect historical terminology.\n"
        "Printed references endure."
    ),
    (
        "Old maps maintain continuity of recorded names.\n"
        "They hold structured memory."
    ),
    (
        "Maps provide context beyond coordinates.\n"
        "They reveal recorded narrative."
    ),
    (
        "Cartography captures a snapshot of its era.\n"
        "Geography becomes archive."
    ),
    (
        "Maps serve as quiet documentation of place.\n"
        "History remains printed."
    ),
    (
        "Through maps, the evolution of borders is visible.\n"
        "Time reshapes lines."
    ),
    (
        "Historical maps preserve language tied to geography.\n"
        "Names remain inscribed."
    ),
    (
        "Maps reflect how space was defined.\n"
        "Documentation holds continuity."
    ),
    (
        "In archived maps, recorded identity remains accessible.\n"
        "Ink preserves context."
    ),
    (
        "Maps capture recorded spatial understanding.\n"
        "History becomes structured."
    ),
    (
        "Old cartographic works reveal layered perspective.\n"
        "Each edition reflects its moment."
    ),
    (
        "Maps maintain visual memory of landscapes.\n"
        "Printed lines endure."
    ),
    (
        "Through historical maps, context remains visible.\n"
        "Geography reflects recorded time."
    ),
    (
        "Maps preserve official designations of place.\n"
        "Documentation shapes narrative."
    ),
    (
        "Cartography documents structured geography.\n"
        "Identity remains labeled."
    ),
    (
        "Maps connect present viewers with past records.\n"
        "They offer perspective."
    ),
    (
        "Historical atlases maintain continuity through pages.\n"
        "Geography remains documented."
    ),
    (
        "Maps reveal recorded presence through naming.\n"
        "Ink holds continuity."
    ),
    (
        "Through maps, archived geography becomes accessible.\n"
        "History remains outlined."
    ),
    (
        "Maps quietly store structured memory.\n"
        "Documentation sustains visibility."
    ),
    (
        "Old maps reflect earlier frameworks of understanding.\n"
        "Time is visible in detail."
    ),
    (
        "Maps maintain documented spatial identity.\n"
        "Geography remains structured."
    ),
    (
        "Historical mapping keeps archived terminology alive.\n"
        "Names endure across editions."
    ),
    (
        "Maps reflect continuity despite changing borders.\n"
        "Documentation preserves context."
    ),
    (
        "Through cartography, recorded landscapes remain present.\n"
        "History holds form."
    ),
    (
        "Maps stand as references of recorded eras.\n"
        "Geography retains memory."
    ),
    (
        "Old maps keep documentation accessible.\n"
        "Printed names endure."
    ),
    (
        "Maps preserve the framework of historical geography.\n"
        "Identity remains labeled."
    ),
    (
        "Through archived maps, the past remains traceable.\n"
        "Ink holds perspective."
    ),
    (
        "Maps reflect official record at specific moments.\n"
        "Time becomes visible."
    ),
    (
        "Cartography connects documentation with geography.\n"
        "Memory remains structured."
    ),
    (
        "Maps offer continuity through recorded detail.\n"
        "Landscapes remain visible."
    ),
    (
        "Historical maps preserve context beyond borders.\n"
        "They maintain recorded reference."
    ),
    (
        "Maps document structured naming of regions.\n"
        "Continuity remains clear."
    ),
    (
        "Through maps, spatial identity is archived.\n"
        "History holds shape."
    ),
    (
        "Old maps capture official perspectives of their era.\n"
        "Documentation remains intact."
    ),
    (
        "Maps preserve structured understanding of place.\n"
        "Ink keeps record."
    ),
    (
        "Cartography offers visual continuity across time.\n"
        "Geography becomes archive."
    ),
    (
        "Maps reflect how land was once organized.\n"
        "Recorded names endure."
    ),
    (
        "Historical maps maintain documented terminology.\n"
        "Continuity persists."
    ),
    (
        "Maps hold structured traces of earlier periods.\n"
        "Time remains visible."
    ),
    (
        "Through maps, the documentation of place survives.\n"
        "Geography reflects record."
    ),
    (
        "Maps connect viewers to archived context.\n"
        "Identity remains labeled."
    ),
    (
        "Old maps preserve reference points across decades.\n"
        "Printed detail holds memory."
    ),
    (
        "Maps reflect recorded geography in structured form.\n"
        "Continuity becomes visible."
    ),
    (
        "Cartographic archives sustain historical reference.\n"
        "Names remain documented."
    ),
    (
        "Maps reveal continuity in spatial identity.\n"
        "History stays outlined."
    ),
    (
        "Through maps, earlier geographic labels remain clear.\n"
        "Documentation persists."
    ),
    (
        "Maps preserve structured context of their era.\n"
        "Time becomes visible in ink."
    ),
    (
        "Historical maps maintain documented presence.\n"
        "Geography holds record."
    ),
    (
        "Maps reflect continuity through archived detail.\n"
        "Names remain inscribed."
    ),
    (
        "Through cartography, spatial history is preserved.\n"
        "Identity remains visible."
    ),
    (
        "Maps document the recorded understanding of land.\n"
        "Continuity remains structured."
    ),
    (
        "Old maps connect generations through visual archive.\n"
        "Geography holds memory."
    ),
    (
        "Maps preserve official geographic reference.\n"
        "History remains printed."
    ),
    (
        "Through archived cartography, time remains traceable.\n"
        "Documentation sustains identity."
    ),
    (
        "Maps reflect recorded perspective across eras.\n"
        "Continuity endures."
    ),
    (
        "Historical maps maintain the visibility of place names.\n"
        "Ink preserves context."
    )
(
    "Maps preserve geographic references across time.\n"
    "They quietly reflect recorded history."
),
(
    "Historical maps maintain visual continuity.\n"
    "Names remain documented in print."
),
(
    "Old maps provide structured insight into the past.\n"
    "Geography becomes archive."
),
(
    "Maps capture official designations of their era.\n"
    "History is outlined in ink."
),
(
    "Through cartography, earlier landscapes stay visible.\n"
    "Documentation preserves context."
),
(
    "Maps reflect how territories were once defined.\n"
    "Recorded detail endures."
),
(
    "Archived maps maintain the language of place.\n"
    "Names carry historical continuity."
),
(
    "Maps offer perspective on geographic evolution.\n"
    "Borders shift, records remain."
),
(
    "Old atlases connect generations visually.\n"
    "Printed lines hold memory."
),
(
    "Maps preserve structured references to land.\n"
    "Time leaves traces on paper."
),
(
    "Historical cartography reflects documented identity.\n"
    "Geography remains visible."
),
(
    "Maps quietly store recorded terminology.\n"
    "Continuity persists through editions."
),
(
    "Through maps, past designations remain traceable.\n"
    "Documentation shapes understanding."
),
(
    "Maps capture how regions were historically labeled.\n"
    "Names endure across decades."
),
(
    "Cartographic archives preserve official references.\n"
    "Ink safeguards context."
),
(
    "Maps maintain spatial documentation of their time.\n"
    "History becomes structured."
),
(
    "Old maps reveal recorded frameworks of geography.\n"
    "Continuity stays visible."
),
(
    "Maps reflect formal geographic records.\n"
    "Printed detail holds significance."
),
(
    "Through preserved maps, spatial memory survives.\n"
    "Time is mapped in lines."
),
(
    "Historical maps document naming conventions.\n"
    "Continuity remains printed."
),
(
    "Maps preserve recorded landscapes.\n"
    "Geography connects past and present."
),
(
    "Cartography captures official views of space.\n"
    "Documentation keeps perspective alive."
),
(
    "Maps reflect archived geographic structure.\n"
    "Names remain inscribed."
),
(
    "Old maps maintain reference points across eras.\n"
    "History stays visible."
),
(
    "Maps serve as visual records of documentation.\n"
    "Time becomes traceable."
),
(
    "Through cartography, spatial context is preserved.\n"
    "Identity remains outlined."
),
(
    "Maps document the formal organization of land.\n"
    "Continuity endures."
),
(
    "Historical maps connect printed record to geography.\n"
    "Memory holds shape."
),
(
    "Maps preserve official geographic terminology.\n"
    "Ink sustains documentation."
),
(
    "Old cartographic works reflect structured identity.\n"
    "Names remain recorded."
),
(
    "Maps reveal geographic understanding of earlier periods.\n"
    "Time appears in boundaries."
),
(
    "Through maps, archived context becomes visible.\n"
    "Documentation bridges generations."
),
(
    "Maps maintain continuity of printed reference.\n"
    "History remains accessible."
),
(
    "Historical atlases reflect recorded organization.\n"
    "Geography holds continuity."
),
(
    "Maps preserve documented naming of regions.\n"
    "Identity remains labeled."
),
(
    "Through cartography, the past stays outlined.\n"
    "Ink records perspective."
),
(
    "Maps capture structured geographic history.\n"
    "Continuity appears in print."
),
(
    "Old maps maintain visible record of change.\n"
    "Borders tell a story."
),
(
    "Maps reflect the official record of land.\n"
    "Documentation sustains clarity."
),
(
    "Through preserved maps, earlier contexts remain intact.\n"
    "Geography reflects time."
),
(
    "Maps serve as references of recorded eras.\n"
    "Continuity endures."
),
(
    "Historical maps keep spatial terminology alive.\n"
    "Names remain documented."
),
(
    "Maps maintain visual evidence of geography.\n"
    "Ink preserves memory."
),
(
    "Through cartography, structured documentation survives.\n"
    "Identity stays visible."
),
(
    "Maps reveal recorded spatial identity.\n"
    "History becomes structured."
),
(
    "Old maps provide access to archived context.\n"
    "Continuity remains present."
),
(
    "Maps preserve formal geographic outlines.\n"
    "Documentation remains steady."
),
(
    "Historical mapping reflects recorded designations.\n"
    "Names endure."
),
(
    "Maps capture layers of geographic documentation.\n"
    "Time leaves its imprint."
),
(
    "Through maps, archived landscapes remain traceable.\n"
    "Ink carries continuity."
),
(
    "Maps maintain structured geographic reference.\n"
    "History stays outlined."
),
(
    "Old maps preserve terminology across decades.\n"
    "Documentation connects eras."
),
(
    "Maps reflect recorded presence in space.\n"
    "Identity holds shape."
),
(
    "Through cartography, formal naming remains visible.\n"
    "Continuity persists."
),
(
    "Maps document spatial organization clearly.\n"
    "Time becomes readable."
),
(
    "Historical maps connect documentation with geography.\n"
    "Memory remains printed."
),
(
    "Maps preserve continuity of reference points.\n"
    "History stays accessible."
),
(
    "Old atlases reflect structured geographic identity.\n"
    "Ink safeguards context."
),
(
    "Maps reveal recorded classification of land.\n"
    "Names remain visible."
),
(
    "Through preserved maps, spatial continuity is traceable.\n"
    "Documentation remains intact."
),
(
    "Maps maintain clarity of geographic record.\n"
    "Time holds form."
),
(
    "Historical cartography preserves official references.\n"
    "Continuity endures."
),
(
    "Maps reflect documented naming conventions.\n"
    "Identity stays labeled."
),
(
    "Through maps, archived geography connects generations.\n"
    "Ink sustains record."
),
(
    "Maps preserve structured depiction of place.\n"
    "History remains outlined."
),
(
    "Old maps keep documented identity accessible.\n"
    "Continuity persists."
),
(
    "Maps reveal layers of recorded geographic change.\n"
    "Time reshapes lines."
),
(
    "Through cartography, printed geography survives.\n"
    "Documentation remains visible."
),
(
    "Maps maintain spatial identity in structured form.\n"
    "Names hold continuity."
),
(
    "Historical maps reflect archived designations.\n"
    "Ink preserves perspective."
),
(
    "Maps connect visual record with geographic context.\n"
    "History remains structured."
),
(
    "Old maps document formal geographic boundaries.\n"
    "Continuity stays visible."
),
(
    "Maps preserve official labeling of regions.\n"
    "Time becomes readable."
),
(
    "Through maps, earlier documentation remains clear.\n"
    "Identity persists."
),
(
    "Maps reflect continuity in geographic reference.\n"
    "Printed detail endures."
),
(
    "Historical maps maintain visibility of place names.\n"
    "Documentation bridges time."
),
(
    "Maps capture recorded spatial frameworks.\n"
    "History holds form."
),
(
    "Old cartography preserves archived naming.\n"
    "Continuity remains."
),
(
    "Maps maintain geographic record across editions.\n"
    "Ink sustains clarity."
),
(
    "Through preserved maps, context remains accessible.\n"
    "Time leaves outline."
),
(
    "Maps reflect documented territorial understanding.\n"
    "Identity stays visible."
),
(
    "Historical maps preserve official terminology.\n"
    "Continuity persists."
),
(
    "Maps reveal structured spatial documentation.\n"
    "History remains traceable."
),
(
    "Old maps connect recorded past with present viewers.\n"
    "Ink carries continuity."
),
(
    "Maps maintain printed memory of landscapes.\n"
    "Documentation sustains perspective."
),
(
    "Through cartography, geographic identity remains structured.\n"
    "Names endure."
),
(
    "Maps preserve archived representation of land.\n"
    "Continuity remains steady."
),
(
    "Historical maps document organized geography.\n"
    "Time remains visible."
),
(
    "Maps reflect continuity of recorded space.\n"
    "Identity stays outlined."
),
(
    "Old maps maintain documented presence of regions.\n"
    "Ink preserves clarity."
),
(
    "Maps serve as structured references of geography.\n"
    "History remains accessible."
),
(
    "Through preserved atlases, spatial continuity survives.\n"
    "Documentation connects eras."
),
(
    "Maps capture official geographic record.\n"
    "Continuity remains visible."
),
(
    "Historical maps keep naming visible across time.\n"
    "Ink sustains memory."
),
(
    "Maps preserve documentation through structured design.\n"
    "Identity remains labeled."
),
(
    "Through cartography, the record of place endures.\n"
    "Time remains outlined."
)

]
        },
        "hashtags": {
            "base": [
                "#HistoricalMaps",
                "#Archive",
                "#DocumentedHistory",
            ],
           "extra": [
    "#HistoricalMaps",
    "#MapsThroughTime",
    "#Cartography",
    "#MapArchives",
    "#OldMaps",
    "#MapsOfHistory",
    "#GeographyThroughTime",
    "#HistoricalCartography",
    "#MapPreservation",
    "#CartographyLegacy",
    "#MapsAndMemory",
    "#GeographyRecords",
    "#ArchivedMaps",
    "#MappingHistory",
    "#MapsDocumentHistory",
    "#CartographicRecords",
    "#HistoricalGeography",
    "#MapHeritage",
    "#MemoryThroughMaps",
    "#MapsOfThePast",
    "#MapStories",
    "#CartographyArchive",
    "#GeographicLegacy",
    "#MapsAndHeritage",
    "#HistoricAtlas",
    "#DocumentedMaps",
    "#TimeThroughMaps",
    "#MapCollections",
    "#MapsAndMemoryMatters",
    "#MapsMatter",
    "#HistoricalMapping",
    "#MapsPreserveHistory",
    "#CartographyThroughTime",
    "#GeographyLegacy",
    "#MapsAndCulture",
    "#HistoricalRecords",
    "#MapDocumentation",
    "#MapsOfRegions",
    "#PreserveMaps",
    "#MapResearch",
    "#MapStudy",
    "#HistoricalAtlasCollection",
    "#ArchiveMaps",
    "#MapsAndIdentity",
    "#MapsAcrossGenerations",
    "#MapsOfHeritage",
    "#HistoricalGeographyRecords",
    "#MapsAndContinuity",
    "#MappingMemory",
    "#CartographicHeritage",
    "#HistoricalMapsMatter",
    "#MapsPreserveCulture",
    "#MapsAndHistory",
    "#GeographyArchives",
    "#MapPreservationMatters",
    "#MapsAcrossTime",
    "#MapsAndLegends",
    "#OldCartography",
    "#MapsLegacy",
    "#MapMemory",
    "#HistoricalMappingRecords",
    "#MapsAndDocumentation",
    "#MapPreserve",
    "#CartographyLegacyMatters",
    "#GeographicMemory",
    "#MapsAndPast",
    "#MapsReflectHistory",
    "#PreservedMaps",
    "#MapIdentity",
    "#HistoricalAtlasMatters",
    "#MapsAndTime",
    "#MapsThroughGenerations",
    "#MappingLegacy",
    "#MapArchivesMatter",
    "#MapsAndContinuity",
    "#HistoricalPlacesMaps",
    "#MapStoriesMatter",
    "#PreserveCartography",
    "#MapResearchMatters",
    "#MapsAndCulturalHeritage",
    "#MapsAndDocumentationMatters",
    "#MapsAcrossRegions",
    "#HistoricMapsCollection",
    "#MapsAndPreservation",
    "#MappingHeritage",
    "#MapsMatterAcrossTime",
    "#MapsAndRecord",
    "#HistoricCartography",
    "#MapsForHistory",
    "#MapsAndIdentityMatters",
    "#MappingThePast",
    "#MapsAcrossGenerationsMatter",
    "#MapsAndHumanMemory",
    "#MapsAndHistoricalContext",
    "#MapsThroughAges",
    "#MapsAndContinuityMatters",
    "#MapsAndCulturePreservation",
    "#HistoricalMapsCollection",
    "#MapsLegacyMatters",
    "#MapHeritageMatters",
    "#MapsPreserveIdentity",
    "#MapsAndHistoricalStudy",
    "#MapsAndMemoryPreservation",
    "#MappingHistoryMatters",
    "#HistoricMapsArchives",
    "#MapsAndGeographyLegacy"

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
    "Everyone faces daily challenges.\n"
    "Patience and hope help us move forward."
),
(
    "Difficult times teach us inner strength.\n"
    "Support from others eases the burden."
),
(
    "Every hard experience carries a lesson.\n"
    "Resilience gives us the ability to continue."
),
(
    "Challenges are a natural part of life.\n"
    "Hope always lights the way."
),
(
    "In tough moments, human connections matter.\n"
    "Mutual support strengthens the soul."
),
(
    "Suffering teaches us empathy for others.\n"
    "Understanding and kindness lighten the pain."
),
(
    "Life is full of ups and downs.\n"
    "Patience gives us the strength to carry on."
),
(
    "Every difficult experience shapes part of who we are.\n"
    "Hope maintains our balance."
),
(
    "Hard moments pass quickly with time.\n"
    "Connection and support make a big difference."
),
(
    "Facing challenges reveals our endurance.\n"
    "Caring for others eases loneliness."
),
(
    "Difficulties make us value simple moments.\n"
    "Gratitude softens suffering."
),
(
    "Daily struggles teach us patience.\n"
    "Family and friends are invaluable support."
),
(
    "Every tough day carries an opportunity for growth.\n"
    "Hope gives us a reason to continue."
),
(
    "In hard times, social bonds are essential.\n"
    "A kind word can lighten the load."
),
(
    "Difficult experiences build character.\n"
    "Optimism illuminates the path."
),
(
    "Patience is the key to overcoming hardships.\n"
    "Mutual support strengthens relationships."
),
(
    "Every small challenge teaches resilience.\n"
    "Hope makes life brighter."
),
(
    "Challenges give us valuable lessons.\n"
    "Compassion helps us move forward."
),
(
    "Life is full of tests.\n"
    "Patience gives us strength to endure."
),
(
    "Every tough experience creates inner strength.\n"
    "Hope keeps our spirit alive."
),
(
    "Hard moments teach appreciation.\n"
    "Support from others eases pain."
),
(
    "Facing suffering requires patience.\n"
    "Hope gives a reason to continue."
),
(
    "Challenges build stronger characters.\n"
    "Mutual support lightens the burden."
),
(
    "Every difficulty teaches a valuable lesson.\n"
    "Hope gives us strength."
),
(
    "Difficult experiences shape resilient personalities.\n"
    "Optimism makes the journey easier."
),
(
    "Patience reduces the weight of challenges.\n"
    "Support from others eases suffering."
),
(
    "Every hard experience brings a learning opportunity.\n"
    "Hope gives extra strength."
),
(
    "Daily challenges shape our character.\n"
    "Compassion lifts the spirit."
),
(
    "Difficulties reveal inner strength.\n"
    "Optimism makes hardships easier to bear."
),
(
    "Every tough experience carries a chance to grow.\n"
    "Social support makes us stronger."
),
(
    "In the face of suffering, human connections are vital.\n"
    "A kind word can ease the pain."
),
(
    "Challenges create resilient personalities.\n"
    "Hope fuels our energy to continue."
),
(
    "Every difficulty carries a lesson.\n"
    "Patience helps us overcome it."
),
(
    "Hard experiences teach us endurance.\n"
    "Support from others makes the journey easier."
),
(
    "Life is full of small and large challenges.\n"
    "Hope lights our path."
),
(
    "Patience reduces the weight of difficulties.\n"
    "Compassion helps us overcome pain."
),
(
    "Every daily challenge shapes our character.\n"
    "Mutual support makes us stronger."
),
(
    "Difficult experiences teach valuable life lessons.\n"
    "Optimism makes the path brighter."
),
(
    "Facing hardship helps us discover resilience.\n"
    "Hope strengthens the spirit."
),
(
    "Even small struggles carry a chance for growth.\n"
    "Support from loved ones eases the load."
),
(
    "Challenges remind us of the value of kindness.\n"
    "Compassion softens pain."
),
(
    "Life tests our patience in many ways.\n"
    "Hope gives us strength to persevere."
),
(
    "Every tough moment teaches gratitude.\n"
    "Mutual support lightens burdens."
),
(
    "Hardships shape resilience within us.\n"
    "Optimism makes life easier."
),
(
    "Facing challenges builds character.\n"
    "Hope helps us move forward."
),
(
    "Even in difficult times, kindness matters.\n"
    "Support lifts the soul."
),
(
    "Daily struggles help us appreciate simple joys.\n"
    "Patience guides the way."
),
(
    "Challenges teach us endurance and empathy.\n"
    "Hope is our companion through it all."
),
(
    "Hard moments test our inner strength.\n"
    "Support from others eases the journey."
),
(
    "Every difficulty carries an opportunity for growth.\n"
    "Optimism helps us continue."
),
(
    "Life's hardships teach resilience.\n"
    "Mutual care lightens the weight."
),
(
    "Facing suffering reveals our capacity to endure.\n"
    "Compassion helps heal."
),
(
    "Challenges shape stronger, wiser people.\n"
    "Hope guides our path."
),
(
    "Even tough experiences have lessons to teach.\n"
    "Support from loved ones brings comfort."
),
(
    "Hard times remind us of the importance of connection.\n"
    "Patience helps us carry on."
),
(
    "Every struggle teaches strength and perseverance.\n"
    "Kindness eases the burden."
),
(
    "Challenges build resilience in daily life.\n"
    "Hope helps us stay motivated."
),
(
    "Difficult experiences create empathy and understanding.\n"
    "Support softens the load."
),
(
    "Even in adversity, we find opportunities to grow.\n"
    "Optimism keeps us moving forward."
),
(
    "Life's challenges strengthen our character.\n"
    "Compassion uplifts the heart."
),
(
    "Every hardship teaches lessons of patience.\n"
    "Hope fuels our endurance."
),
(
    "Difficulties reveal hidden strength within us.\n"
    "Support from others makes us resilient."
),
(
    "Challenges bring growth and understanding.\n"
    "Optimism lights the path ahead."
),
(
    "Hard times help us value the good moments.\n"
    "Patience and care sustain us."
),
(
    "Every struggle strengthens our character.\n"
    "Hope guides us through darkness."
),
(
    "Even small challenges teach resilience.\n"
    "Support and kindness make the journey lighter."
),
(
    "Difficult experiences foster empathy.\n"
    "Optimism provides energy to continue."
),
(
    "Challenges remind us of human connection.\n"
    "Patience helps us persevere."
),
(
    "Life's hardships shape our inner strength.\n"
    "Support eases the load."
),
(
    "Every tough moment teaches a valuable lesson.\n"
    "Hope inspires us to move forward."
),
(
    "Challenges create character and endurance.\n"
    "Compassion makes hardships lighter."
),
(
    "Even in difficult times, we can find growth.\n"
    "Optimism lights the way."
),
(
    "Hard experiences reveal our resilience.\n"
    "Support from loved ones helps carry us."
),
(
    "Life is full of challenges, but hope persists.\n"
    "Patience guides our steps."
),
(
    "Every struggle is a chance to learn and grow.\n"
    "Kindness eases the pain."
),
(
    "Difficult moments teach endurance.\n"
    "Mutual support strengthens us."
),
(
    "Challenges remind us of the value of empathy.\n"
    "Hope sustains the spirit."
),
(
    "Even small hardships teach important lessons.\n"
    "Optimism helps us continue our journey."
),
(
    "Facing difficulties strengthens character.\n"
    "Compassion lifts the heart."
),
(
    "Life's challenges are opportunities to grow.\n"
    "Patience and support help us persevere."
),
(
    "Every struggle teaches resilience and hope.\n"
    "Connection eases the burden."
),
(
    "Hard moments help us appreciate everyday joys.\n"
    "Optimism fuels strength."
),
(
    "Challenges create understanding and empathy.\n"
    "Mutual support carries us forward."
),
(
    "Even in adversity, growth is possible.\n"
    "Hope lights the way."
),
(
    "Difficult experiences teach patience and endurance.\n"
    "Support from others strengthens us."
),
(
    "Challenges build character and resilience.\n"
    "Compassion softens hardships."
),
(
    "Every tough day is a lesson in perseverance.\n"
    "Optimism guides our path."
),
(
    "Life's struggles shape empathy and strength.\n"
    "Hope helps us move forward."
),
(
    "Facing challenges teaches inner resilience.\n"
    "Support eases the journey."
),
(
    "Even small hardships strengthen our character.\n"
    "Patience and optimism keep us going."
),
(
    "Difficult moments foster understanding.\n"
    "Mutual care eases the load."
),
(
    "Challenges help us grow emotionally.\n"
    "Hope and support make life lighter."
)
(
    "Life is full of ups and downs.\n"
    "Every challenge is an opportunity to grow."
),
(
    "Difficult moments test our patience.\n"
    "Compassion helps lighten the burden."
),
(
    "Even small hardships can teach big lessons.\n"
    "Hope gives us the strength to move forward."
),
(
    "Challenges build resilience in our character.\n"
    "Support from loved ones eases the journey."
),
(
    "Every struggle has a purpose.\n"
    "Patience and kindness guide us through."
),
(
    "Hard times can reveal inner strength.\n"
    "Optimism helps us keep going."
),
(
    "Life’s obstacles teach us perseverance.\n"
    "Connection with others softens the load."
),
(
    "Even in tough situations, there is room for growth.\n"
    "Hope lights the path."
),
(
    "Difficult experiences make us wiser.\n"
    "Support from friends brings comfort."
),
(
    "Challenges remind us to value small joys.\n"
    "Patience helps us endure."
),
(
    "Hardships shape resilience and courage.\n"
    "Kindness makes them easier to face."
),
(
    "Every struggle carries a hidden lesson.\n"
    "Optimism gives us energy to continue."
),
(
    "Life tests our patience daily.\n"
    "Mutual support strengthens our spirits."
),
(
    "Difficult moments teach empathy.\n"
    "Hope keeps our hearts open."
),
(
    "Even small challenges help us grow.\n"
    "Patience makes the journey lighter."
),
(
    "Challenges build inner strength.\n"
    "Compassion eases the pain."
),
(
    "Hard times show us what matters most.\n"
    "Support from loved ones sustains us."
),
(
    "Every struggle is an opportunity to learn.\n"
    "Optimism helps us move forward."
),
(
    "Difficulties create resilience.\n"
    "Patience and hope guide our steps."
),
(
    "Life’s challenges make us stronger.\n"
    "Connection with others brings comfort."
),
(
    "Even in hardship, growth is possible.\n"
    "Support softens the journey."
),
(
    "Challenges teach perseverance.\n"
    "Optimism fuels our spirit."
),
(
    "Hard moments develop empathy.\n"
    "Patience helps us endure."
),
(
    "Every struggle strengthens character.\n"
    "Hope gives us courage."
),
(
    "Difficult experiences bring wisdom.\n"
    "Support makes the load lighter."
),
(
    "Life’s obstacles teach resilience.\n"
    "Connection helps us carry on."
),
(
    "Even small hardships have value.\n"
    "Patience and hope guide us."
),
(
    "Challenges reveal inner courage.\n"
    "Compassion lightens our hearts."
),
(
    "Hard times teach life lessons.\n"
    "Optimism helps us move forward."
),
(
    "Every struggle carries opportunity.\n"
    "Support makes challenges easier."
),
(
    "Difficult moments strengthen character.\n"
    "Hope gives us energy to continue."
),
(
    "Life’s obstacles develop patience.\n"
    "Connection eases the burden."
),
(
    "Even tough experiences bring growth.\n"
    "Optimism lights the path."
),
(
    "Challenges teach endurance.\n"
    "Support softens the weight of struggle."
),
(
    "Hard times build inner strength.\n"
    "Patience guides us through."
),
(
    "Every difficulty has a lesson.\n"
    "Hope makes the journey possible."
),
(
    "Difficult experiences reveal resilience.\n"
    "Connection with others gives comfort."
),
(
    "Life’s challenges shape character.\n"
    "Optimism provides energy to keep going."
),
(
    "Even in hardship, patience is key.\n"
    "Support eases the journey."
),
(
    "Challenges build courage and empathy.\n"
    "Hope lights the way."
),
(
    "Hard times show us inner strength.\n"
    "Connection helps us endure."
),
(
    "Every struggle teaches resilience.\n"
    "Optimism fuels perseverance."
),
(
    "Difficult moments teach patience.\n"
    "Support lifts the heart."
),
(
    "Life’s challenges develop character.\n"
    "Hope gives courage to continue."
),
(
    "Even small hardships strengthen our spirit.\n"
    "Compassion eases the load."
),
(
    "Challenges teach valuable lessons.\n"
    "Optimism guides our path."
),
(
    "Hard experiences build resilience.\n"
    "Support makes the burden lighter."
),
(
    "Every struggle brings growth.\n"
    "Patience and hope sustain us."
),
(
    "Difficult moments reveal inner courage.\n"
    "Connection softens the journey."
),
(
    "Life’s challenges make us stronger.\n"
    "Optimism helps us move forward."
),
(
    "Even in hard times, growth is possible.\n"
    "Support brings comfort."
),
(
    "Challenges teach perseverance and patience.\n"
    "Hope guides our steps."
),
(
    "Hardships build resilience and empathy.\n"
    "Compassion eases the weight."
),
(
    "Every struggle strengthens character.\n"
    "Optimism lights the way."
),
(
    "Difficult moments teach endurance.\n"
    "Support helps us carry on."
),
(
    "Life’s challenges reveal inner strength.\n"
    "Hope keeps us moving forward."
),
(
    "Even small difficulties teach lessons.\n"
    "Patience sustains our spirit."
),
(
    "Challenges shape our courage.\n"
    "Compassion guides our path."
),
(
    "Hard times develop resilience.\n"
    "Optimism fuels our journey."
),
(
    "Every struggle is an opportunity to grow.\n"
    "Support eases the challenge."
),
(
    "Difficult experiences teach empathy.\n"
    "Hope gives strength to continue."
),
(
    "Life’s obstacles create character.\n"
    "Connection lightens the burden."
),
(
    "Even in hardship, growth is possible.\n"
    "Patience keeps us strong."
),
(
    "Challenges teach perseverance.\n"
    "Optimism sustains our efforts."
),
(
    "Hard moments reveal inner courage.\n"
    "Support helps carry the load."
),
(
    "Every difficulty strengthens the spirit.\n"
    "Hope guides our journey."
),
(
    "Difficult experiences bring growth.\n"
    "Connection softens hardship."
),
(
    "Life’s challenges teach patience and resilience.\n"
    "Optimism lights the way."
),
(
    "Even small struggles strengthen us.\n"
    "Support gives comfort."
),
(
    "Challenges develop courage and strength.\n"
    "Hope keeps us moving forward."
),
(
    "Hard times teach valuable lessons.\n"
    "Patience sustains us through challenges."
),
(
    "Every struggle offers an opportunity.\n"
    "Connection eases the burden."
),
(
    "Difficult moments reveal resilience.\n"
    "Optimism fuels perseverance."
),
(
    "Life’s obstacles strengthen character.\n"
    "Support helps us endure."
),
(
    "Even in tough times, growth is possible.\n"
    "Hope guides our steps."
),
(
    "Challenges teach patience and empathy.\n"
    "Compassion softens difficulties."
),
(
    "Hard experiences build inner strength.\n"
    "Optimism provides energy to continue."
),
(
    "Every struggle helps us grow.\n"
    "Support eases the journey."
),
(
    "Difficult moments teach endurance and courage.\n"
    "Hope sustains our spirit."
),
(
    "Life’s challenges develop resilience.\n"
    "Connection makes the journey lighter."
),
(
    "Even small hardships teach valuable lessons.\n"
    "Patience and hope guide us forward."
),
(
    "Challenges reveal inner strength.\n"
    "Compassion helps us persevere."
),
(
    "Hard times shape character.\n"
    "Optimism keeps us moving."
),
(
    "Every struggle is a chance to grow.\n"
    "Support eases the burden."
),
(
    "Difficult experiences teach courage.\n"
    "Hope lights the path ahead."
),
(
    "Life’s obstacles build resilience.\n"
    "Connection brings comfort."
),
(
    "Even in adversity, growth is possible.\n"
    "Patience strengthens the spirit."
),
(
    "Challenges teach perseverance.\n"
    "Optimism guides the journey."
),
(
    "Hard moments develop empathy and strength.\n"
    "Support eases hardships."
),
(
    "Every struggle strengthens our heart.\n"
    "Hope keeps us moving forward."
),
(
    "Difficult times teach patience and resilience.\n"
    "Connection softens the load."
),
(
    "Life’s challenges reveal inner courage.\n"
    "Optimism fuels perseverance."
),
(
    "Even small difficulties build character.\n"
    "Support makes the path easier."
),
(
    "Challenges teach us to endure.\n"
    "Hope guides the spirit."
),
(
    "Hard experiences foster growth.\n"
    "Compassion lightens the burden."
),
(
    "Every struggle carries a lesson.\n"
    "Optimism sustains the journey."
),
(
    "Difficult moments reveal strength.\n"
    "Support helps us continue."
),
(
    "Life’s obstacles build courage.\n"
    "Patience and hope guide us."
),
(
    "Even in hardship, resilience grows.\n"
    "Connection eases the path."
),
(
    "Challenges teach patience and endurance.\n"
    "Optimism fuels our journey."
),
(
    "Hard times develop inner strength.\n"
    "Support makes struggles lighter."
),
(
    "Every struggle is an opportunity to learn.\n"
    "Hope guides the heart."
)
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




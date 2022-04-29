import os
import sys
from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, SUDO_USERS, OWNER_NAME, CHANNEL

START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ("الأحد", 60 * 60 * 24 * 7),
    ("يوم", 60 * 60 * 24),
    ("الساعة", 60 * 60),
    ("الدقيقة", 60),
    ("الثانيه", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(filters.command(["بنك"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
    await m.delete()
    start = time()
    current_time = datetime.utcnow()
    m_reply = await m.reply_text("⚡")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(
        f"<b>🏓 بـنـك/b> `{delta_ping * 1000:.3f} بالثانيه` \n<b>⏳ شغال</b> - `{uptime}`"
    )


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["اعادة تشغيل"], prefixes=f"{HNDLR}")
)
async def restart(client, m: Message):
    await m.delete()
    SimoMusic = await m.reply("1")
    await SimoMusic.edit("2")
    await SimoMusic.edit("3")
    await SimoMusic.edit("4")
    await SimoMusic.edit("5")
    await SimoMusic.edit("6")
    await SimoMusic.edit("7")
    await SimoMusic.edit("8")
    await SimoMusic.edit("9")
    await SimoMusic.edit("**تم اعادة تشغيل سورس سيمو ميوزك بنجاح ✓**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@Client.on_message(filters.command(["الاوامر"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    SIMMM = f"""
👋 اهلا {m.from_user.mention}!
قــائـمه الاوامـر لــسورس ســيمو [ {OWNER_NAME} ](t.me/{CHANNEL})

Ж――――――اوامــر التشـغيل――――――Ж
✿ | لتشغيل صوتية في المكالمة أرسل ⇦ [ `{HNDLR}تشغيل  + اسم الاغنية` ]
✿ | لتشغيل فيديو في المكالمة  ⇦ [ `{HNDLR}تشغيل_فيديو  + اسم الاغنية` ]
Ж――――――اوامــر الاعاده و الايــقاف――――――Ж
✿ | لأيقاف الاغنية او الفيديو مؤقتآ  ⇦ [ `{HNDLR}استئناف` ]
✿ | لأيقاف الاغنية  ⇦ [ `{HNDLR}ايقاف` ]
✿ | لأعاده تشغيل الاغنية ⇦  [ `{HNDLR}ايقاف_الاستئناف` ]
Ж――――――اوامــر التخطي و العشـوائيـه――――――Ж
✿ | لتغطي الاغنية الحالية و تشغيل الاغنية التالية ⇦ [ `{HNDLR}تخطي` ]
✿ | لتشغيل الاغنية عشوائية من قناة او مجموعة  ⇦ [ `{HNDLR}اغنيه عشوائية` ]
Ж――――――اوامــر التـنزيل――――――Ж
✿ | لتحميل صوتية أرسل ⇦ [ `{HNDLR}تحميل + اسم الاغنية او الرابط` ]
✿ | لتحميل فيديو  ⇦  [ `{HNDLR}تحميل_فيديو + اسم الاغنية او الرابط` ]
Ж――――――اوامــر الادمــن――――――Ж
✿ | لأعاده تشغيل التنصيب أرسل ⇦  [ `{HNDLR}ريستارت` ]
Ж――――――معــلومـات――――――Ж
المطور 🌐 : {OWNER_NAME}
القناة ツ : @{CHANNEL}
"""
    await m.reply(SIMM)


@Client.on_message(filters.command(["السورس"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    SIMM = f"""
<b>- مرحبا {m.from_user.mention}!

🎶 هذا هو سورس سيمو ميوزك

🤖  اختصاص هذا البوت لتشغيل مقاطع صوتية او مقاطع الفيديو في المكالمات الصوتية

⚒️ لعرض اوامر السورس ارسل  {HNDLR}الاوامر

📚 • قناة السورس  : @ADWSL</b>
"""
    await m.reply(SIMM, disable_web_page_preview=True)

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


@Client.on_message(filters.command(["م"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    SIMM = f"""
👋 اهلا {m.from_user.mention}!
 [ {OWNER_NAME} ](t.me/{CHANNEL})
🛠 هذه هي قائمـة اوامر السـورس

- أوامر المستخدمين: 

• {HNDLR}تشغيل [عنوان المطقع | رابط يوتيوب | الرد على ملف مقطع صوتي] - لتشغيل مقطع صوتي في المكالمه

• {HNDLR}تشغيل_فيديو [عنوان الفيديو | رابط يوتيوب | الرد على الفيديو] - لتشغيل فيديو في المكالمة

• {HNDLR}تحميل  - لتحميل صوتيه 

• {HNDLR}تحميل_فيديو  -  لتحميل مقطق فيديو

• {HNDLR}بنك - لعرض سرعه النت للبوت

• {HNDLR}م - لعرض اوامر سورس ميوزك سيمو 

- أوامر المشرفين  : 

• {HNDLR}استئناف - لمواصلة تشغيل المقطع الصوتي أو الفيديو المتوقف

• {HNDLR}ايقاف - لإيقاف تشغيل المقطع الصوتي أو مقطع فيديو مؤقتًا

• {HNDLR}تخطي - لتخطي المقطع الصوتي أو الفيديو الحالي وتشغيل ما بعده

• {HNDLR}انهاء - لإنهاء التشغيل

المطور ༒ : {OWNER_NAME}
القناة ✪ : @{CHANNEL}
"""
    await m.reply(SIMM, disable_web_page_preview=True)


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

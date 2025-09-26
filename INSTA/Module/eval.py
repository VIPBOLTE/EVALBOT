import os
import re
import subprocess
import sys
import traceback
from inspect import getfullargspec
from io import StringIO
from time import time

from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import Config
from INSTA import app



OWNER_ID = Config.OWNER_ID
EVAL = Config.OWNER_ID


# ---------------- AEXEC (fixed) ---------------- #
async def aexec(code, client, message):
    env = {
        "client": client,
        "message": message,
        "app": app,
        "Config": Config,
        "os": os,
    }
    # build async function dynamically
    exec(
        "async def __aexec(client, message):\n"
        + "".join(f" {line}\n" for line in code.split("\n")),
        env,
    )
    return await env["__aexec"](client, message)


async def edit_or_reply(msg: Message, **kwargs):
    func = msg.edit_text if msg.from_user.is_self else msg.reply
    spec = getfullargspec(func.__wrapped__).args
    await func(parse_mode=enums.ParseMode.HTML, **{k: v for k, v in kwargs.items() if k in spec})


# ---------------- EVAL ---------------- #
# List of restricted keywords
BLOCKED_KEYWORDS = ["Config", "os.environ", "os.system", "subprocess", "app", "__import__"]

@app.on_message(filters.command("seval"))
async def executor(client: app, message: Message):
    if len(message.command) < 2:
        return await edit_or_reply(message, text="<b>What to eval?</b>")

    cmd = message.text.split(" ", maxsplit=1)[1]

    # Check for restricted content
    if any(kw in cmd for kw in BLOCKED_KEYWORDS):
        return await edit_or_reply(message, text="❌ <b>Access Denied:</b> Restricted code")

    t1 = time()
    old_stderr, old_stdout = sys.stderr, sys.stdout
    redirected_output = sys.stdout = StringIO()
    redirected_error = sys.stderr = StringIO()
    exc = None

    try:
        await aexec(cmd, client, message)
    except Exception:
        exc = traceback.format_exc()

    stdout, stderr = redirected_output.getvalue(), redirected_error.getvalue()
    sys.stdout, sys.stderr = old_stdout, old_stderr
    evaluation = exc or stderr or stdout or "✅ Success"

    final_output = f"<b>⥤ Result :</b>\n<pre>{evaluation}</pre>"
    t2 = time()

    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton(text="⏳", callback_data=f"runtime {round(t2-t1, 3)}")]]
    )

    await edit_or_reply(message, text=final_output[:4000], reply_markup=keyboard)


@app.on_callback_query(filters.regex(r"runtime"))
async def runtime_func_cq(_, cq):
    runtime = cq.data.split()[1]
    await cq.answer(f"Runtime: {runtime} Seconds", show_alert=True)


# ---------------- SHELL ---------------- #
@app.on_message(filters.command("sh") & filters.user(EVAL))
async def shellrunner(_, message: Message):
    if len(message.command) < 2:
        return await edit_or_reply(message, text="<b>Example:</b>\n/sh git pull")
    cmd = message.text.split(None, 1)[1]
    shell = re.split(r""" (?=(?:[^'"]|'[^']*'|"[^"]*")*$)""", cmd)
    try:
        process = subprocess.Popen(shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        output = (stdout.decode() + stderr.decode()).strip()
    except Exception as e:
        return await edit_or_reply(message, text=f"<b>ERROR :</b>\n<pre>{e}</pre>")
    if not output:
        output = "None"
    if len(output) > 4000:
        with open("output.txt", "w+", encoding="utf8") as f:
            f.write(output)
        await app.send_document(message.chat.id, "output.txt", reply_to_message_id=message.id)
        os.remove("output.txt")
    else:
        await edit_or_reply(message, text=f"<b>OUTPUT :</b>\n<pre>{output}</pre>")


if __name__ == "__main__":
    app.run()

import asyncio
import os
import shlex
import heroku3

from functools import wraps
from pyrogram.types import Message
from typing import Tuple
from html_telegraph_poster import TelegraphPoster
from bot import HEROKU_API_KEY, HEROKU_APP_NAME

# Implement by https://github.com/jusidama18
@@ -73,41 +68,3 @@ def fetch_heroku_git_url(api_key, app_name):
    return heroku_app.git_url.replace("https://", "https://api:" + api_key + "@")

HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)

def post_to_telegraph(a_title: str, content: str) -> str:
    """ Create a Telegram Post using HTML Content """
    post_client = TelegraphPoster(use_api=True)
    auth_name = "slam-mirrorbot"
    post_client.create_api_token(auth_name)
    post_page = post_client.post(
        title=a_title,
        author=auth_name,
        author_url="https://github.com/breakdowns/slam-mirrorbot",
        text=content,
    )
    return post_page["url"]


async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    """ run command in terminal """
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )


# Solves ValueError: No closing quotation by removing ' or " in file name
def safe_filename(path_):
    if path_ is None:
        return
    safename = path_.replace("'", "").replace('"', "")
    if safename != path_:
        os.rename(path_, safename)
    return safename

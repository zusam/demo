#!/usr/bin/env python3

import random, string, json, sys, os, time
import requests


def post_message(msg, group_id, API_ROOT, key):
    files = []
    if "files" in msg:
        for file in msg["files"]:
            r = requests.post(
                API_ROOT + "/files",
                files={
                    "file": file,
                },
                headers={"x-auth-token": key},
            )
            file = r.json()
            print(file)
            files.append(file["id"])

    r = requests.post(
        API_ROOT + "/messages",
        data=json.dumps({"group": group_id, "data": msg["data"], "files": files}),
        headers={"Content-Type": "application/json", "x-auth-token": key},
    )


if __name__ == "__main__":

    API_ROOT = sys.argv[1]
    TOKEN = sys.argv[2]
    message_dir = sys.argv[3]
    group_id = sys.argv[4]

    msg = {"files": []}
    if os.path.isdir(message_dir + os.sep + "files"):
        for filepath in os.listdir(message_dir + os.sep + "files"):
            with open(message_dir + os.sep + "files" + os.sep + filepath, "rb") as file:
                msg["files"].append(file.read())

    with open(message_dir + os.sep + "title.txt", "r") as file:
        msg["title"] = file.read()
    with open(message_dir + os.sep + "text.txt", "r") as file:
        msg["text"] = file.read()

    msg["data"] = {"title": msg["title"], "text": msg["text"]}

    post_message(msg, group_id, API_ROOT, TOKEN)

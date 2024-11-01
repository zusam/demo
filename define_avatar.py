#!/usr/bin/env python3

import json
import sys
import requests


def define_avatar(api_key, avatar_path, API_ROOT):
    r = requests.post(
        API_ROOT + "/files",
        files={"file": open(avatar_path, "rb")},
        headers={"x-auth-token": api_key},
    )
    if r.status_code == requests.codes.created:
        data = r.json()
        avatar_id = data["id"]
        r = requests.get(
            API_ROOT + "/me",
            headers={"Content-Type": "application/json", "x-auth-token": api_key},
        )
        if r.status_code == requests.codes.ok:
            data = r.json()
            r = requests.put(
                API_ROOT + "/users/{}".format(data["id"]),
                data=json.dumps({"avatar": avatar_id}),
                headers={"Content-Type": "application/json", "x-auth-token": api_key},
            )
            print("define_avatar got return status: {}".format(r.status_code))


if __name__ == "__main__":

    API_ROOT = sys.argv[1]
    TOKEN = sys.argv[2]
    avatar_path = sys.argv[3]

    define_avatar(TOKEN, avatar_path, API_ROOT)

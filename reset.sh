#!/bin/sh

echo "[$(date +'%Y-%m-%d %H:%M:%S')] Reset demo"
/zusam/api/bin/console zusam:init zusam demo-group zusam --seed zusam --remove-existing

sleep 3

TOKEN="$(sqlite3 /zusam/data/data.db -line "select secret_key from 'user' where name = 'zusam';" | awk '{print $3}')"
GROUP_ID="$(sqlite3 /zusam/data/data.db -line "select id from 'group' where name = 'demo-group';" | awk '{print $3}')"
API_ROOT="http://localhost:8080/api"

sleep 1
python3 /usr/local/bin/post_message.py "$API_ROOT" "$TOKEN" /assets/message/1 "$GROUP_ID"
sleep 1
python3 /usr/local/bin/post_message.py "$API_ROOT" "$TOKEN" /assets/message/2 "$GROUP_ID"
sleep 1
python3 /usr/local/bin/post_message.py "$API_ROOT" "$TOKEN" /assets/message/3 "$GROUP_ID"
sleep 1
python3 /usr/local/bin/post_message.py "$API_ROOT" "$TOKEN" /assets/message/4 "$GROUP_ID"
sleep 1
python3 /usr/local/bin/post_message.py "$API_ROOT" "$TOKEN" /assets/message/5 "$GROUP_ID"

sleep 3
python3 /usr/local/bin/define_avatar.py "$API_ROOT" "$TOKEN" /assets/zusam.png

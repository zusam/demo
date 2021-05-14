FROM zusam:latest

COPY assets /assets
COPY define_avatar.py /usr/local/bin/define_avatar.py
COPY post_message.py /usr/local/bin/post_message.py
COPY reset.sh /usr/local/bin/reset.sh
COPY run.sh /usr/local/bin/run.sh
RUN set -xe \
    && apk add curl sqlite python3 py3-requests \
    && mkdir -p /zusam/data \
    && chmod +x /usr/local/bin/*

CMD ["run.sh"]

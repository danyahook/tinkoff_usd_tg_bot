FROM python:3.10

WORKDIR /usr/src/tinkoff_usd_tg_bot

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /usr/src/tinkoff_usd_tg_bot/requirements.txt

RUN pip install -U pip --no-cache-dir && \
    pip install --no-cache-dir wheel && \
    pip install --no-cache-dir -r requirements.txt

COPY bot.py /usr/src/tinkoff_usd_tg_bot/bot.py

COPY ./tinkoff_bot /usr/src/tinkoff_usd_tg_bot/tinkoff_bot

RUN chmod +x bot.py
CMD python3 bot.py;
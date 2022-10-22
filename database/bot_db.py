import sqlite3
from config import bot
import random


def sql_create():
    global db, cursor
    db = sqlite3.connect('bot.sqlite3')
    cursor = db.cursor()
    if db:
        print('База данных подключена!')

    db.execute(
        "CREATE TABLE IF NOT EXISTS list"
        "(id INTEGER PRIMARY KEY, name_m  TEXT,"
        "direction TEXT, age INTEGER, group_m INTEGER)"
    )
    db.commit()

async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO list VALUES (?,?,?,?,?)", tuple(data.values()))
        db.commit()

async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM list").fetchall()
    random_user = random.choice(result)
    await bot.send_message(message.from_user.id, f'ID: {random_user[0]}\n'
                                                 f'Name: {random_user[1]}\nDirection: {random_user[2]}\n'
                                                 f'Age: {random_user[3]}\nGroup: {random_user[4]}\n')

async def sql_command_all():
    return cursor.execute("SELECT * FROM list").fetchall()

async def sql_command_delete(id):
    cursor.execute("DELETE FROM list WHERE id = ?", (id,))
    db.commit()

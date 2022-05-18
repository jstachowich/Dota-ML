from functions import *
import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def build_hero():
    ret = """
INSERT INTO
    heroes (hero_id, name)
VALUES
"""
    heroes_dict = get_heroes()

    for i in heroes_dict:
        if i == 137:
            ret += f"""    ({i}, "{heroes_dict[i]}")"""
        else:
            ret += f"""    ({i}, "{heroes_dict[i]}"),\n"""
    ret += """;"""
    return ret

def build_recent(username):
    ret = """
INSERT or REPLACE INTO
    recent (match_id, win, hero_id, kills, deaths, XPM, GPM, damage, cs)
VALUES
"""
    recent_list = build_recent_list(username)

    for i in recent_list:
        ret += f"""    ({i[0]}, {i[1]}, {i[2]}, {i[3]}, {i[4]}, {i[5]}, {i[6]}, {i[7]}, {i[8]}),\n"""
    ret = ret[:-2]
    ret += """;"""
    return ret


# add directory to database here
connection = create_connection(r"AddConnectionPathHere") 

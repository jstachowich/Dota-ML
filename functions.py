import requests
import json
import sqlite3
import pandas as pd



userid = 119080300


def get_heroes():
    raw = requests.get('https://api.opendota.com/api/heroes')
    data_list = json.loads(raw.text)
    final = {}
    for hero in data_list:
        final[hero['id']] = hero['localized_name']
    return final


def get_matches(username):
    data_raw = requests.get('https://api.opendota.com/api/players/%d/matches' % username)
    data_list = json.loads(data_raw.text)
    return data_list

def get_recent_matches(username):
    data_raw = requests.get('https://api.opendota.com/api/players/%d/recentMatches' % username)
    data_list = json.loads(data_raw.text)
    return data_list

def build_recent_list(username):
    data_raw = requests.get('https://api.opendota.com/api/players/%d/recentMatches' % username)
    data_list = json.loads(data_raw.text)

    ret = []
    for d in data_list:
        win = 0
        if d['player_slot'] > 127 and d['radiant_win'] == False:
            win = 1
        ret.append([d['match_id'], win, d['hero_id'], d['kills'], d['deaths'],
                d['xp_per_min'], d['gold_per_min'], d['hero_damage'],
                d['last_hits']])

    return ret
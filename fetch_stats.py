#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

BASE_URL = 'https://fantasy.premierleague.com/api/'


def get_general_data():
    """
    fetch info from premier league API: players' IDs, names, positions, prices and teams
    :return: a dictionary
    """
    url = BASE_URL + 'bootstrap-static' + '/'
    response = requests.get(url)
    output = response.json()
    players_dict_vertical = {'players': []}
    players_dict_horizontal = {'players': []}
    ids, names, positions, prices, points, teams = [], [], [], [], [], []

    teams_dict = {}
    for team in output['teams']:
        teams_dict[team['id']] = team['name']

    for player in output['elements']:
        ids.append(player['id'])
        names.append(player['web_name'])
        prices.append(player['now_cost'])
        #points.append(player['total_points'])
        team = teams_dict[player['team']]
        teams.append(team)
        element_type = player['element_type']
        for pose_type in output['element_types']:
            if pose_type['id'] == element_type:
                position = pose_type['singular_name']
                positions.append(pose_type['singular_name'])

        players_dict_horizontal['players'].append({
            player['id']:
                {'name': player['web_name'], 'price': player['now_cost'], 'position': positions, 'team': team
                 }})

    players_dict_vertical['players'].append({
        'ids': ids, 'positions': positions, 'names': names, 'prices': prices, 'teams': teams
    })

    return players_dict_vertical


def get_player_stats(player_id):
    """ get game week points for player"""
    url = BASE_URL + 'element-summary/' + str(player_id) + '/'
    response = requests.get(url)
    output = response.json()

    points = []
    minutes = []
    for game in output['history']:
        points.append(game['total_points'])
        #minutes.append(game[minutes])

    return points




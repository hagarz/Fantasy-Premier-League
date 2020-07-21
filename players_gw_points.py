#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Hagar Zemach'

from fetch_stats import get_general_data, get_player_stats
from visualization import data_to_excel

NUMBER_OF_GW = 37


def main():
    """ gets players stats and writes it to excel"""

    # get players details (teams name, players id, players name etc'):
    general_stats = get_general_data()

    # get players points for each GameWeek
    players_data = general_stats['players'][0]
    players_gw_points = {}

    for i in range(NUMBER_OF_GW):
        players_gw_points['GW ' + str(i + 1)] = []

    for id in players_data['ids']:
        players_points_list = get_player_stats(player_id=id)

        difference = NUMBER_OF_GW - len(players_points_list)
        if difference < 0: difference = 0

        for i in range(NUMBER_OF_GW):
            if i < difference:
                players_gw_points['GW ' + str(i + 1)].append(0)
            else:
                try:
                    players_gw_points['GW ' + str(i + 1)].append(players_points_list[i-difference])
                except KeyError as e:
                    print("KeyError", e, "for player id", id)
                except IndexError as index_error:
                    print("IndexError", index_error, "for player", id)
                    players_gw_points['GW ' + str(i + 1)].append(0)

    combined_stats = combine_data_to_arrays(general_stats, players_gw_points)

    data_to_excel(combined_stats)


def combine_data_to_arrays(general_dict, players_points):
    """ combining general details and players' GW points to one dictionary"""
    data_lists = {}

    for entry in general_dict['players'][0]:
        data_lists[entry] = general_dict['players'][0][entry]

    for entry in players_points:
        data_lists[entry] = players_points[entry]

    return data_lists


if __name__ == '__main__':

    main()

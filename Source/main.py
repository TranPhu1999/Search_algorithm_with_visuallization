from os import path
from Depth_First_Search import depth_first_search
from Breadth_First_Search import breadth_first_search
from Greedy_Best_First_Search import greedy_best_first_search
from A_Star_Search import a_star_search
from Bonus_Search import bonus_search
from Support import visualize_maze, read_file

import sys

if __name__ == "__main__":
    # try: 
    bonus_point, maze_map, start, end = read_file("../Maps/"+sys.argv[2])

    print(f'Starting point (x, y) = {start[0], start[1]}')
    print(f'Ending point (x, y) = {end[0], end[1]}')

    for _, point in enumerate(bonus_point):
        print(f'Bonus point at position (x, y) = {point[0], point[1]} with point {point[2]}')

    # select algorithm
    if sys.argv[1] == "dfs":
        depth_first_search(maze_map,start,end,bonus_point)
    elif sys.argv[1] == "bfs":
        breadth_first_search(maze_map,start,end,bonus_point)
    elif sys.argv[1] == "gbfs":
        greedy_best_first_search(maze_map,start,end,bonus_point)
    elif sys.argv[1] == "ass":
        a_star_search(maze_map,start,end,bonus_point)
    elif sys.argv[1] == "bs":
        bonus_search(maze_map,start,end,bonus_point)
    else:
        print("Invalid algorithm. Syntax: python main.py <dfs/bfs/gbfs/ass> <map>")

    # except:
    #     print("Error, try again with syntax: python main.py <dfs/bfs/gbfs/ass> <map>")
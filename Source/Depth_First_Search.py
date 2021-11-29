import numpy as np
from Support import visualize_maze

def dfs_travel(map, current_pos, start, end, visited, bonus):
    row = current_pos[0]
    column = current_pos[1]
    
    route = []
    found = False

    if row == end[0] and column == end[1]:
        route.append((row,column))
        return True, route

    map[row][column] = 'o'
    visited.append((row,column))

    # ^
    if not found:
        if (map[row-1][column] != 'x' and map[row-1][column] != 'o'):
            found, route = dfs_travel(map,(row-1,column), start, end, visited, bonus)
    
    # >
    if not found:
        if (map[row][column+1] != 'x' and map[row][column+1] != 'o'):
            found, route = dfs_travel(map,(row,column+1), start, end, visited, bonus)
    
    # v
    if not found:
        if (map[row+1][column] != 'x' and map[row+1][column] != 'o'):
            found, route = dfs_travel(map,(row+1,column), start, end, visited, bonus)

    # <
    if not found: 
        if (map[row][column-1] != 'x' and map[row][column-1] != 'o'):
            found, route = dfs_travel(map,(row,column-1), start, end, visited, bonus)
    if not found:
        return False, []

    if found:
        route.append((row,column))
        return found, route

def depth_first_search(maze_map,start,end, bonus = None):
    temp_map = maze_map
    visited = []
    found, route = dfs_travel(temp_map, start, start, end, visited, bonus)
    for i in range(len(visited)):
        if i < len(visited) - 1:
            visualize_maze(maze_map,bonus,start,end,[],visited[:i])
        else:
            visualize_maze(maze_map,bonus,start,end,route,visited,len(route))




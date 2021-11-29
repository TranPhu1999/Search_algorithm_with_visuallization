import numpy as np
from Support import visualize_maze

def breadth_first_search(maze_map,start,end, bonus = None):
    visited = []
    queue = [start]
    while queue[0][0] != end[0] or queue[0][1] != end[1]:
        row = queue[0][0]
        column = queue[0][1]
        if (row,column) not in visited:
            visited.append((row,column)) # store coordinate of visited block

        neighbor = [(row-1,column),(row,column+1),(row+1,column),(row,column-1)] # ^ > v <
        for i in range(len(neighbor)):
            x = neighbor[i][0]
            y = neighbor[i][1]
            if maze_map[x][y] == ' ':
                queue.append((x,y))
                maze_map[x][y] = (row,column) # save the coordinate of the current block as previous value           

        queue.pop(0)
    
    # recontruct route
    route = [end]
    while route[-1][0] != start[0] or route[-1][1] != start[1]:
        route.append(maze_map[route[-1][0]][route[-1][1]])
    total_cost = len(route)
    
    # visualize progress
    for i in range(len(visited)):
        if i < len(visited) - 1:
            visualize_maze(maze_map,bonus,start,end,[],visited[:i])
        else:
            visualize_maze(maze_map,bonus,start,end,route,visited,total_cost)



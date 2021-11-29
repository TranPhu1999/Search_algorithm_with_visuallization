import numpy as np
from Support import visualize_maze, heuristic_euclidean

def greedy_best_first_search(maze_map,start,end, bonus = None):
    visited = []
    queue = [(start[0],start[1],0)]
    while True:
        if len(queue)==0:
            print("Can not find any path!")
            break
        
        # if block end have had value of the coordinate of the previous block then break
        if maze_map[end[0]][end[1]] != ' ':
            break

        # find the block with the lowest cost to go to the end in the queue
        min = 0       
        for i in range(len(queue)):
            if queue[i][2] < queue[min][2]:
                min = i       

        current = queue.pop(min)
        row = current[0]
        column = current[1]
        if (row,column) not in visited:
            visited.append((row,column)) # store coordinate of visited block for visuallize

        neighbor = [(row-1,column),(row,column+1),(row+1,column),(row,column-1)] # ^ > v <
        for i in range(len(neighbor)):
            x = neighbor[i][0]
            y = neighbor[i][1]
            if maze_map[x][y] == ' ':
                queue.append((x,y, heuristic_euclidean((x,y),end) ))
                maze_map[x][y] = (row,column) # save the coordinate of the current block as previous value
        
    route = [end]
    # recontruct path
    while route[-1][0] != start[0] or route[-1][1] != start[1]:
        route.append(maze_map[route[-1][0]][route[-1][1]])
    
    # visualize progress
    for i in range(len(visited)):
        if i < len(visited) - 1:
            visualize_maze(maze_map,bonus,start,end,[],visited[:i])
        else:
            visualize_maze(maze_map,bonus,start,end,route,visited, len(route))



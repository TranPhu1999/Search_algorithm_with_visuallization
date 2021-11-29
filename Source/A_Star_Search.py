import numpy as np
from Support import visualize_maze, heuristic_euclidean, heuristic_manhatan, heuristic_euclidean_2

def a_star_search(maze_map,start,end, bonus = None):
    visited = []
    queue = [(start[0],start[1])] # (x, y, heuristic + path cost, path cost)
    maze_map[start[0]][start[1]] = (0,0,0,0)
    while True:
        if len(queue)==0:
            print("Can not find any path!")
            break

        # find the block with the lowest cost to go to the End in the queue
        min = 0      
        for i in range(len(queue)):
            if maze_map[queue[i][0]][queue[i][1]][2] < maze_map[queue[min][0]][queue[min][1]][2]:
                min = i                
        if queue[min][0] == end[0] and queue[min][1] == end[1]:
            break  
        
        current = queue.pop(min)
        row = current[0]
        column = current[1]
        if (row,column) not in visited:
            visited.append((row,column)) # store coordinate of visited block for visuallize

        neighbor = [(row-1,column),(row,column+1),(row+1,column),(row,column-1)] # ^ > v <
        for i in range(len(neighbor)):            
            x = neighbor[i][0]
            y = neighbor[i][1]
            # if neighbor is not wall and not in visited list
            if maze_map[x][y] != 'x' and (x,y) not in visited:                        
                # if neighbor is emty or have shorter path from the start
                new_cost = maze_map[row][column][3]+ 1         
                if (x,y) not in queue or maze_map[x][y][3] > new_cost:
                    queue.append((x,y))
                    # save the coordinate of the current block as previous value
                    maze_map[x][y] = (row,column,heuristic_euclidean_2((x,y),end)+new_cost,new_cost)
                    # maze_map[x][y] = (row,column,heuristic_manhatan((x,y),end)+new_cost,new_cost)
                    # maze_map[x][y] = (row,column,heuristic_euclidean((x,y),end)+new_cost,new_cost)

    route = [end[:2]]
    # recontruct path
    while route[-1][0] != start[0] or route[-1][1] != start[1]:
        route.append(maze_map[route[-1][0]][route[-1][1]][:2])
    
    # visualize progress
    for i in range(len(visited)):
        if i < len(visited) - 1:
            visualize_maze(maze_map,bonus,start,end,[],visited[:i])
        else:
            visualize_maze(maze_map,bonus,start,end,route,visited, len(route))



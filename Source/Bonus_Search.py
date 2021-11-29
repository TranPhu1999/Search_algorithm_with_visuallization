import numpy as np
from Support import visualize_maze

def bonus_search(maze_map,start,end, bonus = None):
    visited = []
    queue = [(start[0],start[1])] 
    maze_map[start[0]][start[1]] = (0,0,0) # (x, y, path cost)
    collected_bonus = 0
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

                # Check if the block have bonus score
                bonus_score = 0
                for i in range(len(bonus)):
                    if x == bonus[i][0] and y == bonus[i][1]:
                        bonus_score = bonus[i][2]
                        break
                        
                # if neighbor is emty or have shorter path from the start
                new_cost = maze_map[row][column][2]+ 1 + bonus_score              
                if (x,y) not in queue or maze_map[x][y][2] > new_cost:
                    queue.append((x,y))
                    # save the coordinate of the current block as previous value                    
                    maze_map[x][y] = (row,column,new_cost,new_cost)

    route = [end[:2]]
    # recontruct path
    while route[-1][0] != start[0] or route[-1][1] != start[1]:
        route.append(maze_map[route[-1][0]][route[-1][1]][:2])
    
    # Caculate collected bonus
    collected_block = []
    for i in range(len(route)):
        for j in range(len(bonus)):
            if route[i][0] == bonus[j][0] and route[i][1] == bonus[j][1]:
                collected_bonus += bonus[j][2]
                collected_block.append((route[i]))
    
    # visualize progress
    for i in range(len(visited)):
        if i < len(visited) - 1:
            visualize_maze(maze_map,bonus,start,end,[],visited[:i])
        else:
            visualize_maze(maze_map,bonus,start,end,route,visited, len(route) + collected_bonus, collected_block)





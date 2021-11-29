from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
from IPython import display
import os
import math

from numpy import log, log10, log1p, log2, logaddexp

VISUALLIZE_SPEED = 0.05
#interactive on
plt.ion()

def heuristic_euclidean(a,b):
    return (((a[0]-b[0])**2 + (a[1]-b[1])**2)**(1/2))

def heuristic_euclidean_2(a,b):
    d= ((a[0]-b[0])**2 + (a[1]-b[1])**2)**(1/2)
    return d*2

def heuristic_manhatan(a,b):
    return abs(a[0]-b[0]) + abs(a[1] - b[1])

def visualize_maze(matrix, bonus, start, end, route=None, visited=None, total_cost = None, collected_block = None):
    """
    Args:
      1. matrix: The matrix read from the input file,
      2. bonus: The array of bonus points,
      3. start, end: The starting and ending points,
      4. route: The route from the starting point to the ending one, defined by an array of (x, y), e.g. route = [(1, 2), (1, 3), (1, 4)]
      5. visited: The array of visited block in the maze
    """
    #1. Define walls and array of direction based on the route
    walls=[(i,j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j]=='x']

    if route:
        direction=[]
        for i in range(1,len(route)):
            if route[i][0]-route[i-1][0]>0:
                direction.append('^') #^
            elif route[i][0]-route[i-1][0]<0:
                direction.append('v') #v        
            elif route[i][1]-route[i-1][1]>0:
                direction.append('<')
            else:
                direction.append('>')

        direction.pop(0)

    if route:
        for i in range(1,len(route)-1):
            visited.remove(route[i])
    #2. Drawing the map
    plt.clf()
    # ax=plt.figure(dpi=100).add_subplot(111)

    # for i in ['top','bottom','right','left']:
    #     ax.spines[i].set_visible(False)

    plt.scatter([i[1] for i in visited],[-i[0] for i in visited],
                    marker='x',s=100,color='grey')

    plt.scatter([i[1] for i in walls],[-i[0] for i in walls],    
                marker='s',s=100,color='black')      

    plt.scatter([i[1] for i in bonus],[-i[0] for i in bonus],
                    marker='P',s=100,color='green')

    plt.scatter(start[1],-start[0],marker='*',
                s=200,color='gold')

    if route:
        for i in range(len(route)-2):
            plt.scatter(route[i+1][1],-route[i+1][0],
                        marker=direction[i],s=120,color='red')

    if collected_block:
        plt.scatter([i[1] for i in collected_block],[-i[0] for i in collected_block],
                        marker='P',s=100,color='green')

    plt.text(end[1],-end[0],'EXIT',color='red',
         horizontalalignment='center',
         verticalalignment='center')
    plt.xticks([])
    plt.yticks([])
    plt.title("Cost: "+ str(total_cost))
    plt.show(block=False)
    if route:
        plt.waitforbuttonpress(timeout = -1)
    else:
        plt.pause(VISUALLIZE_SPEED)

def read_file(file_name: str = 'maze.txt'):
    f=open(file_name,'r')        
    n = next(f)[:-1]
    bonus_points = []

    n_bonus_points = int(n)    
    for i in range(n_bonus_points):
        x, y, reward = map(int, next(f)[:-1].split(' '))
        bonus_points.append((x, y, reward))

    text=f.read()
    matrix=[list(i) for i in text.splitlines()]
    f.close()

    #Get start and end point
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=='S':
                start=(i,j)

            elif matrix[i][j]==' ':
                if (i==0) or (i==len(matrix)-1) or (j==0) or (j==len(matrix[0])-1):
                    end=(i,j)
                    
            else:
                pass

    return bonus_points, matrix, start, end
import time
import math
from result import *

#Checking if X is in bounds
def isValid(X, M, N):
    if X[0] < 0 or X[0] >= M or X[1] < 0 or X[1] >= N:
        return False
    return True

def esdf(M, N, obstacle_list):
    """
    :param M: Row number
    :param N: Column number
    :param obstacle_list: Obstacle list
    :return: An array. The value of each cell means the closest distance to the obstacle
    """
    #The ESDF, the distance from the nearest obstacle, set to infinity to start
    distance = [[9999 for i in range(N)] for j in range(M)]

    #Index of the closest Obstacle
    closestObstacle = [[9999 for i in range(N)] for j in range(M)]

    #Propogate the distances using BFS from the obstacles (Each adjacent pixel is a connected node)
    Queue = []

    #Add the Obstacles to the Queue, initialize distance values
    for i in obstacle_list:
        Queue.append(i)
        closestObstacle[i[0]][i[1]] = i
        distance[i[0]][i[1]] = 0

    #Adjacent pixel directions
    directions = [[-1,-1], [-1,0], [0,-1], [-1,1], [1,-1], [1,0], [0,1],[1,1]]
    new = []
    
    while len(Queue) != 0:
        curr = Queue.pop(0)
        
        for i in directions:
            new = [curr[0]+i[0],curr[1]+i[1]]
            
            if isValid(new, M, N):
                #Find closest Obstacle
                O = closestObstacle[curr[0]][curr[1]]
                d = math.sqrt((new[0]-O[0])**2 + (new[1]-O[1])**2)

                #If new distance is closer, update distance and add to Queue
                if d < distance[new[0]][new[1]]:
                    distance[new[0]][new[1]] = d
                    closestObstacle[new[0]][new[1]] = O
                    #Propogate further
                    Queue.append(new)
    return distance
    pass


if __name__ == '__main__':
    st = time.time()
    for _ in range(int(2e4)):
        assert np.array_equal(esdf(M=3, N=3, obstacle_list=[[0, 1], [2, 2]]), res_1)
        assert np.array_equal(esdf(M=4, N=5, obstacle_list=[[0, 1], [2, 2], [3, 1]]), res_2)

    et = time.time()
    print(et-st)

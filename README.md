# multi-drone-quiz

This is an implementation of the Image Foresting Transform (IFT) Algorithm, shown here: https://www.researchgate.net/publication/8331682_The_image_foresting_transform_theory_algorithms_and_applications

This algorithm takes the obstacles as the "roots" and performs an outward search to all the adjacent nodes. In our case, an adjacent node is the pixels next to it. The cost of the edge is the Euclidean distance between it and the "root". Propogating outward, this becomes similar to a shortest distance problem, as the algorithm finds the shortest distance from each vertex to the closest obstacle.
As shown by the paper above, the execution time of this algorithm is in order of O(M+N), or linear time and O(M+N) space. This is because each node has to only be expanded only once, because the queue is maintained in order of discovery, i.e. the node closer to the obstacle is visited first.

Numpy implementation executed slower than the Python list implementation, so chose the fast one here. You can also use the PyIFT library, but I chose to implement from scratch for the purposes of this quiz.

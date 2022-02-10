# TSP-using-nearest-neighbor-and-2opt-3opt
TSP using nearest neighbor and 2opt-3opt  with time constraint of 5 minutes
run the run.sh file
or run python file input file name
out put will be in console with graph
program makes output.txt file wait for 300 sec to see complete output in file
on console one by one best output will print.


****
viewing output on console is recomended.
*** 

<h3>Abstract:</h3>
<p>&nbsp;&nbsp;
Using any algorithm find the tour with least cost tour between cities forming Hamiltonian cycle
in given time limit of 300 sec. It encloses the concept of Travelling Salesman Problem. There is no known algorithm to solve the TSP that is both optimal and efficient
</p>
<h3>Algorithms used In the code:<h3>
<h4>&nbsp;&nbsp;Nearest Neighbor:</h4>
<p>&nbsp;&nbsp;&nbsp;&nbsp;The Nearest-Neighbor Algorithm begins at any vertex and follows the edge of least weight from that vertex. At every subsequent vertex, it follows the edge of least weight that leads to a city not yet visited, until it returns to the starting point.
</p>
<h5>Algorithm:</h5><i>
<h6>&nbsp;&nbsp;function nearest neighbor (distance matrix, starting point):
</h6><h6>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;path = [starting point]</h6>
<h6>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cost = 0</h6>
<h6>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mask <-store visited</h6>
<h6>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for i in range(number of nodes): path<-add nearest city to current city(path(i-1)) which is unvisited visited<-path[i]</h6>
<h6>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return path, cost</h6>
</i>
<h4>&nbsp;&nbsp;Repetitive Nearest-Neighbor Algorithm</h4>
<p>&nbsp;&nbsp;&nbsp;&nbsp;The Repetitive Nearest-Neighbor Algorithm applies the nearest-neighbor algorithm repeatedly, using each of the vertices as a starting point. It selects the starting point that produced the shortest circuit.</p>
<h5>Algorithm:</h5><i>
<h6>&nbsp;&nbsp;bestcost = infinite</h6>
<h6>&nbsp;&nbsp;for city in range(number of cities):</h6>
<h6>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;path, cost = nearest neighbor (distance matrix, city)</h6>
<h6>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if cost < bestcost:</h6>
<h6>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bestcost = cost</h6>
<h6>&nbsp;&nbsp;&nbsp;&nbsp;route = path</h6>
</i>
<h4>&nbsp;&nbsp;2-opt algorithm</h4> 
 <p>&nbsp;&nbsp;&nbsp;&nbsp;2-opt algorithm is one of the most basic and widely used heuristic for obtaining approximative solution of TSP problem. 2-opt starts with random initial tour and it improves the tour incrementally by exchanging 2 edges in the tour with two other edges.</br><i> Δij=c(u1,u2)+c(v1,v2)−(c(u1,v1)+.c(u2,v2))<i></p> 
<h5>Algorithm:</h5> <i>
<h6>&nbsp;&nbsp;improved = True </h6>
<h6>&nbsp;&nbsp;while improved: for i in range(1, len(route) - 2):</h6> 
<h6>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for j in range(i + 1, len(route)): </h6>
<h6>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if j - i == 1:</h6> 
<h6>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;continue </h6>
<h6>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if check_cost_change(cost_mat, best[i - 1], best[i], best[j - 1], best[j]) < 0:</h6>
<h6>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;best[i:j] = best[j - 1:i - 1:-1] route = best</h6>

import numpy as np
from matplotlib import pyplot as plt
from queue import PriorityQueue
import time
import sys

ts= time.time()
f2 = open("output.txt", "w+")
class TSP:

    def __init__(self):
        self.adj = []
        self.que = PriorityQueue()
        self.points = {}
        self.nut = 0
        self.plt=plt

    def nearestN(self, A, start):
        path = [start]
        cost = 0
        N = A.shape[0]
        mask = np.ones(N, dtype=bool)
        mask[start] = False

        for i in range(N-1):
            last = path[-1]
            next_ind = np.argmin(A[last][mask])
            next_loc = np.arange(N)[mask][next_ind]
            path.append(next_loc)
            mask[next_loc] = False
            cost += A[last, next_loc]

        return path, cost

    def solve(self, f, n):
        for i in range(0, n):
            self.points[i] = [float(j) for j in f.readline().strip().split()]
        route=[]
        for i in range(0, n):
            self.adj.append([float(i) for i in f.readline().strip().split()])
        A = np.array(self.adj)
        mn=float("inf")
        for i in range(n):
            path,cost=self.nearestN(A,i)
            self.que.put((cost+self.adj[path[0]][path[-1]],path))
            if cost<mn:
                mn=cost
                route=path
                #print(k[1])
        print(route)
        print("-)", mn)
        rrt = self.two_opt(route)
        print("*", rrt)
        print("-)", self.cost_cal(rrt, self.adj))
        print("wait for final best.....(will take at most 4 min more from program run)..")
        print("time:",time.time() - ts,"sec")
        return route

    def cost_change(self, cost_mat, n1, n2, n3, n4):
        return cost_mat[n1][n3] + cost_mat[n2][n4] - cost_mat[n1][n2] - cost_mat[n3][n4]
    def cost_cal(self, route, cost_mat):
        sm=0
        for i in range(1,len(route)):
            sm+=cost_mat[route[i-1]][route[i]]
        return sm

    def switch3(self,path, i, j, k):
        temp = []
        for x in range(0, i):
            temp.append(path[x])
        for x in range(j, k):
            temp.append(path[x])
        for x in range(i, j):
            temp.append(path[x])
        for x in range(k, len(path)):
            temp.append(path[x])
        temp.append(temp[0])
        return temp,self.cost_cal(temp,self.adj)

    def three_opt(self, route):
        mincost = self.cost_cal(route, self.adj)
        best = route[:-1]
        for i in range(len(route)-2):
            for j in range(i):
                for k in range(j):
                    path = best
                    path,cost = self.switch3(path, k, j, i)
                    if (mincost > cost):
                        mincost = cost
                        best = path[:-1]
                    if time.time()-ts>290:
                        break
                if time.time() - ts > 290:
                    break
            if time.time() - ts > 290:
                break
        best.append(best[0])
        self.plot_path(best)
        best=best[:-1]
        print("best path using 3opt:", best)
        f2.write(",".join([str(i) for i in best]))
        print("length of route", len(best))
        f2.write("\n"+str(len(best))+"\n")
        print("number of distinct elements in route", len(set(best)))
        print("least cost achieved:", mincost)
        f2.write("least cost achieved:"+ str(mincost))
        print("time spend: ", time.time() - ts, "sec")
        self.plt.show()
        return best

    def two_opt(self, route):
        route.append(route[0])
        best = route
        for kk in range(30):
            for i in range(1, len(route) - 2):
                for j in range(i + 1, len(route)):
                    if j - i == 1: continue
                    if self.cost_change(self.adj, best[i - 1], best[i], best[j - 1], best[j]) < 0:
                        best[i:j] = best[j - 1:i - 1:-1]
                route = best
        return best

    def plot_path(self,bst_route):
        x_c = []
        y_c = []
        for ji in range(n + 1):
            x_c.append(self.points[bst_route[ji]][0])
            y_c.append(self.points[bst_route[ji]][1])
        self.plt.plot(x_c, y_c, label="stars", color="blue", marker="*")

    def repeat2opt(self):
        cost_mat = self.adj
        cst = float("inf")
        bst_route = None
        for rn in range(90):
            i = self.que.get()[1]
            best_route = self.two_opt(i)
            ccst = self.cost_cal(best_route, cost_mat)
            if ccst < cst:
                bst_route = best_route
                cst = ccst

        self.plot_path(bst_route)
        bst_route = bst_route[:-1]
        print("best path using 2opt:", bst_route)
        print("length of route", len(bst_route))
        print("number of distinct elements in route", len(set(bst_route)))
        print("least cost achieved:", cst)
        print("wait for 3opt: till time limit exceeds...")
        bst_route.append(bst_route[0])
        print("time spend: ",time.time() - ts,"sec")
        self.plt.show()
        self.three_opt(bst_route)

if __name__ == '__main__':
    argn = len(sys.argv)
    f=None

    if(argn>1):
        f = open(sys.argv[1], "r")
    else:
        f = open(input("enter file name"), "r")
    print("time begins: 0")
    fn = f.readline().strip()
    n = int(f.readline().strip())
    findPath=TSP()
    nut = n
    route = findPath.solve(f, n)
    findPath.repeat2opt()
    f.close()
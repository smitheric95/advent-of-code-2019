import math
import csv 
import pandas as pd

def manhattan_distance(x,y):
    return sum(abs(a-b) for a,b in zip(x,y))


# lay first wire
# lay second, keeping track of overlaps
# return overlap shortest distance from origin

class CrossedWires:
    def __init__(self, x, y, org_x, org_y):
        self.graph = pd.DataFrame([[0 for _ in range(y)] for _ in range(x)])
        self.origin = (org_x, org_y)
        self.graph.iloc[org_y][org_x] = -1
        self.closest_intersection = None

    def lay_wires(self, file_name):
        with open(file_name) as f:
            csv_file = csv.reader(f)

            for i, wire in enumerate(csv_file):
                print(i)
                for loc in wire:
                    direction = loc[0]
                    length = int(loc[1:])
                    
                    cur_x = self.origin[1]
                    cur_y = self.origin[0]

                    if direction == 'U':
                        self.graph[self.graph.iloc[cur_y:cur_y+length][cur_x][i]] = 1
                    elif direction == 'D':
                        self.graph[self.graph.iloc[cur_y-length:cur_y][cur_x][i]] = 1
                    elif direction == 'R':
                        self.graph[self.graph.iloc[cur_y][cur_x:cur_x+length][i]] = 1
                    elif direction == 'L':
                        self.graph[self.graph.iloc[cur_y][cur_x-length:cur_x][i]] = 1

                    # self.print_grid()

    def find_intersections(self):
        if 1 > 0:
            # check to see if wire has been laid before
            
            # store shortest distance
            pass

if __name__ == "__main__":
    my_graph = CrossedWires(10,11, 0, 9)
    my_graph.graph.iloc[0:5, 0] += 1
    # for col in my_graph.graph[0:5]:
    #     my_graph.graph.loc[0, col] = [5,5]

    print(my_graph.graph)
    # my_graph.lay_wires('03/input2.csv')
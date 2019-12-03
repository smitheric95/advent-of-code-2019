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
        self.origin = (org_y, org_x)
        self.graph.iloc[org_y][org_x] = -1
        self.closest_intersection = None

    def lay_wires(self, file_name):
        with open(file_name) as f:
            csv_file = csv.reader(f)

            for i, wire in enumerate(csv_file):
                cur_x = self.origin[1]
                cur_y = self.origin[0]
                
                for loc in wire:
                    
                    direction = loc[0]
                    length = int(loc[1:])
                    
                    print(cur_x, cur_y)

                    if direction == 'U':
                        if cur_y == self.origin[1]:
                            cur_y -= 1

                        self.graph.iloc[cur_y-length:cur_y, cur_x] += 1
                        cur_y -= length
                    elif direction == 'D':
                        if cur_y == self.origin[1]:
                            cur_y += 1
                        
                        # bug
                        self.graph.iloc[cur_y:cur_y+length, cur_x] += 1
                        cur_y += length-1
                    elif direction == 'R':
                        if cur_x == self.origin[0]:
                            cur_x += 1
                            
                        self.graph.iloc[cur_y, cur_x+1:cur_x+length+1] += 1
                        cur_x += length
                    elif direction == 'L':
                        if cur_x == self.origin[0]:
                            cur_x -= 1

                        self.graph.iloc[cur_y, cur_x-length:cur_x] += 1
                        cur_x -= length+1
                    
                    # print(self.graph)

    def find_intersections(self):
        if 1 > 0:
            # check to see if wire has been laid before
            
            # store shortest distance
            pass

if __name__ == "__main__":
    my_graph = CrossedWires(10,11, 1, 8)
    # my_graph.graph.iloc[0:5, 0] += 1

    print(my_graph.graph)
    print("---------------")
    my_graph.lay_wires('03/input2.csv')
    print(my_graph.graph)

"""
R8,U5,L5,D3
U7,R6,D4,L4
"""
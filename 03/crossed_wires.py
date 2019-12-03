import math
import csv 

def manhattan_distance(x,y):
    return sum(abs(a-b) for a,b in zip(x,y))


# lay first wire
# lay second, keeping track of overlaps
# return overlap shortest distance from origin

class CrossedWires:
    def __init__(self, x, y, org_x, org_y):
        # store origin at center
        self.graph = [[(0,0) for _ in range(y)] for _ in range(x)]
        self.origin = (org_x, org_y)
        self.closest_intersection = None

    def __str__(self):
        print(self.graph)

    def lay_wires(self, file_name):
        with open(file_name) as f:
            csv_file = csv.reader(f)

            for i, wire in enumerate(csv_file):
                for loc in wire:
                    direction = loc[0]
                    length = int(loc[1:])
                    
                    cur_x = self.origin[1]
                    cur_y = self.origin[0]

                    if direction == 'U':
                        self.graph[cur_y:cur_y+length][cur_x][i] = 1
                    elif direction == 'D':
                        self.graph[cur_y-length:cur_y][cur_x][i] = 1
                    elif direction == 'R':
                        self.graph[cur_y][cur_x:cur_x+length][i] = 1
                    elif direction == 'L':
                        self.graph[cur_y][cur_x-length:cur_x][i] = 1

    def find_intersections(self):
        if 1 > 0:
            # check to see if wire has been laid before
            
            # store shortest distance
            pass

if __name__ == "__main__":
    my_graph = CrossedWires(10,11, 1, 1)
    my_graph.lay_wires('input2.csv')
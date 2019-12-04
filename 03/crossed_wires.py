import math
import csv 
import pandas as pd


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

            increment_value = 1

            for i, wire in enumerate(csv_file):
                cur_x = self.origin[1]
                cur_y = self.origin[0]
                
                for loc in wire:
                    direction = loc[0]
                    length = int(loc[1:])

                    if direction == 'U':
                        self.graph.iloc[cur_y-length:cur_y, cur_x] += increment_value
                        cur_y -= length

                    elif direction == 'D':
                        self.graph.iloc[cur_y+1:cur_y+length+1, cur_x] += increment_value
                        cur_y += length

                    elif direction == 'R':
                        self.graph.iloc[cur_y, cur_x+1:cur_x+length+1] += increment_value
                        cur_x += length

                    elif direction == 'L':
                        self.graph.iloc[cur_y, cur_x-length:cur_x] += increment_value
                        cur_x -= length

                increment_value += 99


    def shortest_intersection(self):
        intersections = []

        for col in self.graph:
            rows = list(self.graph[col][(self.graph[col] % 10 > 0) & (self.graph[col] // 100 > 0)].index)
            for row in rows:
                intersections.append((row, col))

        min = 100000

        for y, x in intersections:
            cur = self.manhattan_distance(self.origin, (y, x))
            if cur < min:
                min = cur

        return min

    # should be static
    def manhattan_distance(self, x, y):
        return sum(abs(a - b) for a, b in zip(x, y))

if __name__ == "__main__":
    """
    R8,U5,L5,D3
    U7,R6,D4,L4
    """
    my_graph = CrossedWires(20000, 20000, 10000, 10000)
    my_graph.lay_wires('input1.csv')

    print(my_graph.shortest_intersection())

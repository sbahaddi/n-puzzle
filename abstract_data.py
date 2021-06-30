class parser(object):
    def __init__(self, name_file):
        self.name_file = name_file

    def parser_file(self):
        pass

    def validation(self):
        pass

    def get_goal(self):
        pass


class solver(object):
    """class define data struct Puzzle and method need """
    def __init__(self):
        pass

    def F(self):
        pass

    def H(self):
        pass


class Node(object):
    def __init__(self, puzzle, depth, cost):
        self.graph = puzzle
        self.depth = depth
        self.cost = cost
        self.dims = len(puzzle)

    def generate_child(self):
        list_childern = []
        stps = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        x, y = self.find(-1)
        for stp in stps:
            i, j = stp
            array = self.shuffle(x, y, x + i, y + i)
            cost = self.get_goal(array)
            depth = self.depth + 1
            list_childern.append(Node(array, depth, cost))
        return list_childern

    def shuffle(self, x, y, x1, y1):
        """ swap tow element"""
        if x1 >= 0 and y1 >= 0 and y1 < self.dims and x1 < self.dims:
            puzzle = self.graph.copy()
            puzzle[y][x], puzzle[y1][x1] = puzzle[y1][x1], puzzle[y][x]
            return puzzle
        return None

    def get_goal(self, puzzle):
        gol = [[1, 2, 3], [4, -1, 5], [6, 7, 8]]
        cost = 0
        for i in range(self.dims):
            for j in range(self.dims):
                if puzzle[i][j] != -1:
                    x, y = self.find(puzzle[i][j])
                    cost += abs(x - i) + abs(y - j)
        return cost

    def find(self, elem):
        for i in range(self.dims):
            for j in range(self.dims):
                if self.graph[i][j] == elem:
                    return (i, j)
        return None


class Heap(object):
    """abstract data  for priority queue """

    def __init__(self):
        pass

class parser(object):
    def __init__(self, name_file):
        self.name_file = name_file

    def parser_file(self):
        pass

    def validation(self):
        pass


class Solver(object):
    """class define data struct Puzzle and method need """

    def __init__(self, puzzleStart, puzzleGoal):
        self.puzzleStart = Node(puzzleStart, 0, 0)
        self.puzzleGoal = puzzleGoal

### I am working with ordered list but priority queue must be implemented to get less element heapq
    def puzzleSolving(self):
        Heap = []
        Heap.append(puzzleStart)
        while True:
            puzzleCurrent = Heap[0]
            del Heap[0]
            for puzzle in puzzleCurrent.generate_child():
                item = Node(puzzle, self.F(puzzle, puzzleCurrent.depth))
                if item.cost == 0:
                    break
                Heap.append(item)
            Heap = sorted(Heap, key=lambda x: x.cost)

    def F(self, puzzle, depth):
        h = self.H(puzzle)
        cost = h + depth + 1
        return cost

    def H(self, puzzle):
        # gol = self.puzzleGoal
        gol = [[1, 2, 3], [4, -1, 5], [6, 7, 8]]
        cost = 0
        for i in range(len(puzzle)):
            for j in range(len(puzzle)):
                if puzzle[i][j] != -1 and puzzle[i][j] == gol[i][j]:
                    x, y = Node.find(puzzle[i][j])
                    cost += abs(x - i) + abs(y - j)
        return cost


class Node(object):
    def __init__(self, puzzle, depth, cost):
        self.graph = puzzle
        self.depth = depth
        self.cost = cost
        self.dims = len(puzzle)

    def generate_child(self):
        list_childern = []
        stps = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        x, y = Node.find(self.graph, -1)
        for stp in stps:
            i, j = stp
            array = self.shuffle(x, y, x + i, y + i)
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

    @classmethod
    def find(cls, puzzle, elem):
        for i in range(len(puzzle)):
            for j in range(len(puzzle)):
                if puzzle[i][j] == elem:
                    return (i, j)
        return None


class Heap(object):
    """abstract data  for priority queue """

    def __init__(self):
        pass

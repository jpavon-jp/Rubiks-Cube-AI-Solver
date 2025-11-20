# Homework 1 Josue Pavon ML.py

from collections import deque
import heapq
import time  # To measure execution time

# Rubik's Cube 2x2x2 Solver

class Cube2x2:
    def __init__(self):
        # Each face has 4 stickers (2x2)
        self.faces = {
            'Up': ['White'] * 4,
            'Down': ['Yellow'] * 4,
            'Front': ['Red'] * 4,
            'Back': ['Orange'] * 4,
            'Left': ['Green'] * 4,
            'Right': ['Blue'] * 4
        }

    def is_solved(self):
        return all(len(set(stickers)) == 1 for stickers in self.faces.values())

    def copy(self):
        new_cube = Cube2x2()
        new_cube.faces = {face: stickers.copy() for face, stickers in self.faces.items()}
        return new_cube

    def rotate_Up(self):
        f = self.faces
        f['Up'][0], f['Up'][1], f['Up'][3], f['Up'][2] = f['Up'][2], f['Up'][0], f['Up'][1], f['Up'][3]
        f['Front'][0:2], f['Right'][0:2], f['Back'][0:2], f['Left'][0:2] = \
            f['Right'][0:2], f['Back'][0:2], f['Left'][0:2], f['Front'][0:2]

    def rotate_Down(self):
        f = self.faces
        f['Down'][0], f['Down'][1], f['Down'][3], f['Down'][2] = f['Down'][2], f['Down'][0], f['Down'][1], f['Down'][3]
        f['Front'][2:4], f['Left'][2:4], f['Back'][2:4], f['Right'][2:4] = \
            f['Left'][2:4], f['Back'][2:4], f['Right'][2:4], f['Front'][2:4]

    def rotate_Front(self):
        f = self.faces
        f['Front'][0], f['Front'][1], f['Front'][3], f['Front'][2] = f['Front'][2], f['Front'][0], f['Front'][1], f['Front'][3]
        f['Up'][2], f['Up'][3], f['Right'][0], f['Right'][2], f['Down'][0], f['Down'][1], f['Left'][1], f['Left'][3] = \
            f['Left'][3], f['Left'][1], f['Up'][2], f['Up'][3], f['Right'][0], f['Right'][2], f['Down'][1], f['Down'][0]

    def rotate_Back(self):
        f = self.faces
        f['Back'][0], f['Back'][1], f['Back'][3], f['Back'][2] = f['Back'][2], f['Back'][0], f['Back'][1], f['Back'][3]
        f['Up'][0], f['Up'][1], f['Left'][0], f['Left'][2], f['Down'][2], f['Down'][3], f['Right'][1], f['Right'][3] = \
            f['Right'][1], f['Right'][3], f['Up'][0], f['Up'][1], f['Left'][2], f['Left'][0], f['Down'][2], f['Down'][3]

    def rotate_Left(self):
        f = self.faces
        f['Left'][0], f['Left'][1], f['Left'][3], f['Left'][2] = f['Left'][2], f['Left'][0], f['Left'][1], f['Left'][3]
        f['Up'][0], f['Up'][2], f['Front'][0], f['Front'][2], f['Down'][0], f['Down'][2], f['Back'][3], f['Back'][1] = \
            f['Back'][3], f['Back'][1], f['Up'][0], f['Up'][2], f['Front'][0], f['Front'][2], f['Down'][0], f['Down'][2]

    def rotate_Right(self):
        f = self.faces
        f['Right'][0], f['Right'][1], f['Right'][3], f['Right'][2] = f['Right'][2], f['Right'][0], f['Right'][1], f['Right'][3]
        f['Up'][1], f['Up'][3], f['Back'][2], f['Back'][0], f['Down'][1], f['Down'][3], f['Front'][1], f['Front'][3] = \
            f['Front'][1], f['Front'][3], f['Up'][1], f['Up'][3], f['Back'][2], f['Back'][0], f['Down'][1], f['Down'][3]

    def apply_move(self, move):
        moves = {
            'Up': self.rotate_Up,
            'Down': self.rotate_Down,
            'Front': self.rotate_Front,
            'Back': self.rotate_Back,
            'Left': self.rotate_Left,
            'Right': self.rotate_Right
        }
        if move in moves:
            moves[move]()

# Search Algorithms for the 2x2x2 Cube

def dfs_solver(start_cube, max_depth=7):
    stack = deque()
    visited = set()
    stack.append((start_cube, []))

    while stack:
        current_cube, path = stack.pop()
        state = str(current_cube.faces)

        if state in visited or len(path) > max_depth:
            continue
        visited.add(state)

        if current_cube.is_solved():
            return path

        for move in ["Up", "Down", "Front", "Back", "Left", "Right"]:
            new_cube = current_cube.copy()
            new_cube.apply_move(move)
            stack.append((new_cube, path + [move]))
    return None

def bfs_solver(start_cube):
    queue = deque()
    visited = set()
    queue.append((start_cube, []))

    while queue:
        current_cube, path = queue.popleft()
        state = str(current_cube.faces)

        if state in visited:
            continue
        visited.add(state)

        if current_cube.is_solved():
            return path

        for move in ["Up", "Down", "Front", "Back", "Left", "Right"]:
            new_cube = current_cube.copy()
            new_cube.apply_move(move)
            queue.append((new_cube, path + [move]))
    return None

def heuristic(cube):
    return sum(1 for face in cube.faces.values() if len(set(face)) > 1)

def a_star_solver(start_cube):
    heap = []
    visited = set()
    counter = 0
    MAX_DEPTH = 12

    heapq.heappush(heap, (heuristic(start_cube), counter, start_cube, []))

    while heap:
        _, _, current_cube, path = heapq.heappop(heap)
        state = str(current_cube.faces)

        if state in visited or len(path) > MAX_DEPTH:
            continue
        visited.add(state)

        if current_cube.is_solved():
            return path

        for move in ["Up", "Down", "Front", "Back", "Left", "Right"]:
            new_cube = current_cube.copy()
            new_cube.apply_move(move)
            new_path = path + [move]
            counter += 1
            heapq.heappush(heap, (len(new_path) + heuristic(new_cube), counter, new_cube, new_path))
    return None

# 3x3x3 simplified Cube Class 

class Cube3x3:
    def __init__(self):
        self.faces = {
            'Up': ['White'] * 9,
            'Down': ['Yellow'] * 9,
            'Front': ['Red'] * 9,
            'Back': ['Orange'] * 9,
            'Left': ['Green'] * 9,
            'Right': ['Blue'] * 9
        }

    def is_solved(self):
        return all(len(set(face)) == 1 for face in self.faces.values())

    def copy(self):
        new_cube = Cube3x3()
        new_cube.faces = {face: stickers.copy() for face, stickers in self.faces.items()}
        return new_cube

    def rotate_Up(self):
        f = self.faces
        temp = f['Front'][0:3]
        f['Front'][0:3] = f['Right'][0:3]
        f['Right'][0:3] = f['Back'][0:3]
        f['Back'][0:3] = f['Left'][0:3]
        f['Left'][0:3] = temp

    def apply_move(self, move):
        if move == 'Up':
            self.rotate_Up()

# BFS Solver for 3x3x3 Cube (I'm only testing 1 move scramble)
def bfs_solver_3x3(start_cube, max_depth=1):
    queue = deque()
    visited = set()
    queue.append((start_cube, []))

    while queue:
        current_cube, path = queue.popleft()
        state = str(current_cube.faces)

        if state in visited or len(path) > max_depth:
            continue
        visited.add(state)

        if current_cube.is_solved():
            return path

        for move in ['Up']:
            new_cube = current_cube.copy()
            new_cube.apply_move(move)
            queue.append((new_cube, path + [move]))
    return None

# Main Testing for All 3 Tests

if __name__ == "__main__":
    # Test 1 - DFS 2x2x2 (1 move)
    print("\n TEST 1: Scramble = ['Up']")
    cube1 = Cube2x2()
    cube1.apply_move("Up")
    start = time.time()
    dfs_result = dfs_solver(cube1)
    print("DFS Result:", dfs_result, "| Steps:", len(dfs_result), "| Time: {:.6f}s".format(time.time() - start))

    # Test 2 - BFS and A* 2x2x2 (2 moves)
    print("\n TEST 2: Scramble = ['Up', 'Front']")
    cube2 = Cube2x2()
    cube2.apply_move("Up")
    cube2.apply_move("Front")
    start = time.time()
    bfs_result = bfs_solver(cube2)
    print("BFS Result:", bfs_result, "| Steps:", len(bfs_result), "| Time: {:.6f}s".format(time.time() - start))
    start = time.time()
    a_star_result = a_star_solver(cube2)
    print("A* Result:", a_star_result, "| Steps:", len(a_star_result), "| Time: {:.6f}s".format(time.time() - start))

    # Test 3 – A* 2x2x2 (4 moves)
    #print(" TEST 3: Scramble = ['Up', 'Left', 'Front', 'Down']")
    #cube3 = Cube2x2()
    #for move in ["Up", "Left", "Front", "Down"]:
    #    cube3.apply_move(move)
    #start = time.time()
    #a_star_hard_result = a_star_solver(cube3)
    #print("A* Result:", a_star_hard_result, "| Steps:", len(a_star_hard_result), "| Time: {:.6f}s".format(time.time() - start))


    # Test 4 – BFS 3x3x3 (1 move)
    print("\n TEST 4: Cube 3x3x3 Scramble = ['Up']")
    cube4 = Cube3x3()
    cube4.apply_move("Up")
    start = time.time()
    result_3x3 = bfs_solver_3x3(cube4, max_depth=3)
    print("BFS Result:", result_3x3, "| Steps:", len(result_3x3), "| Time: {:.6f}s".format(time.time() - start))




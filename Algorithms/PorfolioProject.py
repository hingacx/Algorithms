from collections import deque


"""
An algorithm that solves the dungeon board game and returns the minimum moves required to complete the game
as well as the path taken. It uses dynamic programming and tracing to find an optimal solution and the optimal
solution itself.

The scenario is that you're given a game board in the form of a 2-D array with obstacles on it. Can you navigate
from a source cell to a destination cell in minimal moves? If so, determine the path of minimum distance with
the constraints of moving Left, Right, Up and Down only. 
"""



def optimal_solution(Count, Board, src, dst):
    """
    Finds an optimal solution to get from the source cell
    to the destination cell.
    """
    row = dst[0]
    col = dst[1]

    # ansr will contain the answer in a string form.
    ansr = " (" + str(row+1) + ", " + str(col+1) + ") "
    # moves contain the amount of moves in string form.
    moves = " "

    # Tracking backwards from the destination cell until we reach the source cell.
    while (row, col) != src:
        # Checking to see if the previous move was down.
        if Board[row][col] - 1 == Board[row-1][col]:
            ansr = "(" + str(row) + ", " + str(col+1) + ") " + "-> " + ansr
            moves = "D" + moves
            row, col = row-1, col
        # Checking to see if the previous move was up.
        elif row+1 < len(Board) and Board[row][col] - 1 == Board[row+1][col]:
            ansr = "(" + str(row+2) + ", " + str(col+1) + ") " + "-> " + ansr
            moves = "U" + moves
            row, col = row+1, col
        # Checking to see if the previous move was right.
        elif Board[row][col] - 1 == Board[row][col-1]:
            ansr = "(" + str(row+1) + ", " + str(col) + ") " + "-> " + ansr
            moves = "R" + moves
            row, col = row, col-1
        # Checking to see if the previous move was left.
        elif col+1 < len(Board[0]) and Board[row][col] - 1 == Board[row][col+1]:
            ansr = "(" + str(row+1) + ", " + str(col+2) + ") " + "-> " + ansr
            moves = "L" + moves
            row, col = row, col+1

    # Concatenating the ansr and moves strings before returning them.
    ansr = "The minimum count is " + str(Count-1) + " and a possible path is:" + moves + "\n" + ansr
    return ansr


def puzzle_helper(Board, src, dst):
    """
    Helper function that finds the minimum amount of cells passed through.
    Returns min number of cells or None if their is no path.
    """
    N = len(Board)     # Number of board rows
    M = len(Board[0])  # Number of board columns

    # Creating two priority queues with a deque.
    # and adding the Source coordinates to it.
    row_que, col_que = deque(), deque()
    row_que.append(src[0])
    col_que.append(src[1])

    # Utilization memoization in the form of a dictionary so that cells are
    # only explored once. Source cell is added since it holds the starting
    # coordinates.
    visited = {(src[0], src[1])}

    # This changes the cell value by +1 for each each cell which
    # represents the number of cells away from the source cell.
    # This is used to track the route/path taken.
    Board[src[0]][src[1]] = 0

    # Minimum number of cells passed through to get to the destination.
    count = 0

    # Starting at level 1. Since this is a BFS functionality, we'll track
    # the current level of cells to search.
    level = 1
    # Potential future levels/neighbor cells to search.
    next_level = 0
    # Contains the legal directions of a move.
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    # While loop that runs until all cells have been exhausted or the destination
    # cell is found.
    while len(row_que) > 0:
        # Moves are held in priority queue fashion so that at each "level" all those
        # cells are searched first before moving to the "next level". The priority
        # queue is split up into two queues for easier implementation, but work in
        # sync.
        row = row_que.popleft()
        col = col_que.popleft()

        # Found the destination which is the base case.
        # Returns the path to get there in the form of a
        # string as well as number of moves.
        if (row, col) == dst:
            return optimal_solution(count, Board, src, dst)

        # Checks all the legal move combinations from the current cell
        # and adds them to the priority queues.
        for move in directions:
            new_row = row + move[0]
            new_col = col + move[1]

            # Checking to see which new moves are valid and in bounds.
            if new_row < 0 or new_col < 0 or new_row >= N or new_col >= M:
                continue

            # Checking to see if the move has been completed already.
            if (new_row, new_col) in visited:
                continue

            # Find next move because a obstacle is in the way.
            if Board[new_row][new_col] == '#':
                continue

            # Add the moves to their respective queues and updates their
            # status as visited. Also if the code reached this far, a
            # new level of neighboring cells to search have been found.
            row_que.append(new_row)
            col_que.append(new_col)
            visited.add((new_row, new_col))
            # Updating new levels of cells to search for BFS.
            next_level += 1

            # Updating the cell value on the board.
            Board[new_row][new_col] = Board[row][col] + 1

        # Decrementing the current level as it's been searched.
        # So the search continues at the next level.
        level -= 1
        if level == 0:
            # Updates level to number of new levels of cells found.
            level = next_level
            # Reset new/next levels count.
            next_level = 0
            # Update minimum number of cells transversed through to
            # get to the destination cell.
            count += 1

    # If the base case was not found, then returns None.
    return None


def dungeon_puzzle(Board, Source, Destination):
    """
    Returns the minimum amount of cells passed through to reach
    a Destination cell from a Source cell.
    """
    # Converting the tuple coordinates to individual numbers/int.
    srow, scol = Source[0], Source[1]
    drow, dcol = Destination[0], Destination[1]

    # Checking to see if the coordinates fall within the board's boundaries.
    if Board[srow-1][scol-1] == "#":
        return None
    if Board[drow-1][dcol-1] == "#":
        return None
    if Board == Source:
        return None

    # Calls a helper function that returns the minimum cells passed through
    # if their exists a path.
    return puzzle_helper(Board, (srow-1, scol-1), (drow-1, drow-1))


# Gameboard example. "-" are valid spots to move, where "#" represents an obstacle.

sample1 = [['-', '-', '-', '-', '-'],
          ['-', '-', '#', '-', '-'],
          ['-', '-', '-', '-', '-'],
          ['#', '-', '#', '#', '-'],
          ['-', '#', '-', '-', '-']]
#print(dungeon_puzzle(sample1, (1, 3), (3,3)))
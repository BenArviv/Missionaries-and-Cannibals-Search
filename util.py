# utils.py
#
# This file contains basic helper functions to make

import heapq

ACTIONS = ((1, 0, 1), (2, 0, 1), (0, 1, 1), (0, 2, 1), (1, 1, 1))

class Problem:
    def __init__(self, initial_state=(3, 3, 1)):
        self.initial_state = initial_state
    
    def getStartState(self):
        return self.initial_state
    
    def isGoalState(self, state):
        return state == (0, 0, 0)
    
    def getSuccessors(self, state, alpha): # state is a tuple of (left_missionaries, left_cannibals, left_boat)
        successors = []
        
        for action in ACTIONS:
            new_state = (state[0] + alpha * action[0], state[1] + alpha * action[1], state[2] + alpha * action[2])
            if self.isValid(new_state):
                successors.append(new_state)
        
        return successors
    
    def isValid(self, state):
        "state is a vector of the form (m,c,b)"
        
        # check if the number of missionaries and cannibals on each bank is non-negative
        if state[0] < 0 or state[1] < 0 or (3 - state[0]) < 0 or (3 - state[1]) < 0:
            return False
        
        # check if the number of cannibals on each bank does not exceed the number of missionaries
        if (state[0] > 0 and state[1] > state[0]) or ((3 - state[0]) > 0 and (3 - state[1]) > (3 - state[0])):
            return False
        
        # check if the boat is on either bank
        if state[2] not in [0,1]:
            return False
        
        # otherwise, the state is valid
        return True

# stack implementation for IDDFS
class Stack:
    "A container with a last-in-first-out (LIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Push 'item' onto the stack"
        self.list.append(item)

    def pop(self):
        "Pop the most recently pushed item from the stack"
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the stack is empty"
        return len(self.list) == 0
    
# queue implementation for BFS
class Queue:
    "A container with a first-in-first-out (FIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Enqueue the 'item' into the queue"
        self.list.insert(0,item)

    def pop(self):
        """
          Dequeue the earliest enqueued item still in the queue. This
          operation removes the item from the queue.
        """
        return self.list.pop()
    
    def isEmpty(self):
        "Returns true if the queue is empty"
        return len(self.list) == 0
    
# priority queue implementation for GBFS and A*
class PriorityQueue:
    """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.
    """
    def  __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def update(self, item, priority):
        # If item already in priority queue with higher priority, update its priority and rebuild the heap.
        # If item already in priority queue with equal or lower priority, do nothing.
        # If item not in priority queue, do the same thing as self.push.
        for index, (p, c, i) in enumerate(self.heap):
            if i == item:
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority, c, item))
                heapq.heapify(self.heap)
                break
        else:
            self.push(item, priority)
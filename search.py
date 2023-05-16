import util
      

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    
    frontier = util.Queue() # Queue of (nodes, depth, path) triples
    reached = [] # list of nodes that have been reached
    expanded_nodes = 0
    depth = 1 # depth of the tree
    
    if problem.isGoalState(problem.getStartState()):
        return 0, []
    
    frontier.push((problem.getStartState(), depth, []))
    
    while not frontier.isEmpty():
        node, dp, path = frontier.pop()
        reached.append(node)
        expanded_nodes += 1 # increment number of nodes expanded
        factor = (-1) ** dp # change multiplication factor
        
        if problem.isGoalState(node):
            return expanded_nodes, path
        
        for child in problem.getSuccessors(node, factor):
            if child not in reached and child not in (frontierNode[0] for frontierNode in frontier.list):
                updatedPath = path + [child]
                frontier.push(((child), dp + 1, updatedPath))
    
    return -1, []

def iterative_deepening_search(problem):
    "Search the deepest nodes in the search tree first."
    
    def depth_limited_search(problem, depth, expanded_nodes):
        frontier = util.Stack() # Stack of (nodes, depth, path) triples
        reached = [] # list of nodes that have been reached

        if problem.isGoalState(problem.getStartState()):
            return 0, []
        
        frontier.push((problem.getStartState(), 1, []))
        
        while not frontier.isEmpty():
            node, dp, path = frontier.pop()
            reached.append(node)
            expanded_nodes += 1 # increment number of nodes expanded
            factor = (-1) ** dp # change multiplication factor
            
            
            if problem.isGoalState(node):
                print("depth: ", depth - 1)
                return expanded_nodes, 0, path
            
            if dp + 1 > depth: # child nodes are beyond the depth limit
                continue
            
            for child in problem.getSuccessors(node, factor):
                if child not in reached and child not in (frontierNode[0] for frontierNode in frontier.list):
                    updatedPath = path + [child]
                    frontier.push(((child), dp + 1, updatedPath))
    
        return 'cutoff', expanded_nodes, [] # cutoff
    
    depth = 1
    expanded_nodes = 0
    while True:
        result, expanded_nodes, path = depth_limited_search(problem, depth, expanded_nodes)
        if result == 'cutoff':
            depth += 1
        else:
            return result, path

def greedy_best_first_search(problem):
    "Search the node that has the lowest heuristic first."
    
    frontier = util.PriorityQueue() # Queue of (node, depth, cost, path) quadruples
    reached = [] # list of nodes that have been reached
    expanded_nodes = 0
    depth = 1 # depth of the tree
    
    if problem.isGoalState(problem.getStartState()):
        return 0, []
    
    frontier.push((problem.getStartState(), depth, 0, []), 0)
    
    while not frontier.isEmpty():
        node, dp, cost, path = frontier.pop()
        reached.append(node)
        expanded_nodes += 1 # increment number of nodes expanded
        factor = (-1) ** dp # change multiplication factor
        
        if problem.isGoalState(node):
            return expanded_nodes, path
        
        for child in problem.getSuccessors(node, factor):
            heuristic_value = heuristic(child) # h(x) = (missionariesLeft + cannibalsLeft) / 2
            updatedPath = path + [child]
            
            if child not in reached and child:
                frontier.update(((child), dp + 1, heuristic_value, updatedPath), heuristic_value)

def a_star_search(problem):
    "Search the node that has the lowest combined cost and heuristic first."
    
    frontier = util.PriorityQueue() # Queue of (node, depth, cost, path) quadruples
    reached = [] # list of nodes that have been reached
    expanded_nodes = 0
    depth = 1 # depth of the tree
    # trips = 0 # number of trips taken
    
    if problem.isGoalState(problem.getStartState()):
        return 0, []
    
    frontier.push((problem.getStartState(), depth, 0, []), 0)
    
    while not frontier.isEmpty():
        node, dp, cost, path = frontier.pop()
        reached.append(node)
        expanded_nodes += 1 # increment number of nodes expanded
        factor = (-1) ** dp # change multiplication factor, -1: boat going right, 1: boat going left
        # trips += 1
        
        if problem.isGoalState(node):
            return expanded_nodes, path
        
        for child in problem.getSuccessors(node, factor):
            updatedCost = cost + (2 + factor) # +1 if the boat is going right, +3 if the boat is going left
            heuristic_value = 0.5 * updatedCost + heuristic(child) # h(x) = (missionariesLeft + cannibalsLeft) / 2
            updatedPath = path + [child]
            
            if child not in reached and child:
                frontier.update(((child), dp + 1, updatedCost, updatedPath), heuristic_value)


def heuristic(node):
    return (node[0] + node[1]) / 2 # h(x) = (missionariesLeft + cannibalsLeft) / 2


def run(): # run the search algorithms
    
    problem = util.Problem()
    
    expanded_nodes, path = breadthFirstSearch(problem)
    print("BFS:")
    print("Expanded Nodes: ", expanded_nodes)
    print("Path: ", path)
    print("----------------------------------------")
    
    expanded_nodes, path = iterative_deepening_search(problem)
    print("IDDFS:")
    print("Expanded Nodes: ", expanded_nodes)
    print("Path: ", path)
    print("----------------------------------------")
    
    expanded_nodes, path = greedy_best_first_search(problem)
    print("IDDFS:")
    print("Expanded Nodes: ", expanded_nodes)
    print("Path: ", path)
    print("----------------------------------------")
    
    expanded_nodes, path = a_star_search(problem)
    print("A*:")
    print("Expanded Nodes: ", expanded_nodes)
    print("Path: ", path)
    
run()
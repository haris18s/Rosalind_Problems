def parse_file(filename):
    """
       Parses a file containing trees in Newick format and node-pair distance queries.

       Each tree is provided in Newick format on one line, and is followed by a second line
       containing two node labels (separated by space), for which the distance should be computed.
           Parameters:
        filename (str): Path to the input file.
            Returns:
        tuple:
            - parent_maps (List[dict]): A list of dictionaries, where each dictionary represents
              a tree in the form {parent: [child1, child2, ...]}.
            - queries (List[Tuple[str, str]]): A list of tuples, each containing a pair of node names
              (x, y) representing the query for the corresponding tree.
        """
    with open(filename) as f:
        lines = [line.strip() for line in f if line.strip()]

    parent_maps = []
    queries = []
    for i in range(0, len(lines), 2):
        new_wick_str = lines[i]
        query = lines[i+1].split()

        parent_map = parse_indiv_newick(new_wick_str)
        parent_maps.append(parent_map)

        x, y = query
        queries.append((x, y))
    return parent_maps, queries


def parse_indiv_newick(newick_str):
    """
        Parses a single Newick-formatted tree string into a dictionary representing the tree's structure.
        Internal nodes are auto-named (e.g., 'internal_1'). Leaf names are preserved.
    Parameters:
        newick_str (str): A string in Newick format representing a single tree (with or without semicolon).

    Returns:
        dict: A dictionary where each key is a parent node (e.g., an internal node),
              and each value is a list of its children in left-to-right order.
        """

    #Remove surrinoudning white space and final semicolon
    newick_str = newick_str.strip().rstrip(";")
    parent_map = {}
    #Stack to track current parsing state
    stack = []
    internal_node_counter = 1 #to name internal nodes
    i = 0
    while i < len(newick_str):
        char = newick_str[i]

        if char =="(": #start a new internal node grouping
            stack.append('(')

        elif char == ")":
            #end of a group. pop all children from the stuck until new '('
            children = []
            while stack and stack[-1] != "(":
                child = stack.pop()
                children.insert(0, child)

            stack.pop() #remove '(' from stack

            internal_node = f"internal_{internal_node_counter}" #the internal node is iused instead of the parent
            internal_node_counter += 1
            #map internal node to its children
            parent_map[internal_node] = children
            #push internal node back to stack as a node
            stack.append(internal_node)
        elif char == ",":
            #comma appears sibling nodes, nothing to do
            pass
        else:
            #parse leaf nodes name (can be multiple chars)
            start = i
            while i < len(newick_str) and newick_str[i] not in '(),':
                i += 1
            leaf = newick_str[start:i]
            stack.append(leaf)
            continue #skip the increment since we moved i
        i += 1 #move to next character
    return parent_map


def InvertChildParent(parent_map):
    """Invert parent_map from parent --> children to
                               child -->parent
        Args:
        parent_map (dict): Dictionary with structure {parent: [child1, child2, ...]}.

    Returns:
        dict: Dictionary with structure {child: parent}.
    """
    child_to_parent = {}
    for parent, children in parent_map.items():
        for child in children:
            child_to_parent[child] = parent
    print(child_to_parent)
    return child_to_parent


def path_to_root(node, child_to_parent):
    """
        Traces the path from a given node to the root of the tree, following parent-child relationships.

        Args:
            node (str): The starting node whose path to the root is to be traced.
            child_to_parent (dict): A dictionary where the keys are child nodes and the values are their respective parent nodes.

        Returns:
            list: A list of nodes from the given node to the root, inclusive.
            The root is the last node in the list, which has no parent.
            """
    path = []
    while node in child_to_parent:#Trace until you find a root
        path.append(node)
        node = child_to_parent[node] #move to the parent
    path.append(node)
    return path


def find_distance(x, y, parent_map):
    """Find the distance between two nodes by directly comparing their paths to the root."""
    # Get paths from both nodes to the root
    path_x = path_to_root(x, parent_map)
    path_y = path_to_root(y, parent_map)

    #Reverse the paths to compare from the root
    reversed_x = path_x[::-1]
    reversed_y = path_y[::-1]

    #Find the common part of the paths (from the root upwards)
    i = 0
    while i < len(reversed_x) and i < len(reversed_y) and reversed_x[i] == reversed_y[i]:
        i += 1

    #Calculate the distance: steps to go up from `x` to the common ancestor and from `y` to the common ancestor
    distance = (len(reversed_x) - i) + (len(reversed_y) - i)

    return distance


def final_distances(parent_maps, queries):
    distances_per_tree = []
    #iterate over each tree and correspnding query
    for idx in range(len(parent_maps)):
        parent_map = parent_maps[idx] #get current map
        x, y = queries[idx][0], queries[idx][1] #get query
        #Invert to child--> parent
        child_to_parent = InvertChildParent(parent_map)
        #find distance between nodes x,y
        distance = find_distance(x, y, child_to_parent)
        distances_per_tree.append(distance)

    print(" ".join(map(str, distances_per_tree)))  # convert each distance to string and then join


def main():
    parent_maps, queries = parse_file("rosalind_nwck.txt")
    final_distances(parent_maps, queries)

if __name__ == "__main__":
    main()
"""Rosalind problme : Completing a tree (https://rosalind.info/problems/tree/)
 The script finds the number of compoents in a graph.
 After determining the number of connected components, we can calculate the minimum numbe of edges needed to connect
 all the components. if connected components k, it will require k-1 edgees -1
 """

def parse_graph(filename):
    """
    Reads a file containing graph data and builds an adjacency list representation.

    Parameters:
        filename (str): The name of the file containing the graph data.

    Returns:
        n (int): The number of nodes in the graph.
        adj_list (dict): An adjacency list representing the graph.
    """
    with open(filename) as f:
        data = f.readlines()
        n = int(data[0])
        #initialize dic, with ky for all nodes, some nodes may not connected with others
        adj_list = {node: [] for node in range(1, n+1)}

        for line in data[1:]:  # Skip the first line, assuming it holds node count
            line = line.strip()

            #Skip lines that don't contain enough information
            if len(line) < 2:
                continue
            #because it is an undirected graph
            u,v = map(int, line.split())
            adj_list[u].append(v)
            adj_list[v].append(u)

    print("Parsed graph:", adj_list)
    return n, adj_list


def count_connected_components(n,graph):
    """
    Counts the number of connected components in a graph using Depth-First Search (DFS).

    Parameters:
        n (int): The number of nodes in the graph.
        graph (dict): An adjacency list where keys are nodes, and values are lists of connected nodes.

    Returns:
        component_count (int): The number of connected components in the graph.
    """
    visited_nodes= set()
    component_count = 0

    #Inner funciton to perform DFS from a given node
    def dfs(node):
        """Function to perform depth first search for given node. When the visited nodes reaching the end, means
          there is not other connection, so it is the end of one component"""
        #Use a stack for DFS traversal to avoid recursion limits in large graphs
        stack = [node]

        #Process nodes in the stack
        while stack:
            current = stack.pop()
            #if current is unsvited mark it as visited
            if current not in visited_nodes:
                visited_nodes.add(current)
                #Add all adjacent nodes to the stack for further exploration
                stack.extend(graph.get(current, [] ))

    #Loop through each node to ensure all compnents are explored
    for node in range(1, n+1):
        #if node not visited, is the start of new component
        if node not in visited_nodes:
            dfs(node)
            component_count +=1

    return component_count

def main():
    nodes, graph = parse_graph('test.txt')
    k_compontents = count_connected_components(nodes, graph)
    edges_to_add = k_compontents -1
    print("Edges needed to connect all components:", edges_to_add)

if __name__ == "__main__":
    main()


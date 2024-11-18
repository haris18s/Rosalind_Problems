

def parse_file(filename):
    """
    Reads a file containing sequences, one sequence per line, and stores them in a list.

    Args:
        filename (str): The name of the file containing DNA sequences.
    Returns:
        list[str]: A list of sequences.
    """
    sequences = []
    with open(filename) as f:
        data = f.readlines()

    for line in data:
        line = line.rstrip()
        sequences.append(line)

    return sequences

class Trie:
    """
    A Trie data structure to efficiently store and process DNA sequences.

    Attributes:
        childNode (list): List of child nodes (size 4 for A, T, C, G).
        endOfWord (bool): Marks if a node represents the end of a word.
        child_id (int): Unique identifier for the node.
    """

    def __init__(self):
        self.childNode = [None] *4
        self.endOfWord = False
        #Hold unique identifuer of the node
        self.child_id = None



    def char_to_index(self, char ):
        """
        Maps a character to an index (0 for A, 1 for T, 2 for C, 3 for G).

        Args:
            char (str): A character (A, T, C, or G).
        Returns:
            int: The corresponding index for the character.
        """
        mapping = {"A":0, "T": 1, "C":2, "G":3}

        return mapping[char]

    def insertString(self, string):
        """
        Inserts a string into the Trie.

        Args:
            string (str): The string to be inserted.
        """
        node =self

        #Traverse each nt in the str
        for nt in string:
            #Get the index
            index = self.char_to_index(nt)
            #if the child node doesnt exist, create it
            if node.childNode[index] is None:
                node.childNode[index] = Trie()
            node = node.childNode[index] #move to childnode

        #mark the end of the world, at the end
        node.endOfWord = True



    def assign_node_ids(self, current_id = 1):
        """
        Recursively assigns unique IDs to each node in the Trie.

        Args:
            current_id (int): The starting ID to assign.
        Returns:
            int: The next avialble id"""

        #Assign curent id to this node
        self.child_id = current_id
        #increment id for the next node
        current_id +=1
        for child in self.childNode:
            if child is not None:
                current_id = child.assign_node_ids(current_id)
        return current_id



    def encode_edges(self, parent_id):
        """
        Encodes the edges of the Trie as a list of (parent_id, child_id, character) tuples.

        Args:
            parent_id (int): The ID of the parent node.
        Returns:
            List[Tuple[int, int, str]]: A list of encoded edges.
        """
        edges = []
        for index, child in enumerate(self.childNode):
            #if child node ecists
            if child is not None:
                #get the character for the current index
                char = ["A", "T", "C", "G"][index]
                #Add edge to the list
                edges.append((parent_id, child.child_id, char))
                #recursively encode edges for child node
                edges.extend(child.encode_edges(child.child_id))

        return edges


if __name__ == "__main__":

    # Example usage:
    lis = ['ATAGA', 'ATC', 'GAT']
    trie = Trie()

    #seqs = parse_file("rosalind_trie.txt")
    seqs = ['ATAGA', 'ATC', 'GAT']

    #Inset each string to the trie
    for string in seqs:
        trie.insertString(string)
    #Assign unique ids to all nodes in the Trie
    trie.assign_node_ids()

    #Encode edges as ((parent_id, child_id, character))
    edges = trie.encode_edges(1)

    #Output
    with open('output1.txt', "w") as output:
        for edge in edges:
            line = " ".join(map(str, edge))
            output.write(f'{line} \n')


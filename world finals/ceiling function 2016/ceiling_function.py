import sys
"""Import the 'sys' module to read input from the command line and the typing module for type hints"""
from typing import List, Tuple
"""import 'List' & 'Tuple'"""
def Create_Tag(tree: List[int]) -> str:
    """function 'creat_Tag' to create a tag for the current tree,
    it does that with the help of a modified tree walk algorithmus,
    it construct a signature for the tree based on its structure."""
    if not tree:
        """check if tree = nil"""
        return "X"
    """if so then return 'X'"""
    root_value = tree[0]
    """otherwise set the root to be the first value in the list (tree)"""
    left_subtree = [x for x in tree[1:] if x < root_value]
    """if the current value is less than its parent then add it to 'left_subtree'"""
    right_subtree = [x for x in tree[1:] if x >= root_value]
    """if the current value more or equal to its parent then add it 'right_subtree"""
    left_signature = Create_Tag(left_subtree)
    """create a signature for each node in the left subtree"""
    right_signature = Create_Tag(right_subtree)
    """create a signature for each node in the right subtree"""
    return f"(N{left_signature}{right_signature})"
"""for each node we calculate its signature as follows:
we put each node in brackets, then we concatinate :
'N' : for node, followed by its left child followed by its right child
'X' : for value NIL (child of a leafs)"""
def solver() -> None:
    """function 'solver' that findes the number of diffrent tree shapes."""
    for line in sys.stdin:
        """read the input"""
        n, k = map(int, line.split())
        """from the first input line, split the two values and define:
        n : the number of prototypes (trees).
        k : the number of layers (nodes)."""
        distinct_Tags = set()
        """create a set 'distinct_Tags' to store trees tags"""
        for i in range(n):
            """iteration over n lines of input"""
            L = list(map(int, sys.stdin.readline().split()))
            """create a list 'L' from the values in this line,
            'L' represent a BST by inserting its value into a BST inorder."""
            Tag = Create_Tag(L)
            """find the unique tag for this list (tree) """
            distinct_Tags.add(Tag)
            """add the created tag in the set 'distinct_Tags'"""
        diffrent_tree_shapes = len(distinct_Tags)
        """calculate the number of diffrent tree shapes,
        which is the number of tages in set 'distinct_Tags'."""
        print(diffrent_tree_shapes)
        """output the number of diffrent tree shapes"""
solver()
"""call faunction 'solver' to find a solution for one case"""
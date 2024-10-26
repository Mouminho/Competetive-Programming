import sys

def deep_first_search(u, p):
    L1 = []
    """empty list created to store the recursive call of deep_first_search"""
    for v in graph[u]:
        """go through the neighboring node of the current node 'u' """
        if v != p:
            """To avoid an endless loop, only look at edges a,b and b,a once
            and so we check if neighbore node is not equal to parent node 'p' """
            L1.append(deep_first_search(v, u))
            """Append the result of the recursive call to `deep_first_search` with `v` as the new current node and `u` as the new parent node"""
    L1.sort(key=lambda x: (-x[0], x[1]))
    """Sort the list `L1` based on two criteria:
    1. Sort in descending order based on the first element of each tuple in `L1`.
    2. Sort in ascending order based on the second element of each tuple in `L1`."""
    attackers, lost = castles[u]
    """get attackers and the value of lost which is missings+guards for the current node 'u' in dictionary 'castles' """
    for i in range(len(L1)):
        attackers = max(attackers, lost + L1[i][0])
        """Update the number of attackers by taking the maximum of the current number of attackers 
        and `lost` plus the number of attackers from the recursive call."""
        lost += L1[i][1]
        """ update 'lost' by adding 'lost' + the numbers of guard """
    return max(attackers, lost), lost

#

cases = 0
""" initialize the variable Cases to keep in track the number of test Cases"""
while True:
    """ in this loop it go and insert the input data of a castle in the dictionary"""
    numbers_of_castles = int(input())
    if numbers_of_castles == 0:
        """before ending the loop there would be a 0 input. test if there is 0 
        and then break the loop and end the code"""
        break
    castles = {}
    """creat a dictionary to store the number of castles as key and the information 
    of each castle as value pair"""
    graph = {}
    """this graph dictionary to represent the graph of the castles
    and the line between each of them as key: Value pair"""
    for i in range(1, numbers_of_castles+1):
        """loop for from range 1 to numbers_of_castles + 1"""
        attackers, missings, guards = map(int, input().split())
        """input castles information in the variables 'attackers', 'missings' and 'guards'
        which each mean corrisponding to each variable:
        minimum numbers needed to attack and capture a castle,
        numbers of soldiers expected to die
        and number of soldiers must be left at the castle to defend it"""
        castles[i] = max(attackers, missings+guards), missings+guards
        """calculate maximum numbers of attackers if the numbers of attackers is > missing+ guards
        and the value of the missings+guards"""
        graph[i] = []
        """initialize an empty list for each castle to explian each castle where to go
        and which other castles is it connected to"""
    for j in range(numbers_of_castles-1):
        u, v = map(int, input().split())
        """map the input of Edges between each castles into two variables 
        'u' and 'v' and since it undirected Edges it means it can go back and forth just one time
        between 2 castles"""
        graph[u].append(v)
        graph[v].append(u)
        """take each castles as nodes 'key' and each castle it go to as 'value part'"""
    return_value = float('inf'), float('inf')
    """tuple as variable to find the minimum result 'return value'"""
    for i in range(1, numbers_of_castles+1):
        return_value = min(return_value, deep_first_search(i, -1))
        """return value as minimum between the current return value and the value of methode
        deep-first-search with the current variable
        """
    print(f"Case {cases+1}: {return_value[0]}")
    """print the result of the current test case"""
    cases += 1
    """increment the number of cases if there is more than one more test cases in the input"""
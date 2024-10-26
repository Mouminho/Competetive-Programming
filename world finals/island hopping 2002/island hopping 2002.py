import math

class IslandEdge:
    """Define a class named 'IslandEdge'.
    This class represents an edge between two islands, with a source, destination, and distance."""
    def __init__(self, source=0, destination=0, distance=0):
        """Initialize an IslandEdge object with source, destination, and distance."""
        self.source = source
        self.destination = destination
        self.distance = distance

    def __lt__(self, other_edge):
        """The method '__lt__' is used to sort the edges based on their distances."""
        return self.distance < other_edge.distance

def calculate_average_distance(num_islands, X_COORDINATES, Y_COORDINATES, ISLAND_MASSES):
    """Calculate the average distance between the islands."""
    EDGES = []
    representative = [i for i in range(num_islands)]
    set_weights = [1] * num_islands
    island_masses_copy = ISLAND_MASSES.copy()

    for i in range(num_islands):
        for j in range(i + 1, num_islands):
            distance = math.hypot(X_COORDINATES[i] - X_COORDINATES[j], Y_COORDINATES[i] - Y_COORDINATES[j])
            EDGES.append(IslandEdge(i, j, distance))
            """Calculate Euclidean distance between 2 islands using 'math.hypot' function.
            Create an IslandEdge object with source, destination, and distance, and add it to the 'EDGES' list."""

    EDGES.sort()
    """Sort 'EDGES' in ascending order based on distances."""
    total_mass = sum(ISLAND_MASSES)
    """Calculate the total mass of island masses."""
    weighted_distance_sum = 0
    """Initialize the variable 'weighted_distance_sum' to 0."""

    def find_set_representative(element):
        """Find the representative (parent) of the set containing 'element' in the disjoint-set data structure."""
        if representative[element] == element:
            return element
        else:
            representative[element] = find_set_representative(representative[element])
            return representative[element]
            """If the parent of `element` is equal to `element`, it means that `element` is the representative of the set,
            so it is returned. Otherwise, the function is called recursively with the parent of `element` as the argument."""

    def join_sets(element_x, element_y):
        """Merge the sets containing 'element_x' and 'element_y'."""
        root_x = find_set_representative(element_x)
        root_y = find_set_representative(element_y)
        
        if root_x != root_y:
            if set_weights[root_x] > set_weights[root_y]:
                representative[root_y] = root_x
                set_weights[root_x] += set_weights[root_y]
                island_masses_copy[root_x] += island_masses_copy[root_y]
            else:
                representative[root_x] = root_y
                set_weights[root_y] += set_weights[root_x]
                island_masses_copy[root_y] += island_masses_copy[root_x]
                """Merge the set containing 'element_x' into the set containing 'element_y'."""

    for edge in EDGES:
        u = edge.source
        v = edge.destination
        if find_set_representative(u) != find_set_representative(v):
            """Check if the source and destination islands belong to different sets."""
            if find_set_representative(u) == find_set_representative(0):
                """Check if 'u' belongs to the set containing the element '0'."""
                weighted_distance_sum += island_masses_copy[find_set_representative(v)] * edge.distance
                """Calculate the weighted distance between the sets containing 'u' and 'v'."""
            if find_set_representative(v) == find_set_representative(0):
                """Check if 'v' belongs to the set containing the element '0'."""
                weighted_distance_sum += island_masses_copy[find_set_representative(u)] * edge.distance
                """Calculate the weighted distance between the sets containing 'u' and 'v'."""
            join_sets(u, v)
            """Iterate through the sorted EDGES.
            Check if the source and destination islands of the edge belong to different sets.
            If the source or destination belongs to the set containing element '0', update 'weighted_distance_sum' and
            join the sets."""

    return weighted_distance_sum / total_mass
    """Calculate the average distance."""

def solve():
    case_count = 0
    MAX_ISLANDS = 50

    while True:
        num_islands = int(input())
        """Input the number of islands."""
        if num_islands == 0 or num_islands > MAX_ISLANDS:
            break
        """If the number of islands is 0, then break."""
        X_COORDINATES = [0] * num_islands
        Y_COORDINATES = [0] * num_islands
        ISLAND_MASSES = [0] * num_islands
        """Create three lists with a length of 'num_islands' to store the coordinates of the island and its mass.
        'ISLAND_MASSES' represents the number of population of an island."""
        for i in range(num_islands):
            X_COORDINATES[i], Y_COORDINATES[i], ISLAND_MASSES[i] = map(float, input().split())
            """Input the coordinates of an island and its population (its mass)."""
        average_distance = calculate_average_distance(num_islands, X_COORDINATES, Y_COORDINATES, ISLAND_MASSES)
        print(f"Island Group: {case_count + 1} Average {average_distance:.2f}\n")
        case_count += 1
solve()
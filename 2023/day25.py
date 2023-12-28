import networkx as nx
from submit_if_correct import submit_if_correct
YEAR = 2023 

# ------------------ #
DAY = 25 # CHANGE THIS
# ------------------ #

def solve_part_1(input, test_case=True):
    # -------------PART 1------------- #
    TRUE_ANSWER = 54

    # build graph from input
    G = nx.Graph()
    for line in input.splitlines():
        src, adjacent = line.split(': ')
        for dest in adjacent.split(' '):
            G.add_edge(src, dest)

    # find min_cut
    min_cut = nx.minimum_edge_cut(G)

    # remove min_cut from graph
    G.remove_edges_from(min_cut)

    # find subgraphs
    connected_components = nx.connected_components(G)

    # multiply together sizes of subgraphs
    answer = 1
    for component in connected_components:
        answer *= len(component)

    if test_case:
        print(f'(TEST) Part 1: {answer}')
        submit_if_correct(solve_part_1, answer, TRUE_ANSWER, DAY, 1, YEAR)
    else:
        print(f'(REAL) Part 1: {answer}')
    return answer


part1=open(f"ex_inputs/day{DAY}/1.txt","r")
solve_part_1(part1.read(), test_case=True)

"""
in this function we do these things:
1. collect all messages from all processes
2. send messages to processes
3. update the tree of all processes
    - if any message doesn't receive or is garbage then the process add null value to that node
    - the process tree should be full only with null values
4. after f+1 round start making decisions
5. print the decision of all nodes in all trees of all processes

"""
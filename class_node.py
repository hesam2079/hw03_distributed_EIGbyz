''' in this class we have two methods and three values
value for value of node 0,1
path is string of x in pseudocode
and leaf flag is flag that if it is true then the node is leaf else node is non leaf

method new_val calculate the new value of node
method get_val return the value of node'''

class Node:
    def __init__(self, value, path, leaf_flag):
        self.value = value
        self.path = path
        self.leaf_flag = leaf_flag

    def new_val(self, my_childes, v0=0):
        if not self.leaf_flag: # check that i'm a leaf of not
            for child in my_childes:
                if child.value is None:
                    child.value = v0
            count = 0
            for child in my_childes:
                if child.value == v0:
                    pass
                else:
                    count += 1
            if count > len(my_childes):
                self.value = 1
            else:
                self.value = 0
        else:
            pass # if i am a leaf so my value is self.value and nothing's gonna to change

    def get_value(self, my_childes, v0=0): # calculate the value and return it
        self.new_val(my_childes, v0)
        return self.value
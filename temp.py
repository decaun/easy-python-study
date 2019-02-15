'''def get_squares_gen(n): # generator approach
    for x in range(n):
        yield x ** 2 # we yield, we don't return
        
result=get_squares_gen(5)
print(result)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(result.__next__())'''

import binary_search_tree

a=binary_search_tree.binary_search_tree()
a.insert('80')
a.insert('820')
a.print_tree()
print(a.find('80').value)
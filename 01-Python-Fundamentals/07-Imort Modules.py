# print('my_module')
# test = 'test string'
# def find_index(to_search, target):
#     for i,value in enumerate(to_search):
#         if value == target:
#             return i
#             return -1

# import Import Modules as my_module
# couirse = ['Math', 'Art', 'History', 'CompSci']
# index = my_module.find_index(course, 'Art')
# print(index)  # Output: 1

def outer():
    x = 'outerx'
    def inner():
        # x = 'innerx'
        print(x)

    inner()
    print(x)    
outer()    
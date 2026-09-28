print('my_module')
test = 'test string'
def find_index(to_search, target):
    for i,value in enumerate(to_search):
        if value == target:
            return i
            return -1

# from my_module import find_index
# course = ['his','math','phy']
# index = find_index(course,'phy')
# print(index)
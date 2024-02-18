def unique(number_list):
    number_set = set()
    for number in number_list:
        if number not in number_set:
            number_set.add(number)
    return number_set

#def bio():
#    n = int(input("Введите число элементов в генеалогическом дереве: "))
#    tree = {}
#    for i in range(1, n):
#        child, parent = input(f"Введите имя потомка и родителя ({i}): ").split()
#    tree[parent] = child
#    queue = sorted(list(tree.keys()))
#    while queue:
#        person = queue.pop(0)
#        height = 0
#        if person in tree:
#            children = tree[person].split()
#            if children:
#                queue.extend(children)
#                height += 1
#        print(f"{person}: {height}")

def height(man):
    if man not in p_tree:
        return 0
    else:
        return 1 + height(p_tree[man])

    ##############
    # MAIN BLOCK #
    ##############

print("Выберите номер задания от 1 до 2")
nn = int(input("Номер: "))
if nn == 1:
    numbers = int(input('Введите количество чисел: '))
    number_list = []
    for _ in range(numbers):
        num = int(input('Введите число: '))
        number_list.append(num)
    result = unique(number_list)
    print(f'В списке {numbers} чисел, из которых {len(result)} различных.')
if nn == 2:
    p_tree = {}
    n = int(input("Введите число элементов в генеалогическом древе: "))
    for i in range(n - 1):
        child, parent = input("Введите пару потомок - родитель: ").split()
        p_tree[child] = parent

    heights = {}
    for man in set(p_tree.keys()).union(set(p_tree.values())):
        heights[man] = height(man)

    for key, value in sorted(heights.items()):
        print(key, value)

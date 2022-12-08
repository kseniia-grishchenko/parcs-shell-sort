# def shellSort(arr):
#     gap = len(arr) // 2
#     while gap > 0:
#         j = gap
#         while j < len(arr):
#             i = j - gap
#             while i >= 0:
#                 if arr[i + gap] > arr[i]:
#                     break
#                 else:
#                     arr[i + gap], arr[i] = arr[i], arr[i + gap]
#                 i = i - gap
#             j += 1
#         gap = gap // 2
#
#
# arr2 = [12, 34, 54, 2, 3]
# print("input array:", arr2)
#
# shellSort(arr2)
# print("sorted array", arr2)


import random
array_numbers = []
f = open('500000.txt', 'w')
for i in range(500000):
    num = random.randint(10000, 10000000)
    array_numbers.append(num)
    print(int(num))
    f.write(str(num))
    f.write(' ')
f.close()
print(array_numbers)
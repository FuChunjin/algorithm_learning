# # 1st bubble sort
# # __author__: Fyilyer
# # 2020.5.24

# # 定义一个数字列表
# arr = [54, 26, 10, 3, 49, 10, 1, 4]
# 
# # 打印的长度为８,实际上把8放在range里面只能取到7，因为range是左闭右开的
# print(len(arr))
# 
# # 冒泡排序，range索引左闭右开
# def bubble_sort(arr):
#     for i in range(1, len(arr)):
#         # 错误示范,但也可以实现该项功能，只不过复杂度很高，增加了很多无效计算，可以自己推一下
#         for j in range(0, len(arr)-1):
#             if arr[i] > arr[j]:
#                 arr[i], arr[j] = arr[i], arr[j]
#             else:
#                 arr[i], arr[j] = arr[j], arr[i]
#     print(arr)
# bubble_sort(arr)




# # __version__: 2nd bubble sort
# # __author__: Fyilyer
# # __date__: 2020.5.24
# 
# # 定义一个数字列表
# arr = [54, 26, 10, 3, 49, 10, 1, 4]
# 
# # 打印的长度为８,实际上把8放在range里面只能取到7，因为range是左闭右开的
# print(len(arr))
# 
# # 冒泡排序，range索引左闭右开,注意这一版和第一版的区别，因为i=j+1，所以把i替换成了j+1
# def bubble_sort(arr):
#     for i in range(1, len(arr)):
#         # 注意这里的len(arr)-1在循环多次之后，实际上是对末端已排好的序列的多余计算
#         for j in range(0, len(arr)-1):
#             if arr[j+1] > arr[j]:
#                 arr[j+1], arr[j] = arr[j+1], arr[j]
#             else:
#                 arr[j+1], arr[j] = arr[j], arr[j+1]
#     print(arr)
# bubble_sort(arr)



# __version__: 3rd bubble sort
# __author__: Fyilyer
# __date__: 2020.5.24

# 定义一个数字列表
arr = [54, 26, 10, 3, 49, 10, 1, 4]

# 打印的长度为８,实际上把8放在range里面只能取到7，因为range是左闭右开的
print(len(arr))

# 冒泡排序，range索引左闭右开,注意这一版和第一版的区别，因为i=j+1，所以把i替换成了j+1
def bubble_sort(arr):
    for i in range(1, len(arr)):
        # 这里的len(arr)-i才是正确的，已排好序的数字干嘛还要再排一遍？所以应该减去i
        for j in range(0, len(arr)-i):
            if arr[j+1] > arr[j]:
                arr[j+1], arr[j] = arr[j+1], arr[j]
            else:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    print(arr)
bubble_sort(arr)

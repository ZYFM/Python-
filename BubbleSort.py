# 冒泡排序
# 比较相邻元素，若第一个比第二个大，则交换位置，每次循环可将最大值放到列表尾部，
# 下次循环则从第0个到第n-2个进行比较交换操作

def bubble_sort(lst):
    length = len(lst)

    for index in range(length):
        for j in range(1, length-index):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]

    return lst

###################################
testlst=[2,4,1,7,5,6,9,10,8]
print(bubble_sort(testlst))

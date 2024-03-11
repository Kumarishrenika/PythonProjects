# Find Maximum and Minimum Element:
# Create a program that finds the maximum and minimum elements in an array

def cal_max_min(li):
    length = len(li)
    max_e = li[0]
    min_e = li[0]
    print(min_e)
    for i in li:
        if i > max_e:
            max_e = i
        elif i < min_e:
            min_e = i

    return f"{max_e} it is max \n {min_e} it is min"
          
result = cal_max_min([1,2,3])
print(result)




# def cal_max_min(li):
#     length = len(li)
#     greater = max(li)
#     lesser = min(li)

#     return  f"This is greater: {greater} \n this is list:{lesser}"
          
# result = cal_max_min([1,12,3])
# print(result)
def evens(list):
    even_list = []
    for i in list:
      if i % 2 == 0:
          even_list.append(i)
    return even_list
print(evens([1,2,3,4,5,6,7,8,9,10]))

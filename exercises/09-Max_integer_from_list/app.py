my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

# Your code here
def max_integer(list):
    
    highest_value=0
    for each in list:
        if each > highest_value:
            highest_value=each
    
    return highest_value

print(max_integer(my_list))
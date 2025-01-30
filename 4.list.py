# list
# 1D list
# 2D list


# 1D List
friends = ['Kawsar', 'Samim', 'Imran', 'Delowar', 'Fahad']
# print(friends)


# access data from list
# print(friends[0])

# access last value
friends_size = len(friends) # get size of list
last_friend = friends[friends_size -1]
# print(last_friend)


# slicing from list
# start, jekoyta nibo tar number
# ekhane start hobe 0 theke and second paramater e bole dibo amar koyta lagbe
# print(friends[0:3])

# iterate list by using loop
# for i in range(len(friends)):
    # print(friends[i])


# direct value access without range
# for name in friends:
#     print(name)



# 2D List
demo_var = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for row in range(len(demo_var)):
#     for col in range(len(demo_var[row])):
#         # print(demo_var[row][col])
#         print(row, col)


# without index iterate
for row in demo_var:
    for col in row:
        print(col)





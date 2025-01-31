
car = {"brand": "Toyota", "model": "HF", "price": 520000}
# print(car)


# access specific value
# print(car['model'])


# get keys
# print(car.keys())


# get values
# print(car.values())


#  get key values
# print(car.items())


# iterate
# for key in car:
#     # print(key)
#     print(car[key])


# if i get key values 
# for key, value in car.items():
#     print(key, value)



# dictionary method
# clear() removes all the elements from a dictionary.
# car.clear()
# print(car)


# copy() returns a copy of the specified dictionary.
# copied_dict = car.copy()
# print(copied_dict)


# fromKeys() 


# get() returns the value of the item with the specified key. if key not found then return default value
# x = car.get('model', 'SW')
# print(x)


# items() returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
# x = car.items()
# print(x) 

# When an item in the dictionary changes value, the view object also gets updated
# car['price'] = 10000000 
# print(x) 
# print(car) 


# keys() returns a view object. 
# x = car.keys()
# print(x)

# When an item is added in the dictionary, the view object also gets updated
# car['color'] = 'Black' 
# print(x) 
# print(car) 


# pop() removes the specified item from the dictionary and return the removed value only
# x = car.pop('price')
# print(x)
# print(car)


# popItem() Remove the last item from the dictionary and return the removed key value
# x = car.popitem()
# print(x)
# print(car)


# setdefault() returns the value of the item with the specified key. If the key does not exist, insert the key, with the specified value
# x = car.setdefault('model', 'SW')
# x = car.setdefault('year', '2025')
# print(x)
# print(car)


# update() inserts the specified items to the dictionary
# car.update({'year': 2025})
# print(car)


# values() returns a view object. The view object contains the values of the dictionary, as a list
x = car.values()
print(x)



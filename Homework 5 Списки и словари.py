food = ['apple', 'peach', 'banana' , 'orange' , 'kiwi', 'pear']
print(food)
first_element = food[0]
last_element = food[-1]
print(f'first_element: {first_element}')
print(f'last_element: {last_element}')
print(food[2:5])
food[2] = 'grape'
print(food)
#
dictionary = {'apple': 'яблоко', 'peach': 'персик', 'banana': 'банан', 'grape': 'виноград'}
print(dictionary)
print(dictionary.get('grape'))
dictionary['kiwi'] = 'киви'
print(dictionary)
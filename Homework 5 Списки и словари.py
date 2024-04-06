food = ['apple', 'peach', 'banana' , 'orange' , 'kiwi', 'pear']
print(food)
ans = food[::len(food) - 1] #Попросиь объснить
print(ans)
print(food[2:4])
food[3] = 'grape'
print(food)
#
dictionary = {'apple': 'яблоко', 'peach': 'персик', 'banana': 'банан', 'grape': 'виноград'}
print(dictionary)
print(dictionary.get('grape'))
dictionary['kiwi'] = 'киви'
print(dictionary)
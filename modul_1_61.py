# Практическое задание по теме "Словари и множества"
# Андрей Галкин

my_dict = {'Den': 2000 , 'Max': 2001, 'Yana': 2002}
print('Dict:',my_dict)
print('Existing value:',my_dict['Yana'])
print('Not existing value:',my_dict.get('Uliy'))
my_dict.update ({'Vany' : 2005,'Nina': 2006 })
a=my_dict.pop('Max')
print('Deleted value:',a)
print('Modified dictionary:',my_dict)
print(' ')

my_set= {100,3.14,100,'User', 100, 'User',3.14}
print('Set:',my_set)
my_set.add(50)
my_set.add('Men')
my_set.remove(100)
print('Modified set:',my_set)

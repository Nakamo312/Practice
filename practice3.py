#1__________________________________
school_dict = {'1a': 27 ,
              '2a': 21,
              '3a': 25,
              '4a': 18,
              '5a': 31 ,
              '6a': 23,
              '7a': 19,
              '8a': 25,
              '9a': 25,
              '10a': 33,}
def amount_students(key):
    return school_dict[key]

def change_data(_dict,n):
    new_dict = _dict
    for i in range(n):
        key = input('Введите класс:')
        value = input('Введите новые данные:')
        new_dict[key] = value
        return new_dict
#2__________________________________
def add_data(_dict,n):
    new_dict = _dict
    for i in range(n):
        key = input('Введите класс:')
        value = input('Введите новые данные:')
        new_dict[key] = value
        return new_dict

def del_data(_dict,n):
    new_dict = _dict
    for i in range(n):
        key = input('Введите класс:')
        del new_dict[key]
        return new_dict

#3__________________________________
country_cities = {  'Russia': ['Moscow','Samara',],
                        'USA': ['New-York'],
                   'GERMANY' : ['Berlin']}

countries = ['Russia','USA','GERMANY']
cities = ['Moscow','New-York','Berlin']

def search_country(_cities):
    country_cities = dict()
    for i in range(len(_cities)):
        if _cities[i] in cities:
            for j in range(len(cities)):
                if _cities[i] == cities[j]:
                    country_cities[countries[j]] = cities[j]
    return country_cities
print(search_country(['Moscow']))

#4__________________________________

string = 'pythonist'

def create_dict(string):
    _dict = dict()
    for i in string:
        if i in _dict:
            _dict[i] +=1
        else:
            _dict[i] = 1
    return _dict
print(create_dict(string))

#6__________________________________

f = lambda a,b : (a*b -a) / (a+b)
print(f(3,2))
#7__________________________________
l1 = lambda x: x+10
l2 = lambda x : x**2
l3 = lambda x : 1/x
lambda_list = [l1,l2,l3]

lambda_select = lambda index,x:lambda_list[index](x)

print(lambda_select(1,2))
#8__________________________________
l1 = lambda x: x-1
l2 = lambda x : abs(x)-2
l3 = lambda x : x

my_dict = {"positive": l1,
           "neutral": l3,
           "negative": l2 }
values = [-3,12,0,11,-1]

def calc(values):
    _values = []
    for i in values:
        if i == 0:
            _values.append(my_dict["neutral"](i))
        elif i > 0:
            _values.append(my_dict["positive"](i))
        else:
            _values.append(my_dict["negative"](i))

    return _values
print(calc(values))

#10__________________________________

my_list = [3,4,1]

new_list = list(map(lambda x: x*3 , my_list))
print(new_list)
#11__________________________________
area = lambda b,h: b*h/2
#12__________________________________
list_of_keys = [1,2,3]
list_of_values = ['a','b','c']
dictionary = dict()
for key, value in zip(list_of_keys, list_of_values):
    dictionary[key] = value
#13__________________________________
my_list = [3,7,9]
new_list = list(map(lambda x: x**2,my_list))
#14__________________________________
list_1 = [1,2,3]
list_2 = [4,5,6]

list_3 = list(map(lambda x: x[0]**x[1] ,list(zip(list_1, list_2))))
print(list_3)

#15__________________________________
list_1 = [1,2,3]
new_list = list(map(lambda x: str(x)+'s' if x != 1 else x , list_1))
print(new_list)
#16__________________________________

resList = list ( filter ( lambda item: item % 2 != 0, [-2, -1, 0, 1, 2] ) )
print(resList)

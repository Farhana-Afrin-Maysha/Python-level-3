nums = [0,1,2,3,4,5,6,7,8,9]

my_list = [n for n in nums]
print (my_list)

my_list = [n for n in nums if n%2 == 0]
print (my_list)

my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
print (my_list)

names = ['Farhana','Mahfuz','Efrana','Maruf']
heros = ['Snowwhite','Superman','Chindrella','Wolverine']

my_dict = {name: hero for name, hero in zip (names, heros)}
print (my_dict)

# set comprehensions
nums = [0,1,2,3,4,5,6,7,8,9]


my_set = {n for n in nums}
print (my_set)

# generator expresion
nums = [0,1,2,3,4,5,6,7,8,9]

my_gen = (n*n for n in nums)

for i in my_gen:
    print (i)
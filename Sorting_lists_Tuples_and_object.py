li = [0,9,2,3,8,5,6,7,3,1]

s_li = sorted(li, reverse=True)

print('Sorted Variable:\t', s_li)


print('Original Variable:\t', li)

# code to sort the original list with sorting method
li.sort()
print('Original Variable:\t', li)

# touple does not have a sorting method , so sorting function is needed
tup = (0,9,2,3,8,5,6,7,3,1)
s_tup =sorted(tup)
print('Tuple\t',s_tup)

# dictionary sorting only sorts the key
di = {'name': 'Farhana', 'age':26, 'courses':'Math'}
s_di = sorted(di)
print ('Dict\t', s_di)



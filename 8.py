tuple_a = ('Apple', 'Banana', 'Sapota', 'DalimbeHannu')
tuple_b = ('Potato', 'Brinjal', 'Eeerekai', 'Aagalkai')
my_list = list(zip(tuple_a,tuple_b))

for val in range(len(my_list)):
	print (my_list[val])

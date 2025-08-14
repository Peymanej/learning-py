my_dict = {
    'color' : 'Green',
    'size' : 'Medium',
     }
print (my_dict)
print ('Color: ', my_dict['color'])
print ('Size: ', my_dict['size'])

my_dict['type'] = 'Safe'
my_dict['score'] = 25 # type: ignore
print (my_dict)

del my_dict['type']
print (my_dict)

test_ = ''
test_ = input ('what is your favorite key?')
print (f'{my_dict.get(test_, 'Yourfavorite key is not in the dictionary!')}') 


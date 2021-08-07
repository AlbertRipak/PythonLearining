motorcycle = []
motorcycle.append('yamaha')
motorcycle.append('test')
motorcycle.append('honda')
motorcycle.append('upiter')
motorcycle.append('bmw')
print(motorcycle)

#t = motorcycle.index('test')
'''
if 'test' in motorcycle:
    #del motorcycle[t]
    motorcycle.remove('test')
else:
    print('error')
'''
motorcycle.remove('test')
for moto in motorcycle:
    print(moto)
def make_album(name_musician, name_album, countyty=''):
    make_alb = {'name_mus': name_musician, 'name_alb': name_album}
    if countyty:
        make_alb['countyty'] = countyty
    return make_alb
var1 = make_album('one', 'two')
print(var1)
var2 = make_album('three', 'four')
print(var2)
var3 = make_album('five', 'sex', 'seven')
print(var3)
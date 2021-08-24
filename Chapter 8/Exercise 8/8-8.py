def make_album(name_musician, name_album, countyty=''):
    diction = {'name_m': name_musician, 'name_a': name_album}
    if countyty:
        diction['countyty'] = countyty
    return diction

while True:
    print("\nPlease enter musician album: ")
    print("(enter 'q' at any time to quit)")
    name_m = input("Enter name musician: ")
    if name_m == 'q':
        break
    name_a = input("Enter name album: ")
    if name_a == 'q':
        break
    countyty = input("Enter countyty: ")
    if countyty == 'q':
        break

    full_info = make_album(name_m, name_a, countyty)
    print(full_info)
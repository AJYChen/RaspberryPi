def menu(wine, entree, dessert):
    return {'wine':wine, 'entree': entree, 'dessert':dessert};

print(menu('chardonnay', 'chicken', 'cake'));
print(menu(dessert='bagel', entree='beef', wine='bordeaux'));
print(menu('entree', dessert='flan', entree='fish'));

def menu1(wine, entree, dessert='pudding'):
    return {'wine':wine, 'entree': entree, 'desert':dessert};
#use default
print(menu1('chardonnay', 'chicken'))


#not use default
print(menu1('chardonnay', 'chicken', 'chicken'))
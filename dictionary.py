aa = {}
bb = {
    'Thomas':'45',
    'Andrew':'35',
    'Angela':'48',
    'Zoe':'12'
    }
print(bb)
bb['Queena'] = '4'
print(bb)
bb['Queena'] = '04'
print(bb)

qwe = [['1','2'],['3','4'],['5','6']]
print(qwe)
print(dict(qwe))
print(list(qwe))

signals = {
    'green': 'go',
    'yellow': 'go faster',
    'red': 'smile for the camera'
    };
#keys()
print(list(signals.keys()));
#values()
print(list(signals.values()));
#items
print(list(signals.items()));

original_signals = signals.copy();
print(original_signals)
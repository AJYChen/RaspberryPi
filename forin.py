rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter'];
current = 0;
while current < len(rabbits):
    print(rabbits[current]);
    current += 1;

for rabbit in rabbits:
    print(rabbit);
    
word = 'cat'
for letter in word:
    print(letter)

accusation = {'room':'ballroom',
              'weapon':'lead pipe',
              'person':'col. Mustard'
              };

for card in accusation:
    print(card);

for value in accusation.values():
    print(value);

for item in accusation.items():
    print(item);

for card, contents in accusation.items():
    print('Card', card, 'Has the contents', contents);



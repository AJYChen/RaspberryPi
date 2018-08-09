#!usr/bin/python3.5
disaster = True;
if disaster:
    print("Woe!");
else:
    print("Whee!");

furry = True;
small = True;
if furry:
    if small:
        print("It's a cat.");
    else:
        print("It's a bear!");
else:
    if small:
        print("It's a skink!");
    else:
        print("It's a human. or a hairless bear.");


color = "puce"
if color == "red":
    print("It's a tomato");
elif color == "green":
    print("It's a grenn pepper");
elif color == "bee purple":
    print("I don't know what it is");
else:
    print("I've never heard of the color", color);

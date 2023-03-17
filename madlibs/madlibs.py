# The fill-in sentence:

scenario = '''It was a [adjective], cold November day.
I woke up to the [adjective] smell of [type of bird] roasting 
in the [room in a house] downstars. I [verb(past tense)] down 
the stairs to see if I could help [verb] the dinner. My mom
said, "See if [relative's name] needs a fresh [noun]." So I
carried a tray of glasses full of [a liquid] into the
[verb ending in -ing] room. When i got there, I couldn't
believe my [part of the body (plural)]! There were [plural noun]
[verb ending in -ing] on the [noun]!
'''
print("Fill in the following scenario:\n")
print(scenario)

in1 = input("adjective: ")
in2 = input("adjective: ")
in3 = input("type of bird: ")
in4 = input("room in a house: ")
in5 = input("verb(past tense): ")
in6 = input("verb: ")
in7 = input("relative's name: ")
in8 = input("noun: ")
in9 = input("a liquid: ")
in10 = input("verb ending in -ing: ")
in11 = input("part of the body(plural): ")
in12 = input("plural noun: ")
in13 = input("verb ending in -ing: ")
in14 = input("noun: ")

filled = f'''It was a {in1}, cold November day.
I woke up to the {in2} smell of {in3} roasting 
in the {in4} downstars. I {in5} down 
the stairs to see if I could help {in6} the dinner. My mom
said, "See if {in7} needs a fresh {in8}." So I
carried a tray of glasses full of {in9} into the
{in10} room. When i got there, I couldn't
believe my {in11}! There were {in12}
{in13} on the {in14}!
'''

print(filled)

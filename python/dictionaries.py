fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit",
         }
#order_key =sorted(list(fruit.keys()))
#for f in order_key:
#    print(f+" = "+fruit[f])

#for f in sorted(fruit.keys()):
#  print(f+" = "+fruit[f])

#for val in fruit.values():
 #   print(val)
#print("*"*80)

#fruit_keys = fruit.keys()
##print(fruit_keys)
#fruit["tomato"]= "not nice with icecream"
#print(fruit_keys)

print(fruit.items())
f_tuple=tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item,description= snack
    print(item+" is "+description)
print(dict(f_tuple))
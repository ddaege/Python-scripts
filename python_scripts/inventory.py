import pprint

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']

}

inventory.update({"pocket" : ['seashells', 'strange berry', 'lint']})

inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] = inventory['gold']+50
inventory['sheaths'] = ' '
inventory['sheaths'] = ['broad sword', 'long sword', 'great sword']

pprint.pprint(inventory)


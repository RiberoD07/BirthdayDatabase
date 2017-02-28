# inventory.py
stuff = {'arrow':12,'gold coin':42,'rope':1,'torch':6,'dagger':1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory,loot):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        while(len(dragonLoot) != 0):
            if(dragonLoot[-1] in stuff):
                stuff[dragonLoot[-1]]+=1
                dragonLoot.pop()
            else:
                dragonLoot.pop()
        print(str(v) + " " + str(k))
        item_total += int(v)
    print("Total number of items: " + str(item_total))

displayInventory(stuff,dragonLoot)


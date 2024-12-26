def organizeInventory(inventory):
  if len(inventory)==0:
    return {}
  
  result = {}
  for inventory in inventory:
     category = inventory["category"]
     name = inventory["name"]
     quantity = inventory["quantity"]

     if category not in result:
        result[category] = {}
     if name not in result[category]:
        result[category][name] = quantity
     else:
        result[category][name] += quantity

  return result


inventory = [
    { "name": "doll", "quantity": 5, "category": "toys" },
    { "name": "car", "quantity": 3, "category": "toys" },
    { "name": "ball", "quantity": 2, "category": "sports" },
    { "name": "car", "quantity": 2, "category": "toys" },
    { "name": "racket", "quantity": 4, "category": "sports" }
]


print(organizeInventory(inventory)) # {'toys': {'doll': 5, 'car': 5}, 'sports': {'ball': 2, 'racket': 4}}
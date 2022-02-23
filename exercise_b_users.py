from http.client import UnimplementedFileMode


users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
print(users["Jonathan"]["twitter"])

# 2. Get Erik's hometown
print(users["Erik"]["home_town"])

# 3. Get the array of Erik's lottery numbers
print(users["Erik"]["lottery_numbers"])

# 4. Get the species of Avril's pet Monty
print(users["Avril"]["pets"][0]["species"])

# 5. Get the smallest of Erik's lottery numbers
lottery_num = users["Erik"]["lottery_numbers"]
print(min(lottery_num))

# 6. Return an array of Avril's lottery numbers that are even
lot_num = users["Avril"]["lottery_numbers"]
for num in lot_num:
  if num %2 == 0:
    print (num)

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
lottery_num.append(7)
print(lottery_num)

# 8. Change Erik's hometown to Edinburgh
users["Erik"]["hometown"] = "Edinburgh"
print(users["Erik"]["hometown"])

# 9. Add a pet dog to Erik called "Fluffy"
new_dog = {"name": "Fluffy", "species": "dog"}
new_pet = users["Erik"]["pets"]
new_pet.append(new_dog)
print(new_pet)

# 10. Add another person to the users dictionary
new_user = { "Mate": {
    "twitter": "belus90",
    "lottery_numbers": [12, 16, 3, 2, 6, 90],
    "home_town": "Gyor"
}
}
users.update(new_user)
print(users)
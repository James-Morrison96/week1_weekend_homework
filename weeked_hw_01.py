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

Twitter_handle = users["Jonathan"] ["twitter"]
print (Twitter_handle)


# 2. Get Erik's hometown
Hometown = users["Erik"] ["home_town"]
print(Hometown)
# 3. Get the list of Erik's lottery numbers
lottery_numbers = users["Erik"] ["lottery_numbers"]
print(lottery_numbers)
# 4. Get the species of Avril's pet Monty
Animal_type = users["Avril"] ["pets"], 
print(Animal_type)
# 5. Get the smallest of Erik's lottery numbers
print("Smallest element is:", lottery_numbers[2])
# 6. Return an list of Avril's lottery numbers that are even

lottery_numbers_1 = users["Avril"] ["lottery_numbers"]
print(lottery_numbers_1)
lottery_numbers_1 = [12, 14, 33, 38, 9, 25]
for num in lottery_numbers_1:
    if num % 2 == 0:
        print(num)

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers

lottery_numbers.append(7)
print(lottery_numbers)

# 8. Change Erik's hometown to Edinburgh

users["Erik"]["home_town"] = "Edinburgh"
print(users)
# 9. Add a pet dog to Erik called "fluffy"

users ["Erik"]["pets"] = {"name" : "fluffy",
                          "species" : "dog"}
print(users)
 

# 10. Add another person to the users dictionary
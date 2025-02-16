from bisect import bisect_left

def sPairs(spells, potions, success):
    potions.sort()  # Step 1: Sort potions
    res = []

    for spell in spells:  # Step 2: Iterate over spells
        minPotion = (success + spell - 1) // spell
        index = bisect_left(potions, minPotion)  # Step 3: Binary search
        res.append(len(potions) - index)  # Step 4: Count successful potions

    return res

# Test Cases
spells1 = [5,1,3]
potions1 = [1,2,3,4,5]
success1 = 7
print(sPairs(spells1, potions1, success1))  # Output: [4, 0, 3]

spells2 = [3,1,2]
potions2 = [8,5,8]
success2 = 16
print(sPairs(spells2, potions2, success2))  # Output: [2, 0, 2]
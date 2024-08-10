def max_monsters_defeated(n, e, monsters):
    
    monsters.sort(key=lambda x: x[0])
    
    defeated_count = 0
    
    for power, bonus in monsters:
        if e >= power:
            e += bonus
            defeated_count += 1
        else:
            break
    
    return defeated_count


n = int(input())
e = int(input())
monsters = []
for _ in range(n):
    power = int(input())
    monsters.append([power, 0])
for i in range(n):
    bonus = int(input())
    monsters[i][1] = bonus

result = max_monsters_defeated(n, e, monsters)
print(result)

#Magic and Sword

def spell_damage(spell: str) -> int:
    if spell == "fire":
        return 200
    elif spell == "water":
        return 300
    elif spell == "earth":
        return 400
    else:
        return 100

def spell_radius(spell: str, lvl: str) -> int:
    if (spell, lvl) == ("fire", "1"):
        return 20
    elif (spell, lvl) == ("fire", "2"):
        return 30
    elif (spell, lvl) == ("fire", "3"):
        return 50
    elif (spell, lvl) == ("water", "1"):
        return 10
    elif (spell, lvl) == ("water", "2"):
        return 25
    elif (spell, lvl) == ("water", "3"):
        return 40
    elif (spell, lvl) == ("earth", "1"):
        return 25
    elif (spell, lvl) == ("earth", "2"):
        return 55
    elif (spell, lvl) == ("earth", "3"):
        return 70
    elif (spell, lvl) == ("air", "1"):
        return 18
    elif (spell, lvl) == ("air", "2"):
        return 38
    else:
        return 60

def intersection(cx: int, cy: int, radius: int, rx: int, ry: int, width: int, height: int) -> bool:
    cDx = abs(cx - (rx + width / 2))
    cDy = abs(cy - (ry + height / 2))
    if (cDx > (width / 2 + radius)) or (cDy > (height / 2 + radius)):
        return False
    elif (cDx <= width / 2) or (cDy <= height / 2):
        return True
    else:
        return ((cDx - width/2)**2 + (cDy - height/2)**2) <= radius**2
    

T = int(input())
for _ in range(T):
    pos = list(map(int, input().split()))
    w, h, x0, y0 = pos[0], pos[1], pos[2], pos[3]
    attack = input().split()
    spell, lvl, cx, cy = attack[0], attack[1], int(attack[2]), int(attack[3])
    if intersection(cx, cy, spell_radius(spell, lvl), x0, y0, w, h):
        print(spell_damage(spell))
    else:
        print(0)
# The code is provided with the hlp of AI baba.

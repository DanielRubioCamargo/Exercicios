from random import choice

elements = [0,0,0,1,2,3]

eChoice = choice(elements)

def probability(value : int) -> float:
    global elements
    prob = elements.count(value)/len(elements)
    return int(prob*100)

prob0 = probability(2)
print(f"Probabilidade de vim o numero 0 : {prob0}%")
print(eChoice)
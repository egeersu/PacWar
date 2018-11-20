from _PyPacwar import battle
import numpy as np



def vanilla_score(gene1, gene2):
    rounds, survivors1, survivors2 = battle(gene1, gene2)
    i = 0
    if survivors2 > survivors1: i=1

    if rounds < 100: return (20,0)[i]
    elif rounds < 200: return (19,1)[i]
    elif rounds < 300: return (18,2)[i]
    elif rounds < 500: return (17,3)[i]
    else:
        if survivors1 == 0 or survivors2 == 0:
            return (17,3)[i]
        if survivors1 > survivors2: c = survivors1 / survivors2
        else: c = survivors2 / survivors1
        if c > 10: return (13,7)[i]
        elif c > 3: return (12,8)[i]
        elif c > 1.5: return (11,9)[i]
        return 10



test1 = "0 3 1 0 0 0 0 0 0 3 1 3 0 1 2 1 3 2 3 3 3 3 3 2 2 2 1 2 1 1 2 1 3 1 1 1 2 1 1 3 1 1 3 1 1 2 0 1 3 1".split()
test2 = [0, 3, 1, 0, 0, 1, 2, 3, 3, 3, 3, 0, 2, 2, 0, 0, 3, 2, 3, 3, 3, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 1, 3, 0, 1, 1, 1, 2, 3, 1, 1, 2, 0]
print(vanilla_score(test1, test2))

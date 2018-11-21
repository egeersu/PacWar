from _PyPacwar import battle
import numpy as np
import writers

def real_score(gene1, gene2):
    pass


#BEWARE: score avg is float at the end, might cause reading problems
#optimize: reading champions from txt every time
def champion_score(gene1):
    scores = []
    champions = writers.read_genes('champions.txt')
    for champ in champions:
        champ_gene, champ_score = champ
        score = vanilla_score(gene1, champ_gene)
        scores.append(score)
    return sum(scores)/float(len(scores))

#pop has to be even
def duel_scores(population):
    #match genes into groups of 2
    duels = [population[i:i+2] for i in range(0, len(population), 2)]
    scores = []
    for duel in duels:
        duel_score = vanilla_score(duel[0][0], duel[1][0])
        scores.append(duel_score)
        scores.append(20 - duel_score)
    return scores

#population will halve
def dueling_stage(population):
    


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
#print(vanilla_score(test1, test2))
#g1 = writers.random_gene()
#writers.initialize_champions(20)
#print(champion_score(test2))

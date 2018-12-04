from _PyPacwar import battle
import numpy as np
import writers

def initialize_files(num):
    writers.initialize_champions(num)

def get_pop_scores(pop):
    scores = []
    for g in pop:
        scores.append(real_score(g, pop))
    return scores


def real_score(gene1, pop):
    score = 0.5 * champion_score(gene1[0]) + 0.5 * pop_score(gene1[0], pop)
    #print("champ:", champion_score(gene1[0]), "pop:" ,pop_score(gene1[0], pop))
    return score

def pop_score(gene1, pop):
    totalVanilla = 0
    for g in pop:
        gene2 = g[0]
        s = vanilla_score(gene1, gene2)
        totalVanilla += s
    return totalVanilla/len(pop)


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
    duels = [population[i:i+2] for i in range(0, len(population), 2)]
    newpop = []
    for duel in duels:
        gene1 = duel[0][0]
        gene2 = duel[1][0]
        rounds, survivors1, survivors2 = battle(gene1, gene2)
        if survivors1 > survivors2:
            newpop.append((gene1, 0.0))
        else:
            newpop.append((gene2, 0.0))
    print(len(newpop))
    return newpop


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



def sort_genes(pop, scores):
    for i in range(len(scores)):
        scores[i] = (pop[i][0], scores[i])
    scores.sort(key=lambda tup: tup[1], reverse = True)
    genes = []
    for s in scores:
        genes.append((s[0], 0))
    return genes


def check_if_champions(pop):
    champs = writers.read_champions()
    new_champs = []
    new_scores = []



    for p in pop:
        gene1 = p[0]

        for champ in champs:
            gene2 = champ[0]
            if (gene2, 0) not in new_champs:
                rounds, survivors1, survivors2 = battle(gene1, gene2)
                gene2_score = real_score((gene2, 0), pop)
                new_champs.append((gene2, 0))
                new_scores.append(gene2_score)

            if (gene1, 0) not in new_champs:
                if survivors1 > survivors2:
                        gene1_score = real_score((gene1, 0), pop)
                        new_champs.append((gene1, 0))
                        new_scores.append(gene1_score)

    new_champs = sort_genes(new_champs, new_scores)[0:12]

    writers.clear_champions()
    writers.write_genes(new_champs, "champions.txt")
    #print(new_champs)
    print("Best Gene: ", new_champs[0][0], max(new_scores))
    return new_champs

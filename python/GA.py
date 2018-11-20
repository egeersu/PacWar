import numpy
import battles
import random
#import writers

def random_gene():
    gene = []
    for i in range(50):
        gene.append(random.choice([0,1,2,3]))
    return gene

def random_population(size):
    population = []
    for i in range(size):
        population.append((random_gene(), 0))
    return population

#GA Algorithms
def main():
    pass






def selection(population):
    #match genes into groups of 2
    duels = [population[i:i+2] for i in range(0, len(population), 2)]
    print(duels)
    for duel in duels:
        print(duel)
        score = battles.vanilla_score(duel[0][0], duel[1][0])
        print(score)

def crossover(population, p):
    pass


def mutate(population, p):
    for gene in population:
        for i in range(len(gene[0])):
            if random.random() < p:
                options = [0,1,2,3]
                options.remove(gene[0][i])
                gene[0][i] = random.choice(options)

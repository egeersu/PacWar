import numpy
import battles
import random

def random_gene():
    gene = []
    for i in range(5):
        gene.append(random.choice([0,1,2,3]))
    return gene

def random_population(size):
    population = []
    for i in range(size):
        population.append(random_gene())
    return population

#GA Algorithms
def selection():
    pass

def mutate(population, p):
    for gene in population:
        for i in range(len(gene)):
            if random.random() < p:
                options = [0,1,2,3]
                options.remove(gene[i])
                gene[i] = random.choice(options)



pop1 = random_population(2)
print(pop1)
mutate(pop1, 0.1)
print(pop1)
mutate(pop1, 0.1)
print(pop1)

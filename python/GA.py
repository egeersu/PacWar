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
    iter = 50
    pop_size = 50
    mutation = 0.05
    pop = random_population(50)
    print(battles.population_scores(pop))



def crossover(population, p):
    pass


def mutate(population, p):
    for gene in population:
        for i in range(len(gene[0])):
            if random.random() < p:
                options = [0,1,2,3]
                options.remove(gene[0][i])
                gene[0][i] = random.choice(options)


if __name__== "__main__":
  main()

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
def main2():
    #Initialize documents

    #Hyper Parameters
    iter = 50
    pop_size = 1024
    mutation = 0.05
    pop = random_population(pop_size)
    #Tournament
    for i in range(iter):
        for i in range(6):
            pop = battles.dueling_stage(pop)

        #Main GA algorithm
        scores = battles.get_pop_scores(pop)
        pop = sort_genes(pop, scores)
        crossover(pop, 0.5)

def main():
    #Hyper Parameters
    generations = 10
    GA_rounds = 50
    pop_size = 1024
    mutation_p = 0.05
    crossover_p = 0.3

    for generation in range(generations):
        pop = random_population(pop_size)
        #Tournament
        for duel_round in range(6):
            pop = battles.dueling_stage(pop)
        #GA
        for GA_round in range(GA_rounds):
            print(GA_round)
            scores = battles.get_pop_scores(pop)
            pop = sort_genes(pop, scores)
            print(pop[0], battles.real_score(pop[0], pop))
            crossover(pop, crossover_p)
            mutate(pop, mutation_p)

        battles.check_if_champions(pop)


def sort_genes(pop, scores):
    for i in range(len(scores)):
        scores[i] = (pop[i][0], scores[i])
    scores.sort(key=lambda tup: tup[1], reverse = True)
    genes = []
    for s in scores:
        genes.append((s[0], 0))
    return genes


def crossover(pop, p):
    last_index = int(len(pop) * 0.6)
    if last_index % 2 == 1: last_index -= 1
    winners = pop[0:last_index]
    for ge in pop:
        gene1 = ge[0]
        for i in range(len(gene1)):
            if random.random() < p:
                gene2 = random.choice(winners)[0]
                g1 = gene1[i]
                g2 = gene2[i]
                gene1[i] = g2
                gene2[i] = g1
    return pop


def crossover2(sorted_genes, p):
    last_index = int(len(sorted_genes) * 0.8)
    if last_index % 2 == 1: last_index -= 1
    good_genes = sorted_genes[0:last_index]
    pairs = [good_genes[i:i+2] for i in range(0, len(good_genes), 2)]
    for pair in pairs:
        gene1, gene2 = pair
        for i in range(len(gene1)):
            if random.random() < p:
                g1 = gene1[i]
                g2 = gene2[i]
                gene1[i] = g2
                gene2[i] = g1
    return sorted_genes


def mutate(population, p):
    for gene in population:
        for i in range(len(gene[0])):
            if random.random() < p:
                options = [0,1,2,3]
                options.remove(gene[0][i])
                gene[0][i] = random.choice(options)
    return population



if __name__== "__main__":
  main()

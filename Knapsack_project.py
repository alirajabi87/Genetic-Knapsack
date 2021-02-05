from MyKnapsack import Knapsack
import numpy as np
import random
from deap import tools, base, algorithms, creator
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

# Genetic Algorithm Constatnt
POPULATION = 50  # number of individuals in population
P_CROSSOVER = 0.9  # probability for crossover
P_MUTATION = 0.1  # probability for mutation

MAX_GENERATION = 50

HALL_OF_FAME_SIZE = 5

RANDOM_SEED = 42
random.seed(RANDOM_SEED)

agent = Knapsack(400)

toolbox = base.Toolbox()
toolbox.register("zeroOrone", np.random.randint, 2)  # , size=len(agent)
# toolbox.register("zeroOrone", random.randint, 0, 1)


creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox.register("IndividualCreator", tools.initRepeat, creator.Individual, toolbox.zeroOrone, len(agent))
toolbox.register("populationCreator", tools.initRepeat, list, toolbox.IndividualCreator)


def knapsackValue(individual):
    return (agent.getValue(individual),)


toolbox.register("evaluate", knapsackValue)

toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=1.0 / len(agent))


def main():
    population = toolbox.populationCreator(n=POPULATION)
    print(f"Length of Population: {len(population)}")

    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("max", np.max)
    stats.register("mean", np.mean)
    hof = tools.HallOfFame(HALL_OF_FAME_SIZE)

    population, logbook = algorithms.eaSimple(population,
                                              toolbox,
                                              cxpb=P_CROSSOVER,
                                              mutpb=P_MUTATION,
                                              ngen=MAX_GENERATION,
                                              stats=stats,
                                              halloffame=hof,
                                              verbose=True)

    maxFitnessValues, meanFitnessValues = logbook.select("max", "mean")
    # print("Hall of fame individuals = ", *hof.items, sep="\n")
    # print("Best ever individual = ", hof.items[0])

    plt.plot(maxFitnessValues, color='red')
    plt.plot(meanFitnessValues, color='green')
    plt.xlabel('Generation')
    plt.ylabel('Max / Average Fitness')
    plt.title('Max and Average fitness over Generation')
    plt.show()
    best = hof.items[0]
    agent.print(best)


if __name__ == '__main__':
    main()

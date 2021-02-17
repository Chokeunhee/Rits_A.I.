
import random
import matplotlib.pyplot as plt
import numpy as np

def objective_function(X):
    x=X[0]
    y=X[1]
    value =  20 * np.sin((np.pi/2) * (x - 2 * np.pi)) + 20 * np.sin((np.pi/2) 
    * (y - 2 * np.pi)) + ((x - 2 * np.pi) ** 2) + ((y - 2 * np.pi) ** 2)
    return value

bounds = [(0,10),(0,10)]
num_var = 2
mm = 1
num_particles = 100
iterations =30
w = 0.8
c1 = 1
c2 = 2

class individualParticle:
    def __init__(self,bounds):
        self.individualposition = []
        self.individualvolocity = []
        self.individualBestPosition = []
        self.individualBestFitness = initial_fitness
        self.individualFitness = initial_fitness
        for i in range(num_var):
            self.individualposition.append(random.uniform(bounds[i][0],bounds[i][1]))
            self.individualvolocity.append(random.uniform(-1,1))

    def evaluate(self,objective_function):
        self.individualFitness = objective_function(self.individualposition)
        if self.individualFitness > self.individualBestFitness:
            self.individualBestPosition = self.individualposition
            self.individualBestFitness = self.individualFitness
        
    def velocity_update(self, groupBestPosition):
        for i in range(num_var):
            r1 = random.random()
            r2 = random.random()
        CognitiveVelocity = c1*r1*(self.individualBestPosition[i]-self.individualposition[i])
        SocialVelocity = c2*r2*(groupBestPosition[i]-self.individualposition[i])
        self.individualvolocity[i] = w*self.individualvolocity[i]+CognitiveVelocity+SocialVelocity
        
    def position_update(self,bounds):
        for i in range(num_var):
            self.individualposition[i]=self.individualposition[i]+self.individualvolocity[i] 
            if self.individualposition[i]>bounds[i][1]:
                self.individualposition[i]=bounds[i][1]
            if self.individualposition[i]<bounds[i][0]:
                self.individualposition[i]=bounds[i][0]

initial_fitness = -float("inf")
groupBestFitness = initial_fitness 
groupBestPosition = []
swarm = []
for i in range(num_particles):
    swarm.append(individualParticle(bounds))

A = []

for i in range(iterations):
    for j in range(num_particles):
        swarm[j].evaluate(objective_function)
        
        if swarm[j].individualFitness > groupBestFitness:
            groupBestPosition = list(swarm[j].individualposition)
            groupBestFitness = float(swarm[j].individualFitness)
        
    for j in range(num_particles):
        swarm[j].velocity_update(groupBestPosition)
        swarm[j].position_update(bounds)
    
    print('iteration: {}, {}'.format(i,groupBestFitness))
    A.append(groupBestFitness)
    
print("[x,y] coordinate : ",groupBestPosition)
print("global Maximum",groupBestFitness)

X = np.linspace(0,iterations,iterations)
plt.title("particle swarm optimization")
plt.xlabel("iteration")
plt.ylabel("global maximum")
plt.plot(X,A)
plt.show()






           
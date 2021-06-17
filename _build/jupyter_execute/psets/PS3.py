#!/usr/bin/env python
# coding: utf-8

# # Agent based simulations
# 
# ## ugly solution

# In[1]:


from IPython.display import clear_output
import random
import time
N = 80
types = ['x', 'o']
K = 10
threshold = 0.6
positions = [['.' for x in range(K)] for y in range(K)]

def display(positions):
    for row in positions:
        for cell in row:
            print(cell, end=' ')
        print('')

def get_available(positions):
    return [(i,j) for i in range(K) for j in range(K) if positions[i][j] == '.']

def get_neighbors(i,j):
    return [positions[a][b]
     for a in range(max(0, i-1), min(K, i+2))
     for b in range(max(0, j-1), min(K, j+2))
    if not (a==i and b==j) and positions[a][b] != '.']


free = get_available(positions)
random.shuffle(free)
agent_positions = free[:N]
agent_types = random.choices(types, k=N)
for (i,j),c in zip(agent_positions, agent_types):
    positions[i][j] = c

display(positions)

# update agents
def p_same(c, neighbors):
    if len(neighbors) == 0:
        return 0.5
    else:
        similar = 0
        for n in neighbors:
            if n == c:
                similar += 1
        return similar/len(neighbors)

def choose(c, neighbors):
    return p_same(c, neighbors) < threshold

def calc_segregation(positions):
    agents = [(i, j, positions[i][j])
     for i in range(K)
     for j in range(K)
     if positions[i][j] != '.']
    n = len(agents)
    tot = 0
    for i,j,c in agents:
        tot += p_same(c, get_neighbors(i,j))
    return tot/n

timesteps = 30
record = [0]*timesteps
for timestep in range(timesteps):
    moved = False
    record[timestep] = calc_segregation(positions)
    for i in range(len(agent_types)):
        prior_pos = agent_positions[i]
        if choose(agent_types[i], get_neighbors(*prior_pos)):
            free = get_available(positions)
            pos = random.choice(free)
            agent_positions[i] = pos
            positions[pos[0]][pos[1]] = agent_types[i]
            positions[prior_pos[0]][prior_pos[1]] = '.'
            moved = True
            clear_output(wait=True)
            display(positions)

print(record)


# Why is it ugly?
# 
# well, the agent_position and agent_types lists are totally superfluous.  In effect they just create two places where we need to keep track of stuff.
# 
# Second, we have no need to ever look at a list of free positions, so why not just make one method that picks a free position, and use it when needed.
# 
# ## better no class solution

# In[2]:


from IPython.display import clear_output
import random
import time
N = 80
types = ['x', 'o']
K = 10
threshold = 0.6
positions = [['.' for x in range(K)] for y in range(K)]

def display(positions):
    for row in positions:
        for cell in row:
            print(cell, end=' ')
        print('')

def get_rand_available(positions):
    free_positions = [(i,j)
     for i in range(K)
     for j in range(K)
     if positions[i][j] == '.']
    return random.choice(free_positions)

def get_neighbors(i,j):
    return [positions[a][b]
     for a in range(max(0, i-1), min(K, i+2))
     for b in range(max(0, j-1), min(K, j+2))
    if not (a==i and b==j) and positions[a][b] != '.']

# initialize
for i in range(N):
    c = random.choice(types)
    i,j = get_rand_available(positions)
    positions[i][j] = c

display(positions)

# update agents
def p_same(c, neighbors):
    if len(neighbors) == 0:
        return 0.5
    else:
        return neighbors.count(c) / len(neighbors)

def choose(c, neighbors):
    return p_same(c, neighbors) < threshold

def get_agents(positions):
    return [(i, j, positions[i][j])
     for i in range(K)
     for j in range(K)
     if positions[i][j] != '.']

def calc_segregation(positions):
    agents = get_agents(positions)
    n = len(agents)
    tot = 0
    for i,j,c in agents:
        tot += p_same(c, get_neighbors(i,j))
    return tot/n

timesteps = 30
record = []
moved = True
while moved:
    moved = False
    record.append(calc_segregation(positions))
    agents = get_agents(positions)
    for i,j,c in agents:
        if choose(c, get_neighbors(i,j)):
            new_i, new_j = get_rand_available(positions)
            positions[new_i][new_j] = c
            positions[i][j] = '.'
            moved = True
            clear_output(wait=True)
            display(positions)

print(record)


# This is still a bit suboptimal.

# In[3]:


class agent():
    types = ['x', 'o']
    def __init__(self, i, j, min_same=0.5, max_same=1):
        self.pos = (i, j)
        self.type = random.choice(self.types)
        self.min_same = min_same
        self.max_same = max_same

    def choice(self, neighbors):
        if len(neighbors) == 0:
            return False
        else:
            p_same = (neighbors.count(self.type) / len(neighbors))
            return p_same < self.min_same or p_same > self.max_same

class environment():
    agents = []
    def __init__(self, K, N, min_same=0.5, max_same=1):
        self.K = K
        self.positions = set([(i,j) for i in range(K) for j in range(K)])
        self.agents = [agent(*self.get_position(), min_same, max_same)
                       for _ in range(N)]
        self.record = [self.summary()]

    def __str__(self):
        string = ''
        a_tuple = {a.pos:a.type for a in self.agents}
        for i in range(self.K):
            for j in range(self.K):
                try:
                    string += a_tuple[(i,j)] + ' '
                except KeyError:
                    string += '. '
            string += '\n'
        return string

    def get_position(self):
        used_positions = set([a.pos for a in self.agents])
        return random.choice(list(self.positions - used_positions))

    def get_neighbors(self, i, j):
        neighborhood = set([(a,b)
                             for a in range(max(0, i-1), min(self.K, i+2))
                             for b in range(max(0, j-1), min(self.K, j+2))
                             if (a,b) != (i,j)])
        return [agent.type for agent in self.agents if agent.pos in neighborhood]

    def summary(self):
        """
        Return average (across agents) proportion of neighbors of the same type.
        """
        t = 0
        n = 0
        for agent in self.agents:
            neighbors = self.get_neighbors(*agent.pos)
            if neighbors:
                t += neighbors.count(agent.type) / len(neighbors)
                n += 1
        return t/n

    def step(self):
        """
        simulate one timestep by looping through all agents and moving if they so choose.
        :return: True if any agent moved
        """
        moved = False
        for agent in self.agents:
            if agent.choice(self.get_neighbors(*agent.pos)):
                agent.pos = self.get_position()
                moved = True
        return moved

    def simulate(self, fps=True):
        if fps:
            print(self)
        while self.step():
            self.record.append(self.summary())
            if fps:
                time.sleep(1/fps)
                clear_output(wait=True)
                print(self)

e = environment(K=20,N=380, min_same=0.5, max_same=1)
e.simulate(30)
e.record


# 

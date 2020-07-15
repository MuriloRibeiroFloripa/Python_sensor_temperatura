import numpy as np
np.random.seed(1234)

def motion(N, T, h):
    """
    Simulates a Brownian motion
    :param int N : the number of discrete steps
    :param int T: the number of continuous time steps
    :param float h: the variance of the increments
    """   
    dt = 1. * T/N  # the normalizing constant
    random_increments = np.random.normal(0.0, 1.0 * h, N)*np.sqrt(dt)  # the epsilon values
    brownian_motion = np.cumsum(random_increments)  # calculate the brownian motion
    brownian_motion = np.insert(brownian_motion, 0, 0.0) # insert the initial condition
    
    return brownian_motion, random_increments

N = 29 # the number of discrete steps
T = 1 # the number of continuous time steps
h = 1 # the variance of the increments
dt = 1.0 * T/N  # total number of time steps

# generate a brownian motion
X, epsilon = motion(N, T ,h)
print(X )


# import numpy as np
# import matplotlib.pyplot as plt

# np.random.seed(5)

# fig = plt.figure()
        
# T = 1
# N = 300 # Number of points, number of subintervals = N-1
# dt = T/(N-1) # Time step
# t = np.linspace(0,T,N)


# dX = np.sqrt(dt) * np.random.randn(1,N)
# X = np.cumsum(dX, axis=1)
# print(t)


# # plt.plot(t, X[0,:])
# # plt.xlabel('Time $t$', fontsize=14)
# # plt.ylabel('Random Variable $X(t)$', fontsize=14)
# # plt.title('1D Brownian Path', fontsize=14)
# # axes = plt.gca()
# # axes.set_xlim([0,1])
# # plt.xticks(fontsize=14)
# # plt.yticks(fontsize=14)
# # plt.tight_layout()
# # plt.show()
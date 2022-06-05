# coding: utf-8
import numpy as np
import random
import matplotlib.pyplot as plt


# ----------------------PSO参数设置---------------------------------
class PSO():
    def __init__(self, pN, dim, max_iter):
        self.w = 0.6
        self.c1 = 2
        self.c2 = 2
        self.r1 = 0.6
        self.r2 = 0.3
        self.pN = pN  # 粒子数量
        self.dim = dim  # 搜索维度
        self.max_iter = max_iter  # 迭代次数
        self.X = np.zeros((self.pN, self.dim))  # 所有粒子的位置和速度
        self.Y = np.zeros((self.pN, self.dim))
        # self.Z = np.zeros((self.pN, self.dim))
        self.V = np.zeros((self.pN, self.dim))
        self.pbest = np.zeros((self.pN, self.dim))  # 个体经历的最佳位置和全局最佳位置
        self.gbest = np.zeros((1, self.dim))
        self.p_fit = np.zeros(self.pN)  # 每个个体的历史最佳适应值
        self.fit = 1e10  # 全局最佳适应值

    # ---------------------目标函数-----------------------------
    def function(self, X,Y):
        # k1=0.5
        # k2=0.5
        # MIN=99999
        # for i in range(1,465,1):

            # y6 = 1.47+0.01*i

            # if new<MIN:
            #     MIN = new
        # MIN = 1 - (1 - X) ^ Y + 1 / Y
        return 1 - (1 - X) ** Y + 1 / Y

    # ---------------------初始化种群----------------------------------
    def init_Population(self):
        for i in range(self.pN):
            for j in range(self.dim):
                self.X[i][j] = random.uniform(0.00003, 0.0001)
                self.Y[i][j] = random.uniform(0, 500)
                # self.Z[i][j] = random.uniform(0, 0.6)

                self.V[i][j] = random.uniform(0, 1)
            self.pbest[i] = self.X[i]
            tmp = self.function(self.X[i],self.Y[i])
            self.p_fit[i] = tmp
            if tmp < self.fit:
                self.fit = tmp
                self.gbest = self.X[i]

                # ----------------------更新粒子位置----------------------------------

    def iterator(self):
        fitness = []
        for t in range(self.max_iter):
            for i in range(self.pN):  # 更新gbest\pbest
                temp = self.function(self.X[i],self.Y[i])
                if temp < self.p_fit[i]:  # 更新个体最优
                    self.p_fit[i] = temp
                    self.pbest[i] = self.X[i]
                    if self.p_fit[i] < self.fit:  # 更新全局最优
                        self.gbest = self.X[i]
                        self.fit = self.p_fit[i]
            for i in range(self.pN):
                self.V[i] = self.w * self.V[i] + self.c1 * self.r1 * (self.pbest[i] - self.X[i]) + \
                            self.c2 * self.r2 * (self.gbest - self.X[i])
                self.X[i] = self.X[i] + self.V[i]

                if (1-self.X[i])**self.Y[i]*self.X[i]<1/(self.Y[i]+1)*self.Y[i]  or (1-self.X[i])**self.Y[i]*self.X[i]>1/(self.Y[i]-1)*self.Y[i]:

                    self.X[i] = self.X[i] - self.V[i]

                if self.X[i]>0.0001 :
                    self.X[i]=0.0001

                elif self.X[i]<0.00003:
                    self.X[i]=0.00003
            fitness.append(self.fit)
            print(self.X[0],self.Y[0], end=" ")
            print(self.fit)  # 输出最优值
        return fitness

        # ----------------------程序执行-----------------------


my_pso = PSO(pN=300, dim=1, max_iter=200)
my_pso.init_Population()
fitness = my_pso.iterator()
# -------------------画图--------------------
plt.figure(1)
plt.title("Figure1")
plt.xlabel("iterators", size=14)
plt.ylabel("fitness", size=14)
t = np.array([t for t in range(0, 200)])
fitness = np.array(fitness)
plt.plot(t, fitness, color='b', linewidth=3)
plt.show()

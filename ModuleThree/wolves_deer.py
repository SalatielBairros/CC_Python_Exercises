class Ecosystem:
    def __init__(self, deer_0=1.5, wolves_0=1.5, deer_growth=2/3, deer_predation=4/3, wolves_predation=1.0, wolves_decay=1.0, dt=0.0):
        self.initialDeer = deer_0
        self.initialWolves = wolves_0
        self.currentDeer = deer_0
        self.currentWolves = wolves_0
        self.maxWolves = wolves_0
        self.deerGrowth = deer_growth
        self.deerPredation = deer_predation
        self.wolvesPredation = wolves_predation
        self.wolvesDecay = wolves_decay
        self.timeIncrement = dt

    @staticmethod
    def create(deer_0=1.5, wolves_0=1.5, deer_growth=2/3, deer_predation=4/3, wolves_predation=1.0, wolves_decay=1.0, dt=0.0):
        return Ecosystem(deer_0, wolves_0, deer_growth, deer_predation, wolves_predation, wolves_decay, dt)

    def __nextStep(self):
        self.__updateAnimalsCount()
        self.__verifyMaxWolves()        

    def __getNextStepWolvesCount(self):
        newCount = self.currentWolves + (self.timeIncrement * (
            (self.wolvesPredation * self.currentWolves * self.currentDeer) - (self.wolvesDecay * self.currentWolves)))
        if(newCount < 0):
          newCount = 0;
        return newCount

    def __getNextStepDeerCount(self):
        newCount = self.currentDeer + (self.timeIncrement * (
            (self.deerGrowth * self.currentDeer) - (self.deerPredation * self.currentWolves * self.currentDeer)))
        if(newCount < 0):
          newCount = 0;
        return newCount

    def __updateAnimalsCount(self):
      wolves = self.__getNextStepWolvesCount()
      deer = self.__getNextStepDeerCount()

      self.currentDeer = deer
      self.currentWolves = wolves

    def __verifyMaxWolves(self):
        if(self.currentWolves > self.maxWolves):
            self.maxWolves = self.currentWolves

    def runEcosystem(self, stepNumber):
        for n in range(stepNumber - 1):
            self.__nextStep()
        return self


def wolves_and_dear(deer_0, wolves_0, deer_growth, deer_predation, wolves_predation, wolves_decay, dt, n):
    print('deer_0: ' + str(deer_0) +', wolves_0: ' + str(wolves_0) +', deer_growth: ' + str(deer_growth)+ ', deer_predation: ' + str(deer_predation) + ', wolves_predation: ' + str(wolves_predation) + ', wolves_decay: ' + str(wolves_decay) + ', dt: ' + str(dt) + ', n: ' + str(n))
    value = Ecosystem.create(deer_0, wolves_0, deer_growth, deer_predation, wolves_predation, wolves_decay, dt).runEcosystem(n).maxWolves
    print(value)
    return value

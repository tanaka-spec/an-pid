import numpy as np


KP = 1
KI = 1
KD = 1


class AN_PID:
    def __init__(self, dt, max_u, kp=KP, ki=KI, kd=KD, learning_factor_p=0.005, 
                learning_factor_i=0.005, learning_factor_d=0.001):
        self.errors = np.array([0, 0])
        self.max_u = max_u
        self.T = dt
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.learning_factor_p = learning_factor_p
        self.learning_factor_i = learning_factor_i
        self.learning_factor_d = learning_factor_d
        return


    def activation_func(self, value):
        return self.max_u * np.tanh(value / self.max_u)

    
    def compute(self, error):
        error1 = self.errors[-1]
        error2 = self.errors[-2]

        o1 = self.kp * error1 + \
            self.ki * self.T * np.sum(self.errors) + \
            self.kd / self.T * (error1 - error2)

        np.append(self.errors, error)

        o = self.activation_func(o1) + \
            self.kp * self.activation_func(error - error1) + \
            self.ki * self.T * np.sum(self.activation_func(self.errors)) + \
            self.kd / self.T * self.activation_func(error - 2 * error1 + error2)

        output = self.activation_func(o)
        self.set_k(output, error, error1, error2)

        return output

    
    def set_k(self, u, error, error1, error2):
        cl = 0

        q = np.exp(-(error - cl) ** 2 / 2) * (error - cl)
        self.kp -= self.learning_factor_p * error * self.max_u * q * \
                (1 - (u / self.max_u) ** 2) * self.activation_func(error - error1)
        self.ki -= self.learning_factor_i * error * self.max_u * q * \
                (1 - (u / self.max_u) ** 2) * self.activation_func(error)
        self.kd -= self.learning_factor_d * error * self.max_u * q * \
                (1 - (u / self.max_u) ** 2) * \
                self.activation_func((error - 2 * error1 + error2) / self.T)
        return
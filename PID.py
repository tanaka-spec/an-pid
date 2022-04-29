class PID:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.last_error = 0
        self.sum_error = 0
        return


    def compute(self, error: float, dt: float):
        derivative_error = (error - self.last_error) / dt
        integral_error = self.sum_error + error * dt
        self.last_error = error
        self.sum_error += error
        return self.kp * error + self.ki * integral_error + self.kd * derivative_error


    def set_gains(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        return
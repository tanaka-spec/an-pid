import turtle


GRAVITY = 9.81
MAX_THRUST = 20


class Drone:
    def __init__(self, init_x=0, init_y=0, v_i=0, mass=1):
        self.Drone = turtle.Turtle()
        self.Drone.shape('square')
        self.Drone.color('black')
        self.Drone.penup()
        self.Drone.goto(init_x, init_y)
        self.ddy = 0
        self.dy = v_i
        self.y = init_y
        self.mass = mass
        self.max_thrust = MAX_THRUST
        return


    def input(self, thrust, dt):
        self.set_ddy(thrust)
        self.set_dy()
        self.set_y()
        self.draw()
        return


    def set_ddy(self, thrust):
        if thrust < 0:
            thrust = 0
        elif thrust > self.max_thrust:
            thrust = self.max_thrust

        self.ddy = - GRAVITY + thrust / self.mass
        return

    
    def set_dy(self):
        self.dy += self.ddy
        return

    
    def set_y(self):
        self.y += self.dy
        return

    
    def draw(self):
        self.Drone.sety(self.y)
        return
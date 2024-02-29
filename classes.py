from math import sin, cos, radians

class Object:
    def __init__(self, xoffset, yoffset, speed, angle, rot_speed, points, dt):

        self.g = 9.81
        angle = radians(45)
        self.vx = speed * cos(angle)
        self.vy = speed * sin(angle)

        self.wv = radians(rot_speed)
        self.dt = dt

        # Triangle at origo
        self.object_at_origo = points
        
        # Determine object at position
        self.object = points
        for p in self.object:
            p[0] += xoffset
            p[1] += yoffset

        # determine center of mass
        cmx = 1/3 * (self.object[0][0] + self.object[1][0] + self.object[2][0])
        cmy = 1/3 * (self.object[0][1] + self.object[1][1] + self.object[2][1])
        self.cm = [[cmx, cmy]]


    def get_new_cm(self):
        cmx = self.cm[-1][0] + self.vx * self.dt
        vyl = self.vy - self.g * self.dt
        cmy = self.cm[-1][1] + vyl * self.dt
        self.cm.append([cmx, cmy])
        self.vy = vyl
        return self.cm[-1]
    
    def get_new_rotation(self):
        dr = self.wv * self.dt
        i = 0
        for p in self.object_at_origo:
            self.object_at_origo[i][0] = p[0] * cos(dr) - p[1] * sin(dr)
            self.object_at_origo[i][1] = p[1] * sin(dr) + p[1] * cos(dr)
            i += 1
        
        return self.object_at_origo
        

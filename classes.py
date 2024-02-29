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
        self.object = [[x + xoffset, y + yoffset] for x, y in points]

        # determine center of mass
        sumx = 0
        for x in self.object:
            sumx += x[0]
        cmx = 1/len(points) * (sumx)

        sumy = 0
        for x in self.object:
            sumy += x[1]

        cmy = 1/len(points) * (sumy)
        
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

        rotated_point = [point[:] for point in self.object_at_origo]
        i = 0
        for p in rotated_point:
            x, y = p
            rotated_point[i][0] = x * cos(dr) - y * sin(dr)
            rotated_point[i][1] = x * sin(dr) + y * cos(dr)
            i += 1
        
        self.object_at_origo = rotated_point
        return rotated_point
        

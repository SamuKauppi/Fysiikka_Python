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

        self.j = 0.03


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
    
    def update_position(self):
        # Move center of mass
        self.get_new_cm()
        # get rotation vector
        new_object = self.get_new_rotation()
        # Sum center off mass and rotation
        new_object = [[x + self.cm[-1][0], y + self.cm[-1][1]] for x, y in new_object]
        # Update object
        self.object = new_object

    def hits_ground(self):
        for point in self.object:
            # get rp
            rp = self.get_rp(self.cm[-1][0], self.cm[-1][1], point[0], point[1])
            # get cross product between rp and angular speed
            rxw = self.get_wxrp(rp)
            # get point speed on y-axis
            vpy = self.vy + rxw[1]

            # check for collision on ground
            if(point[1] < 0 and vpy < 0):

                rxn = abs(self.get_rxn(rp, [0, 1]))

                # get impulse
                i = -2 * (self.vy / (1 + ((rxn)**2) / self.j))
                
                self.vy += i/1


    def get_rp(self, cmx, cmy, px, py):
        rpx = px - cmx
        rpy = py - cmy
        return [rpx, rpy]
    
    def get_wxrp(self, rp):
        rpxwx = -self.wv * rp[1]
        rpxwy = self.wv * rp[0]
        return[rpxwx, rpxwy]
    
    def get_rxn(self, rp, n):
        rxn = rp[0] * n[1] - rp[1] * n[0]
        return rxn
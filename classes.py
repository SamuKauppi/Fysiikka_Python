from math import sin, cos, radians

class Object:
    def __init__(self, xoffset, yoffset, speed, angle, rot_speed, points, dt, e, j):

        self.is_coll = False
        self.j = j
        self.e = e
        self.dt = dt
        self.m = 10

        self.g = 9.81
        angle = radians(45)
        self.vx = speed * cos(angle)
        self.vy = speed * sin(angle)

        self.wv = radians(rot_speed)

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

        if self.is_coll == False:
            vyl = self.vy - self.g * self.dt
        else:
            vyl = -self.e * self.vy

        cmy = self.cm[-1][1] + vyl * self.dt
        self.cm.append([cmx, cmy])
        self.vy = vyl
        self.is_coll = False
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
        # TODO: make t and n vector instead only ground
        n = [0, 1, 0]
        for point in self.object:

            # get rp (vector from center of mass to point)
            rp = self.get_rp(self.cm[-1][0], self.cm[-1][1], point[0], point[1])

            # get cross product between rp and angular speed
            wv = [0, 0, self.wv]        # make angular speed into vector
            wxrp = self.cross(wv, rp)

            # get point speed on y-axis
            vpy = self.vy + wxrp[1]

            # check for collision on ground
            if(point[1] < 0 and vpy < 0):

                # get speed in x-axis
                vpx = self.vx + wxrp[0]

                # get dot product between vp and n
                vpn = (vpx * n[0]) + (vpy * n[1])

                # get cross product between rp and n (only k)
                rpxn = self.cross(rp, n)[2]

                # get impulse
                rpxn2 = abs(rpxn)**2
                i = -(1 + self.e) * (vpn / ((1/self.m) + rpxn2 / self.j))

                self.vy = self.vy + (i / self.m) * n[1]
                self.vx = self.vx + (i / self.m) * n[0]
                self.wv = self.wv + (i / self.j) * rpxn
                self.is_coll = True


    def get_rp(self, cmx, cmy, px, py):
        rpx = px - cmx
        rpy = py - cmy
        return [rpx, rpy, 0]
    
    def cross(self, a, b):
        c = [a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]]

        return c
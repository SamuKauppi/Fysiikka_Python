from math import sin, cos, radians, sqrt

class Object:
    def __init__(self, xoffset, yoffset, speed, angle, rot_speed, points, dt, e, j, m):

        self.is_coll = False
        self.j = j
        self.e = e
        self.dt = dt
        self.m = m

        self.g = 9.81
        angle = radians(angle)
        self.vx = speed * cos(angle)
        self.vy = speed * sin(angle)

        self.wv = radians(rot_speed)
        self.kulma = 0

        # Triangle at origo
        self.object_at_origo = points

        # Determine object at position
        self.object = [[x + xoffset, y + yoffset] for x, y in points]

        # determine center of mass        
        self.cm = [xoffset, yoffset]


    def update_position(self):
        # Move center of mass
        self.cm = self.get_new_cm()
    
        self.kulma = self.kulma + self.wv * self.dt

        i = 0
        for p in self.object:
            p[0] = self.object_at_origo[i][0] * cos(self.kulma) - self.object_at_origo[i][1] * sin(self.kulma) + self.cm[0]
            p[1] = self.object_at_origo[i][0] * sin(self.kulma) + self.object_at_origo[i][1] * cos(self.kulma) + self.cm[1]
            i+= 1


    def get_new_cm(self):

        if self.is_coll == False:
            self.vy = self.vy - self.g * self.dt

        cmx = self.cm[0] + self.vx * self.dt
        cmy = self.cm[1] + self.vy * self.dt
        self.is_coll = False

        return [cmx, cmy]

    def hits_ground(self, g_point1, g_point2):
        # TODO: make t and n vector instead only ground
        a = (g_point2[1] - g_point1[1]) / (g_point2[0] - g_point1[0])
        b = g_point1[1] - a * g_point1[0]

        l = sqrt((g_point1[0] - g_point2[0])**2 + (g_point1[1] - g_point2[1])**2)
        t = [(g_point1[0] - g_point2[0]) / l, (g_point1[1] - g_point2[1]) / l]
        n = [-t[1], t[0], 0]

        for point in self.object:

            # get rp (vector from center of mass to point)
            rp = self.get_rp(self.cm[0], self.cm[1], point[0], point[1])

            # get cross product between rp and angular speed
            wv = [0, 0, self.wv]        # make angular speed into vector
            wxrp = self.cross(wv, rp)

            # get point speed on y-axis
            vpy = self.vy + wxrp[1]

            #axb = a * point[0] + b
            
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

                # update velocity and angular velocity
                self.vy = self.vy + (i / self.m) * n[1]
                self.vx = self.vx + (i / self.m) * n[0]
                self.wv = self.wv + (i / self.j) * rpxn
                self.is_coll = True
                break


    def get_rp(self, cmx, cmy, px, py):
        rpx = px - cmx
        rpy = py - cmy
        return [rpx, rpy, 0]
    
    def cross(self, a, b):
        c = [a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]]

        return c

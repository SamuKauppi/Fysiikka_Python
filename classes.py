from math import sin, cos, radians, sqrt

def pythagora(a, b):
    return sqrt((a)**2 + (b)**2)

def cross(a, b):
        c = [a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]]

        return c

def get_n(g_point1, g_point2):
    # get the length from p1 to p2 (ground points)
    l = pythagora(g_point1[0] - g_point2[0], g_point1[1] - g_point2[1])
     # get t
    t = [(g_point1[0] - g_point2[0]) / l, (g_point1[1] - g_point2[1]) / l]
    # get n from t
    return [-t[1], t[0], 0]

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

        # get n vector
        n = get_n(g_point1, g_point2)

        # get a
        a = (g_point2[1] - g_point1[1]) / (g_point2[0] - g_point1[0])

        # get b
        b = g_point1[1] - a * g_point1[0]

        for point in self.object:

            # get rp (vector from center of mass to point)
            rp = self.get_rp(self.cm[0], self.cm[1], point[0], point[1])

            # get cross product between rp and angular speed
            wv = [0, 0, self.wv]        # make angular speed into vector
            wxrp = cross(wv, rp)        
            
            # get speeds of the point
            vpy = self.vy + wxrp[1]
            vpx = self.vx + wxrp[0]

            # get dot product between vp and n
            vpn = (vpx * n[0]) + (vpy * n[1])

            # get the height of the ground at point x-pos with the function ax+b
            axb = a * point[0] + b
            
            # check for collision on ground
            if(point[1] < axb and vpn < 0):

                # get cross product between rp and n (only k)
                rpxn = cross(rp, n)[2]

                # get impulse
                rpxn2 = abs(rpxn)**2
                i = -(1 + self.e) * (vpn / ((1/self.m) + rpxn2 / self.j))

                # update velocity and angular velocity
                self.vy = self.vy + (i / self.m) * n[1]
                self.vx = self.vx + (i / self.m) * n[0]
                self.wv = self.wv + (i / self.j) * rpxn
                # set collision flag true
                self.is_coll = True
                break


    def get_rp(self, cmx, cmy, px, py):
        rpx = px - cmx
        rpy = py - cmy
        return [rpx, rpy, 0]
    
    def set_new_speeds(self, data):
        self.vx = data[0]
        self.vy = data[1]
        self.wv = data[2]
    

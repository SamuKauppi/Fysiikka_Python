from classes import cross, get_n, pythagora

def handle_coll(side_obj, coll_obj, coll_point):

    # find the closest side to the collsion point
    closest_side = 0
    shortest_dist = 0
    for i in range(len(side_obj.object)):

        i_next = i + 1
        if(i_next >= len(side_obj.object)):
            i_next = 0

        r1 = pythagora(coll_point[0] - side_obj.object[i][0], coll_point[1] - side_obj.object[i][1])
        r2 = pythagora(coll_point[0] - side_obj.object[i_next][0], coll_point[1] - side_obj.object[i_next][1])

        r = r1 + r2

        if shortest_dist == 0 or r < shortest_dist:
            closest_side = [side_obj.object[i], side_obj.object[i_next]]
            shortest_dist = r

    # collision vector
    n = get_n(closest_side[0], closest_side[1])

    # get vector from cmA to point
    rapx = coll_point[0] - coll_obj.cm[0]
    rapy = coll_point[1] - coll_obj.cm[1]
    rap = [rapx, rapy, 0]

    # get vector from cmB to point
    rbpx = coll_point[0] - side_obj.cm[0]
    rbpy = coll_point[1] - side_obj.cm[1]
    rbp = [rbpx, rbpy, 0]

    # Cross products 
    rapxn = cross(rap, n)[2]
    rbpxn = cross(rbp, n)[2]

    # Get get speeds
    wva = [0, 0, coll_obj.wv]
    vapx = coll_obj.vx + cross(wva, rap)[0]
    vapy = coll_obj.vy + cross(wva, rap)[1]

    wvb = [0, 0, side_obj.wv]
    vbpx = side_obj.vx + cross(wvb, rbp)[0]
    vbpy = side_obj.vy + cross(wvb, rbp)[1]

    # get relative speed between each other
    vab = [vapx - vbpx, vapy - vbpy]
    vabn = vab[0] * n[0] + vab[1] * n[1]

    e = (coll_obj.e + side_obj.e) / 2

    a = abs(rapxn)**2 /  coll_obj.j
    b = abs(rbpxn)**2 /  side_obj.j

    i = -(1 + e) * (vabn / ((1/coll_obj.m) + (1/side_obj.m) + a + b))

    vxa = coll_obj.vx + (i / coll_obj.m) * n[0]
    vya = coll_obj.vy + (i / coll_obj.m) * n[1]

    vxb = side_obj.vx - (i / side_obj.m) * n[0]
    vyb = side_obj.vy - (i / side_obj.m) * n[1]

    wa = coll_obj.wv + (i / coll_obj.j) * rapxn
    wb = side_obj.wv - (i / side_obj.j) * rbpxn

    return [[vxa, vya, wa], [vxb, vyb, wb]]


# checks collision between a point and obj
def is_object_collision(obj, point):
 
    has_coll = True
    for i in range(len(obj)):

        i_next = i + 1
        if(i_next >= len(obj)):
            i_next = 0

        # get vector from this point to next point
        rox = obj[i_next][0] - obj[i][0]
        roy = obj[i_next][1] - obj[i][1]
        ro = [rox, roy, 0]

        # get vector from this point to point
        rpx = point[0] - obj[i][0]
        rpy = point[1] - obj[i][1]
        rp = [rpx, rpy, 0]

        rxp = cross(ro, rp)[2]

        if rxp < 0:
            return False
    
    return has_coll
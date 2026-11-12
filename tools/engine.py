import math
from datetime import datetime, timezone
R = math.pi / 180
JD0, SYN = 2451550.1, 29.530588

def jd(t):
    return t.timestamp() / 86400 + 2440587.5

def geo(t):
    j = jd(t); d = j - 2451545
    sl = 180 - 360 * (((j - JD0) / SYN) % 1)
    ls = (280.46 + 0.9856474 * d) * R
    om = (125.04 - 0.0529539 * d) * R
    M = (134.96 + 13.06499295 * d) * R
    F = (93.27 + 13.22935 * d) * R
    return sl, 1.54 * math.sin(ls - om), -6.3 * math.sin(M), 6.7 * math.sin(F)

def elev(lat, lon, bd, bl):
    x = math.sin(lat*R)*math.sin(bd*R) + math.cos(lat*R)*math.cos(bd*R)*math.cos((lon-bl)*R)
    return math.degrees(math.asin(max(-1, min(1, x))))

def sun_earth(lat, lon, t):
    sl, sd, el, ed = geo(t)
    return elev(lat, lon, sd, sl), elev(lat, lon, ed, el)
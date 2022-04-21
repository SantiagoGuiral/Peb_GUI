import math

def q(x):
    q=0.5*math.erfc(x/math.sqrt(2))
    return q

def voltage (at,vt):
    vr=vt*10**(-at/20)
    return vr

def sigma (N):
    sigma=math.sqrt(N)
    return sigma

def peb(bits,ProbErrorTramos):
    P=1
    unos=bits.count("1")
    if(unos%2!=0):
        for pos in range(len(bits)):
            if bits[pos]=="1":
                P*=ProbErrorTramos[pos]
            else:
                P*=(1-ProbErrorTramos[pos])
        return P
    else:
        return 0

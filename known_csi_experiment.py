#experiment A

from math import sqrt
import random

payload_a = [0.8,0.5]

eta_min = [0.2,0.2]
R_samples = 4
comp_times = [0.08,0.1,0.07]
def acc(a,b):
    return 0.55 + 0.25*sqrt(a) + 0.2*sqrt(b)
acc_uno = 0
records = []
feasability = []
print(acc_uno)
rand = random.Random(7)
if (max(comp_times) < 1/R_samples):
    
    for i in range(100):
        capacity_c = [rand.uniform(1.2,4.8), rand.uniform(0.8,3)]
        p = payload_a[0]*eta_min[0]/capacity_c[0]
        q = payload_a[1]*eta_min[1]/capacity_c[1]
        if (max(p,q) < 1/R_samples):
            print("Feasableee")
            feasability.append(True)
        else:
            feasability.append(False)

        #theorem 3.1
        eta = [min(1,capacity_c[0]/R_samples/payload_a[0]), min(1,capacity_c[1]/R_samples/payload_a[1])]
        acc_uno = acc(eta[0],eta[1])
        r = payload_a[0]*eta[0]/capacity_c[0]
        s = payload_a[1]*eta[1]/capacity_c[1]

        comm_d = max(max(comp_times),max(r,s))
        throughput = 1/comm_d

        #uniform policy
        uni_eta = min(1,capacity_c[0]/R_samples/payload_a[0], capacity_c[1]/R_samples/payload_a[1])
        t = payload_a[0]*uni_eta/capacity_c[0]
        u = payload_a[1]*uni_eta/capacity_c[1]
        d_uni = max(max(comp_times),max(t,u))
        throughput_uni = 1/d_uni
        acc_uni = acc(uni_eta, uni_eta)
        #record the results
        records.append({"slot":i, "capacity_1":capacity_c[0], "capacity_2":capacity_c[1], "eta_min":eta_min[0], "eta_min2":eta_min[1], "acc":acc_uno, "throughput":throughput, "uni_eta":uni_eta, "throughput_uni":throughput_uni, "d_uni": d_uni, "acc_uni":acc_uni})
print(records)
print(feasability)

#experiment B
a_b = [1,0.8]
R_b = [2,3]
eta_min_b = 0.2
w_b = [0.6,0.4]
records_b = []
for i in range(100):
    capacity_c_b = rand.uniform(1.3,3.5)
    eta_b = [1,2]
    Acc_b = [0.55+ 0.45*sqrt(eta_b[0]), 0.6+ 0.4*sqrt(eta_b[1])]
    Sv_min = a_b[0]*eta_min_b*R_b[0]/capacity_c_b
    SL_min = a_b[1]*eta_min_b*R_b[1]/capacity_c_b
    if ((Sv_min + SL_min) <=1):
        print("ayyy feasableee")
    else:
        print("nahh")
    lower = Sv_min
    upper = 1-SL_min
    if upper < lower:
        upper = lower
    steps = int(round(upper-lower)/0.001)
    for k in range(steps+1):
        Sv = lower + k*0.001
        if Sv > upper:
            Sv = upper
        
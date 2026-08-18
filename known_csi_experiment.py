#experiment A

from cmath import sqrt
import random

payload_a = [0.8,0.5]

eta_min = [0.2,0.2]
R_samples = 4
comp_times = [0.08,0.1,0.07]
def acc(a):
    return 0.55 + 0.25*sqrt(a[0]) + 0.2*sqrt(a[1])
acc_uno = 0

print(acc_uno)
rand = random.Random(7)
if (max(comp_times) < 1/R_samples):
    
    for i in range(100):
        capacity_c = [rand.uniform(1.2,4.8), rand.uniform(0.8,3)]
        p = payload_a[0]*eta_min[0]/capacity_c[0]
        q = payload_a[1]*eta_min[1]/capacity_c[1]
        if (max(p,q) < 1/R_samples):
            print("Feasableee")

        #theorem 3.1
        eta = [min(1,capacity_c[0]/R_samples/payload_a[0]), min(1,capacity_c[1]/R_samples/payload_a[1])]
        acc_uno = acc(eta)
        r = payload_a[0]*eta[0]/capacity_c[0]
        s = payload_a[1]*eta[1]/capacity_c[1]

        comm_d = max(max(payload_a),max(r,s))
        throughput = 1/comm_d

        #uniform policy
        uni_eta = min(1,capacity_c[0]/R_samples/payload_a[0], capacity_c[1]/R_samples/payload_a[1])
        t = payload_a[0]*uni_eta/capacity_c[0]
        u = payload_a[1]*uni_eta/capacity_c[1]
        d_uni = max(max(payload_a),max(t,u))
        throughput_uni = 1/d_uni

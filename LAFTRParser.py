from astropy.io  import ascii
import numpy as np
import matplotlib.pyplot as plt ; plt.rcdefaults()

objects = ('Channel 1', 'Channel 2', 'Channel 3', 'Channel 4', 'Channel 5', 'Channel 6')
y_pos = np.arange(len(objects))
c1,c2,c3,c4,c5,c6 = 0,0,0,0,0,0
data = ascii.read('CS137DataTest/LAFTR0.TXT')
convdata = np.arange(0,len(data[1][:]),1)

counter = 0
data[4][:] = str(data[4][:])
PPS = 0
FPGACLOCK = 0
for x in data:
    temp = bin(int(x[0],16))[2:].zfill(8)
    b = bin(int(x[1],16))[2:].zfill(8)
    c = bin(int(x[2],16))[2:].zfill(8)
    d = bin(int(x[3],16))[2:].zfill(8)
    e = bin(x[4])[2:].zfill(8)
    t = str(x[5])
    f = bin(x[5])[2:].zfill(8)
    if int(temp[2:-2],2) < 3 and int(temp[2:-2],2) >=1 :
        c1 = c1+1
    if int(temp[2:-2],2) < 7 and int(temp[2:-2],2) >=3 :
        c2 = c2 +1
    if int(temp[2:-2],2) < 15 and int(temp[2:-2],2) >=7 :
        c3 = c3 + 1
    if int(temp[2:-2],2) < 31 and int(temp[2:-2],2) >=15 :
        c4 = c4 +1
    if int(temp[2:-2],2) == 42:
        counter = counter+1
    if int(temp[2:-2],2) < 63 and int(temp[2:-2],2) >=31 :
        c5 = c5 +1
    if int(temp[2:-2],2) < 10000 and int(temp[2:-2],2) >=63 :
        c6 = c6 + 1
    FPGACLOCK = temp[-2:]+b[:]+c[:]+d[:]+e[0]
    PPS = e[1:]+f[:]
performance = [c1,c2,c3,c4,c5,c6]
#Do do the whole data I need to parse it myself.


plt.bar(y_pos,performance,align ='center',alpha = 0.5)
plt.xticks(y_pos,objects)
plt.ylabel('Counts')
plt.title("Energy Spectrum from CS-137 Test for FPGA")
plt.show()

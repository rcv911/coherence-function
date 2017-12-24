from numpy import *
from matplotlib.pyplot import *
from numpy.fft import rfft

dt=0.004
N=1250

x=loadtxt('one_subject_network_source_1.txt')
y=loadtxt('one_subject_network_source_2.txt')
x=x.reshape((84,N))
y=y.reshape((84,N))
Fx=zeros((84,(N/2+1)))
Fy=zeros((84,(N/2+1)))
x1=zeros((84,(N/2+1)))
y1=zeros((84,(N/2+1)))
Cxy=zeros(N/2+1)
border=zeros(N/2+1) # confidence interval

# spectrum of 2 signals
for el in range(84):
    Fx=fft.rfft(x[el,:])
    x1[el]=abs(Fx)/(len(Fx)/2)
    
    Fy=fft.rfft(y[el,:])
    y1[el]=abs(Fy)/(len(Fy)/2)
    # coherence function
    Cxy+=(Fx.conj()*Fy)/(((abs(Fx)**2)*(abs(Fy)**2))**0.5)

# freqs          
freq=linspace(0, 1/(2*dt), (len(x[0,:])/2) + 1)

for el in range(len(border)):
    border[el]=1/(84**0.5)

cut = 500
# draw
figure('coherence function EEG')
xlabel('f, Hz')
ylabel('Cxy')
plot(freq[:cut], abs(Cxy[:cut])/84, 'k')
plot(freq[:cut], border[:cut], 'r', lw = 2)
grid()
# savefig('coherence_function_EEG.png')
show()
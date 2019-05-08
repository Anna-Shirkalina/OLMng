import numpy
import neuron
from neuron import h, gui
import matplotlib.pyplot as plt
import efel
import glob
import IPython, os
from currents_visualization import plotCurrentscape

### Instantiate Model ###
h.load_file("init_model.hoc")

cell = h.cell
if cell == 1:
    cellname = 'Gormadoc'
    DNQX_Hold = 0.004
    h.ic_hold.amp = DNQX_Hold
    TTX_Hold = -0.0290514
elif cell == 2:
    cellname = 'Isembard'
    DNQX_Hold = -0.005
    h.ic_hold.amp = DNQX_Hold
    TTX_Hold = -0.0508

modelnum = h.modelnum
if modelnum == 1:
    modelname = '1st'
elif modelnum == 2:
    modelname = '2nd'
elif modelnum == 3:
    modelname = '3rd'
elif modelnum == 4:
    modelname = '4th'
elif modelnum == 5:
    modelname = '5th'
elif modelnum == 6:
    modelname = 'FT'

### Load Experimental ###
Exp_Dir = cellname + '_exp_data'

files_listB = glob.glob1(Exp_Dir, "*_0pA_dnqx.dat")
files_list01 = glob.glob1(Exp_Dir, "*-90pA_dnqx.dat")
files_list0 = glob.glob1(Exp_Dir, "*-120pA_dnqx.dat")
files_list1 = glob.glob1(Exp_Dir, "*+30pA_dnqx.dat")
files_list2 = glob.glob1(Exp_Dir, "*+60pA_dnqx.dat")
files_list3 = glob.glob1(Exp_Dir, "*+90pA_dnqx.dat")

dataB = numpy.loadtxt(os.path.join(Exp_Dir,files_listB[0]))
data01 = numpy.loadtxt(os.path.join(Exp_Dir,files_list01[0]))
data0 = numpy.loadtxt(os.path.join(Exp_Dir,files_list0[0]))
data1 = numpy.loadtxt(os.path.join(Exp_Dir,files_list1[0]))
data2 = numpy.loadtxt(os.path.join(Exp_Dir,files_list2[0]))
data3 = numpy.loadtxt(os.path.join(Exp_Dir,files_list3[0]))
dataB = dataB[1:80000,:]
data01 = data01[1:80000,:]
data0 = data0[1:80000,:]
data1 = data1[1:80000,:]
data2 = data2[1:80000,:]
data3 = data3[1:80000,:]

### Setup Recordings and Distance Vector ###
t_vec = h.Vector()  
t_vec.record(h._ref_t)

v_vec0 = h.Vector()
v_vec0.record(h.soma[0](0.5)._ref_v)

v_vec = h.Vector()
v_vec.record(h.dend[0](0)._ref_v)

Ih = h.Vector()
Ih.record(h.dend[0](0)._ref_ih_Ih)

INa = h.Vector()
INa.record(h.dend[0](0)._ref_ina_Nadend)

IKa = h.Vector()
IKa.record(h.dend[0](0)._ref_ik_Ika)

IKdrf = h.Vector()
IKdrf.record(h.dend[0](0)._ref_ik_Ikdrf)

IKdrs = h.Vector()
IKdrs.record(h.dend[0](0)._ref_ik_Ikdrs)

Im = h.Vector()
Im.record(h.dend[0](0)._ref_ik_IM)

IKCa = h.Vector()
IKCa.record(h.dend[0](0)._ref_ik_kca)

ICaL = h.Vector()
ICaL.record(h.dend[0](0)._ref_ica_cal)

ICaT = h.Vector()
ICaT.record(h.dend[0](0)._ref_ica_cat)

Il = h.Vector()
Il.record(h.dend[0](0)._ref_i_passsd)

labels = ('gKA','gKdrf','gKdrs','gKCa','gM','gL','gNa','gCaT','gCaL','gH')

h.ic_step.amp = -0.12 + (TTX_Hold-DNQX_Hold)
h.run()
vvec0 = numpy.array(v_vec)
vvec00 = numpy.array(v_vec0)
tvec0 = numpy.array(t_vec)

pIKa = numpy.array(IKa)
pIKdrf = numpy.array(IKdrf)
pIKdrs = numpy.array(IKdrs)
pIKCa = numpy.array(IKCa)
pIm = numpy.array(Im)
pIl = numpy.array(Il)
pINa = numpy.array(INa)
pICaT = numpy.array(ICaT)
pICaL = numpy.array(ICaL)
pIh = numpy.array(Ih)

r0 = [pIKa,pIKdrf,pIKdrs,pIKCa,pIm,pIl,pINa,pICaT,pICaL,pIh]

fig0 = plotCurrentscape(vvec0, r0)
fig0.savefig('PLOTfiles/' + cellname + '_Currentscape0_' + modelname + '.pdf',dpi=500)
fig0.savefig('PLOTfiles/' + cellname + '_Currentscape0_' + modelname + '.png',dpi=500)
fig0.clf()
plt.close(fig0)

h.ic_step.amp = -0.09 + (TTX_Hold-DNQX_Hold)
h.run()
vvec01 = numpy.array(v_vec)
vvec010 = numpy.array(v_vec0)
tvec01 = numpy.array(t_vec)

pIKa = numpy.array(IKa)
pIKdrf = numpy.array(IKdrf)
pIKdrs = numpy.array(IKdrs)
pIKCa = numpy.array(IKCa)
pIm = numpy.array(Im)
pIl = numpy.array(Il)
pINa = numpy.array(INa)
pICaT = numpy.array(ICaT)
pICaL = numpy.array(ICaL)
pIh = numpy.array(Ih)

r01 = [pIKa,pIKdrf,pIKdrs,pIKCa,pIm,pIl,pINa,pICaT,pICaL,pIh]

fig01 = plotCurrentscape(vvec01, r01)
fig01.savefig('PLOTfiles/' + cellname + '_Currentscape01_' + modelname + '.pdf',dpi=500)
fig01.savefig('PLOTfiles/' + cellname + '_Currentscape01_' + modelname + '.png',dpi=500)
fig01.clf()
plt.close(fig01)

h.ic_step.amp = 0.03
h.run()
vvec1 = numpy.array(v_vec)
vvec10 = numpy.array(v_vec0)
tvec1 = numpy.array(t_vec)

pIKa = numpy.array(IKa)
pIKdrf = numpy.array(IKdrf)
pIKdrs = numpy.array(IKdrs)
pIKCa = numpy.array(IKCa)
pIm = numpy.array(Im)
pIl = numpy.array(Il)
pINa = numpy.array(INa)
pICaT = numpy.array(ICaT)
pICaL = numpy.array(ICaL)
pIh = numpy.array(Ih)

r1 = [pIKa,pIKdrf,pIKdrs,pIKCa,pIm,pIl,pINa,pICaT,pICaL,pIh]

fig1 = plotCurrentscape(vvec1, r1)
fig1.savefig('PLOTfiles/' + cellname + '_Currentscape1_' + modelname + '.pdf',dpi=500)
fig1.savefig('PLOTfiles/' + cellname + '_Currentscape1_' + modelname + '.png',dpi=500)
fig1.clf()
plt.close(fig1)

h.ic_step.amp = 0.06
h.run()
vvec2 = numpy.array(v_vec)
vvec20 = numpy.array(v_vec0)
tvec2 = numpy.array(t_vec)

pIKa = numpy.array(IKa)
pIKdrf = numpy.array(IKdrf)
pIKdrs = numpy.array(IKdrs)
pIKCa = numpy.array(IKCa)
pIm = numpy.array(Im)
pIl = numpy.array(Il)
pINa = numpy.array(INa)
pICaT = numpy.array(ICaT)
pICaL = numpy.array(ICaL)
pIh = numpy.array(Ih)

r2 = [pIKa,pIKdrf,pIKdrs,pIKCa,pIm,pIl,pINa,pICaT,pICaL,pIh]

fig2 = plotCurrentscape(vvec2, r2)
fig2.savefig('PLOTfiles/' + cellname + '_Currentscape2_' + modelname + '.pdf',dpi=500)
fig2.savefig('PLOTfiles/' + cellname + '_Currentscape2_' + modelname + '.png',dpi=500)
fig2.clf()
plt.close(fig2)

h.ic_step.amp = 0.09
h.run()
vvec3 = numpy.array(v_vec)
vvec30 = numpy.array(v_vec0)
tvec3 = numpy.array(t_vec)

pIKa = numpy.array(IKa)
pIKdrf = numpy.array(IKdrf)
pIKdrs = numpy.array(IKdrs)
pIKCa = numpy.array(IKCa)
pIm = numpy.array(Im)
pIl = numpy.array(Il)
pINa = numpy.array(INa)
pICaT = numpy.array(ICaT)
pICaL = numpy.array(ICaL)
pIh = numpy.array(Ih)

r3 = [pIKa,pIKdrf,pIKdrs,pIKCa,pIm,pIl,pINa,pICaT,pICaL,pIh]

fig3 = plotCurrentscape(vvec3, r3)
fig3.savefig('PLOTfiles/' + cellname + '_Currentscape3_' + modelname + '.pdf',dpi=500)
fig3.savefig('PLOTfiles/' + cellname + '_Currentscape3_' + modelname + '.png',dpi=500)
fig3.clf()
plt.close(fig3)

def plot_responses1():
    plt.subplot(3,1,1)
    plt.plot(tvec1, vvec10, color='r', label='Model')
    plt.plot(data1[:,0],data1[:,1], color='b', label='Experimental')
    # plt.legend()
    plt.xlim(0,4000)
    plt.subplot(3,1,2)
    plt.plot(tvec2, vvec20, color='r', label='Model')
    plt.plot(data2[:,0],data2[:,1], color='b', label='Experimental')
    # plt.legend()
    plt.xlim(0,4000)
    plt.subplot(3,1,3)
    plt.plot(tvec3, vvec30, color='r', label='Model')
    plt.plot(data3[:,0],data3[:,1], color='b', label='Experimental')
    # plt.legend()
    plt.xlim(0,4000)
    plt.tight_layout()

def plot_responses2():
    plt.subplot(2,1,1)
    plt.plot(tvec0, vvec00, color='r', label='Model')
    plt.plot(data0[:,0],data0[:,1], color='b', label='Experimental')
    # plt.legend()
    plt.xlim(0,4000)
    plt.ylim(numpy.amin([-110,numpy.amin(vvec00)-5,numpy.amin(data0[:,1])-5]),numpy.amax([25,numpy.amax(vvec00),numpy.amax(data0[:,1])]))
    plt.subplot(2,1,2)
    plt.plot(tvec01, vvec010, color='r', label='Model')
    plt.plot(data01[:,0],data01[:,1], color='b', label='Experimental')
    # plt.legend()
    plt.xlim(0,4000)
    plt.ylim(numpy.amin([-110,numpy.amin(vvec010)-5,numpy.amin(data01[:,1])-5]),numpy.amax([25,numpy.amax(vvec010),numpy.amax(data01[:,1])]))
    plt.tight_layout()

# Plot depolarization steps
plot_responses1()
plt.savefig('PLOTfiles/' + cellname + '_Traces1_' + modelname + '.pdf', bbox_inches='tight')
plt.savefig('PLOTfiles/' + cellname + '_Traces1_' + modelname + '.png', bbox_inches='tight')
plt.gcf().clear()
plt.cla()
plt.clf()
plt.close()

# Plot hyperpolarization steps
plot_responses2()
plt.savefig('PLOTfiles/' + cellname + '_Traces2_' + modelname + '.pdf', bbox_inches='tight')
plt.savefig('PLOTfiles/' + cellname + '_Traces2_' + modelname + '.png', bbox_inches='tight')
plt.gcf().clear()
plt.cla()
plt.clf()
plt.close()


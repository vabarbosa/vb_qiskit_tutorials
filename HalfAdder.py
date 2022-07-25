#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import QuantumCircuit


# In[2]:


from qiskit.providers.aer import AerSimulator
sim=AerSimulator()


# In[8]:


qc=QuantumCircuit(4,2)
#qc.x(0)
#qc.x(1)
#qc.x([0,1])
qc.ccx(0,1,2)
qc.cx(0,3)
qc.cx(1,3)
qc.measure(2,1)
qc.measure(3,0)
qc.draw()


# In[9]:


job=sim.run(qc)
result=job.result()
result.get_counts()


# In[ ]:





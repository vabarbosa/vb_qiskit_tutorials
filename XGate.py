#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import QuantumCircuit


# In[2]:


from qiskit.providers.aer import AerSimulator
sim=AerSimulator()


# In[3]:


qc=QuantumCircuit(3,3)
qc.x([0,1])
qc.measure([0,1,2],[0,1,2])
qc.draw()


# In[4]:


job=sim.run(qc)
result=job.result()
result.get_counts()


# In[ ]:





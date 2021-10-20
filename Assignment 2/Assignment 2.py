#!/usr/bin/env python
# coding: utf-8

# In[29]:


import torch


print("Axis of motion w \n", w)

#3x3 rotation matrix along z axis
def get_rot_mat(theta):
    theta = torch.tensor(theta)
    return torch.tensor([[torch.cos(theta), -torch.sin(theta), 0],
                         [torch.sin(theta), torch.cos(theta), 0],
                          [0,           0 ,                   1]])


def rodrigues_formula(axis, theta):
    R = torch.eye(3) + torch.sin(theta) * axis + (1-torch.cos(theta)) * torch.dot(axis,axis)
    return R

#input 1x3 axis, rotation angle theta
w = torch.tensor([0, 0, 1])

theta = get_rot_mat(45)
print("45 degree Rotation matrix theta \n", theta)

r = rodrigues_formula(w, theta)
print("Exponential map of the rotation angle \n", r)


# In[ ]:





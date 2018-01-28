
# coding: utf-8

# ### Problem Statement 1:
# Write a Python Program to implement your own myreduce() function which works exactly
# like Python's built-in function reduce()

# In[20]:


def myreduce(reduce_function,collection):
    result = collection[0] if len(collection) > 0 else None
    for x in collection[1:]:
        result = reduce_function(result,x)
    return result


# In[22]:


myreduce(lambda x,y:x+y,[1,2,3,4])


# ### Problem Statement 2:
# Write a Python program to implement your own myfilter() function which works exactly
# like Python's built-in function filter()

# In[23]:


def myfilter(filter_function,collection):
    return [x for x in collection if filter_function(x) ]


# In[33]:


set(myfilter(lambda x: x < 0, [1,2,-3]))


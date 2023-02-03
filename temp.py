import numpy as np

def gradient_descent(x,y):
    m_curr=b_curr=0
    iter = 1000
    n = len(x)
    learning_rate=0.01
    for i in range(iter):
        y_predicted=m_curr * x + b_curr
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        cost = (1/n)*sum((y-y_predicted)**2)
        m_curr = m_curr - learning_rate*md
        b_curr = b_curr - learning_rate*bd
        print('m {},b {},iteration {},cost {}'.format(m_curr,b_curr,i,cost))
        
x = np.array([1,2,3,4,5])
y = np.array([2,5,8,11,14])
print(gradient_descent(x, y))
        
    

    
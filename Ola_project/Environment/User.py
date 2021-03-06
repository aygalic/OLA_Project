import numpy as np
import random
# superclass
class User:
    # constructor
    def __init__(self, primary):
        # for each product an user has a reservation price
        self.reservation_price = [] # 5x1
        # stores the id {0,1,2,3,4} of products clicked
        self.products_clicked = []
        # stores the id {0,1,2,3,4} of products bought
        self.cart = []
        # stores the quantities of items bought for each product
        self.quantities = []
        # graph with the influence probabilities between the products
        self.P = np.zeros((5,5))
        # primary product shown
        self.primary = primary# {0,1,2,3,4} 


    # graph with the click probabilities on the products 
    def generate_graph(self, distribution):
        graph = np.zeros((5,5))
        graph = distribution
        return graph
            


# Inheritance
# 3 classes of users:

# targeted buyer, lower probability to click other products after the first
class User0(User):
    def __init__(self, primary, fixed_weights):
        User.__init__(self, primary)
        self.reservation_price = [10,20,30,40,50]  + np.random.normal(1, scale=2, size=5) # average reservation price
        # uncertain weight of the graph
        if fixed_weights!=1:
            self.P = User.generate_graph(self, np.random.uniform(0, 0.5, size=(5,5))) #lower influence probabilities
        # known weight of the graph
        else:
            self.P = User.generate_graph(self, 
        np.array([[0.1612583 , 0.02990957, 0.0215376 , 0.27068635, 0.25147687],
       [0.4918155 , 0.39001488, 0.12488759, 0.41009003, 0.32833393],
       [0.25435096, 0.32939066, 0.25589946, 0.18488915, 0.36627083],
       [0.27801728, 0.47490127, 0.33253022, 0.48659868, 0.42396207],
       [0.04359364, 0.45397953, 0.31312689, 0.41816953, 0.24363287]]))



# curious buyer, more variable budget, higher probability to click on other products
class User1(User):
    def __init__(self, primary, fixed_weights):
        User.__init__(self, primary)
        self.reservation_price = [10,20,30,40,50]  + np.random.normal(1, scale=4, size=5) # more variable reservation price
        if fixed_weights!=1:
            self.P = User.generate_graph(self, np.random.uniform(0.2, 1, size=(5,5))) # higher influence probabilities
        else:
            self.P = User.generate_graph(self, 
        np.array([[0.1612583 , 0.02990957, 0.0215376 , 0.27068635, 0.25147687],
       [0.4918155 , 0.39001488, 0.12488759, 0.41009003, 0.32833393],
       [0.25435096, 0.32939066, 0.25589946, 0.18488915, 0.36627083],
       [0.27801728, 0.47490127, 0.33253022, 0.48659868, 0.42396207],
       [0.04359364, 0.45397953, 0.31312689, 0.41816953, 0.24363287]]))


# buyer with higher budget 
class User2(User):
    def __init__(self, primary, fixed_weights):
        User.__init__(self, primary)
        self.reservation_price = [15,25,35,45,55] + np.random.normal(1, scale=3, size=5) # higher reservation price
        if fixed_weights!=1:
            self.P = User.generate_graph(self, np.random.uniform(0, 1, size=(5,5))) # more variable influence probabilities
        else:
            self.P = User.generate_graph(self, 
        np.array([[0.1612583 , 0.02990957, 0.0215376 , 0.27068635, 0.25147687],
       [0.4918155 , 0.39001488, 0.12488759, 0.41009003, 0.32833393],
       [0.25435096, 0.32939066, 0.25589946, 0.18488915, 0.36627083],
       [0.27801728, 0.47490127, 0.33253022, 0.48659868, 0.42396207],
       [0.04359364, 0.45397953, 0.31312689, 0.41816953, 0.24363287]]))


#homogenous user class (used in the first steps)  
class homogeneous_users(User):
    def __init__(self, primary, fixed_weights):
        User.__init__(self, primary)
        self.reservation_price = [10,23,35,41,54] + np.random.normal(0, scale=2, size=5) # small variance
        if fixed_weights!=1:
            self.P = User.generate_graph(self, np.random.uniform(0.2, 1, size=(5,5)))
        else:
            self.P = User.generate_graph(self, 
        np.array([[0.1612583 , 0.02990957, 0.0215376 , 0.27068635, 0.25147687],
       [0.4918155 , 0.39001488, 0.12488759, 0.41009003, 0.32833393],
       [0.25435096, 0.32939066, 0.25589946, 0.18488915, 0.36627083],
       [0.27801728, 0.47490127, 0.33253022, 0.48659868, 0.42396207],
       [0.04359364, 0.45397953, 0.31312689, 0.41816953, 0.24363287]]))

import numpy as np

def get_unique_loto(num):
    sample = np.arange(1, 101)
    res = list()
    for i in range(num):
        res.append(np.random.choice(sample, replace=False, size=(5, 5)))
    res = np.array(res)

    return res

print(get_unique_loto(3))

#def get_unique_loto(num):
    
#    import numpy as np
    
#    loto = np.zeros(num*5*5, dtype = np.int8)
    
#    for k in range(num):
#        for i in range(5*5):
#            repeat = True
            
#            while repeat:
#                repeat = False
#                random_number = np.random.randint(1,101)

#                if i > 0:
#                    for j in range(i):
#                        if loto[k*25+j] == random_number:
#                            repeat = True
#                            break
         
#                loto[k*25+i]=random_number

#    loto.shape = (num,5,5)
    
#    return loto


#def any_normal(*vectors):
#    for vec1 in vectors:
#        for vec2 in vectors:
#            if np.dot(vec1,vec2) == 0:
#                return True
#    return False

    # Напишите тело функции


#vec1 = np.array([2, 1])
#vec2 = np.array([-1, 2])
#vec3 = np.array([3,4])
#print(any_normal(vec1, vec2, vec3))
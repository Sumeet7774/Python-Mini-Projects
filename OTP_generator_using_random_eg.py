# Using Random displaying random numbers from 1 to 100 

import random as r

n = 10000
otp_list = [i for i in range(1000,n)]
print('Random numbers for otp are: ',r.choice(otp_list))
#print(otp_list)


num_list =[i for i in range(1,101)]
print('From 1 to 100 random numbers is: ',r.choice(num_list))



# Write a program to order confirmation system of laptop from given list

laptop = ['Dell','Lenevo','Asus','HP','Acer']
print(laptop)

product_id = 7059
l_index = int(input('Enter Laptop index: '))
amount = int(input('Enter amount of laptop: '))


try:
    x = laptop[l_index]
    print('The product id of laptop is: ',product_id)
    print('The name of laptop is: ',x)
    print('The amount of laptop is: ',amount)
    q = input('Do you want to confirm your order? Then Type Yes: ')
    if q == 'Yes':
        print('Your order is successfully placed')
    else : 
        print('Your order is cancelled')
    
    
except IndexError:
    print('The laptop is not found in the list')    

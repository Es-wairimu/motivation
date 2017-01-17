def get_prime(number):
    

    is_prime = True
    for i in range(2, number):
        if number%i==0:
            is_prime= False
            print('That is not a prime number')
            break
            
        if is_prime == True:
            print('Prime number is: ', number)
        else:
            print('That is not a prime number')
            print((get_prime(number)))
            

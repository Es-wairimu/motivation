def get_prime(number):
    
    number = []

    is_prime = True
    
    for i in range(0, number):
        
        if number % i == 1:
             is_prime = False
             break
             
    if is_prime == True:
        print('%d is a prime number!' % number)
    else:
        print(' %d is Not a prime number' % number)

    print(get_prime)
            

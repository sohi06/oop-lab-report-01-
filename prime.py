is_prime=lambda n:n>1 and all(n%i!=0 for i in range(2,int(n**0.5)+1))
print(is_prime(2))
print(is_prime(3))
from random import randint, seed

seed(10)
random_dictionary = {i: randint(1, 10) for i in range(5)}
print(random_dictionary)

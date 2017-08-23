print("Hello, World!")

#lists
alphabet = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(',')
print("length: ", len(alphabet))

#slicing
print(alphabet[3:])         #cut off first 3
print(alphabet[5:-3])       #cut off first 5 and last 3

#for loop
for letter in alphabet:
    print("letter: ", letter)

#for range
x = 0
for index in range(10):
    x += 10
    print("X = ", x)

#fizzbuzz
for num in range(1, 101):
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)





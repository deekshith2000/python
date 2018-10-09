n = int(input('Enter the number of layers:'))
a=0
s = ' '

for i in range(n-1,-1,-1):          #loop for different layers
    print('\n')
    a+=1
    for k in range(1,i+1):          #loop for providing space before star
        print(' ',end='')
    for j in range(1,a+1):          #loop for stars
        print('*',end=' ')
    
a = input()

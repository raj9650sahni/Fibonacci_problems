''' 
Hello sir I have done this problems in python language as i am much more comfortable in python.
Here is the four mentioned problems in a single function
'''

def fibo(n):
    n1=0 
    n2=1
    c=0
    ans = []
    
    if n==0:
        ans.append(0)
    if n==1:
        ans.append(n1)
    else:
        while c<n:
            ans.append(n1)
            temp = n1 + n2
            n1 = n2
            n2 = temp
            c+=1
    
    
    print( "Fibonacci series : ",ans)   # 1 . here i am printing fibonacci sequence 
    
    print("Reverse output : ",ans[::-1]) # 2. Here i am printing fibonacci sequence in reverse
    
    
     
       
    oddCount = 0
    evenCount = 0
    for num in ans:
        if num%2==0:
            evenCount +=1
        else:
            oddCount +=1
            
     #Here i have printed count of even number and count of odd numbers in fibonacci series      
    print("Even count : " + str(evenCount),  " odd count : " + str(oddCount))
    
    
    
    
    #here i have created another list to add modified elements in this list like add 4 in even numbers and 3 in odd numbers
    addList = []   
    for num in ans:
        if num%2==0:
            addList.append(num + 4)
        else:
            addList.append(num + 3)
            
    print("After adding 4 and 3 : ",addList)
    

print(fibo(n))

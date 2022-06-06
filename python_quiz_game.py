print('Welcome to quiz!')
playing=input("do you want toplay the game ")
print(playing)
if playing.lower() != "yes":
    quit()
    
print("okay let's play")
score=0
count=0
answar=input("What is the long form of CPU:")
if answar.lower()=='central processing unit':
    print('correct!')
    score=score+1
    count=count+1

else:
    print('wrong answar')
    count=count+1
    
answar=input("What is the pet name of Doni:")
if answar.lower()=='mahi' or answar.lower()=='msd':
    print('correct!')   
    score=score+1
    count=count+1
    

else:
    print('wrong answar')
    count=count+1

answar=input("What is the GPU:")
if answar.lower()=='graphics processing unit':
    print('correct!')
    score=score+1
    count=count+1
else:
    print('wrong answar')
    count=count+1

answar=input("What is the RAM stands for:")
if answar.lower()=='random access memory':
    print('correct!')
    score=score+1
    count=count+1
else:
    print('wrong answar')
    count=count+1
    
answar=input("What is the long form of NZA:")
if answar.lower()=='netzwerk academy':
    print('correct!')
    score=score+1
    count=count+1
else: 
    print('wrong answar')
    count=count+1
print("your score is %d  outof %d"%(score,count))



from math import sqrt
#print from 1 to 10
for i in range(1,11):
    print(i)

#  print chessboard from(1,1)to(8,8)
for i in range(1,9):
    for j in range(1,9):
        print(f"({i},{j})")    

# distance
for x0 in range(1,9):
    for y0 in range(1,9):
      for x1 in range(1,9):
          for y1 in range (1,9):
              if(x0==x1)&(y0==y1):
                  continue
              distance=sqrt((x1-x0)**2+(y1-y0)**2)
      print(f"({x0},{y0})",'to',f"({x1},{y1})",distance)

#4





       
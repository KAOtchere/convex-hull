#Author: Kwabena Aboagye-Otchere

#This function computes the convex hull of 2d points (brute force)
#The function takes an array of points as input and returns an array of points as output
#The output array contains the points that form the convex hull of the input

def computeConvex(points):
  #Array to store points which form the convex
  convexHull = []

  #Loop for first point of line segments
  for i in range(len(points)-1):

    #Loop for second points of line segments
    for j in range(i+1, len(points)):
      isConvex = True
      previousPoint = 0

      #Loop to check which side of the line segment the other points in the input array fall on
      for k in range(len(points)):
        if k!=i and k!=j:
          position = ((points[j][1] - points[i][1]) * points[k][0]) + ((points[i][0] - points[j][0]) * points[k][1]) - ((points[i][0] * points[j][1]) - (points[i][1] * points[j][0]))
          #The commented print statement below tracks the algorithms operation at each iteration
          #print("point1: (%2d , %2d) point2: (%2d , %2d) previouspos: %2d  currentPoint: (%2d, %2d) currentPointPos: %2d" %(points[i][0],points[i][1],points[j][0],points[j][1],previousPoint,points[k][0],points[k][1],position))
          if previousPoint >= 0 and position >=0 or previousPoint <= 0 and position <=0:
            previousPoint = position
          else:
            isConvex = False
            break 

      if isConvex:
        convexHull.append(points[i])
        convexHull.append(points[j])

  #Removes the duplicated points which were appended as a result of the line segment approach
  convexHull = list(dict.fromkeys(convexHull))
  return convexHull


#Test case to check the correctness of the algorithm
#7 coordinates are expected to be part of the with the coordinates being (-5,0), (0,-5), (6,11), (6,-3), (-3,11), (-6,4) and (4,-4)

a = (0,-4/3)
b = (12/7,0)
c = (-1,5)
d = (-5,0)
e = (0,-5)
f = (-3,3)
g = (5,1)
h = (0,10)
i = (6,11)
j = (6,-3)
k = (-6,4)
l = (-3,11)
m = (2,4)
n = (4,-4)
o = (1/5,3/2)
points = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o]
print((computeConvex(points)))

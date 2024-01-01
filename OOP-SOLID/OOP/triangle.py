import math

class Triangle:
    def __init__(self):
        self.points = []
    
    def add_point(self,point):
        self.points.append(point)
        
    def distance(self,point1,point2):
        x1, y1 = point1
        x2, y2 = point2
        
        return round(math.sqrt((x2-x1)**2 + (y2-y1)**2),3)
    
    def perimeter(self):
        if len(self.points) < 3:
             print("Enter valid points")
             return 
        
        point1, point2, point3 = self.points
        
        length1 = self.distance(point1,point2)
        length2 = self.distance(point2,point3)
        length3 = self.distance(point1,point3)

        first_sum=length1+length2
        second_sum=length2+length3
        third_sum=length1+length3
        if first_sum<= length3 or second_sum<= length1 or third_sum <= length2:
            print("Invalid points")
            return 0
        return length1+length2+length3
    
    def is_equal(self,another_triangle):
        for point in self.points:
            if point not in another_triangle.points:
                return False
        return True

t1 = Triangle()
t1.add_points((0,0))
t1.add_points((0,3))
t1.add_points((4,0))
print(t1.perimeter())

t2 = Triangle()
t2.add_points((1,2))
t2.add_points((2,1))
t2.add_points((1,5))
print(t2.perimeter())

print(t2.is_equal(t1))

t3 = Triangle()
t3.add_points((1,2))
t3.add_points((2,1))
t3.add_points((1,5))
print(t3.is_equal(t1))
print(t1 == t3)
print(t1.is_equal(t3))

        
    

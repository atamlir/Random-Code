
import math 

def is_point_black_or_white(p,x,y):
	degree_of_point = lambda x,y : math.degrees(math.atan2(y-50,x-50))
	distance_of_point = lambda x,y: math.sqrt((x - 50)**2 + (y-50)**2)
	if x >= 50 and y>=50:
		return 'Black' if degree_of_point(x,y) < p * 360/100 and distance_of_point(x,y) <= 50 else "white"
	elif x >= 50 and y < 50:
		return 'Black' if 180 + degree_of_point(x,y) < p * 360/100 and distance_of_point(x,y) <= 50 else "white"
	elif x < 50 and y < 50:
		return 'Black' if 360 + degree_of_point(x,y) < p * 360/100 and distance_of_point(x,y) <= 50 else "white"
	elif x < 50 and y > 50:
		return 'Black' if 270 + degree_of_point(x,y) < p * 360/100 and distance_of_point(x,y) <= 50 else "white"


number_of_points = int(input())

for i in xrange(number_of_points):
	p , x, y = map(int,raw_input().split())
	print "Case #" + str(1 + i) + ": " + is_point_black_or_white(p,x,y)
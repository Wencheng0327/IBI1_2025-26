#4.1
a = 5.08
b = 5.33
c = 5.55
d = b - a
e = c - b
if d > e:
    print ( "Population	growth is decelerating in Scotland." )
elif d == e:
    print ( "Population	growth is stable in Scotland." )
elif d < e:
    print ( "Population	growth is accelerating in Scotland." )

#4.2
X = True
Y = False
W = X or Y
# the truth table for W:
# X        Y        W
# Ture     True     True
# Ture     False    True
# False    True     True
# False    False    False 
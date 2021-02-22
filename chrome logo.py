from turtle import*
title('Tawheed')

bgcolor('white')
colormode(225)
r = 120
seth(-150)
up()

# the red petal

color('#ff3e30')
begin_fill()
fd(r)
down()
rt(90)
circle(-r, 120)
fd(r*3**.5)
lt(120)
circle(2*r, 120)
lt(60)
fd(r*3**.5)
end_fill()

# green petal

lt(180)
color('#179c52')
begin_fill()
fd(r*3**.5)
lt(120)
circle(2*r, 120)
lt(60)
fd(r*3**.5)
lt(180)
circle(-r, 120)
end_fill()

# yellow petal
left(180)
circle(r, 120)
color('#f7b529')
begin_fill()
circle(r, 120)
rt(180)
fd(r*3**.5)
rt(60)
circle(-2*r, 120)
rt(120)
fd(r*3**.5)
end_fill()

up()
lt(90)
fd(r/15)
seth(60)
color('#176bef')
down()
begin_fill()
circle(distance(0, 0))
end_fill()
hideturtle()

mainloop()

module Shapes
(   Point(Point)
,   Shape(Circle, Rectangle, Triangle)
,   surface
,   nudge
) where

-- Define a point type in 2d.
data Point = Point Float Float deriving (Show)

-- Define a shape type in 2d.
data Shape = Circle Point Float
           | Rectangle Point Point
           | Triangle Point Point Point
       deriving (Show)


-- prints the surface of a Shape type.
surface :: Shape -> Float
surface (Circle _ r) = pi * r ^ 2
surface (Rectangle (Point x1 y1) (Point x2 y2)) = (abs $ x2 - x1) * (abs $ y2 - y1)
surface (Triangle (Point x1 y1) (Point x2 y2) (Point x3 y3)) =
        sqrt (s * (s-a) * (s-b) * (s-c))
    where a = sqrt ((x1 - x2) ^ 2 + (y1 + y2) ^ 2)
          b = sqrt ((x2 - x3) ^ 2 + (y2 + y3) ^ 2)
          c = sqrt ((x3 - x1) ^ 2 + (y3 + y1) ^ 2)
          s = (a + b + c) / 2

-- moves a given shape by a given ammount on x and y axis.
nudge :: Shape -> Float -> Float -> Shape
nudge (Circle (Point x y) r) a b = Circle (Point (x+a) (y+b)) r
nudge (Rectangle (Point x1 y1) (Point x2 y2)) a b =
    Rectangle (Point (x1+a) (y1+b)) (Point (x2+a) (y2+b))
nudge (Triangle (Point x1 y1) (Point x2 y2) (Point x3 y3)) a b =
    Triangle (Point (x1+a) (y1+b)) (Point (x2+a) (y2+b)) (Point (x3+a) (y3+b))

module Geometry.Cuboid (volume, area) where


volume :: Float -> Float
volume a b c = (rectArea a b) * c

area :: Float -> Float
area a b c = (reactArea a b) * 2 + (rectArea a c) * 2 + (reactArea c b) * 2

rectArea :: Float -> Float -> Float
rectArea a b = a * b

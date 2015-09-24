-- The game of Dodgy Dice
-- One player game using two six-sided dice. You start with 4 lives and 0 points.
-- You have to get as many points before you run out of lives
-- A round ends when:
--  - you roll 1 at any dice, lose 1 life, score 0 points (independent of how
--    much you gathered so far in the round)
--  - you roll 1 and 1, you loose two lives
--  - you choose to stop rolling, score points for everthing rolled
--  - first 1-3 rounds, make at least one roll before you can stop
--  - rounds 4-6 force at least 2 rolls
--  - rounds 7-9 force at least 3 rolls, etc.
--  - every other dice combination is counted as points.
--  - doubles are worth twice, Eg. 6,6 means (6 + 6) * 2


module Main where



main :: IO ()

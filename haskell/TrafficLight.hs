import YesNo


data TrafficLight = Red | Yellow | Green


instance Eq TrafficLight where
  Red == Red = True
  Yellow == Yellow = True
  Green == Green = True
  _ == _ = False

instance Show TrafficLight where
  show Red = "Red Light"
  show Yellow = "Yellow Light"
  show Green = "Green Light"

instance YesNo TrafficLight where
    yesno Red = False
    yesno Yellow = False
    yesno Green = True

class YesNo a where
    yesno :: a -> Bool

instance YesNo Int where
    yesno 0 = False
    yesno _ = True

instance YesNo [a] where
    yesno [] = False
    yesno _ = True

instance YesNo Bool where
  yesno = id

instance YesNo (Maybe a) where
  yesno (Just _) = True
  yesno Nothing = False

-- works like if.
yesnoIf :: (YesNo a) => a -> b -> b -> b
yesnoIf test yesAction noAction = if yesno test then yesAction else noAction

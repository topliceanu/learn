module Tofu (
    Tofu,
    tofu
) where


class Tofu t where
    tofu :: j a -> t a j -- t has the kind of: * -> (* -> *) -> *

data Barry t k p = Barry {yabba :: p, dabba :: t k}

instance Functor (Barry a b) where
    fmap f (Barry {yabba = x, dabba = y}) = Barry {yabba = f x, dabba = y}

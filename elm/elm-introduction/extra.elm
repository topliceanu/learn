import String

type alias User = {
  name: String,
  bio: String,
  pic: String
}

addBio : String -> User -> User
addBio newBio user =
  { user | bio = newBio }

u = User "alex" "programmer" "mugshot.png"

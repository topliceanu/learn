package main

type User struct {
	ID    int
	Email string
}

func GetUserByID(id int) (*User, error) {
	return nil, nil
}

func GetFollowersForUser(id int) ([]*User, error) {
	return []*User{}, nil
}

func GetFollowerByIDAndUser(id int, userID int) (*User, error) {
	return nil, nil
}

func GetFolloweesForUser(id int) ([]*User, error) {
	return []*User{}, nil
}

func GetFolloweeByIDAndUser(id int, userID int) (*User, error) {
	return nil, nil
}

func SaveUser(user *User) error {
	return nil
}

func RemoveUserByID(id int) error {
	return nil
}

func Follow(followerID, followeeID int) error {
	return nil
}

func Unfollow(followerID, followeeID int) error {
	return nil
}

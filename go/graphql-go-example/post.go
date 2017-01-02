package main

type Post struct {
	ID     int
	UserID int
	Title  string
	Body   string
}

func GetPostByIDAndUser(id int, userID int) (*Post, error) {
	return nil, nil
}

func GetPostsForUser(id int) ([]*Post, error) {
	return []*Post{}, nil
}

func GetPostByID(id int) (*Post, error) {
	return nil, nil
}

func SavePost(post *Post) error {
	return nil
}

func RemovePostByID(id int) error {
	return nil
}

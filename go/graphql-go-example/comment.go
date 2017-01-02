package main

type Comment struct {
	ID     int
	UserID int
	PostID int
	Title  string
	Body   string
}

func GetCommentByIDAndPost(id int, userID int) (*Comment, error) {
	return nil, nil
}

func GetCommentsForPost(id int) ([]*Comment, error) {
	return []*Comment{}, nil
}

func SaveComment(comment *Comment) error {
	return nil
}

func RemoveCommentByID(id int) error {
	return nil
}

// TODO: Implement `TryFrom<String>` and `TryFrom<&str>` for the `Status` enum.
//  The parsing should be case-insensitive.

use thiserror;

#[derive(Debug, Clone, PartialEq)]
pub enum Status {
    ToDo,
    InProgress,
    Done,
}

#[derive(thiserror::Error, Debug)]
pub enum StatusError {
    #[error("`{0}` is not a valid status. Use one of: ToDo, InProgress, Done")]
    Invalid(String),
}

impl TryFrom<String> for Status {
    type Error = StatusError;
    fn try_from(value: String) -> Result<Self, Self::Error> {
        match value.to_lowercase().as_str() {
            "todo" => Ok(Status::ToDo),
            "inprogress" => Ok(Status::InProgress),
            "done" => Ok(Status::Done),
            _ => Err(StatusError::Invalid(value)),
        }
    }
}

impl TryFrom<&str> for Status {
    type Error = StatusError;
    fn try_from(value: &str) -> Result<Self, Self::Error> {
        Status::try_from(String::from(value))
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::convert::TryFrom;

    #[test]
    fn test_try_from_string() {
        let status = Status::try_from("ToDO".to_string()).unwrap();
        assert_eq!(status, Status::ToDo);

        let status = Status::try_from("inproGress".to_string()).unwrap();
        assert_eq!(status, Status::InProgress);

        let status = Status::try_from("Done".to_string()).unwrap();
        assert_eq!(status, Status::Done);
    }

    #[test]
    fn test_try_from_str() {
        let status = Status::try_from("ToDO").unwrap();
        assert_eq!(status, Status::ToDo);

        let status = Status::try_from("inproGress").unwrap();
        assert_eq!(status, Status::InProgress);

        let status = Status::try_from("Done").unwrap();
        assert_eq!(status, Status::Done);
    }

    #[test]
    fn test_try_from_invalid() {
        let status = Status::try_from("Blabla");
        assert!(status.is_err());
        assert_eq!(
            status.unwrap_err().to_string(),
            "`Blabla` is not a valid status. Use one of: ToDo, InProgress, Done"
        );
    }
}

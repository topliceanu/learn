//! # My Crate
//!
//! `my_crate` is a collection of utilities to make performing certain
//! calculations more convenient. THIS IS CRATE-LEVEL DOCUMENTATION!

use std::{fs, env, error::Error};
use core::iter::Iterator;

pub fn run(cfg: &Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(&cfg.file_path)?;
    //println!("File contents:\n{contents}");
    let res: Vec<&str> = if cfg.ignore_case {
        search_case_insensitive(&cfg.query, &contents)
    } else {
        search(&cfg.query, &contents)
    };
    for line in res {
        println!("{line}")
    }
    Ok(())
}

pub fn search<'a>(query: &str, contents: &'a str) -> Vec<&'a str> {
    return contents
        .lines()
        .filter(|line| line.contains(query))
        .collect()
}

pub fn search_case_insensitive<'a>(query: &str, contents: &'a str) -> Vec<&'a str> {
    let query = query.to_lowercase();
    return contents
        .lines()
        .filter(|line| line.to_lowercase().contains(&query))
        .collect();
}

// query and file_path are related so it makes sense to have them in the same struct.
pub struct Config {
    pub query: String,
    pub file_path: String,
    pub ignore_case: bool,
}

impl Config {
    pub fn build(mut args: impl Iterator<Item=String>) -> Result<Config, &'static str> {
        let Some(query) = args.next() else {
            return Err("first argument must be a query string");
        };
        let Some(file_path) = args.next() else {
            return Err("second argument must be a file path");
        };
        let mut ignore_case = env::var("IGNORE_CASE").is_ok();
        if let Some(ignore_case_flag) = args.next() && ignore_case_flag.eq("--ignore-case") {
            ignore_case = true
        };
        return Ok(Config{query, file_path, ignore_case})
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn one_result() {
        let query = "duct";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.
Duct tape.";

        assert_eq!(vec!["safe, fast, productive."], search(query, contents));
    }

    #[test]
    fn case_insensitive() {
        let query = "rUsT";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.
Trust me.";

        assert_eq!(
            vec!["Rust:", "Trust me."],
            search_case_insensitive(query, contents)
        );
    }
}
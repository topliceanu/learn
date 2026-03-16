use std::env;
use std::process;

use minigrep::{Config, run};

fn main() {
    let cfg = Config::build(env::args()).unwrap_or_else(|err| {
        eprintln!("Problem parsing args: {err}");
        process::exit(1)
    }); 

    //println!("searching for {} in file {}", cfg.query, cfg.file_path);

    if let Err(err) = run(&cfg) {
       eprintln!("Application error: {err}");
        process::exit(1)
    }
}



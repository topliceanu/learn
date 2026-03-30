use std::{
    fs, 
    io::{BufReader, prelude::*}, 
    net::{TcpListener, TcpStream}, 
    thread, 
    time::Duration,
};

use rust_book::ch21;

fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();
    let pool = ch21::ThreadPool::new(5);

    for stream in listener.incoming() {
        let stream = stream.unwrap(); // When stream goes out of scope, the connection is closed from the server-side.

        if let Err(err) = pool.execute(|| {
            println!("connection established!");
            handle_connection(stream);
        }) {
            println!("Failed to execute job: {:?}", err)
        }
    }

    println!("shutting down");
}

fn handle_connection(mut stream: TcpStream) {
    let buf_reader = BufReader::new(&stream);
    let http_request: Vec<_> = buf_reader
        .lines()
        .map(|result| result.unwrap())
        .take_while(|line| !line.is_empty())
        .collect();

    println!("Request: {http_request:#?}");

    let request_line = &http_request[0];
    let (status_line, filename) = match request_line.as_ref() {
        "GET / HTTP/1.1" => ("HTTP/1.1 200 OK", "hello.html"),
        "GET /slow HTTP/1.1" => {
            thread::sleep(Duration::from_secs(5));
            ("HTTP/1.1 200 OK", "hello.html")
        },
        _ => ("HTTP/1.1 404 NOT FOUND", "404.html"),
    };
    let contents = fs::read_to_string(filename).unwrap();
    let length = contents.len();
    let response = format!("{status_line}\r\nContent-Length: {length}\r\n\r\n{contents}");
    stream.write_all(response.as_bytes()).unwrap();
}
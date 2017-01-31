use std::io::{Read, Write, BufReader, BufRead};
use std::net::{TcpListener, TcpStream};

fn main() {
    // bind allows us to create a connection on the port
    // and gets it ready to accept connections.
    let listener = TcpListener::bind("0.0.0.0:3000").unwrap();

    // The listener's accept method waits or 'blocks' until
    // we have a connection and then returns a new TcpStream
    // that we can read and write data to.
    let stream = listener.accept().unwrap().0;
    read_request(stream);
}

// This function takes the stream we just got from the
// listener and then reads some data from it.
fn read_request(mut stream: TcpStream) {
    //let mut request_data = String::new();
    let mut reader = BufReader::new(stream);

    // lines until you hit an empty line, which means that the body is next.
    for line in reader.by_ref().lines() {
        if line.unwrap() == "" {
            break;
        }
    }
    let mut line = String::new();
    reader.read_line(&mut line);
    send_response(line, reader.into_inner());

    // The read_to_string method uses the string we pass
    // in and fills it up with the data from the stream.
    //stream.read_to_string(&mut request_data);

    // Finally we print the data
    //println!("{}", request_data);
}

fn send_response(line: String, mut stream: TcpStream) {
    let num: i32 = line.parse().unwrap();
    println!("{}", num);
    let response = format!("HTTP/1.1 200 OK\n\n{}", num);
    stream.write_all(response.as_bytes()).unwrap();
}

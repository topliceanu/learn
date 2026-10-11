use tokio::io::{self, AsyncRead, AsyncReadExt, AsyncWrite};
use tokio::net::TcpListener;

#[tokio::main]
async fn main() -> io::Result<()> {
    let listener = TcpListener::bind("127.0.0.1:9999").await?;

    loop {
        let (socket, _addr)= listener.accept().await?;
        println!("Recevied connection from {}", _addr);
        let (mut rd, mut wr) = io::split(socket);
        tokio::spawn(async move {
            if io::copy(&mut rd, &mut wr).await.is_err() {
                eprintln!("failed to copy");
            }
        });
    }
}
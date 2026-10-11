use tokio::{io::{self, AsyncReadExt, AsyncWriteExt}, net};

#[tokio::main]
async fn main() -> io::Result<()> {
    let socket = net::TcpStream::connect("127.0.0.1:9999").await?;
    let (mut rd, mut wr) = io::split(socket);

    let reader = tokio::spawn(async move {
        let mut buf = [0;1024];
        loop {
            let n = rd.read(&mut buf).await?;
            if n == 0 {
                break;
            }
            println!("{:?}", &buf[..n]);
        }
        Ok::<_, io::Error>(())
    });

    let writer = tokio::spawn(async move {
        wr.write_all(b"hello\r\n").await?;
        wr.write_all(b"world\r\n").await?;
        wr.shutdown().await?;
        Ok::<_, io::Error>(())
    });

    writer.await??;
    reader.await??;
    Ok(())
}
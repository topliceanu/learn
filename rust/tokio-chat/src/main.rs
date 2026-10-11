use std::collections::HashSet;
use std::sync::{Arc, Mutex};

use futures::{SinkExt, StreamExt};
use tokio::net::{TcpStream, TcpListener};
use tokio::sync::broadcast;
use tokio_util::codec::{FramedRead, FramedWrite, LinesCodec};

use tokio_chat::random_name::random_name;

const HELP_MSG: &str = include_str!("./help.txt");

#[derive(Clone)]
struct Names(Arc<Mutex<HashSet<String>>>);
impl Names {
    fn new() -> Self {
        Self(Arc::new(Mutex::new(HashSet::new())))
    }
    fn insert(&self, name: String) -> bool {
        self.0.lock().unwrap().insert(name)
    }
    fn get_unique(&self) -> String {
        let mut name = random_name();
        let mut guard = self.0.lock().unwrap();
        while !guard.insert(name.clone()) {
            name = random_name();
        }
        return name
    }
    fn remove(&self, name: &String) {
        self.0.lock().unwrap().remove(name);
    }
}

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    let server = TcpListener::bind("127.0.0.1:42069").await?;
    let (tx, _) = broadcast::channel::<String>(32); // we are not interested in receiving atm.
    let names = Names::new();
    loop {
        let (tcp, _) = server.accept().await?;
        tokio::spawn(handle_user(tcp, tx.clone(), names.clone()));
    }
}

macro_rules! b {
    ($result:expr) => {
        match $result {
            Ok(ok) => ok,
            Err(err) => break Err(err.into()),
        }
    }
}

async fn handle_user(mut tcp: TcpStream, tx: broadcast::Sender<String>, names: Names) -> anyhow::Result<()> {
    let (reader, writer) = tcp.split();
    let mut stream = FramedRead::new(reader, LinesCodec::new());
    let mut sink = FramedWrite::new(writer, LinesCodec::new());
    let mut rx = tx.subscribe();


    // Generate random name for the user 
    let mut name = names.get_unique();

    sink.send(HELP_MSG).await?;
    sink.send(format!("You are {}", name)).await?;

    let result: anyhow::Result<()> = loop {
        tokio::select! {
            user_msg_raw = stream.next() => {
                let Some(Ok(mut user_msg)) = user_msg_raw else {
                    break Ok(());
                };
                if user_msg.starts_with("/name") {
                    let new_name = user_msg.split_ascii_whitespace().nth(1).unwrap().to_owned();
                    if names.insert(new_name.clone()) {
                        tx.send(format!("{name} is now {new_name}"))?;
                        names.remove(&name);
                        name = new_name;
                    } else {
                        b!(sink.send(format!("{new_name} is already taken")).await);
                    }
                } else if user_msg.starts_with("/help") {
                    b!(sink.send(HELP_MSG).await);
                } else if user_msg.starts_with("/quit") {
                    break Ok(());
                } else {
                    b!(tx.send(format!("{name}: {user_msg}")));
                }
            }
            peer_msg = rx.recv() => {
                b!(sink.send(peer_msg?).await);
            }
        }
    };
    Ok(())
}

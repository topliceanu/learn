use std::time::{Duration, Instant};

use tokio_tut::{delay::Delay, mini_tokio::MiniTokio};

fn main() {
    let mut mini_tokio = MiniTokio::new();
    mini_tokio.spawn(async {
        let when = Instant::now() + Duration::from_millis(1000);
        Delay { when, waker: None }.await;
        println!("done");
    });
    mini_tokio.run();
}
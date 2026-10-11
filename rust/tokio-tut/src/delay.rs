use std::future::Future;
use std::pin::Pin;
use std::sync::{Arc, Mutex};
use std::task::{Context, Poll, Waker}; 
use std::thread;
use std::time::{Instant};

pub struct Delay {
    pub when: Instant,
    pub waker: Option<Arc<Mutex<Waker>>>, 
}

impl Future for Delay {
    type Output = ();

    fn poll(self: Pin<&mut Self>, ctx: &mut Context<'_>) -> Poll<()> {
        if Instant::now() >= self.when {
            return Poll::Ready(());
        }
        if let Some(waker)         = &self.waker {
            let mut waker = waker.lock().unwrap();
            if !waker.will_wake(ctx.waker()) {
                *waker = ctx.waker().clone();
            }
        } else {
            let when = self.when;
            let waker = Arc::new(Mutex::new(ctx.waker().clone()));
            thread::spawn(move || {
                let now = Instant::now();
                if now < when {
                    thread::sleep(when - now);
                }
                let waker = waker.lock().unwrap();
                waker.wake_by_ref();
            });
        }
        Poll::Pending
    }
}
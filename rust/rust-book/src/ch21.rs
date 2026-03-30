use std::thread;
use std::sync::{Arc, Mutex, mpsc::{channel, Sender, Receiver}};
use std::ops::Drop;

#[derive(Debug)]
pub struct ExecuteError(String);

pub struct ThreadPool {
    workers: Vec<Worker>, // Pool owns the workers.
    sender: Option<Sender<Job>>, // We use option in order to get the value from a mutable ref using take().
}

impl ThreadPool {
    // TODO: use std::thread::Builder to spawn threads.
    pub fn new(size: usize) -> Self {
        assert!(size > 0);

        let (sender, receiver) = channel::<Job>();
        let receiver = Arc::new(Mutex::new(receiver));

        let mut workers: Vec<Worker> = Vec::with_capacity(size);
        for idx in 0..size {
            let worker = Worker::new(idx, Arc::clone(&receiver));
            workers.push(worker);
        }
        ThreadPool{workers: workers, sender: Some(sender)}
    }

    pub fn execute<F>(&self, job: F) -> Result<(), ExecuteError>
    where 
        F : FnOnce() + Send + 'static,
    {
        let job = Box::new(job);
        let sender = self.sender.as_ref().ok_or(ExecuteError("ThreadPool shutting down".to_string()))?;
        if let Err(err) = sender.send(job) {
           return Err(ExecuteError(format!("Failed to send job: {:?}", err)))
        }
        Ok(())
    }
}

impl Drop for ThreadPool {
    fn drop(&mut self) {
        println!("Droppin ThreadPool!");
        drop(self.sender.take()); // Stop sending jobs to the workers.
        for worker in self.workers.drain(..) {
            if let Err(err) = worker.handle.join() {
               println!("unable to join worker handle: {:?}", err) 
            } // Wait for each worker in turn to finish work.
        }
    }
}

type Job = Box<dyn FnOnce() + Send + 'static>;

#[derive(Debug)]
pub struct Worker {
    pub id: usize,
    handle: thread::JoinHandle<()>, // Worker owns the thread handle!
}

impl Worker {
    pub fn new(id: usize, receiver: Arc<Mutex<Receiver<Job>>>) -> Self {
        let handle = thread::spawn(move || {
            loop {
                let Ok(receiver) = receiver.lock() else {
                    panic!("failed to aquire the receiver lock");
                };
                match receiver.recv() {
                    Ok(job) => {
                        println!("Worker id={} started a new job", id);
                        job();
                    },
                    Err(_) => {
                        println!("Worker id={} disconnected", id);
                        break
                    },
                }
            }
        });
        Worker{id, handle}
    }
}
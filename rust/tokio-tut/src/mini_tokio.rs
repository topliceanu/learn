use std::{collections::VecDeque, pin::Pin, task::Context};
use futures::{task};
use std::sync::{mpsc, Arc, Mutex};
use std::task::Poll;

pub struct TaskFuture {
    future: Pin<Box<dyn Future<Output=()> + Send>>,
    poll: Poll<()>,
}
impl TaskFuture {
    fn new(future: impl Future< Output=()> + Send + 'static) -> TaskFuture {
        TaskFuture {
            future: Box::pin(future),
            poll: Poll::Pending,
        }
    }
    fn poll(&mut self, ctx: &mut Context<'_>) {
        if self.poll.is_pending() {
            self.poll = self.future.as_mut().poll(ctx);
        }
    }
}

pub struct Task {
    task_future: Mutex<TaskFuture>,
    executor: mpsc::Sender<Arc<Task>>,
}
impl Task {
    pub fn schedule(self: &Arc<Self>) {
        self.executor.send(self.clone());
    }
    pub fn poll(self: Arc<Self>) {
        let waker = task::waker(self.clone());
        let mut ctx = Context::from_waker(&waker);
        let mut task_future = self.task_future.try_lock().unwrap();
        task_future.poll(&mut ctx);
    }
    pub fn spawn<F>(future: F, sender: &mpsc::Sender<Arc<Task>>) 
    where F: Future<Output=()> + Send + 'static {
        let task = Arc::new(Task {
            task_future: Mutex::new(TaskFuture::new(future)),
            executor: sender.clone(),
        });
        let _ = sender.send(task);
    }
}
impl task::ArcWake for Task {
    fn wake_by_ref(arc_self: &Arc<Self>) {
        arc_self.schedule();
    }
}

pub struct MiniTokio {
    scheduled: mpsc::Receiver<Arc<Task>>,
    sender: mpsc::Sender<Arc<Task>>,
}
impl MiniTokio {
    pub fn new() -> Self {
        let (sender, scheduled) = mpsc::channel();
        MiniTokio{ scheduled, sender }
    }
    pub fn spawn<F>(&mut self, future: F)
    where F: Future<Output=()> + Send + 'static {
        Task::spawn(future, &self.sender);
    }

    pub fn run(&mut self) {
        while let Ok(task) = self.scheduled.recv() {
            task.poll();
        }
    }
}
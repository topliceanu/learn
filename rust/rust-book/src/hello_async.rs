use futures::future::{select, Either};
use std::future::Future;
use std::pin::{pin, Pin};
use tokio::time;

pub async fn page_title(url: &str) -> Option<String> {
    let response_text = reqwest::get(url).await.unwrap().text().await.unwrap();
    let html = scraper::Html::parse_document(response_text.as_str());
    let selector = scraper::Selector::parse("title").unwrap();
    html.select(&selector)
        .nth(0)
        .map(|title_element| title_element.inner_html())
}

pub async fn timeout<F: Future>(
    future_to_try: F,
    max_time: time::Duration,
) -> Result<F::Output, time::Duration> {
    match select(pin!(future_to_try), pin!(time::sleep(max_time))).await {
        Either::Left(value) => Result::Ok(value.0),
        Either::Right(_) => Result::Err(max_time),
    }
}

#[cfg(test)]
mod tests_for_timeout {
    use super::*;
    use std::time::Duration;
    use tokio::runtime;

    #[test]
    fn test_timeout() {
        let rt = runtime::Runtime::new().unwrap();
        rt.block_on(async {
            let res = timeout(
                async {
                    time::sleep(Duration::from_millis(10)).await;
                    "done!"
                },
                Duration::from_millis(20),
            )
            .await;
            assert_eq!(res.is_ok(), true, "fn terminates before timout");
            assert_eq!(res, Result::Ok("done!"), "returns the result")
        });
    }
}

// map_stringify takes two arguments: a vector of inputs, and an async function that converts the input to an output,
// where the outputs can be converted to strings. map_stringify returns a vector of stringified outputs.
pub async fn map_stringify<I, O, F>(f: impl Fn(I) -> F, inputs: Vec<I>) -> Vec<String>
where
    O: ToString,
    F: Future<Output = O>,
{
    let f = &f;
    let futs = inputs
        .into_iter()
        .map(|input| async move { f(input).await.to_string() });
    futures::future::join_all(futs).await
}

// Sequential version of futures::future::join_all.
pub async fn join_all_seq<T>(futs: Vec<Pin<&mut dyn Future<Output = T>>>) -> Vec<T> {
    let mut output = vec![];
    for f in futs {
        let res = f.await;
        output.push(res);
    }
    return output;
}

#[cfg(test)]
mod tests_for_seq_map {
    use super::*;
    use tokio::runtime;

    #[test]
    fn test_seq_map() {
        let rt = runtime::Runtime::new().unwrap();
        rt.block_on(async {
            let res = join_all_seq(vec![
                pin!(async {
                    return 1;
                }),
                pin!(async {
                    return 2;
                }),
            ])
            .await;
            assert_eq!(res, vec![1, 2])
        });
    }
}

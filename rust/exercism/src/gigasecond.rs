// See https://exercism.org/tracks/rust/exercises/gigasecond

use time::PrimitiveDateTime as DateTime;
use time::{SignedDuration};

// Returns a DateTime one billion seconds after start.
pub fn after(start: DateTime) -> DateTime {
    start.saturating_add(SignedDuration::new(1_000_000_000, 0))
}

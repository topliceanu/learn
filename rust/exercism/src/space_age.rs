// The code below is a stub. Just enough to satisfy the compiler.
// In order to pass the tests you can add-to or change any of this code.

#[derive(Debug)]
pub struct Duration {
    seconds: u64,
}

impl From<u64> for Duration {
    fn from(seconds: u64) -> Self {
        Duration{ seconds }
    }
}

pub trait Planet {
    const EARTH_ORBITAL_PERIOD_YEARS: f64 = 60.0 * 60.0 * 24.0 * 365.25;
    const ORBITAL_PERIOD: f64;
    fn years_during(d: &Duration) -> f64 {
        ((d.seconds as f64) / Self::EARTH_ORBITAL_PERIOD_YEARS / Self::ORBITAL_PERIOD * 100.0).round() / 100.0
    }
}

macro_rules! new_planet {
    ($planet_name: ident, $orbital_period: expr) => {
        pub struct $planet_name;

        impl Planet for $planet_name {
            const ORBITAL_PERIOD: f64 = $orbital_period;
        }
    };
}

new_planet!(Mercury, 0.2408467);
new_planet!(Venus, 0.61519726);
new_planet!(Earth, 1.0);
new_planet!(Mars, 1.8808158);
new_planet!(Jupiter, 11.862615);
new_planet!(Saturn, 29.447498);
new_planet!(Uranus, 84.016846);
new_planet!(Neptune, 164.79132);

fn assert_in_delta(expected: f64, actual: f64) {
    let diff: f64 = (expected - actual).abs();
    let delta: f64 = 0.01;
    if diff > delta {
        panic!("Your result of {actual} should be within {delta} of the expected result {expected}")
    }
}
#[test]
fn age_on_earth() {
    let seconds = 1_000_000_000;
    let duration = Duration::from(seconds);
    let output = Earth::years_during(&duration);
    let expected = 31.69;
    assert_in_delta(expected, output);
}
#[test]
fn age_on_mercury() {
    let seconds = 2_134_835_688;
    let duration = Duration::from(seconds);
    let output = Mercury::years_during(&duration);
    let expected = 280.88;
    assert_in_delta(expected, output);
}
#[test]
fn age_on_venus() {
    let seconds = 189_839_836;
    let duration = Duration::from(seconds);
    let output = Venus::years_during(&duration);
    let expected = 9.78;
    assert_in_delta(expected, output);
}
#[test]
fn age_on_mars() {
    let seconds = 2_129_871_239;
    let duration = Duration::from(seconds);
    let output = Mars::years_during(&duration);
    let expected = 35.88;
    assert_in_delta(expected, output);
}
#[test]
fn age_on_jupiter() {
    let seconds = 901_876_382;
    let duration = Duration::from(seconds);
    let output = Jupiter::years_during(&duration);
    let expected = 2.41;
    assert_in_delta(expected, output);
}
#[test]
fn age_on_saturn() {
    let seconds = 2_000_000_000;
    let duration = Duration::from(seconds);
    let output = Saturn::years_during(&duration);
    let expected = 2.15;
    assert_in_delta(expected, output);
}
#[test]
fn age_on_uranus() {
    let seconds = 1_210_123_456;
    let duration = Duration::from(seconds);
    let output = Uranus::years_during(&duration);
    let expected = 0.46;
    assert_in_delta(expected, output);
}
#[test]
fn age_on_neptune() {
    let seconds = 1_821_023_456;
    let duration = Duration::from(seconds);
    let output = Neptune::years_during(&duration);
    let expected = 0.35;
    assert_in_delta(expected, output);
}
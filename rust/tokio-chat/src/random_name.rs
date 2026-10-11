use fastrand;

pub static ADJECTIVES: [&str; 6] = [
    "Mushy",
    "Starry",
    "Peaceful",
    "Phony",
    "Amazing",
    "Queasy",
];

pub static ANIMALS: [&str; 6] = [
    "Owl",
    "Mantis",
    "Gopher",
    "Robin",
    "Vulture",
    "Prawn",
];

pub fn random_name() -> String {
    let adjective = fastrand::choice(ADJECTIVES).unwrap();
    let animal = fastrand::choice(ANIMALS).unwrap();
    format!("{adjective}{animal}")
}
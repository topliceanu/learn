fn main() {
    println!("Hello, world!");

    // 1.2 Formatted print
    println!("{} days", 31);

    println!("{0}, this is {1}, this is {0}", "Alice", "Bob");

    println!("{subject} {verb} {object}",
             object="the lazy dog",
             subject="the quick brown fox",
             verb="jumps over");

    println!("{} of {:b} people know binary", 1, 2)
}

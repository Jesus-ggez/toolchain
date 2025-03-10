fn main() {
    let foo: Vec<_> = ('a'..='z').chain('0'..='9').collect();
    println!("{:?}", foo); // "abcdefghijklmnopqrstuvwxyz0123456789"
}

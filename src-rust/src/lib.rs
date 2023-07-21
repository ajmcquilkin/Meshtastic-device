#[no_mangle]
pub extern "C" fn add_from_rust(left: u32, right: u32) -> u32 {
    left + right
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = add_from_rust(2, 2);
        assert_eq!(result, 4);
    }
}
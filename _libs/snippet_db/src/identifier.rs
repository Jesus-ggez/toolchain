use pyo3::prelude::*;

//<
#[pyclass]
pub struct Identifier;

#[pymethods]
impl Identifier {
    #[staticmethod]
    pub fn from_number(num: u32) -> Option<String> {
        if num >= 36*36 {
            return None;
        }

        let base = 36;
        let first = (num / base) as u8;
        let second = (num % base) as u8;

        Some(format!(
                "{}{}",
                Self::encode_digit(first),
                Self::encode_digit(second),
        ))
    }

    #[staticmethod]
    pub fn to_number(s: String) -> Option<u32> {
        let chars: Vec<_> = s.chars().collect();
        let second = Self::decode_digit(chars[1])?;
        let first = Self::decode_digit(chars[0])?;

        Some(first * 36 + second)
    }
}

impl Identifier{
    fn encode_digit(digit: u8) -> char {
        match digit {
            0..=9 => (b'0' + digit) as char,
            10..=35 => (b'a' + (digit - 10)) as char,
            _ => unreachable!(),
        }
    }

    fn decode_digit(c: char) -> Option<u32> {
        match c {
            '0'..='9' => Some(c as u32 - '0' as u32),
            'a'..='z' => Some(10 + (c as u32 - 'a' as u32)),
            _ => None,
        }
    }
}

#[derive(Debug, PartialEq, Eq)]
pub struct Dna {
    sequence: String,
}

#[derive(Debug, PartialEq, Eq)]
pub struct Rna {
    sequence: String,
}

impl Dna {
    pub fn new(dna: &str) -> Result<Dna, usize> {
        let mut sequence = String::with_capacity(dna.len());
        for (i, c) in dna.chars().enumerate() {
            if let 'G' | 'C' | 'T' | 'A' = c {
                sequence.push(c)
            } else {
                return Err(i)
            }
        }
        Ok(Dna{ sequence: sequence })
    }

    pub fn into_rna(self) -> Rna {
        let sequence = self.sequence.chars().map(|nucleotide| {
            match nucleotide {
                'G' => 'C',
                'C' => 'G', 
                'T' => 'A', 
                'A' => 'U',
                _ => unreachable!()
            }
        }).collect();
        Rna { sequence }
    }
}

impl Rna {
    pub fn new(rna: &str) -> Result<Rna, usize> {
        let mut sequence = String::with_capacity(rna.len());
        for (i, c) in rna.chars().enumerate() {
            if !matches!(c, 'C' | 'G' | 'A' | 'U') {
                return Err(i)
            }
            sequence.push(c)
        }
        Ok(Rna{ sequence })
    }
}


#[test]
fn different_rna_are_different() {
    let a = Rna::new("G").unwrap();
    let b = Rna::new("UGCACCAGAAUU").unwrap();
    assert_ne!(a, b);
}
#[test]
fn empty_rna_sequence() {
    let input = "";
    let output = Dna::new(input).unwrap().into_rna();
    let expected = Rna::new("").unwrap();
    assert_eq!(output, expected);
}
#[test]
fn rna_complement_of_cytosine_is_guanine() {
    let input = "C";
    let output = Dna::new(input).unwrap().into_rna();
    let expected = Rna::new("G").unwrap();
    assert_eq!(output, expected);
}
#[test]
fn rna_complement_of_guanine_is_cytosine() {
    let input = "G";
    let output = Dna::new(input).unwrap().into_rna();
    let expected = Rna::new("C").unwrap();
    assert_eq!(output, expected);
}
#[test]
fn rna_complement_of_thymine_is_adenine() {
    let input = "T";
    let output = Dna::new(input).unwrap().into_rna();
    let expected = Rna::new("A").unwrap();
    assert_eq!(output, expected);
}
#[test]
fn rna_complement_of_adenine_is_uracil() {
    let input = "A";
    let output = Dna::new(input).unwrap().into_rna();
    let expected = Rna::new("U").unwrap();
    assert_eq!(output, expected);
}
#[test]
fn rna_complement() {
    let input = "ACGTGGTCTTAA";
    let output = Dna::new(input).unwrap().into_rna();
    let expected = Rna::new("UGCACCAGAAUU").unwrap();
    assert_eq!(output, expected);
}
#[test]
fn invalid_dna_input() {
    let input = "U";
    let output = Dna::new(input);
    let expected = Err(0);
    assert_eq!(output, expected);
}
#[test]
fn invalid_dna_input_at_offset() {
    let input = "ACGTUXXCTTAA";
    let output = Dna::new(input);
    let expected = Err(4);
    assert_eq!(output, expected);
}
#[test]
fn invalid_rna_input() {
    let input = "T";
    let output = Rna::new(input);
    let expected = Err(0);
    assert_eq!(output, expected);
}
#[test]
fn invalid_rna_input_at_offset() {
    let input = "ACGTUXXCTTAA";
    let output = Rna::new(input);
    let expected = Err(3);
    assert_eq!(output, expected);
}
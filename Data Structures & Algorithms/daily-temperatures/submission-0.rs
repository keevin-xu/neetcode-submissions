//stack problems: "next greater" or "next smaller" element
impl Solution {
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        let mut out : Vec<i32> = vec![0; temperatures.len()];
        let mut stack : Vec<(i32,usize)> = Vec::new();
        for i in 0..(out.len()) {
            let curr = temperatures[i];
            while !stack.is_empty() && stack.last().unwrap().0 < curr {
                let last = stack.pop().unwrap().1;
                out[last] = (i-last) as i32;
            }
            stack.push((curr,i));
        }
        out
    }
}

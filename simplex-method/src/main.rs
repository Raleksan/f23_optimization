
extern crate nalgebra as na;
use na::{Vector6, Matrix4x6, Vector4, Matrix, Matrix4};

use itertools::Itertools;

fn main() {

    // A vector of coefficients of objective function - C
    let c 
        = Vector6::from_element((5, 4, 0, 0, 0, 0));

    // A matrix of coefficients of constraint function - A
    let a = Matrix4x6::new(
        6, 4, 1, 0, 0, 0,
        1, 2, 0, 1, 0, 0,
        -1, 1, 0, 0, 1, 0,
        0, 1, 0, 0, 0, 1 );

    // A vector of right-hand side numbers - b
    let b 
        = Vector4::from_element((24, 6, 1, 2));
        
    // Approximation value
    let approx: f32 = 0.001;

    // Step 0. Construct a starting basic feasible solution, 
    // and let B and C_b be its associated basis and objective 
    // coefficients vector, respectively.

    // vec B_0 - feasible basis of the system
    // vec X_b - vector of basic veriables
    // vec C_b - vector of X_b associated objective values
    
    // Size of matrix A 
    let (m, n) = a.shape();

    // Create temparary vector x_b and setting 𝑛 − 𝑚 variables equal to zero
    // Generally we have C_n_{n-m} variants of vector 
    let mut vec_x: Vec<i32> = Vec::new();
    for _i in 0..n-m {
        vec_x.push(0);
    }
    for i in 0..m {
        vec_x.push(1);
    }

    let b_0 = a.columns(n-m, m);
    //println!("{}", b_0);

    let x_b0 = b_0.


}


extern crate nalgebra as na;

use na::{Vector6, Matrix4x6, Vector4};

fn main() {

    // A vector of coefficients of objective function - C
    let C 
        = Vector6::from_element((5, 4, 0, 0, 0, 0));

    // A matrix of coefficients of constraint function - A
    let A = Matrix4x6::new(
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


}

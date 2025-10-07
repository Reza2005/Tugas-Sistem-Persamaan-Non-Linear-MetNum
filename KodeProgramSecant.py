import numpy as np

# Muhamad Reswara Suryawan 21120123140126

def function_F(vec):
    """Mendefinisikan sistem persamaan f(x, y)."""
    x, y = vec
    f1 = x**2 + x * y - 10
    f2 = y + 3 * x * y**2 - 57
    return np.array([f1, f2])

def solve_with_broyden(initial_vec, tolerance=1e-6, max_iterations=100):
    """
    Menemukan solusi sistem persamaan non-linear menggunakan metode Broyden.
    """
    current_vec = np.array(initial_vec, dtype=float)
    x, y = current_vec

    J_approx = np.array([
        [2*x + y, x],
        [3*y**2, 1 + 6*x*y]
    ])
    
    F_vec = function_F(current_vec)

    print(f"{'Iterasi':<8} {'x':<15} {'y':<15} {'Perubahan x':<15} {'Perubahan y':<15}")
    print(f"{0:<8} {x:<15.6f} {y:<15.6f} {0.0:<15.6f} {0.0:<15.6f}")
    
    for i in range(1, max_iterations + 1):
        if np.linalg.det(J_approx) == 0:
            print("Error: Determinan Jacobian mendekati nol.")
            break

        delta_vec = np.linalg.solve(J_approx, -F_vec)
        current_vec += delta_vec
        
        change_x, change_y = abs(delta_vec)
        print(f"{i:<8} {current_vec[0]:<15.6f} {current_vec[1]:<15.6f} {change_x:<15.6f} {change_y:<15.6f}")

        if change_x < tolerance and change_y < tolerance:
            print("\nSolusi konvergen.")
            return current_vec

        F_new = function_F(current_vec)
        func_diff = F_new - F_vec
        
        numerator = np.outer(func_diff - J_approx @ delta_vec, delta_vec)
        denominator = np.dot(delta_vec, delta_vec)
        J_approx += numerator / denominator
        
        F_vec = F_new

    print("\nIterasi maksimum tercapai, solusi tidak konvergen.")
    return current_vec

if __name__ == "__main__":
    solve_with_broyden([1.5, 3.5])

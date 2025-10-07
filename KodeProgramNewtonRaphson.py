# Muhamad Reswara Suryawan 21120123140126

def solve_with_newton(initial_x, initial_y, tolerance=1e-6, max_iterations=100):
    """
    Menemukan solusi sistem persamaan non-linear menggunakan metode Newton-Raphson.
    f1(x, y) = x**2 + x*y - 10 = 0
    f2(x, y) = y + 3*x*y**2 - 57 = 0
    """
    x = initial_x
    y = initial_y

    print(f"{'Iterasi':<8} {'x':<15} {'y':<15} {'Perubahan x':<15} {'Perubahan y':<15}")
    print(f"{0:<8} {x:<15.6f} {y:<15.6f} {0.0:<15.6f} {0.0:<15.6f}")

    for i in range(1, max_iterations + 1):
        u = x**2 + x * y - 10
        v = y + 3 * x * y**2 - 57

        du_dx = 2 * x + y
        du_dy = x
        dv_dx = 3 * y**2
        dv_dy = 1 + 6 * x * y
        
        determinant = du_dx * dv_dy - du_dy * dv_dx
        if abs(determinant) < 1e-10:
            print("Error: Determinan Jacobian mendekati nol. Iterasi dihentikan.")
            break
            
        change_x = - (u * dv_dy - v * du_dy) / determinant
        change_y = (u * dv_dx - v * du_dx) / determinant
        
        x += change_x
        y += change_y
        
        print(f"{i:<8} {x:<15.6f} {y:<15.6f} {abs(change_x):<15.6f} {abs(change_y):<15.6f}")

        if abs(change_x) < tolerance and abs(change_y) < tolerance:
            print("\nSolusi konvergen.")
            return x, y
            
    print("\nIterasi maksimum tercapai, solusi tidak konvergen.")
    return x, y

if __name__ == "__main__":
    solve_with_newton(1.5, 3.5)

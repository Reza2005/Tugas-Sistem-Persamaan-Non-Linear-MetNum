import math

# Muhamad Reswara Suryawan 21120123140126

def g1(x, y):
    """Fungsi iterasi untuk x (g1B)"""
    return math.sqrt(10 - x * y)

def g2(x, y):
    """Fungsi iterasi untuk y (g2A)"""
    return 57 - 3 * x * y**2

def solve_with_jacobi(initial_x, initial_y, tolerance=1e-6, max_iterations=100):
    """
    Menemukan solusi sistem persamaan non-linear menggunakan metode Jacobi.
    """
    x = initial_x
    y = initial_y
    
    print(f"{'Iterasi':<8} {'x':<15} {'y':<15} {'Perubahan x':<15} {'Perubahan y':<15}")
    print(f"{0:<8} {x:<15.6f} {y:<15.6f} {0.0:<15.6f} {0.0:<15.6f}")

    for i in range(1, max_iterations + 1):
        try:
            prev_x, prev_y = x, y
            x = g1(prev_x, prev_y)
            y = g2(prev_x, prev_y)

            change_x = abs(x - prev_x)
            change_y = abs(y - prev_y)

            print(f"{i:<8} {x:<15.6f} {y:<15.6f} {change_x:<15.6f} {change_y:<15.6f}")

            if change_x < tolerance and change_y < tolerance:
                print("\nSolusi konvergen.")
                return x, y
        except ValueError:
            print("Error: Domain negatif pada akar kuadrat.")
            break
        except OverflowError:
            print("Error: Terjadi overflow numerik.")
            break

    print("\nIterasi maksimum tercapai atau error, solusi tidak konvergen.")
    return x, y


if __name__ == "__main__":
    solve_with_jacobi(1.5, 3.5)

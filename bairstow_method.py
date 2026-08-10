import cmath

def clean_root(z, tol=1e-8):
    # Convert complex to real if imaginary part ~ 0
    # Need this because otherwise, the roots will be printed as complex numbers even if they are real
    if isinstance(z, complex):
        if abs(z.imag) < tol:
            return round(z.real, 4)
        return complex(round(z.real, 4), round(z.imag, 4))
    return round(z, 4)


def bairstow(coeffs, r=0.0, s=0.0, tol=1e-6, max_iter=100):
    n = len(coeffs) - 1

    # Base case: linear
    if n == 1:
        root = -coeffs[0] / coeffs[1]
        root = clean_root(root)
        print(f"Root: {root}")
        return [root]

    # Base case: quadratic
    if n == 2:
        a, b, c = coeffs[2], coeffs[1], coeffs[0]
        D = cmath.sqrt(b*b - 4*a*c)
        r1 = (-b + D) / (2*a)
        r2 = (-b - D) / (2*a)

        r1, r2 = clean_root(r1), clean_root(r2)
        print(f"Roots: {r1}, {r2}")
        return [r1, r2]

    # Bairstow iteration
    for _ in range(max_iter):
        b = [0]*(n+1)
        c_arr = [0]*(n+1)

        b[n] = coeffs[n]
        b[n-1] = coeffs[n-1] + r*b[n]

        for i in range(n-2, -1, -1):
            b[i] = coeffs[i] + r*b[i+1] + s*b[i+2]

        c_arr[n] = b[n]
        c_arr[n-1] = b[n-1] + r*c_arr[n]

        for i in range(n-2, -1, -1):
            c_arr[i] = b[i] + r*c_arr[i+1] + s*c_arr[i+2]

        det = c_arr[2]*c_arr[2] - c_arr[3]*c_arr[1]
        if abs(det) < 1e-12:
            r += 1e-3
            s += 1e-3
            continue

        dr = (-b[1]*c_arr[2] + b[0]*c_arr[3]) / det
        ds = (-b[0]*c_arr[2] + b[1]*c_arr[1]) / det

        r += dr
        s += ds

        if abs(dr) < tol and abs(ds) < tol:
            break

    # Roots of quadratic
    D = cmath.sqrt(r*r + 4*s)
    root1 = (r + D) / 2
    root2 = (r - D) / 2

    root1, root2 = clean_root(root1), clean_root(root2)
    print(f"Roots: {root1}, {root2}")

    # Reduced polynomial
    new_coeffs = b[2:]
    print(f"Reduced polynomial: {[round(x,4) for x in new_coeffs][::-1]}")

    # Recursive call
    return [root1, root2] + bairstow(new_coeffs, r, s, tol, max_iter)
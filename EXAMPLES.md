# Sample Test Set
```
This file contains sample test cases for each algorithm in this repository.
```
---

## Gauss-Jordan Elimination

### Example 1

Solve:

```
x + 2y = 5
3x + 4y = 6
```

**Answer:**
x = -4
y = 9/2

---

### Example 2

Solve:

```
x + y + z = 6
2x - y + 2z = 3
x + 2y + 3z = 14
```

**Answer:**
x = 1/2
y = 3
z = 5/2

---

### Example 3

Solve:

```
2x + 3y - z = 5
4x + y + z = 11
-2x + 5y - 3z = -1
```

**Answer:**
x = 0
y = 4
z = 7

---

### Example 4

Solve:

```
x + 2y + z = 3
2x + 5y + 2z = 6
x + y + 3z = 4
```

**Answer:**
x = 5/2
y = 0
z = 1/2

---

## Gauss Elimination

### Example 1

Solve:

```
x + y = 5
2x - y = 3
```

**Answer:**
x = 8/3
y = 7/3

---

### Example 2

Solve:

```
3x + 2y - z = 1
2x - 2y + 4z = -2
-x + (1/2)y - z = 0
```

**Answer:**
x = 1
y = -2
z = -2

---

### Example 3

Solve:

```
2x + 3y + z = 1
4x + 13y + 7z = 3
-2x - 9y + 5z = 2
```

**Answer:**
x = 1/2
y = -1/8
z = 3/8

---

### Example 4

Solve:

```
x - y = 2
x + y = 4
```

**Answer:**
x = 3
y = 1

---

## LU Decomposition

### Example 1

```
A = [[2, -1, 1],
     [3, 3, 9],
     [4, 5, 2]]
```

**Answer:**

```
L = [[1, 0, 0],
     [3/2, 1, 0],
     [2, 14/9, 1]]

U = [[2, -1, 1],
     [0, 9/2, 15/2],
     [0, 0, -35/3]]
```

---

### Example 2

```
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 10]]
```

**Answer:**

```
L = [[1, 0, 0],
     [4, 1, 0],
     [7, 2, 1]]

U = [[1, 2, 3],
     [0, -3, -6],
     [0, 0, 1]]
```

---

## QR Decomposition

### Example 1

```
A = [[1, 1],
     [1, -1]]
```

**Answer:**

```
Q = (1/√2) * [[1, 1],
              [1, -1]]

R = [[√2, 0],
     [0, √2]]
```

---

## Bairstow’s Method

### Example 1

```
P(x) = x³ - 6x² + 11x - 6
```

**Answer:**
x = 1, 2, 3

---

### Example 2

```
P(x) = x³ - 4x² + 5x - 2
```

**Answer:**
x = 1 (double), x = 2

---

### Example 3

```
P(x) = x⁴ - 5x³ + 6x² + 4x - 8
```

**Answer:**
x = 2 (×3), x = -1

---

### Example 4

```
P(x) = x⁴ - 10x³ + 35x² - 50x + 24
```

**Answer:**
x = 1, 2, 3, 4

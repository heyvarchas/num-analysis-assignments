# 📊 Numerical Analysis Algorithms (Python)

This repository contains implementations of core **numerical methods** used in linear algebra and polynomial root finding. Each algorithm is implemented in a modular way and can be executed through a central driver file.

---

## 📁 Repository Structure

```text
NUM-ANALYSIS-ASSIGNMENTS/
│
├── bairstow_method.py        # Bairstow's Method for polynomial roots
├── gauss_elimination.py      # Gaussian Elimination
├── gauss_jordan.py           # Gauss-Jordan Elimination (RREF)
├── LU_decomposition.py       # LU Decomposition
├── QR_decomposition.py       # QR Decomposition
│
├── helpers.py                # Utility functions (input, formatting, printing)
├── main.py                   # Entry point to run algorithms
│
├── EXAMPLES.md               # Sample inputs & outputs for all methods
├── README.md                 # Project documentation
├── requirements.txt          # Dependencies (if any)
└── .gitignore
```

---

## ⚙️ Features

- 📐 Multiple numerical methods implemented from scratch  
- 🧩 Modular design (each algorithm in a separate file)  
- 🖥️ Interactive input support via terminal  
- 📋 Predefined examples for testing (`EXAMPLES.md`)  
- 🧰 Helper utilities for:
  - Matrix formatting  
  - Pretty printing  
  - User input handling  

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/heyvarchas/num-analysis-assignments.git
```

---

### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv .venv
```

---

### 3. Activate the Virtual Environment

- **Linux / Mac:**
```bash
source .venv/bin/activate
```

- **Windows (PowerShell):**
```bash
.venv\Scripts\Activate
```

---

### 4. Install Dependencies (if any)
```bash
pip install -r requirements.txt
```

> If `requirements.txt` is empty, you can skip this step.

---

### 5. Run the Program
```bash
python main.py
```

---

### 6. Deactivate Virtual Environment (Optional)
```bash
deactivate
```

---

### 💡 Notes on Virtual Environment
- Keeps dependencies isolated from your system Python  
- Ensures reproducibility across different machines  
- `.venv/` is ignored via `.gitignore`  

---

## 🧮 Implemented Algorithms

### 1. Gauss Elimination
- Solves systems of linear equations using forward elimination and back substitution.

### 2. Gauss-Jordan Elimination
- Converts an augmented matrix into **Reduced Row Echelon Form (RREF)**.

### 3. LU Decomposition
- Decomposes a matrix into:
  - Lower triangular matrix (L)
  - Upper triangular matrix (U)

### 4. QR Decomposition
- Factorizes a matrix into:
  - Orthogonal matrix (Q)
  - Upper triangular matrix (R)

### 5. Bairstow’s Method
- Finds roots of higher-degree polynomials (real & complex).

---

## 🧪 Examples / Test Cases

Refer to 👉 `EXAMPLES.md`

Contains:
- Sample inputs  
- Expected outputs  
- Step-style understanding for each method  

---

## 🛠️ Helper Utilities (`helpers.py`)

Includes reusable functions such as:
- Matrix input from user  
- Pretty-printing matrices  
- Formatting outputs  

---

## 🎯 Purpose

This repository is designed for:
- 📚 Students learning numerical analysis  
- 🧠 Understanding algorithmic implementation  
- 🧪 Practicing test cases and manual verification  

---

## 📌 Notes

- All implementations are written **from scratch** (no heavy external libraries)  
- Focus is on **clarity + educational value**  
- Works best with square matrices where applicable  

---

## 🤝 Contributing [Although it's a very simple repo]

Feel free to:
- Add new algorithms  
- Improve implementations  
- Enhance input/output handling  

---

## 📄 License

This project is open-source and free to use for educational purposes.
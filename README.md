# Password Checker Demo

An interactive password validation tool with multiple demos: Python CLI, automated tests, and a web interface.

## 🌐 Live Demo

**[Open the interactive demo →](https://tayyebh.github.io/password-checker)**

## Features

✅ Validates password length (8-20 characters)  
✅ Requires at least one uppercase letter  
✅ Requires at least one special character  
✅ Interactive web demo with real-time feedback  
✅ Automated test suite  
✅ Python CLI tool  

## Quick Start

### 1. Python CLI Demo

```bash
python password_checker.py
```

Then enter passwords to test:
- `abc` → too short
- `Abcdefgh` → needs special character
- `Abcdefgh!` → ✅ valid
- `ABCDEFGHIJKLMNOPQRSTUVWXYZ` → too long
- `abcdefgh` → needs uppercase

### 2. Automated Tests

```bash
python test_password_checker.py
```

Or with pytest:
```bash
pip install pytest
pytest test_password_checker.py -v
```

Runs 5 test cases automatically.

### 3. Web Demo

Open `index.html` in your browser, or visit the [live demo](https://tayyebh.github.io/password-checker) for an interactive password validator with real-time feedback.

## 📁 Files

- `password_checker.py` — Main validation logic (Python CLI)
- `test_password_checker.py` — Automated test suite
- `index.html` — Interactive web interface
- `README.md` — This file

## 🔐 Password Requirements

| Requirement | Details |
|---|---|
| **Length** | 8-20 characters |
| **Uppercase** | At least one A-Z |
| **Special Character** | At least one non-alphanumeric (!@#$%^&* etc.) |

## ✅ Example Valid Passwords

- `Secure@123`
- `MyPass!99`
- `P@ssw0rd`
- `Testing#1`
- `Demo$Pass2`

## ❌ Example Invalid Passwords

- `short` — too short
- `nouppercase!` — missing uppercase
- `NoSpecial123` — missing special character
- `TooLongPasswordWithNumbers123!` — too long (over 20 chars)
- `ABCDEFGHIJKLMNOPQRSTUVWXYZ` — too long

## How to Use GitHub Pages

This repo is set up with GitHub Pages. The web demo is automatically deployed at:

👉 **https://tayyebh.github.io/password-checker**

### Enable GitHub Pages (if needed)

1. Go to **Settings** → **Pages**
2. Select `main` branch as source
3. Save

Your site will be live in a few seconds!

---

**Created by:** Tayyebh  
**Type:** Interactive Demo  
**License:** MIT

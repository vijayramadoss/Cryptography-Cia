# Crypto CIA Project

This project demonstrates a simple implementation of the **CIA Triad in Cryptography**:

---

## Features

* Custom **encryption algorithm** using matrix spiral traversal
* **Decryption algorithm** to recover original text
* Lightweight **hash function** for integrity verification
* Simple CLI-based input/output

---

## How It Works

### 1. Encryption (`encrypt` function)

* Removes spaces from input text
* Arranges characters into a matrix (row-wise)
* Reads characters in a **spiral pattern (clockwise)**
* Produces encrypted text

This ensures **Confidentiality**

---

### 2. Hashing (`unique_hash` function)

* Starts with an initial value `h = 17`
* Iterates through each character:

  * Uses ASCII value (`ord(ch)`)
  * Applies bitwise XOR and shifting
  * Uses modulo to limit hash size
* Produces a numeric hash value

This ensures **Integrity** (detects changes in encrypted data)

---

### 3. Decryption (`decrypt` function)

* Reconstructs the matrix structure
* Fills it in the same spiral order used during encryption
* Reads row-wise to recover original text

This ensures **Availability**

---

## Usage

Run the script:

```bash
python crypto-cia.py
```

### Input:

```
Enter text: Vijay Ramadoss
Enter step size: 5
```

### Output:

```
Encrypted: ydssoRVijaama
Hash Value: 87571
Decrypted: VijayRamadoss

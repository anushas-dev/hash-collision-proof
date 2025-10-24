# Hash Collision Proof 🔐

> A demonstration of hash collisions in cryptographic hash functions

## 📖 Overview

In computer science, a **hash collision** (or **clash**) occurs when two different pieces of data in a hash table share the same hash value. The hash value is derived from a hash function which takes a data input and returns a fixed length of bits.

Although hash algorithms have been created with the intent of being collision resistant, they can still sometimes map different data to the same hash (by virtue of the [pigeonhole principle](https://en.wikipedia.org/wiki/Pigeonhole_principle)). Malicious users can take advantage of this to mimic, access, or alter data.

📚 **Learn more**: [Hash Collision on Wikipedia](https://en.wikipedia.org/wiki/Hash_collision)

---

## 🎯 Quick Example

**Hash Collision Proof** - Two strings producing the same hash value:

### Input
```
Enter 2 strings separated by space: hello world --- hello elloh
```

### String 1: "hello"

| Letter | Pos | Ord | Hash |
|--------|-----|-----|------|
| h      | 1   | 104 | 104  |
| e      | 2   | 101 | 306  |
| l      | 3   | 108 | 630  |
| l      | 1   | 108 | 738  |
| o      | 2   | 111 | 960  |

**Result**: `960 hello`

### String 2: "elloh"

| Letter | Pos | Ord | Hash |
|--------|-----|-----|------|
| e      | 1   | 101 | 101  |
| l      | 2   | 108 | 317  |
| l      | 3   | 108 | 641  |
| o      | 1   | 111 | 752  |
| h      | 2   | 104 | 960  |

**Result**: `960 elloh`

### ✅ Collision Detected!
**Both strings have the same hash value: `960`**

---

## 🔬 How The Hash Algorithm Works

### 1. Hash Function Definition

The hash function `H(S)` from the Python script calculates the hash value as follows:

```python
def hash_function(s):
    hv = 0
    pos = 0
    
    for c in s:
        pos = (pos % 3) + 1  # Repeating multiplier sequence: 1, 2, 3, 1, 2, 3...
        hv = (hv + (pos * ord(c))) % 1000000
    
    return hv
```

### 2. Step-by-Step Process

**Initialize**: `hv = 0` and `pos = 0`

**For each character `c` in the string `S`**:

1. **Update position**: `pos = (pos % 3) + 1`  
   This creates a repeating multiplier sequence: 1, 2, 3, 1, 2, 3...

2. **Update hash value**: `hv = (hv + (pos * ord(c))) % 1000000`  
   Where `ord(c)` is the ASCII value of the character

3. **Mathematical representation**:  
   `H(S) = ( (1 * ord(c₁)) + (2 * ord(c₂)) + (3 * ord(c₃)) + ... ) % 1000000`

---

## 📊 Detailed Calculation Examples

### Example 1: "hello"

We apply the algorithm to the string **"hello"**, using the ASCII values for each character:

```
h = 104
e = 101  
l = 108
l = 108
o = 111
```

#### Step-by-step:

```python
H("hello") = ( (1 * 104) + (2 * 101) + (3 * 108) + (1 * 108) + (2 * 111) ) % 1000000
           = ( 104 + 202 + 324 + 108 + 222 ) % 1000000
           = 960 % 1000000
           = 960
```

✅ **H("hello") = 960**

This calculation matches the table in the README.md.

---

### Example 2: "elloh"

Next, we apply the exact same algorithm to the string **"elloh"**:

```
e = 101
l = 108
l = 108  
o = 111
h = 104
```

#### Step-by-step:

```python
H("elloh") = ( (1 * 101) + (2 * 108) + (3 * 108) + (1 * 111) + (2 * 104) ) % 1000000  
           = ( 101 + 216 + 324 + 111 + 208 ) % 1000000
           = 960 % 1000000  
           = 960
```

✅ **H("elloh") = 960**

This calculation also matches the table in the README.md.

---

## 🎉 Conclusion

### Mathematical Proof

We have mathematically demonstrated that:

- **The input strings are different**: `"hello" ≠ "elloh"`
- **Their hash values are identical**: `H("hello") = H("elloh") = 960`
- **Therefore, a hash collision exists**: ✅

### Key Takeaways

- Hash collisions occur when different inputs produce the same hash output
- The pigeonhole principle guarantees collisions exist for any hash function
- Understanding collisions is crucial for cryptography and data integrity
- Real-world hash functions (like SHA-256) are designed to make collisions computationally infeasible

---

## 🚀 Usage

### Run the Script

```bash
python hash-collision.py
```

### Input Format

```
Enter 2 strings separated by space: string1 string2
```

### Example Output

```
Hash for 'hello': 960
Hash for 'elloh': 960
✅ COLLISION DETECTED!
```

---

## 🛠️ Technologies

- **Language**: Python 3.x
- **Dependencies**: None (uses only standard library)

---

## 🤝 Contributing

Contributions are welcome! This project is tagged for **Hacktoberfest 2025**.

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-hash-function`)
3. Commit your changes (`git commit -m 'Add new hash function example'`)
4. Push to the branch (`git push origin feature/new-hash-function`)
5. Open a Pull Request

---

## 📝 License

This project is open source and available for educational purposes.

---

## 📚 Further Reading

- [Hash Functions (Wikipedia)](https://en.wikipedia.org/wiki/Hash_function)
- [Cryptographic Hash Functions](https://en.wikipedia.org/wiki/Cryptographic_hash_function)
- [Birthday Attack](https://en.wikipedia.org/wiki/Birthday_attack)
- [SHA-256](https://en.wikipedia.org/wiki/SHA-2)

---

**Made with ❤️ for learning and demonstration purposes**
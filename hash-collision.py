def hash_value(s):
    hv = 0
    pos = 0
    for c in s:
        pos = (pos % 3) + 1
        hv = (hv + (pos * ord(c))) % 1000000
    return hv


if __name__ == "__main__":
    parts = input("Enter 2 strings separated by space: ").split()
    if len(parts) != 2:
        print("Please enter exactly 2 strings separated by a space")
    else:
        str1, str2 = parts
        if len(str1) < 3 or len(str2) < 3:
            print("Please enter strings of length greater than 2")
        elif str1 == str2:
            print("Please enter 2 distinct strings")
        else:
            hv1 = hash_value(str1)
            hv2 = hash_value(str2)
            print(f"Hash for '{str1}': {hv1}")
            print(f"Hash for '{str2}': {hv2}")
            if hv1 == hv2:
                print("✅ COLLISION DETECTED!")
            else:
                print(f"No collision. Hashes are different: {hv1} and {hv2}")


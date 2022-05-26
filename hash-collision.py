str1, str2 = input("Enter 2 strings seperated by space, ex: hello world --- ").split(" ")
def hash_value(str):
    hv = 0
    pos = 0
    for c in str:
        pos = ( pos % 3 ) + 1
        hv = (hv + (pos * ord(c))) % 1000000
        print(c,pos,ord(c),hv)   
    print(hv,str)
    return hv
if len(str1) < 3 or len (str2) < 3: 
    print("Please enter strings of length greater than 2")
else: 
    if str1==str2:
        print("Please enter 2 distinct strings")
    else: 
        hv1=hash_value(str1)
        hv2=hash_value(str2)
        if(hv1==hv2):
            print("Strings have same hash value.")
        else:
            print(f"Hashes are different, {hv1} and {hv2}")


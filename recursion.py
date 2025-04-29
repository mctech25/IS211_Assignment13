def fibonacci(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def compareTo(s1, s2):
    if not s1 and not s2:
        return 0
    if not s1:
        return -ord(s2[0])
    if not s2:
        return ord(s1[0])
    if s1[0] != s2[0]:
        return ord(s1[0]) - ord(s2[0])
    return compareTo(s1[1:], s2[1:])

def test_functions():
    # Test fibonacci
    print("Testing fibonacci:")
    for i in range(10):
        print(f"fibonacci({i}) = {fibonacci(i)}")
    
    # Test GCD
    print("\nTesting GCD:")
    print(f"gcd(48, 18) = {gcd(48, 18)}")
    print(f"gcd(54, 24) = {gcd(54, 24)}")
    
    # Test compareTo
    print("\nTesting compareTo:")
    print(f"compareTo('hello', 'hello') = {compareTo('hello', 'hello')}")
    print(f"compareTo('hello', 'world') = {compareTo('hello', 'world')}")
    print(f"compareTo('world', 'hello') = {compareTo('world', 'hello')}")

if __name__ == "__main__":
    test_functions()


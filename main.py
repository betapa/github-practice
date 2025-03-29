from typing import Union, Optional

def add(a: Union[int, float], b: Union[int, float]) -> Optional [Union[int, float]]:
    try:
        result = a + b
    except Exception as e:
        print(e)
        return None

    return result

if __name__ == "__main__":
    print(add(1, 2))  # Output: 3
    print(add(1.5, 2.5))  # Output: 4.0
    print(add(1, 2.5))  # Output: 3.5
    print(add(1.5, 2))  # Output: 3.5

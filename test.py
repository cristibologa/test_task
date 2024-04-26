def test(*args):
    character_counts = {}
    for arg in args:
        for char in arg:
            if char in character_counts:
                character_counts[char] += 1
            else:
                character_counts[char] = 1
    print(character_counts)


test('hello', 'world')

# Exemplu: task_18('hello', 'world') ➞ {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

import math
def unique_hash(text):
    h = 17
    for i, ch in enumerate(text):
        h = h ^ ((ord(ch) << (i % 5)) + (i * 31))
        h = (h * 7) % 100000
    return h
def encrypt(text, cols):
    text = text.replace(" ", "")
    rows = math.ceil(len(text) / cols)
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    k = 0
    for i in range(rows):
        for j in range(cols):
            if k < len(text):
                matrix[i][j] = text[k]
                k += 1
    result = ""
    top, bottom = 0, rows - 1
    left, right = 0, cols - 1
    while top <= bottom and left <= right:
        for i in range(top, bottom + 1):
            if matrix[i][right]:
                result += matrix[i][right]
        right -= 1
        for i in range(right, left - 1, -1):
            if top <= bottom and matrix[bottom][i]:
                result += matrix[bottom][i]
        bottom -= 1
        for i in range(bottom, top - 1, -1):
            if left <= right and matrix[i][left]:
                result += matrix[i][left]
        left += 1
        for i in range(left, right + 1):
            if top <= bottom and matrix[top][i]:
                result += matrix[top][i]
        top += 1
    return result
def decrypt(cipher, cols):
    rows = math.ceil(len(cipher) / cols)
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    k = 0
    for i in range(rows):
        for j in range(cols):
            if k < len(cipher):
                matrix[i][j] = '*'
                k += 1
    top, bottom = 0, rows - 1
    left, right = 0, cols - 1
    k = 0
    while top <= bottom and left <= right:
        for i in range(top, bottom + 1):
            if matrix[i][right] == '*' and k < len(cipher):
                matrix[i][right] = cipher[k]
                k += 1
        right -= 1
        for i in range(right, left - 1, -1):
            if top <= bottom and matrix[bottom][i] == '*' and k < len(cipher):
                matrix[bottom][i] = cipher[k]
                k += 1
        bottom -= 1
        for i in range(bottom, top - 1, -1):
            if left <= right and matrix[i][left] == '*' and k < len(cipher):
                matrix[i][left] = cipher[k]
                k += 1
        left += 1
        for i in range(left, right + 1):
            if top <= bottom and matrix[top][i] == '*' and k < len(cipher):
                matrix[top][i] = cipher[k]
                k += 1
        top += 1
    text = ""
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != '':
                text += matrix[i][j]
    return text
if __name__ == "__main__":
    text = input("Enter text: ")
    cols = int(input("Enter step size: "))
    cipher = encrypt(text, cols)
    print("\nEncrypted:", cipher)
    h = unique_hash(cipher)
    print("Hash Value:", h)
    decrypted = decrypt(cipher, cols)
    print("Decrypted:", decrypted)
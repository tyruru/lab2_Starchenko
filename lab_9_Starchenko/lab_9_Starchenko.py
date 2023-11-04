# def encrypt_message(message, shift):
#     encrypted_message = ""
#     for char in message:
#         if char.isalpha():
#             ascii_offset = ord('A') if char.isupper() else ord('a')
#             # Знаходимо позицію літери в алфавіті і застосовуємо зсув
#             shifted_char = chr(((ord(char) - ascii_offset + shift) % 26) + ascii_offset)
#             encrypted_message += shifted_char
#         else:
#             encrypted_message += char
#     return encrypted_message

# message = "Hello, World!"
# shift = 3

# encrypted_message = encrypt_message(message, shift)

# print("Зашифроване повідомлення:", encrypted_message)

# print('smith' > 'Smith')
# print('Smith' < 'Smith')
# print('Smith' > '1000')
# print('11' < '8')

# s1 = 'Where are the snows of yesteryear?'
# s2 = s1.split()
# s3 = sorted(s2)
# print(s3[1])

# s1 = '12.8'
# i = int(s1)
# s2 = str(i)
# f = float(s2)
# print(s1 == s2)
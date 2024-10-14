import socket

# Bigram substitution cipher key
BIGRAM_KEY = {
    'AB': 'XY', 'CD': 'YZ', 'EF': 'ZA', 'GH': 'BC',
    'IJ': 'DE', 'KL': 'FG', 'MN': 'HI', 'OP': 'JK',
    'QR': 'LM', 'ST': 'NO', 'UV': 'PQ', 'WX': 'RS'
}

def reverse_bigram_key():
    return {v: k for k, v in BIGRAM_KEY.items()}

# Decryption process step by step
def decrypt_bigram(ciphertext):
    reverse_key = reverse_bigram_key()
    print(f"Decryption Key Map: {reverse_key}")  # Show the decryption key map

    plaintext = ''
    for i in range(0, len(ciphertext), 2):
        bigram = ciphertext[i:i+2]
        print(f"Decrypting Bigram: {bigram}")  # Show each bigram being decrypted
        plaintext += reverse_key.get(bigram, bigram)
        print(f"Current Decrypted Text: {plaintext}")  # Show the partially decrypted text

    return plaintext

# Encryption process
def encrypt_bigram(plaintext):
    if len(plaintext) % 2 != 0:
        plaintext += 'X'  # Padding character
    ciphertext = ''
    for i in range(0, len(plaintext), 2):
        bigram = plaintext[i:i+2]
        ciphertext += BIGRAM_KEY.get(bigram, bigram)
    return ciphertext

# Set up the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 65432))  # Use 0.0.0.0 to listen on all interfaces
server_socket.listen()

print("Server is listening for connections...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    encrypted_message = conn.recv(1024).decode()
    if not encrypted_message:
        break

    print(f"Encrypted Message Received: {encrypted_message}")  # Show encrypted message received

    # Show decryption process step by step
    decrypted_message = decrypt_bigram(encrypted_message)
    print(f"Final Decrypted Message: {decrypted_message}")  # Show final decrypted message

    message = input("Enter message to send: ")
    encrypted_message = encrypt_bigram(message)
    print(f"Encrypted Message to Send: {encrypted_message}")  # Show the message before sending
    conn.sendall(encrypted_message.encode())

conn.close()

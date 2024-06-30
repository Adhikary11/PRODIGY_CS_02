from PIL import Image
import numpy as np

def encrypt_image(image_path, key, operation):
    image = Image.open(image_path)
    pixel_array = np.array(image)
    
    if operation == "swap":
        np.random.seed(key)
        indices = np.arange(pixel_array.size)
        np.random.shuffle(indices)
        flat_array = pixel_array.flatten()
        encrypted_array = flat_array[indices]
        encrypted_array = encrypted_array.reshape(pixel_array.shape)
    elif operation == "math":
        encrypted_array = (pixel_array + key) % 256
    else:
        raise ValueError("Unsupported operation")

    encrypted_image = Image.fromarray(encrypted_array.astype(np.uint8))
    return encrypted_image

def decrypt_image(image_path, key, operation):
    image = Image.open(image_path)
    pixel_array = np.array(image)
    
    if operation == "swap":
        np.random.seed(key)
        indices = np.arange(pixel_array.size)
        np.random.shuffle(indices)
        flat_array = pixel_array.flatten()
        decrypted_array = np.zeros_like(flat_array)
        decrypted_array[indices] = flat_array
        decrypted_array = decrypted_array.reshape(pixel_array.shape)
    elif operation == "math":
        decrypted_array = (pixel_array - key) % 256
    else:
        raise ValueError("Unsupported operation")

    decrypted_image = Image.fromarray(decrypted_array.astype(np.uint8))
    return decrypted_image

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt an image? (e/d): ").lower()
        if choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
            continue

        image_path = input("Enter the image file path: ")
        try:
            key = int(input("Enter the key (integer): "))
        except ValueError:
            print("Key must be an integer. Please try again.")
            continue

        operation = input("Enter the operation (swap/math): ").lower()
        if operation not in ['swap', 'math']:
            print("Invalid operation. Please enter 'swap' or 'math'.")
            continue

        if choice == 'e':
            encrypted_image = encrypt_image(image_path, key, operation)
            encrypted_image.save("encrypted_image.png")
            print("Image encrypted and saved as 'encrypted_image.png'.")
        else:
            decrypted_image = decrypt_image(image_path, key, operation)
            decrypted_image.save("decrypted_image.png")
            print("Image decrypted and saved as 'decrypted_image.png'.")

        repeat = input("Do you want to perform another operation? (yes/no): ").lower()
        if repeat != 'yes':
            break

if __name__ == "__main__":
    main()

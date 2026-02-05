COPAMY: CODTECH IT SOLUTIONS

NAME: PADMAKAR SUBHASH MORALE

INTERN ID: CTIS1717

DOMAIN: CYBER SECURITY & ETHICAL HACKING

DURATION: 6 WEEKS

MENTOR: NEELA SANTOSH

Advanced Encryption Tool


### **Advanced Encryption Tool (AET) - A Simple and Secure Way to Protect Your Files**

In today’s digital world, keeping sensitive information safe is more important than ever. Whether it's personal data, financial records, or important work documents, encrypting files is one of the most effective ways to ensure privacy. The **Advanced Encryption Tool (AET)** you've shared is a user-friendly software that helps you easily encrypt and decrypt files using strong encryption techniques. This tool is designed to make the process of protecting your data both simple and secure.

#### **What Does the Tool Do?**

The AET provides an easy-to-use graphical interface, built with **Tkinter**, where users can select a file, enter a password, and either encrypt or decrypt the file with just a few clicks. The encryption process uses **AES-256 (Advanced Encryption Standard)**, one of the most secure encryption algorithms available today, making your data incredibly difficult for anyone to access without the correct password.

Let’s break down how the tool works, the technologies it uses, and how it ensures your data stays safe.

### **How the Tool Works**

#### **1. User-Friendly Interface**

The tool is designed with ease-of-use in mind, so you don't need to be a cryptography expert to use it. Here's what you see when you launch the application:

* **File Selection**: You can browse your system to select the file you want to encrypt or decrypt.
* **Password Entry**: You type in a password that will be used to generate a secure encryption key.
* **Encrypt/Decrypt**: Once you have selected the file and entered your password, you can click the 'Encrypt' or 'Decrypt' button to perform the desired operation.

The application takes care of everything behind the scenes to ensure your data remains safe.

#### **2. Secure Key Generation**

Encryption is all about using a secret key to turn your data into unreadable text (ciphertext) and back again. To ensure your key is strong and unique, the tool generates it from the password you enter using a method called **PBKDF2** (Password-Based Key Derivation Function 2). Here’s how it works:

* **Salt**: A unique random value called a salt is generated each time you encrypt something. This salt is combined with your password to create a key. The salt ensures that even if you use the same password for multiple files, the encrypted results will be different each time.
* **Key Derivation**: The PBKDF2 function takes your password and the salt, then processes it multiple times to create a strong encryption key. This method makes it very difficult for attackers to guess your password, even if they know the salt.

This process makes sure that your encryption key is both secure and difficult to guess, even if someone knows your password.

#### **3. AES Encryption and CBC Mode**

AES (Advanced Encryption Standard) is one of the most trusted encryption algorithms. It’s widely used in everything from securing websites (via HTTPS) to protecting sensitive data in government systems. The tool uses **AES-256**, which is considered very secure and is commonly used in professional environments.

* **AES in CBC Mode**: The tool uses **CBC (Cipher Block Chaining)** mode, which improves security by ensuring that even identical files encrypted with the same key will result in different ciphertext. This is done by XORing each block of plaintext with the previous ciphertext block before encryption.

  Additionally, **a random Initialization Vector (IV)** is generated for each encryption. This ensures that the same file, encrypted twice with the same key, will have different encrypted outputs each time.

* **Padding**: AES works on fixed-size blocks of data. If your file doesn’t match the required size, the tool adds padding to make it fit. This ensures the encryption works correctly without altering the original file content.

#### **4. Decryption**

Decryption is simply the reverse of encryption. To decrypt a file:

* **Extracting the Salt and IV**: The salt and IV used during encryption are stored in the encrypted file. When you want to decrypt it, the tool reads these values to regenerate the key and decrypt the file.

* **Key Regeneration**: The password you provide is combined with the extracted salt to regenerate the exact encryption key used to encrypt the file in the first place. Using this key and the IV, the tool can successfully decrypt the file back to its original form.

#### **5. File Handling and Security**

Throughout the process, the tool makes sure that:

* **The original file stays intact**: Only the encrypted version is modified, leaving the original file unchanged.
* **Encrypted files are saved with a `.enc` extension** so that you can easily identify them.
* **Error Handling**: If anything goes wrong during encryption or decryption (like if the password is wrong or the file can’t be accessed), the tool will notify you with an error message so you can take appropriate action.

### **Libraries and Technologies Behind the Tool**

The **Advanced Encryption Tool** uses a combination of powerful libraries and technologies to ensure your files are securely encrypted and decrypted. Here's a quick look at some of the core components:

1. **PyCryptodome**: This is the backbone of the encryption operations. It provides secure cryptographic primitives like AES encryption, key derivation, and padding. PyCryptodome is a fork of the **PyCrypto** library and is used for implementing the actual encryption and decryption processes.

   * **AES**: For the encryption and decryption operations.
   * **PBKDF2**: For securely generating keys from your password.
   * **Padding and Unpadding**: For handling data that doesn’t fit exactly into AES's required block size.

2. **Tkinter**: This is the graphical user interface (GUI) library used to build the application. Tkinter makes it easy to create windows, buttons, text fields, and file dialogs, allowing users to interact with the encryption tool without needing to write any code.

3. **File Handling**: The tool uses standard file operations in Python to read from and write to the disk. It handles file opening, reading, and writing securely to make sure encrypted files are stored safely.

### **Why This Tool is Secure**

* **AES-256 Encryption**: The AES-256 algorithm is one of the strongest encryption standards available today. It’s used by governments, banks, and corporations to protect sensitive information.
* **PBKDF2 Key Derivation**: By using PBKDF2 with a random salt, the tool ensures that even if someone tries to guess your password, they won’t be able to use simple brute force methods to crack the encryption.
* **Random IVs and Salts**: Every encryption operation uses a different salt and IV, which means even if two identical files are encrypted with the same password, they will look completely different when encrypted.
* **Secure Decryption**: The decryption process is equally secure, ensuring that only the correct password can decrypt the file back to its original state.

### **Conclusion**

The **Advanced Encryption Tool (AET)** is a powerful and secure solution for anyone looking to protect their files. Whether you’re a casual user who just wants to keep some personal files safe or a more advanced user dealing with sensitive information, this tool makes encryption accessible and straightforward.

With its strong use of **AES-256** encryption, **PBKDF2** key derivation, and random salt and IV generation, it ensures that your data stays private and protected. Plus, the easy-to-use graphical interface makes encryption and decryption as simple as clicking a button.

In a world where data security is more important than ever, this tool provides a simple yet effective way to keep your information safe from prying eyes.

OUTPUT
<img width="1536" height="739" alt="Image" src="https://github.com/user-attachments/assets/97dacf3c-bb07-493a-93a0-a2bb60171edd" />

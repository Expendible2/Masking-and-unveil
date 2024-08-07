# Masking-and-unveil
## Overview

The MP-08 Message Encoder and Decoder is a simple graphical user interface (GUI) application built using Python and Tkinter. It allows users to encrypt and decrypt messages using a base64 encoding scheme, providing a straightforward way to secure and access sensitive text data.

## Features

- **Encryption**: Secure your messages by encoding them into base64 format. Simply enter your text and a secret key to encrypt your message.
- **Decryption**: Decode previously encrypted messages back to their original form using the correct secret key.
- **User-Friendly Interface**: Intuitive design with easy-to-use buttons and input fields for a seamless user experience.
- **Reset Functionality**: Clear the input fields with a single click to quickly start a new encryption or decryption task.

## Requirements

- Python 3.x
- Tkinter (usually included with Python installations)


## Usage

1. **Enter your message** in the text box labeled "Enter text for encryption and decryption".
2. **Input your secret key** in the designated entry field. The default key is "1234".
3. **Choose your action**:
   - Click on **ENCRYPT** to encode your message.
   - Click on **DECRYPT** to decode an encrypted message.
   - Use the **RESET** button to clear the input fields.
4. **View Results**:
   - The encrypted or decrypted message will appear in a new window.
   - Ensure that the correct secret key is used for successful decryption.

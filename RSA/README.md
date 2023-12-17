# RSA Encryption Decryption Algorithm

This repository contains a simple implementation of the RSA encryption algorithm
with only one pair of keys. The code in this repository attempts to demonstrate 
data intake and display resultant cipher text and resultant decrpted data.

## Files

- euclid.py: Programs to pick prime numbers
- keygen.py: Programs to generate keys, encrpy and decrypt
- main.py: Program to fetch input, display cipher text and decrypted text

## What is Asymmetric Encryption

Asymmetric Encryption is a type of encryption where to different keys are used to encrypt and decrypt data. One key is public and can be shared by everyone while the other is private and must be kept secret.

The public key is used to encrypt the data pretrasit and the private decypts when the data is received.

## How it works

Say we have Jake and Missy. Missy wants to send a message "Top Club Arsenal" to Jake. Missy would use Jake's public key to encrypt the message to cipher text and Jake would receive the cipher text and decrypt the message using his private key to "Top Club Arsenal"

## KeyGeneration

- Pick two large prime numbers p = 2 and q = 7
- Compute
  - n = p * q = 14
  - z = (p - 1)(q - 1) = 6/*Euler's Totient*/
- We need to evaluate e (encryption no.) and d (decryption no.) such that (e*d) mod z == 1
- Choose a random number e where 1 < e < z/*e < 6: 2, 3, 4, 5*/
  - e must be co-prime to both z = 6 and n = 14
  - e == 5
- Select a number d such that (e * d) mod z == 1
  - The easiest way would be to go through multiples of e == 5 and compute till you find a remainder of 1
  - Cycling from multiples 5, 10, 15 ... 100: e * d == 55 and e * d == 85 suffice so we could pick d == 11
  - d == 11
- Public Key is  (e, n) = (5, 14)
- Private Key is (d, n) = (11, 14)
  
- Encryption:

```

To encrypt
cipher text = pow(actual text, public_key[0]) % public_key[1]
 - say actual_text = 2
 - cipher text = 4 = (2 ** 5) % 14
To decrypt
actual text = pow(cipher text, private_key[0]) % private_key[1]
 - cipher text = 4
 - actual text = 299593.14285714284 = (4 ** 11) % 14
 - focus only on decimal part: .14285714284 * 14 = 2

```

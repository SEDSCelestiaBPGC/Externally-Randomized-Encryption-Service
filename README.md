# Externally-Randomized-Encryption-Service

## Introduction
Cryptography (synonymous to encryption) is the practice or study of techniques for secure communication in the presence of third parties (adversaries). It is very important and necessary, especially in the modern age, for people prefer interactions (both individual and collective) to be as secure and private as possible. If the interaction is of national level, it can be a matter of national safety as well.Encryption is the process of converting the message to be sent (plaintext) to the coded message (ciphertext) using a certain tool (key). One of the modern day encryptions is Vernam cipher, where the key is the letters or characters themselves, and are added in a special way to the plaintext to get ciphertext. It is one of the only few encryption methods considered unbreakable.

## What we wish to do and How
We aim to create an encryption algorithm that depends on randomness naturally found as a source of the key. We shall be doing this in two phases:
### Key generation:
We shall be using one of the following methods to generate a binary sequence:
#### White Noise Analysis: 
Random sounds are recorded, and frequency is divided into those above and below a threshold frequency, so as to assign binary values.
#### Position of Stones in Rice: 
A few stones are placed along with rice and shaken. The position of the stones are noted with respect to a grid
#### Photograph database: 
A photograph is taken (mainly colourful) and a certain characteristic of it is taken (such as average colour). In this case, photograph is divided into grids, and the average colour value of each grid square is taken.

To improve the hence obtained random number sequence, we shall use Genetic Algorithms (with Shannon’s entropy as filter function). In this, we allow the sequence to evolve for a certain number of generations along with mutations (which are random). Shannon’s entropy is used as a ‘marker’ for the‘fitness’ of the final generation.
### Encryption
To encrypt the plaintext, we shall use Vernam cipher (or a modification of it).

To code the encryption and the generating key, we will make use of Python and its various libraries, and code in Google Colab. A basic understanding and knowledge of the above mentioned terms and Python is considered necessary for this project.
## What we wish to achieve: 
After encryption, we shall be comparing it with similar or other existing encryption processes, to see which fares better. Several tests such as randomness of key, length of the key, efficiency, time taken for adversaries to hack are employed.

# AES-Advanced-Encryption-Standard
AES ALGORITHM PROCEDURE:
KEY EXPANSION:
AES begins by expanding a user-provided encryption key.
This key expansion process generates a series of round keys, which are used in each round of encryption.
INITIAL ROUND (ADDROUNDKEY):
The 128-bit plaintext block is XORed with the first round key.
This step initializes the data.
ROUND FUNCTION (10/12/14 ROUNDS):
AES operates with a varying number of rounds (10/12/14 rounds for 128/192/256-bit keys).
In each round, the data block undergoes several transformations:
SUBBYTES: Each byte is substituted using a predefined S-box.
SHIFTROWS: Bytes within rows are shifted to provide diffusion.
MIXCOLUMNS (EXCEPT IN THE FINAL ROUND): Columns are mixed to introduce further diffusion.
ADDROUNDKEY: The data is XORed with the round key.
FINAL ROUND:
The last round is similar to earlier rounds but omits the MixColumns step.
CIPHERTEXT:
After the final round, the result is the ciphertext, representing the encrypted data.

ROUND FUNCTION:
SUBBYTES (SUBSTITUTION LAYER):In this transformation, each byte in the 128-bit data block is replaced with a corresponding byte from a predefined S-box (Substitution Box).
The S-box provides a nonlinear substitution that enhances security and introduces confusion.
This step ensures that similar plaintext bytes do not produce similar ciphertext bytes.
MULTIPLICATIVE INVERSE:
To find the SubBytes output for a byte in the data block, the multiplicative inverse of that byte in the finite field is determined.
This involves finding a value that, when multiplied by the original byte, yields a result of 1 in the finite field.
MATRIX MULTIPLICATION:
The multiplicative inverse found in the previous step is multiplied by the constant matrix 0x8A.
Both the inverse byte and the matrix are represented in binary form.
The binary multiplication is performed, resulting in a new binary value.
XOR WITH CONSTANT (0X63):
The binary result obtained in the previous step is XORed with a fixed constant 0x63, which is predefined in the AES algorithm.
RESULT OF SUBBYTES:
The output obtained after the XOR operation is the result of the SubBytes transformation for the original byte.
SHIFTROWS (PERMUTATION LAYER):
The ShiftRows step rearranges the bytes within each row of the 4x4 data block.
Bytes in the first row remain unchanged.
Bytes in the second row are shifted one position to the left.
Bytes in the third row are shifted two positions to the left.
Bytes in the fourth row are shifted three positions to the left.
This permutation adds diffusion by spreading data across rows.
MIXCOLUMNS (PERMUTATION LAYER, EXCEPT IN THE FINAL ROUND):
MixColumns operates on the columns of the 4x4 data block.
The output of the ShiftRows transformation is multiplied by the following constant matrix:
02 03 01 01
01 02 03 01
01 01 02 03
03 01 01 02
Each column is treated as a polynomial, and matrix multiplication in a finite field is performed.
This operation provides further diffusion and ensures that changes in one byte affect multiple bytes in the column.
In the final round, MixColumns is omitted to simplify decryption.
MATRIX MULTIPLICATION IN FINITE FIELD:
For MixColumns, each column of the 4x4 data block is treated as a polynomial in the finite field of GF(x^8) with the polynomial representation x^8 + x^3 + x^2 + x + 1.
The elements in the matrix to be multiplied (e.g., 02 * 87) are first converted to binary representation. For example, 02 becomes 0010 in binary, and 87 becomes 10000111.
Binary multiplication is performed on these two binary numbers, which results in a new binary value.
CONVERSION TO POLYNOMIAL:
The binary result from the multiplication is then converted back into a polynomial in the finite field.
POLYDIVISION FOR GF(X^8):
The polynomial obtained in the previous step is subjected to polynomial division within the finite field GF(x^8).
This division process continues until the remainder's power is less than that of the divisor (x^8 + x^3 + x^2 + x + 1).
CONVERSION TO DECIMAL:
The divisor polynomial (once the remainder power is less than the divisor) is converted into binary and then into decimal.
Each group of four binary digits represents a decimal value.
OUTPUT OF MIXED COLUMN:
The decimal value obtained in the previous step is the output of the MixColumns transformation for the given column in the data block.
ADDROUNDKEY (KEY MIXING LAYER):
In this step, the round key for the current round is XORed with the data block.
Each byte of the data block is combined with the corresponding byte from the round key.
This step adds the round-specific key material to the data, making it unique for each round.
FINAL ROUND (SIMILAR TO EARLIER ROUNDS WITHOUT MIXCOLUMNS):
The final round is similar to the earlier rounds but omits the MixColumns step.
It consists of SubBytes, ShiftRows, and AddRoundKey operations.
The absence of MixColumns simplifies decryption.

AES KEY GENERATION:
INITIAL KEY DIVISION:
The 128-bit encryption key is divided into 4 words, each consisting of 32 bits (e.g., w0, w1, w2, w3).
Word Generation (w4, w5, etc.):
To find the next series of words, follow these steps words (e.g., w4, w8,):
FOR WORDS MULTIPLE OF 4 (E.G., W4, W8, W12):
Calculate t(i) as follows:
Start with the word w(i-3).
Perform a ROTWORD operation (a left circular shift) on it.
Apply a SubBytes transformation to the result.
XOR the SubBytes result with predefined RCon constants based on the round number.
Example of t(i) calculation for w4
t4 = SubBytes(ROTWORD(w1)) XOR RCon[round_number]
RCon Constants:
RCon constants are predefined values used in the key generation process. They depend on the round number and are represented in hexadecimal format.
Example RCon constants for AES Round 1 to 10
RCon = [  "01", "02", "04", "08", "10", "20", "40", "80", "1B", "36" ]
FOR OTHER WORDS (E.G., W5, W6, W7, W9, W10, W11, ETC.):
Calculate w(i) as the XOR of w(i-1) and w(i-4).
Example of w5 calculation
w5 = w4 XOR w1


OUTPUT:

![aes_algorithm1](https://github.com/Neeraja-Kallamadi/AES-Advanced-Encryption-Standard-/assets/110168775/03dd028c-c29c-418f-85bf-db563513cb59)

![aes_algorithm2](https://github.com/Neeraja-Kallamadi/AES-Advanced-Encryption-Standard-/assets/110168775/5956dd93-cc99-4c28-b72d-b3bdb436c709)

![aes_algorithm3](https://github.com/Neeraja-Kallamadi/AES-Advanced-Encryption-Standard-/assets/110168775/9aec7994-da0b-4fdb-8439-1e5650147158)

![aes_algorithm4](https://github.com/Neeraja-Kallamadi/AES-Advanced-Encryption-Standard-/assets/110168775/f14cc95f-aee4-424c-8b47-f70c08b77d5c)

![aes_algorithm5](https://github.com/Neeraja-Kallamadi/AES-Advanced-Encryption-Standard-/assets/110168775/4ad38694-d3ce-4076-ae87-e797efd8ef11)

![ae![aes_algorithm6](https://github.com/Neeraja-Kallamadi/AES-Advanced-Encryption-Standard-/assets/110168775/5aeba7d2-f10e-41c3-9772-ef175996d097)

![aes_example1](https://github.com/Neeraja-Kallamadi/AES-Advanced-Encryption-Standard-/assets/110168775/907b5365-d29e-429d-99c9-69aaab7df2c0)

![aes_example2](https://github.com/Neeraja-Kallamadi/AES-Advanced-Encryption-Standard-/assets/110168775/f5aecf2a-60d2-4c0f-aaeb-a57ac9f1739b)

![aes_example3](https://github.com/Neeraja-Kallamadi/AES-Advanced-Encryption-Standard-/assets/110168775/a1ae744c-ac8f-4083-862f-43c04f5556c0)

![aes_example4](https://github.com/Neeraja-Kallamadi/AES-Advanced-Encryption-Standard-/assets/110168775/9825db2d-1f17-4219-83c5-59a60f6b3e89)

![aes_output1](https://github.com/Neeraja-Kallamadi/AES-Advanced-Encryption-Standard-/assets/110168775/3213d404-405e-4314-a5ad-1fb78bd22365)

![aes_output2](https://github.com/Neeraja-Kallamadi/AES-Advanced-Encryption-Standard-/assets/110168775/98b4e7b5-0250-4233-b3e0-2fb10d1d6081)

![aes_output3](https://github.com/Neeraja-Kallamadi/AES-Advanced-Encryption-Standard-/assets/110168775/0ab6dc39-cd61-49c5-a7ab-e0e470d88ea1)

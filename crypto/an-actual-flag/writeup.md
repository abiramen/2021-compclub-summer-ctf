# An actual flag

## Authors
@abiramen

## Category
- Crypto

## Description
Was bored, decided to colonise a new planet. Wanted to incorporate the planet name in its flag design - can you find it?

Remember to wrap your answer with `FLAG{}`!

[anactualflag.png](https://github.com/abiramen/2021-compclub-summer-ctf/blob/main/crypto/an-actual-flag/_ctfd/files/anactualflag.png)

## Points
50

## Solution

<details>
<summary>Spoilers</summary>

### Walkthrough

Typically with an image challenge, I would go through
- Metadata (basically non-existent with PNG files)
- Photoshop levels (and other adjustments)
- Steganography
- Hexdump (checking through the raw bytes in the file for any anomaly, but not typical in a beginner's CTF of this level).

It's certainly worth checking through these if everything else fails, but this is a crypto challenge, not a forensics challenge. The wording of the challenge also suggests that the name being hidden in the flag is intrisic to the flag design itself, and not the file.

At this point, we can analyse the colours in the image - there are three of them:

- #486163
- #6b746f
- #706961

It's worth noting this image looks really dull. Breaking each of the colours into their subpixels (or bytes):

- 48 61 63
- 6b 74 6f
- 70 69 61

We can see that none of the bytes are greater than 7F, which is equal to 127 in decimal. This suggests that the colours may be being used to encode ASCII values.

If we convert each byte to their corresponding ASCII values (remember to use the hexadecimal column on the ASCII table), we get

- H a c
- K t o
- P i a

revealing the flag.

### Flag
FLAG{Hacktopia}


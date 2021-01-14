# Shooting Stars

## Authors
@abiramen

## Category
- Crypto

## Description
found this cool book about shooting stars! i love shooting stars. the index fell out though.

Remember to wrap your answer with `FLAG{}`!

[book.txt](https://github.com/abiramen/2021-compclub-summer-ctf/blob/main/crypto/shooting-stars/_ctfd/files/book.txt)
[index.txt](https://github.com/abiramen/2021-compclub-summer-ctf/blob/main/crypto/shooting-stars/_ctfd/files/index.txt)

## Points
35

## Solution

<details>
<summary>Spoilers</summary>

### Walkthrough

The name of the file `index.txt` hints that the numbers in its contents could be some way that we could index the book, just like we index lists/arrays when programming.

We can see the numbers occur in pairs, `(a, b)`. The `a` values can get pretty big, while `b` is always relatively small (at most, 6). This suggests that the second number could be some way of indexing a character within a word. Maybe the first number could be the index of the word we're using?

We can also see a couple of 0s occurring in the index, for example, the second pair is `(0, 0)`. This suggests that both words and characters are zero-indexed, just like lists and arrays in most programming languages start counting from 0.

This is what is known as a book cipher. You could either try manually calculating each of the letters, writing a script to do it, or using a website [like this one](https://www.boxentriq.com/code-breaking/book-cipher) to decode it. You'll need to convert all the index pairs to match the format on that site. Make sure you select the correct options (word number, character number, none), and set the numbering start to 0. Once you do this, you should get your flag.

### Flag
FLAG{lightpollution}
</details>

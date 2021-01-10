# Egg nog

## Authors
@abiramen

## Category
- Forensics

## Description
It's hard to find egg nog after Christmas. It's also hard to find my hidden message, I hope!


[eggnog.jpg](https://github.com/abiramen/2021-compclub-summer-ctf/blob/main/forensics/egg-nog/_ctfd/files/eggnog.jpg)
[steggnog.png](https://github.com/abiramen/2021-compclub-summer-ctf/blob/main/forensics/egg-nog/_ctfd/files/steggnog.png)

## Points
50

## Solution

<details>
<summary>Spoilers</summary>

### Walkthrough
While this challenge uses a set of techniques that are relatively common in CTFs, paying attention to the workshop slides would have helped a lot here.

The first image you want to look at is eggnog.jpg - note that the contents featured in both images are basically identical, although the PNG is of much lower resolution. Looking at the file's metadata, we can see that there is some hidden information in the EXIF data (JPG files can have EXIF data, PNG files don't) - namely, the following string:

`jocksfindquartzglyphvexbmw`

We shall save this for later use.

The second image is named steggnog.png - a huge hint that more advanced image steganography, like least significant bit steganography, might be in use here. Googling `online steganography` yields [this website](https://stylesuxx.github.io/steganography/). Decoding it yields the following:

`FAJI{tzhpzdtpditdfdcjthtzx}`

This is the point where this challenge now becomes more crypto than forensics - we can see the result of our steganography decode looks almost like a flag. This is where we go back to our older string - `jocksfindquartzglyphvexbmw`. Googling this string yields a result about 'perfect pangrams' - sentences with all 26 letters of the alphabet exactly once. You might notice that this perfect pangram makes a perfect key for a _substitution cipher_.

Decoding the substitution cipher (using the perfect pangram as our ciphertext alphabet) on a website like [this](https://cryptii.com/pipes/alphabetical-substitution) gives us our flag.

### Flag
FLAG{notsoinsignificantnow}

### Other notes
The reason the PNG was lower resolution was so that your computer didn't die trying to decode using the steganography tool - fewer pixels means less work. 

</details>

# Spotify

## Authors
@abiramen

## Category
- Forensics

## Description
i made my spotify look pretty do you like it

Your flag will be a number. Wrap the number with `FLAG{}` - for example, if the number is 42, use `FLAG{42}`.

[spotify.jpg](https://github.com/abiramen/2021-compclub-summer-ctf/blob/main/forensics/spotify/_ctfd/files/spotify.jpg)

## Points
20

## Solution

<details>
<summary>Spoilers</summary>

### Walkthrough
I tried to hints for this one in plain sight - taking a look at the two recent search items shows you a song named 'Multiply' and another named 'Resolution' - resolution is a term to describe how many pixels tall and wide an image/video is.

From multiplying the resolution of the image (887 x 606), we get our solution.

### Flag
FLAG{537522}

### Other notes
I made my Spotify look pretty using [Spicetify](https://github.com/khanhas/spicetify-cli) with [this theme](https://github.com/morpheusthewhite/spicetify-themes/tree/master/Dribbblish).
</details>

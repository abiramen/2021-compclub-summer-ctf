# Blank Space

## Authors
@abiramen

## Category
- Forensics

## Description
i love to listen to Taylor Swift while stargazing. here's a picture I took, but my camera was broken


[blankspace.png](https://github.com/abiramen/2021-compclub-summer-ctf/blob/main/forensics/blank-space/_ctfd/files/blankspace.png)

## Points
30

## Solution

<details>
<summary>Spoilers</summary>

### Walkthrough
In the workshop slides, I highly suggested getting either Photoshop or GIMP to use - however, this was entirely solvable with just Microsoft Paint.

I set the background of this image to #ffffff - this is the hexadecimal code for the colour white. I then used the paintbrush to hide the flag to #fffffd - a colour that is extremely close to white, but not quite, making the writing seem basically invisible.

When solving image challenges for CTFs like these, I typically use Photoshop:

1. Open the Levels tool from Edit > Adjustments > Levels
2. Mess around with the input level sliders, and then the output level sliders and see if something reveals itself.

This would've worked perfectly well for this challenge. However, a simpler solution would be:

1. Open the image in Microsoft Paint.
2. Use the Fill bucket tool, and select a colour like black.
3. Click somewhere close to the border of the image, 'flooding the image'.

Paint only fills neighbouring pixels with the exact same colour - this should've revealed the off-white writing.

### Flag
FLAG{st4rBucKs_Lov3Rs}

### Other notes
Yes, this flag was a reference to the misheard 'Starbucks Lovers' lyrics from Taylor Swift's Blank Space.

</details>

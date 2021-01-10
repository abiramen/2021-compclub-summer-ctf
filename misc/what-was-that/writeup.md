# What was that?

## Authors
@haley-gu

## Category
- Misc

## Description
Houston, we've got... a disappearing black hole??

Make sure that the FLAG{} contents are all in lowercase.

[whatwasthat.mp4](https://github.com/abiramen/2021-compclub-summer-ctf/blob/main/misc/what-was-that/_ctfd/files/whatwasthat.mp4)

## Points
25

## Solution

<details>
<summary>Spoilers</summary>

### Walkthrough
This challenge features the distinctive short and long flashes (or dots and dashes used in Morse code). Fortunately, there's also synced beeping noises with the video, which makes interpreting the Morse code a lot easier (although you can just use the video, too!):

1. Open the audio from the video in an audio editor like Audacity.
2. Use the spectrogram to identify where each short (dot) flash or long (dash) sound is, and enter it into a Morse Code translator, and voila!

### Flag
FLAG{no_remorse}
</details>

# compclub

## Authors
@abiramen

## Category
- Crypto

## Description
compclub

```
compclubcompcompcompclubclubcomp compclubcompcompclubclubcompcomp compclubcompcompcompcompcompclub compclubcompcompcompclubclubclub compclubclubclubclubcompclubclub compclubclubcompcompcompclubcomp compclubclubclubclubcompcompclub compclubcompclubcompclubcompcomp compcompclubclubcompcompclubclub compclubcompclubclubclubclubclub compclubclubclubcompcompclubclub compcompclubclubcompcompcompclub compclubclubclubclubcompclubcomp compclubcompcompcompclubcompclub compclubclubcompcompclubcompcomp compclubclubclubclubclubcompclub
```

## Points
30

## Solution

<details>
<summary>Spoilers</summary>

### Walkthrough

We seem to have the strings 'comp' and 'club' as base units here - this seems very much like a binary system!

There also seems to be exactly 8 comps or clubs in a group, or exactly a byte! This suggests that the FLAG could be encoded in ASCII.

We know that all ASCII characters represented as a binary byte start with 0. Since all the groups start with comp, we can guess that comp is 0, and club is 1.

Replacing, we get,

```
01001100 01000001 01000111 01111011 01100010 01111001 01010100 00110011 01011111 01110011 00110001 01111010 01000101 01100100 01111101
```

Converting these into their ASCII characters, we get our flag.

### Flag
FLAG{byT3_s1zEd}


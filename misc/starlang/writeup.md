# starlang

## Authors
@abiramen

## Category
- Misc

## Description
I made my own programming language called starlang! It's pretty self-explanatory. Can you figure out what this program prints?

(Make sure to open the file with a text editor so that you can read its contents.)

[my_program.starlang](https://github.com/abiramen/2021-compclub-summer-ctf/blob/main/misc/starlang/_ctfd/files/my_program.starlang)

## Points
30

## Solution

<details>
<summary>Spoilers</summary>

### Walkthrough
This challenge uses a fake, but straight-forward 'programming language' - this is what we call 'pseudocode', which is a simplified notation to describe how a program or algorithm should work.

There are some things that you might need to be careful for here:

- If a 'branch' of an if statement is true, then we don't need to worry about other branches of the if statement. For example:

```js

if (a) {
    do_something();
} else if (b) {
    do_something_else();
} else if (c) {
    do_other_thing();
} else {
    do_last_thing();
}
```

If `b` is true, then it doesn't matter if `c` is true as well - once we've completed `do_something_else()`, we skip to the end of the entire if statement structure.

- Be careful with 'less than' - this is not the same as 'less than or equal to'.

Following through each of the statements should get you to the flag.

### Flag
FLAG{n3buL0uS_r3d5h1fT}
</details>

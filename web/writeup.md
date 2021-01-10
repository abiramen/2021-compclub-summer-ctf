# simplelogin

## Authors
@abiramen

## Category
- Web

## Description

When I grow up, I want to be a software developer at NASA. I'm still on my way to getting there. I decided to practice my web development skills and make an unbreakable login site. I bet you can't hack me - I'll even tell you that my username is `spaceman`.

Good luck!

[Link to challenge source code - no longer hosted](https://github.com/abiramen/2021-compclub-summer-ctf/tree/main/web/simplelogin-src)

There are three flags that can be found at the above link.

Flag 0 has three parts to it - you'll have to find each part (labelled 1/3, 2/3 and 3/3) and join them together to get the full flag!

## Points
~30 each

## Solution

<details>
<summary>Flag 0 Spoilers</summary>

### Walkthrough

(Replace `Ctrl` with `Cmd` on macOS.)

This first (well, zeroth) flag requires you to view the page source - that is, the code used to render the webpage to you - to look for comments. The flag is split up across three comments in three different files:

- index.html

    This HTML file contains the overall structure of the page, and can be easily found through `Ctrl+Shift+I` and checking the 'Elements' tab or `Ctrl+U`, to view the raw HTML (on Chrome, at least).
- hello.js
    
    JS files usually make a webpage interactive. You could've found this from the 'Sources' tab, or noticing the JS file was loaded in the HTML source code, or even noticing the origin of the sneaky message in the 'Console' tab.

- style.css

    CSS files make pages look pretty. You again could've found this from the 'Sources' tab, or noticing the CSS file was loaded in the HTML source code.

### Flag
FLAG{0_i_f0unD_tHre3_tYpEs_oF_cOmM3NtS}

</details>

<details>
<summary>Flag 1 Spoilers</summary>

### Walkthrough

(Replace `Ctrl` with `Cmd` on macOS.)

CTF authors like to involve cookies in challenges somehow, and this includes me! Using `Ctrl+Shift+I` on Chrome and selecting the Application tab, and then 'Cookies', reveals all cookies set by the current site, including the flag!

### Flag
FLAG{1_i_cHeCkeD_f0r_c0oki3S}

</details>

<details>
<summary>Flag 2 Spoilers</summary>

### Walkthrough

You probably tried to login before anything else, but this is in fact the final flag! Logging in with incorrect details gives us the following message:

'Password did not match expected encoded result: `aXJlQUxMeUxpa0VzUGFjZVNoaVBzMjA3JA==`'

This looks a lot like base-64 encoding - the biggest giveaway is the occurrence of equal signs on the end (which has a 2/3 probability of happening with base-64). Googling for a base-64 decoder gives us plenty of results, and decoding it gets us the password to use with the username 'spaceman' - 'ireALLyLikEsPaceShiPs207$'. Logging in will give you the flag.

You can also decode base-64 on a Linux command line with `echo 'aXJlQUxMeUxpa0VzUGFjZVNoaVBzMjA3JA==' | base64 -d`.

### Flag
FLAG{2_b4Se_64_iS_nOt_eNcrYpTi0n}

</details>

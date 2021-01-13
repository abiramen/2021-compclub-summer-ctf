# firednd-1

## Authors
@abiramen

## Category
- OSINT

## Description
CEO of FireDnD here again!

Quite recently, I had to fire my frontend web developer, because they were doing a terrible job, as you can probably tell from our [incomplete website](https://firednd-syd.web.app). I'm still in the process of removing all traces of him from our current website. Your first task is to find a picture of our fired frontend team member, as I haven't deleted it from our website's resources yet, but I can't find it for some reason.

Good luck!


## Points
30

## Solution

<details>
<summary>Spoilers</summary>

### Walkthrough

Typically when I'm solving a CTF challenge which involves trying to find some hidden resource on a website, I'll open the 'Network' tab of my browser, and start recording the requests the browser is making. These requests can tell me, for example, what images the browser is loading in - a fair initial suspicion would be that the browser is loading this image of the fired team member, but not displaying it.

However, this isn't quite the case. If we visit the /team.html page, we can see that three images are being loaded in: team-1.jpg, team-2.jpg and team-4.jpg. The glaring omission of team-3.jpg suggests that this might be our missing file. Visiting /team-3.jpg gives us our flag!


### Flag
FLAG{h3Lps_t0_c0uNt}

</details>

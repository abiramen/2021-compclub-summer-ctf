# firednd-0

## Authors
@abiramen

## Category
- OSINT

## Description
Hello! CEO of FireDnD here! We're a small startup that aims to connect people together for games of Dungeons and Dragons. [You can check out our (incomplete - more on that later) website here!](https://firednd-syd.web.app)

[If this website is down, you can find the source code here.](https://github.com/abiramen/2021-compclub-summer-ctf/tree/main/osint/firednd-src)

I've got a few tasks for you to complete, but before we start, could you do me a favour?

I'm supposed to meet up with someone after work today. I finish at 5PM, and take 8 minutes to walk from my office to Platform 2 of the nearest\* station. I then need to catch the next T4 train, before I get off at the second stop. Can you figure out what time I get off the train (rounded to the nearest minute)?

Your answer should be a 24-hour time. For example, if your answer is 6:04PM, enter `FLAG{1804}`.

\* Nearest by straight-line distance. The location of a station can be determined by the position of the 'T' logo on Google Maps.

## Points
25

## Solution

<details>
<summary>Spoilers</summary>

### Walkthrough
This requires some minor intelligence gathering:
1. Note that FireDnD's offices are located at 33-39 Hunter Street, Sydney. This can be found on the site's footer, or 'Contact Us' page.
2. The nearest station can be found using the measure distance tool on Google Maps - this is Martin Place station - however, it only barely beats out Central station.
3. We are told that the CEO wishes to take a T4 train from Platform 2 - if you chose Central Station earlier, this is a big clue that something may have gone wrong, as **no T4 trains pass through Central**. T4 trains on Platform 2 of Martin Place station run eastbound towards Bondi Junction. Two stops in this direction takes us to Edgecliff station.
4. We now want to check the train schedule for T4 trains departing after 5:08pm on Fridays. The next train would leave at 5:12, and is scheduled to arrive at 5:16:30pm, making the answer 5:17pm, or 17:17.


### Flag
FLAG{1717}

</details>

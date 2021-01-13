# firednd-2

## Authors
@abiramen

## Category
- OSINT

## Description
No way, it's me, the CEO of [FireDnD](https://firednd-syd.web.app) again!

My fired frontend developer hid a secret webpage on our website. I found out about this cool way to prevent search engines from finding the page, so I used that to prevent the page from showing up. I also replaced the contents of the page. Surely no-one can find it now, right?


## Points
30

## Solution

<details>
<summary>Spoilers</summary>

### Walkthrough

The first big hint in this challenge comes from the 'cool way to prevent search engines from finding' part - this is the exact function of robots.txt. If we visit /robots.txt, we find the following:

```
User-agent: Googlebot
Disallow: /ry4ns-s3cret-p4ge.html
```

We've now got the URL for the secret page! If we pay it a visit, however, we get this:

```
Hi! CEO of FireDnD here! I have taken over Ryan's secret page after firing him. That being said, I heard that nothing is deleted from the internet forever. Surely no one has a copy of the old contents of this page?
```

Unfortunate. Except, not really, because every internet historian's favourite tool, The Internet Wayback Machine at [web.archive.org](web.archive.org) happens to conveniently have a copy of the page!

There's an unloaded image on this page. Looking at the source code, we see

```
<div class="container">
    <h1>Ryan's top secret page</h1>

    <p>Hello, I'm Ryan, a developer at firednd. This is my secret page!</p>

    <p>Here is a secret:</p>
    <img src="/web/20210106050020im_/http://firednd-syd.web.app/FLAG{hiDD3n_in_the_s0uRce}"/>
</div>
```

giving us our flag.


### Flag
FLAG{hiDD3n_in_the_s0uRce}

</detials>

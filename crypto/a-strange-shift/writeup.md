# A strange shift

## Authors
@abiramen

## Category
- Crypto

## Description
Worked two different shifts in one day at Maccas, and I'm too tired to decode this. This dude kept ordering a Chicken Caesar Salad, and uttering this strange code. Can you decode it for me?

```
SQNL{sby_n_ibucqrw_xunsy}
```

## Points
30

## Solution

<details>
<summary>Spoilers</summary>

### Walkthrough
The most obvious hint here is the reference to the Caesar cipher, further confirmed by the use of the word shift. However, we could try all 26 possibilities here, and none of them would result in a coherent FLAG.

The sneakier part that you may not have caught in the wording is the 'two different shifts' - two different Caesar shifts were used.

One thing we can note is that we can expect the message to start with FLAG. If we try to rig a shift so that we get the first letter to be F (+13), we get:

```
FDAY{fol_a_vohpdej_khafl}
```

Interestingly, this also gets the A in the right place, giving us `F_A_`.

Shifting to get L in the second position (-5) gives us 
```
NLIG{nwt_i_dwpxlmr_spint}
```

This time, we also get the G in the right place! This suggests that there are two alternating shifts.

```
FDAY{fol_a_vohpdej_khafl}
NLIG{nwt_i_dwpxlmr_spint}
```

Taking alternating letters, we get our flag.

### Flag
FLAG{not_a_doppler_shift}
</details>

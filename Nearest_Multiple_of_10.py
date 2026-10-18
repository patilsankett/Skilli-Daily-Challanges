def roundToNearest(s: str) -> str:
    num = int(s)
    rem = num%10
    res =  num-rem + 10 if rem >5 else num - rem
    return res
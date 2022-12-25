def snafu_to_dec(snafu):
    """
    Convert a snafu to a decimal number
    """ 
    snafu = str(snafu)
    places = len(snafu)-1
    num = 0
    for i, c in enumerate(snafu):
        dec_spot = 5**(places-i)
        if c == "2":
            num += 2 * dec_spot
        elif c == "1":
            num += dec_spot
        elif c == "-":
            num -= dec_spot
        elif c == "=":
            num -= 2* dec_spot
    return num

def dec_to_snafu(num):
    """
    Convert a decimal number to a snafu
    """
    num = int(num)
    snafu = ""
    while num != 0:
        num, digit = divmod(num, 5)
        if digit in [0, 1, 2]:
            snafu += str(digit)
        elif digit == 3:
            snafu += "="
            num += 1
        elif digit == 4:
            snafu += "-"
            num += 1
    return snafu[::-1] # reverse the string

sum = 0
with open("input.txt") as f:
    for line in f:
        sum += snafu_to_dec(line.strip())
print(sum)
print(f"Part 1: {dec_to_snafu(sum)}")
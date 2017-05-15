
def revenge_of_the_pancakes(s):
    # flip count
    flip_count = 0
    prev = s[0]
    for pancake in s:
        if pancake != prev:
            flip_count += 1
            prev = pancake
    if (s[0] == '-' and flip_count % 2 == 0)\
            or (s[0] == '+' and flip_count % 2 == 1):
        flip_count += 1
    return flip_count


def main():
    t = int(input())
    for i in range(0, t):
        s = input()
        print('Case #%s: %s' % (i+1, revenge_of_the_pancakes(s)))

if __name__ == "__main__":
    main()

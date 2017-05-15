

def count_sheep(n):
    def _count_sheep(k, acc):
        if len(acc) == 10:
            return (k-1)*n

        k_str = str(n*k)
        for digit in k_str:
            acc.add(digit)

        return _count_sheep(k+1, acc)

    if n == 0:
        return 'INSOMNIA'

    ret = _count_sheep(1, set())
    return ret


def main():
    t = int(input())
    for i in range(0, t):
        print('Case #%s: %s' % (i+1, count_sheep(int(input()))))

if __name__ == "__main__":
    main()

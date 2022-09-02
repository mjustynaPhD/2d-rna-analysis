import sys


def create_table(means: str, stds: str):
    with open(means) as f:
        m = f.readlines()

    with open(stds) as f:
        s = f.readlines()

    for a, b in zip(m[1:], s[1:]):
        a_s = a.strip().split(",")
        b_s = b.strip().split(",")
        join = ["%s (%s)" % (x, y) for x, y in zip(a_s[1:], b_s[1:])]
        print(a_s[0], ",".join(join), sep=',')


if __name__ == "__main__":
    means, stds = sys.argv[1], sys.argv[2]
    print(means, stds)
    create_table(means, stds=stds)

import argparse
import os

import pandas as pd

DIRS = ('bgsu', 'rfam', 'novel')

ORDER = [
    'Contextfold',
    'CONTRAfold',
    'MXfold',
    'E2efold',
    'MXfold2',
    'RNA-state-inf',
    'SPOT-RNA',
    'UFold',
    'IPknot',
    'RNAFold',
    'RNAStructure'   
]

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-t',
        '--type',
        type=str,
        help='Define a kind of interactions',
        choices=['std', 'long'],
        default='std'
    )
    return parser.parse_args()


def read_values(means: str, stds: str):
    with open(means) as f:
        m = f.readlines()

    with open(stds) as f:
        s = f.readlines()
    vals = {}
    for a, b in zip(m[1:], s[1:]):
        a_s = a.strip().split(",")
        b_s = b.strip().split(",")
        join = ["%s (%s)" % (x, y) for x, y in zip(a_s[1:], b_s[1:])]
        # print(a_s[0], ",".join(join), sep=',')
        vals[a_s[0]] = join[-1]
    return vals


if __name__ == "__main__":
    parser = parse_args()
    if parser.type == 'std':
        TYPES = ('all', 'canon')
    elif parser.type == 'long':
        TYPES = ('noncanon', 'pseudo')
    else:
        raise ValueError("Unknown type")

    print(f'Types: {TYPES}')
    df = pd.DataFrame()
    for d in DIRS:
        for t in TYPES:
            means = f"{t}-{d}/{t}-means.csv"
            stds = f"{t}-{d}/{t}-stds.csv"
            if not os.path.exists(means) or not os.path.exists(stds):
                print(f"Skipping {means} or {stds}")
                continue
            vals = read_values(means, stds=stds)
            df = pd.concat([df, pd.DataFrame(vals, index=[f"{t}-{d}"])], axis=0)
    
    df = df.T
    if parser.type == 'std':
        df = df.reindex(ORDER)
    df.to_csv(f"{parser.type}-means-stds.tex", sep="&", na_rep='-', lineterminator="\\\\\n")
    print(df)

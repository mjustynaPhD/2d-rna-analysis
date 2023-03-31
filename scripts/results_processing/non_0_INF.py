import argparse




def parse_args():
    parser = argparse.ArgumentParser(description="Script to print molecules with non-zero INF values for a given method.")
    parser.add_argument("path", help="Path to results.rpt file to choose.")
    # add optional argument
    parser.add_argument("-m", "--method", help="Method to print results for.", default="spot-rna")
    return parser.parse_args()


def main(args):
    rpt_lines = read_rpt(args.path)
    method = args.method
    filtered_lines = filter_by_method(rpt_lines, method)
    for line in filtered_lines:
        print(" ".join(line))


def filter_by_method(lines, method):
    res = []
    pdb_id = ""
    for line in lines:
        fields = line.split()
        if len(fields)==0:
            continue
        if len(fields)==1:
            pdb_id = line.strip()
        elif fields[0].startswith(method) and float(fields[-1]) != 0:
            inf = fields[-1]
            res.append([pdb_id, inf])
    return res


def read_rpt(path):
    with open(path, "r") as f:
        lines = f.readlines()
    return lines


if __name__ == "__main__":
    args = parse_args()
    main(args)

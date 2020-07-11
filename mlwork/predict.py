
import argparse


def infer(x):
    return 0  # always return 0


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--pred_in", help="input file for prediction")
    p.add_argument("--pred_out", help="output file for prediction")

    args = p.parse_args()

    # read data
    print("inference...")
    xs = [line.strip() for line in open(args.pred_in)]
    pred_ys = [infer(x) for x in xs]

    # write
    print("write resutls...")
    with open(args.pred_out, "w") as fw:
        fw.write("\n".join([str(y) for y in pred_ys]))

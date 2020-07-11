
from sklearn.metrics import accuracy_score


def do_evaluation(gold_ys, pred_ys):
    return {
        "accuracy": accuracy(gold_ys, pred_ys)
    }


def accuracy(gold_ys, pred_ys):
    return accuracy_score(gold_ys, pred_ys)

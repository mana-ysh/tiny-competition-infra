
def read_gold_data(data_path: str):
    return [
        line.strip() for line in open(data_path)
    ]


def read_pred_data(data_str: str):
    return data_str.split("\n")

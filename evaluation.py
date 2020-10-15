from sklearn.metrics import r2_score, mean_squared_error


def evaluate(gold, predictions):
    r2 = r2_score(gold, predictions)
    sse = mean_squared_error(gold, predictions)
    return sse, r2

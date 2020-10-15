import sklearn as sk


def evaluate(gold, predictions):
    r2 = sk.metrics.r2_score(gold, predictions)
    sse = sk.metrics.mean_squared_error(gold, predictions)
    return sse, r2

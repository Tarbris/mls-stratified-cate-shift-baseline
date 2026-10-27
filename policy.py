"""Editable CATE estimator. Replace the weak pooled contrast in this file."""


class CATEEstimator:
    def __init__(self):
        self.effect = 0.0

    def fit(self, rows):
        treated = [r["y"] for r in rows if r["t"] == 1]
        control = [r["y"] for r in rows if r["t"] == 0]
        self.effect = sum(treated) / len(treated) - sum(control) / len(control)
        return self

    def predict(self, queries):
        return [self.effect for _ in queries]

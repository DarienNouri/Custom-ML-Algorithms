
import numpy as np
import DecisionTreeClassifier


class RandomForestClassifier:
    def __init__(self, n_estimators=100, max_depth=None, random_state=None):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.random_state = random_state
        self.trees = []

    def fit(self, X, y):
        self.trees = []
        for _ in range(self.n_estimators):
            tree = DecisionTreeClassifier(max_depth=self.max_depth)
            X_sample, y_sample = self._bootstrap_sample(X, y)
            tree.fit(X_sample, y_sample)
            self.trees.append(tree)

    def predict(self, X):
        predictions = np.array([tree.predict(X) for tree in self.trees])
        return np.array([np.argmax(np.bincount(predictions[:, i])) for i in range(X.shape[0])])

    def _bootstrap_sample(self, X, y):
        rng = np.random.default_rng(self.random_state)
        indices = rng.choice(len(X), size=len(X), replace=True)
        return X[indices], y[indices]
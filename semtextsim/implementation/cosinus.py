import numpy as np

from semtextsim.interface import Comparer as AbcComparer


class Comparer(AbcComparer):

    def compare_all(self, *texts: np.ndarray) -> np.ndarray:
        results = []
        for t1 in texts:
            results.append([self.eval_pair(t1, t2) for t2 in texts])
        return results

    def compare(self, v1: np.ndarray, v2: np.ndarray) -> float:
        mag1 = np.linalg.norm(v1)
        mag2 = np.linalg.norm(v2)
        if (not mag1) or (not mag2):
            return 0
        return np.dot(np.squeeze(np.asarray(v1)), np.squeeze(np.asarray(v2))) / (mag1 * mag2)

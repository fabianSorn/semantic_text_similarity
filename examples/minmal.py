from semtextsim import MuseEncoder, CosinusSimilarityEvaluator

encoder = MuseEncoder()
evaluator = CosinusSimilarityEvaluator()
reference = encoder.extract_features("Die Katze hat ein schönes Fell.")
actual = encoder.extract_features("Das Fell dieser Katze ist sehr hübsch.")
print(evaluator.eval(reference, actual))

from semtextsim import MuseEncoder, CosinusSimilarityEvaluator
import matplotlib.pyplot as plt
import seaborn as sns
from textwrap import wrap


encoder = MuseEncoder()
evaluator = CosinusSimilarityEvaluator()
sentences = ["Die Katze hat ein schönes Fell.",
             "The cat has a beautiful fur.",
             "Das Fell dieser Katze ist sehr hübsch.",
             "Die Haare dieser Katze sind sehr schön.",
             "Die Augen dieser Katze sind sehr schön.",
             "Das Fell dieses Hundes ist nicht so schön.",
             "Die Arme dieses Mannes sind besonders lang."] 
sim = evaluator.eval(*(encoder.extract_features(s) for s in sentences))

# Represent similarities as a heatmap
sns.set(font_scale=1.2)
g = sns.heatmap(
  sim,
  xticklabels=[ '\n'.join(wrap(l, 20)) for l in sentences ],
  yticklabels=[ '\n'.join(wrap(l, 20)) for l in sentences ],
  vmin=0,
  vmax=1,
  cmap="YlOrRd")
g.set_xticklabels([ '\n'.join(wrap(l, 20)) for l in sentences ], rotation=90)
g.set_title("Semantic Textual Similarity")
plt.show()

import pandas as pd

public_trees = pd.read_excel("data/raw/public-trees.xlsx")
public_trees.to_csv("data/raw/public-trees.csv", index=False)

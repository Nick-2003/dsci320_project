import tidyr
import pandas as pd

df = pd.read_excel("data/raw/public-trees.xlsx")
df = tidyr.separate(df, col="dteday", into=["date", "month", "year"], sep="-")
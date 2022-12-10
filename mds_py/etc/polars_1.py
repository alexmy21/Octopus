# import polars as pl

# df = pl.read_csv("https://j.mp/iriscsv")
# print(df.filter(pl.col("sepal_length") > 5)
#       .groupby("species")
#       .agg(pl.all().sum())
# )

import polars as pl

print(
    pl.read_csv("https://j.mp/iriscsv")
    .lazy()
    .filter(pl.col("sepal_length") > 5)
    .groupby("species")
    .agg(pl.all().sum())
    .collect()
)
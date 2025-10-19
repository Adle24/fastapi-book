import csv
from tabulate import tabulate
import pandas as pd


def read_csv(file: str) -> list[list]:
    with open(file) as f:
        data = [row for row in csv.reader(f, delimiter="|")]

    return data


def read_pandas(file: str) -> pd.DataFrame:
    data = pd.read_csv(file, sep="|")
    return data


print(tabulate(read_csv("./creature.psv")))
print(read_pandas("./creature.psv"))

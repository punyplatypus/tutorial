from pipeline.pipe import DataLoader, Pipeline

def main():
    a = Pipeline(DataLoader("data/boardgames1.csv.zip"))
    df = a.load()
    print(df)

main()
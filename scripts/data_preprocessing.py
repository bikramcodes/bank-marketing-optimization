import pandas as pd

def load_and_clean_data(path):
    df = pd.read_csv(path, sep=';')
    df.columns = df.columns.str.replace('.', '_').str.strip()
    df['y'] = df['y'].map({'yes': 1, 'no': 0})
    return df

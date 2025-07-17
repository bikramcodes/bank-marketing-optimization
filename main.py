from scripts.data_preprocessing import load_and_clean_data
from scripts.feature_engineering import prepare_features
from scripts.modeling import train_and_evaluate

def main():
    df = load_and_clean_data("data/bank-full.csv")
    X_train, X_test, y_train, y_test = prepare_features(df)
    train_and_evaluate(X_train, X_test, y_train, y_test)

if __name__ == "__main__":
    main()

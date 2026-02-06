import numpy as np
import pandas as pd
from load_data import load_data
from preprocessing import preprocess_data
from train_models import train_models
from evaluate import plot_actual_vs_predicted
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error

def main():
    dataset = load_data()

    x, y = preprocess_data(dataset)

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.25, random_state=42
    )

    models = train_models(x_train, y_train)


    for name, model in models.items():
        y_pred = model.predict(x_test)


        plot_actual_vs_predicted(y_test, y_pred, name)

        # Metrics
        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        rmse = np.sqrt(mse)

        print(f"Model: {name}")
        print(f"  MSE  : {mse}")
        print(f"  MAE  : {mae}")
        print(f"  RMSE : {rmse}")
        print(model.score(x_train,y_train)*100, model.score(x_test,y_test)*100)
        print("-" * 9)

    coef_df = pd.DataFrame({
    "Feature": x.columns,
    "LinearRegression": models["LinearRegression"].coef_,
    "Ridge": models["Ridge"].coef_,
    "Lasso": models["Lasso"].coef_
    })

    print(coef_df)



if __name__ == "__main__":
    main()

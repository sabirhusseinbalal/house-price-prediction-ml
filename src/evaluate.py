import matplotlib.pyplot as plt
import seaborn as sns

def plot_actual_vs_predicted(y_true, y_pred, model_name):
    plt.figure(figsize=(5, 4))
    sns.scatterplot(x=y_true, y=y_pred)
    plt.xlabel("Actual Values")
    plt.ylabel("Predicted Values")
    plt.title(f"Actual vs Predicted ({model_name})")
    plt.show()

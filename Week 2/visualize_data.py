import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime

def visualize_data(df):
    os.makedirs("plots", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # Bar plot
    df.value_counts().plot(kind='bar')
    plt.title("Bar Plot")
    plt.savefig(f"plots/bar_plot_{timestamp}.png")
    plt.clf()
    # Line chart
    df.plot()
    plt.title("Line Chart")
    plt.savefig(f"plots/line_chart_{timestamp}.png")
    plt.clf()
    # Histogram
    df.hist()
    plt.suptitle("Histogram")
    plt.savefig(f"plots/histogram_{timestamp}.png")
    plt.clf()

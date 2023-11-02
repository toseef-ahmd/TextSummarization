import matplotlib.pyplot as plt
import pandas as pd


def get_all_graphs(df):
    figsize = (12, 6)

    # Calculate the mean values for ROUGE-2 and ROUGE-3
    mean_rouge2 = df["TextRank ROUGE-2"].mean()
    mean_rouge3 = df["TextRank ROUGE-3"].mean()

    # Create a separate figure for each graph
    plt.figure(figsize=figsize)

    # Plot for TextRank ROUGE-2 and ROUGE-3
    plt.plot(df["Index"], df["TextRank ROUGE-2"], marker='o', label='TextRank ROUGE-2')
    plt.plot(df["Index"], df["TextRank ROUGE-3"], marker='o', label='TextRank ROUGE-3')
    plt.axhline(y=mean_rouge2, color='r', linestyle='--', label=f'Mean ROUGE-2: {mean_rouge2:.3f}')
    plt.axhline(y=mean_rouge3, color='b', linestyle='--', label=f'Mean ROUGE-3: {mean_rouge3:.3f}')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('TextRank ROUGE-2 and ROUGE-3 Summary with Mean')
    plt.legend()
    # plt.grid()
    plt.savefig('TextRank.jpg', format='jpg')
    plt.show()

    # Calculate the mean values for LSA
    mean_lsa_rouge2 = df["LSA ROUGE-2"].mean()
    mean_lsa_rouge3 = df["LSA ROUGE-3"].mean()

    # Create a new figure for LSA
    plt.figure(figsize=figsize)

    # Plot for LSA ROUGE-2 and ROUGE-3
    plt.plot(df["Index"], df["LSA ROUGE-2"], marker='o', label='LSA ROUGE-2')
    plt.plot(df["Index"], df["LSA ROUGE-3"], marker='o', label='LSA ROUGE-3')
    plt.axhline(y=mean_lsa_rouge2, color='r', linestyle='--', label=f'Mean ROUGE-2: {mean_lsa_rouge2:.3f}')
    plt.axhline(y=mean_lsa_rouge3, color='b', linestyle='--', label=f'Mean ROUGE-3: {mean_lsa_rouge3:.3f}')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('LSA ROUGE-2 and ROUGE-3 Summary with Mean')
    plt.legend()
    # plt.grid()
    plt.savefig('LSA.jpg', format='jpg')
    plt.show()

    # Calculate the mean values for Relevance
    mean_relevance_rouge2 = df["Relevance ROUGE-2"].mean()
    mean_relevance_rouge3 = df["Relevance ROUGE-3"].mean()

    # Create a new figure for Relevance
    plt.figure(figsize=figsize)

    # Plot for Relevance ROUGE-2 and ROUGE-3
    plt.plot(df["Index"], df["Relevance ROUGE-2"], marker='o', label='Relevance ROUGE-2')
    plt.plot(df["Index"], df["Relevance ROUGE-3"], marker='o', label='Relevance ROUGE-3')
    plt.axhline(y=mean_relevance_rouge2, color='r', linestyle='--', label=f'Mean ROUGE-2: {mean_relevance_rouge2:.3f}')
    plt.axhline(y=mean_relevance_rouge3, color='b', linestyle='--', label=f'Mean ROUGE-3: {mean_relevance_rouge3:.3f}')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Relevance ROUGE-2 and ROUGE-3 Summary with Mean')
    plt.legend()
    # plt.grid()
    plt.savefig('Relevance.jpg', format='jpg')
    plt.show()


def get_overall_graph(df):
    # Calculate the mean values for all three summarizers
    mean_rouge2 = df["TextRank ROUGE-2"].mean()
    mean_rouge3 = df["TextRank ROUGE-3"].mean()
    mean_lsa_rouge2 = df["LSA ROUGE-2"].mean()
    mean_lsa_rouge3 = df["LSA ROUGE-3"].mean()
    mean_relevance_rouge2 = df["Relevance ROUGE-2"].mean()
    mean_relevance_rouge3 = df["Relevance ROUGE-3"].mean()

    # Create a bar chart
    plt.figure(figsize=(10, 6))

    methods = ["TextRank", "LSA", "Relevance"]
    means_rouge2 = [mean_rouge2, mean_lsa_rouge2, mean_relevance_rouge2]
    means_rouge3 = [mean_rouge3, mean_lsa_rouge3, mean_relevance_rouge3]

    bar_width = 0.35
    index = range(len(methods))

    bar1 = plt.bar(index, means_rouge2, bar_width, label='ROUGE-2')
    bar2 = plt.bar(index, means_rouge3, bar_width, label='ROUGE-3', align='edge')

    plt.xlabel('Summarizer')
    plt.ylabel('Mean Value')
    plt.title('Mean ROUGE-2 and ROUGE-3 Scores for Different Summarizers')

    # Annotate the bars with their mean values
    for i, value in enumerate(means_rouge2):
        plt.text(i - 0.2, value + 0.001, f'{value:.3f}', ha='center', va='bottom')
    for i, value in enumerate(means_rouge3):
        plt.text(i + 0.15, value + 0.001, f'{value:.3f}', ha='center', va='bottom')

    plt.xticks(index, methods)
    plt.legend()
    # plt.grid()

    plt.savefig('OverallTrend.jpg', format='jpg')
    plt.show()


if __name__ == '__main__':
    # Sample data
    df = pd.read_csv("results.csv")
    get_all_graphs(df)
    get_overall_graph(df)

import matplotlib.pyplot as plt
import polars as pl

dataset = "https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv"


def load_dataset():
    df = pl.read_csv(dataset)
    return df

def general_polars_describe():
    """polars describe function in csv"""
    polars_df = pl.read_csv(dataset)
    return polars_df.median(), polars_df.describe()


def bar_visual(df, col):
    """bar graph of a column over all airlines"""
    x = df["airline"]
    y = df[col]
    plt.figure(figsize=(15, 12))
    plt.bar(x, y)
    plt.xlabel("Airlines")
    plt.ylabel(col)
    plt.title(f"{col} over Airlines")
    plt.xticks(rotation=90, fontsize=6)
    plt.savefig(f"{col}.png")


def hist_visual(df, col):
    """histogram of a column over all airlines"""
    plt.figure(figsize=(10, 6))
    plt.hist(df[col])
    plt.xlabel(f"Number of {col}")
    plt.ylabel("Frequency")
    plt.title(f"Frequency of {col}")
    plt.savefig(f"Frequency_{col}_hist.png")


def general_viz_combined(general_df):
    """saves all the figures at once"""
    bar_visual(general_df, "incidents_85_99")
    hist_visual(general_df, "incidents_85_99")
    bar_visual(general_df, "fatal_accidents_85_99")
    hist_visual(general_df, "fatal_accidents_85_99")
    bar_visual(general_df, "fatalities_85_99")
    hist_visual(general_df, "fatalities_85_99")
    bar_visual(general_df, "incidents_00_14")
    hist_visual(general_df, "incidents_00_14")
    bar_visual(general_df, "fatal_accidents_00_14")
    hist_visual(general_df, "fatal_accidents_00_14")
    bar_visual(general_df, "fatalities_00_14")
    hist_visual(general_df, "fatalities_00_14")
    plt.pyplot.close()


def save_to_md():
    """save to markdown"""
    df = load_dataset()
    general_viz_combined(df)
    """generate an md file with outputs"""
    markdown_table1, markdown_table2 = general_polars_describe()
    markdown_table1 = str(markdown_table1)
    markdown_table2 = str(markdown_table2)
    with open("report.md", "w", encoding="utf-8") as file:
        file.write("# Report\n\n")
        file.write("## General Description\n\n")
        file.write(f"{markdown_table1}\n\n")
        file.write(f"{markdown_table2}\n\n")
        file.write("## Visualizations\n\n")
        file.write("### Incidents 85-99\n\n")
        file.write("![Incidents 85-99](incidents_85_99.png)\n\n")
        file.write("![Incidents 85-99](Frequency_incidents_85_99_hist.png)\n\n")
        file.write("### Fatal Accidents 85-99\n\n")
        file.write(
            "![Fatal Accidents 85-99](fatal_accidents_85_99.png)\n\n"
        )
        file.write(
            "![Fatal Accidents 85-99] \
                (Frequency_fatal_accidents_85_99_hist.png)\n\n"
        )
        file.write("### Fatalities 85-99\n\n")
        file.write("![Fatalities 85-99](fatalities_85_99.png)\n\n")
        file.write(
            "![Fatalities 85-99](Frequency_fatalities_85_99_hist.png)\n\n"
        )
        file.write("### Incidents 00-14\n\n")
        file.write("![Incidents 00-14](incidents_00_14.png)\n\n")
        file.write("![Incidents 00-14](Frequency_incidents_00_14_hist.png)\n\n")
        file.write("### Fatal Accidents 00-14\n\n")
        file.write(
            "![Fatal Accidents 00-14](fatal_accidents_00_14.png)\n\n"
        )
        file.write(
            "![Fatal Accidents 00-14] \
                (Frequency_fatal_accidents_00_14_hist.png)\n\n"
        )
        file.write("### Fatalities 00-14\n\n")
        file.write("![Fatalities 00-14](fatalities_00_14.png)\n\n")
        file.write(
            "![Fatalities 00-14](Frequency_fatalities_00_14_hist.png)\n\n"
        )


if __name__ == "__main__":
    general_viz_combined(load_dataset())
    save_to_md()
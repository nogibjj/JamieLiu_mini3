import matplotlib.pyplot as plt
import polars as pl
import os

dataset = "https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv"

output_folder = "visualizations"
os.makedirs(output_folder, exist_ok=True)


def load_dataset():
    """Load the dataset once and reuse it."""
    return pl.read_csv(dataset)


def general_polars_describe(df):
    """Return the median and description of the dataset."""
    return df.median(), df.describe()


def bar_visual(df, col):
    """Create a bar graph for a specific column."""
    x = df["airline"].to_list()  # Convert to list for plotting
    y = df[col].to_list()
    plt.figure(figsize=(15, 12))
    plt.bar(x, y)
    plt.xlabel("Airlines")
    plt.ylabel(col)
    plt.title(f"{col} over Airlines")
    plt.xticks(rotation=90, fontsize=6)
    plt.savefig(f"{output_folder}/{col}.png")
    plt.close()  # Close the figure after saving to avoid memory leaks


def hist_visual(df, col):
    """Create a histogram for a specific column."""
    plt.figure(figsize=(10, 6))
    plt.hist(df[col].to_list())  # Convert to list for plotting
    plt.xlabel(f"Number of {col}")
    plt.ylabel("Frequency")
    plt.title(f"Frequency of {col}")
    plt.savefig(f"{output_folder}/Frequency_{col}_hist.png")
    plt.close()  # Close the figure after saving to avoid memory leaks


def general_viz_combined(df):
    """Generate visualizations for specific columns."""
    columns = [
        "incidents_85_99",
        "fatal_accidents_85_99",
        "fatalities_85_99",
        "incidents_00_14",
        "fatal_accidents_00_14",
        "fatalities_00_14",
    ]

    for col in columns:
        bar_visual(df, col)
        hist_visual(df, col)


def format_polars_table(df):
    """Formats a Polars DataFrame for markdown output."""
    headers = " | ".join(df.columns)
    markdown = f"| {headers} |\n"
    markdown += "| " + " | ".join("---" for _ in df.columns) + " |\n"

    for row in df.rows():
        markdown += "| " + " | ".join(map(str, row)) + " |\n"

    return markdown


def save_to_md(df):
    """Save the report to a markdown file with visualizations."""
    # Generate visualizations
    general_viz_combined(df)

    # Get the descriptive statistics
    median_df, describe_df = general_polars_describe(df)

    # Format Polars DataFrames for markdown
    median_str = format_polars_table(median_df)
    describe_str = format_polars_table(describe_df)

    # Write the report to markdown
    with open("report.md", "w", encoding="utf-8") as file:
        file.write("# Report\n\n")
        file.write("## General Description\n\n")
        file.write(f"### Description\n\n{describe_str}\n\n")
        file.write(f"### Median\n\n{median_str}\n\n")

        file.write("## Visualizations\n\n")
        sections = ["Incidents", "Fatal Accidents", "Fatalities"]
        periods = ["85_99", "00_14"]

        for section in sections:
            for period in periods:
                file.write(f"### {section} {period}\n\n")

                image_path = f"visualizations/{section.lower()}_{period}.png"
                hist_image_path = (
                    f"visualizations/Frequency_{section.lower()}_{period}_hist.png"
                )

                # Write bar chart image
                file.write(f"![{section} {period}]({image_path})\n\n")

                # Write histogram image
                file.write(f"![{section} {period}]({hist_image_path})\n\n")

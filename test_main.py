from main import load_dataset, general_viz_combined, save_to_md


def test_generate_visualizations():
    df = load_dataset()
    general_viz_combined(df)
    save_to_md(df)


if __name__ == "__main__":
    test_generate_visualizations()

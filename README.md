# JamieLiu_mini3

## Overview

## Features

- `.devcontainer` configuration for a consistent Python development environment using Docker.
- **Makefile** to streamline common tasks like setup, testing, linting.
- **GitHub Actions** for automated CI/CD pipeline (testing, linting, and deployment).
- `requirements.txt` for managing Python dependencies.

## Usage

1. **Clone the repository:**

   ```bash
   git clone git@github.com:nogibjj/JamieLiu_mini3.git
   ```

2. **Install dependencies:**

   ```bash
   make install
   ```

3. **Format code:**

   ```bash
   make format
   ```

   ![Alt text](format.png)

4. **Lint code:**

   ```bash
   make lint
   ```

   ![Alt text](lint.png)

5. **Test code:**

   ```bash
   make test
   ```

   ![Alt text](test.png)

6. **Run all steps (Install, Format, Lint, Test):**

   ```bash
   make all
   ```

## **Summary Statistics**:

![Alt text](statistics.png)

## **Visualization Example**:

### Fatalities 00-14

![Fatalities 00-14](fatalities_00_14_over_Airlines.png)

![Fatalities 00-14](Frequency_of_fatalities_00_14_histogram.png)

See detailed statistics and visualizations in this [report](/report.md)

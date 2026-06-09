# ETL Pipeline

This project contains a simple **Extract → Transform → Load (ETL)** pipeline implemented in `etl_pipeline.py`.

## What the pipeline does

### 1) Extract
- Loads the input dataset from:
  - `data/sample_data.csv`
- Prints the original dataset to the console.

### 2) Transform
The script performs the following preprocessing steps using `scikit-learn`:

#### Missing value handling
- **Numerical columns** (`Age`, `Salary`):
  - Missing values are replaced with the **mean** (`SimpleImputer(strategy='mean')`).
- **Categorical column** (`Department`):
  - Missing values are replaced with the **most frequent category** (`SimpleImputer(strategy='most_frequent')`).

#### Categorical encoding
- `Department` is converted from text to integers using **LabelEncoder**.

#### Feature scaling
- `Age` and `Salary` are standardized using **StandardScaler** (zero mean, unit variance).

### 3) Load
- Saves the processed dataset to:
  - `data/processed_data.csv`
- Prints the processed dataframe and the output path.

### 4) Visualization
- After processing, the script plots a bar chart showing **Salary by Name** using `matplotlib`.
- The plot is displayed via `plt.show()`.

## Files
- `etl_pipeline.py` — ETL logic (load, clean/transform, save, and plot)
- `data/sample_data.csv` — input data
- `data/processed_data.csv` — output of the pipeline

## How to run
From the project folder:
```bash
python etl_pipeline.py
```

Running the script will read `data/sample_data.csv`, process it, save `data/processed_data.csv`, and display the chart.


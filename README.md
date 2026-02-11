# Real Estate Data Analysis Dashboard – São Paulo

This project consists of an exploratory data analysis and visualization pipeline applied to real estate listings in São Paulo. It was developed with a focus on clean data processing, statistical rigor, modular architecture, and reproducible analytical workflows using Python.

Although built as a study project, the structure and design follow professional standards commonly adopted in data analysis and business intelligence environments.

---

## Project Overview

The objective of this project is to:

- Perform structured data cleaning and transformation
- Separate listings into sale and rental categories
- Compute robust statistical indicators
- Derive price per square meter metrics
- Aggregate insights by neighborhood
- Build a scalable foundation for an interactive dashboard using Streamlit

The dataset contains inconsistencies and limited neighborhood depth. These characteristics were intentionally preserved to simulate real-world data imperfection and to demonstrate proper analytical handling.

---

## Technical Stack

- Python 3
- Pandas (data manipulation and transformation)
- NumPy (statistical computation)
- Matplotlib (data visualization)
- Streamlit (interactive dashboard)
- MySQL (planned database modeling layer)

---

## Data Processing Architecture

The project implements a modular data pipeline in which the user provides only the dataset path. All transformations are executed sequentially through a structured workflow.

Main processing steps:

- CSV ingestion
- Currency cleaning and normalization
- Classification of listing type (sale or rental)
- Creation of numeric price field
- Removal of sale outliers
- Area standardization and validation
- Numeric casting of structural attributes
- Computation of price per square meter (sales only)

This modular structure ensures maintainability, scalability, and clear separation of responsibilities.

---

## Statistical Approach

For sale listings, the following measures are calculated:

- Median price
- Median price per square meter
- Standard deviation
- Minimum and maximum values

The median is used as the primary central tendency metric to reduce distortion caused by extreme high-value properties.

---

## Aggregated Analysis

Neighborhood-level aggregation includes:

- Median price per square meter
- Total number of listings per neighborhood

All neighborhoods are included in the aggregation to preserve dataset integrity. Interpretation is performed with awareness of sample size variability.

---

## Visualization Layer

The current implementation includes:

- Top 10 most expensive neighborhoods ranked by median price per square meter (sale listings)
- Horizontal bar chart optimized for readability and ranking clarity

Planned enhancements:

- Sale vs rental comparative analysis
- KPI summary indicators
- Interactive filters
- Database integration layer
- Improved layout and analytical segmentation

---

## Execution

1. Clone the repository:

git clone https://github.com/your-username/your-repository.git


2. Install dependencies:

pip install pandas numpy matplotlib streamlit


3. Run the dashboard:

streamlit run app.py


---

## Project Status

- Data processing pipeline implemented
- Statistical analysis with NumPy completed
- Initial visualization layer implemented
- Dashboard interface under development
- Database modeling planned

---

## Author

👤 Emilio Roberto Fernandes Silva

This project was developed as part of a structured study plan focused on Data Analysis and dashboard development using Python.

---

## License

This repository is intended for educational and portfolio purposes.

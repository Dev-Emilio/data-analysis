# Real Estate Data Analysis Dashboard – São Paulo

## Live Demo

Access the deployed dashboard:

https://data-analysis-dashboard-sao-paulo.streamlit.app/

---

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
- Build a scalable and interactive dashboard using Streamlit  

The dataset contains inconsistencies and limited neighborhood depth. These characteristics were intentionally preserved to simulate real-world data imperfection and to demonstrate proper analytical handling.

---

## Technical Stack

- Python 3  
- Pandas (data manipulation and transformation)  
- NumPy (statistical computation)  
- Plotly (interactive visualization layer)  
- Streamlit (interactive dashboard interface)  
- MySQL (database integration layer – architecture ready)  

---

## Data Processing Architecture

The project implements a modular data pipeline in which the user provides only the dataset path (or database connection). All transformations are executed sequentially through a structured workflow.

### Main processing steps:

- CSV ingestion or database query execution  
- Currency cleaning and normalization  
- Classification of listing type (sale or rental)  
- Creation of numeric price field  
- Removal of sale outliers  
- Area standardization and validation  
- Numeric casting of structural attributes  
- Computation of price per square meter (sales only)  

This modular structure ensures maintainability, scalability, and clear separation of responsibilities between processing, analysis, and visualization layers.

---

## Statistical Approach

For sale listings, the following measures are calculated:

- Mean price  
- Median price  
- Standard deviation  
- Mean price per square meter  
- Minimum and maximum values  

The median remains the primary central tendency metric to reduce distortion caused by extreme high-value properties.

---

## Aggregated Analysis

Neighborhood-level aggregation includes:

- Median price per square meter  
- Total number of listings per neighborhood  
- Ranking of neighborhoods by value per square meter  

All neighborhoods are included in the aggregation to preserve dataset integrity. Interpretation is performed with awareness of sample size variability.

---

## Visualization Layer

The dashboard interface is structured as a wide-format analytical layout optimized for business readability.

### Current visual components include:

- KPI section with dynamic metrics (mean price, median price, price per m², total listings)  
- Sales price distribution histogram  
- Price per square meter distribution histogram  
- Area vs. price scatter plot  
- Neighborhood ranking by median price per square meter  

### Interactive sidebar filters:

- Neighborhood selection  
- Listing type (sale / rental)  
- Price range filtering  
- Dynamic Top N ranking control  

All visualizations are built with Plotly for interactivity and rendered through Streamlit in a responsive layout.

The dashboard also includes contextual explanation panels (expanders) for each graph, improving interpretability and business communication clarity.

---

## Execution

### 1. Clone the repository:

```bash
git clone https://github.com/Dev-Emilio/data-analysis.git
```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
```
### 3. Run the dashboard:
```bash
streamlit run app.py
```

## Project Status

* Data processing pipeline implemented
* Statistical analysis completed
* Interactive visualization layer implemented
* Responsive dashboard layout structured
* MySQL integration architecture prepared
* Project ready for deployment via Streamlit Cloud

### Author

**Emilio Roberto Fernandes Silva**

This project was developed as part of a structured study plan focused on Data Analysis, Python development, and dashboard engineering.

### License

This repository is intended for educational and portfolio purposes.

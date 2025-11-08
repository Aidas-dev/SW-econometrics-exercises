# SW-econometrics-exercises
This repository holds completed empirical exercises from "Introduction to Econometrics, 4th Edition" by Stock and Watson.
Link to site: [Stock and Watson website](https://media.pearsoncmg.com/ph/bp/bp_stock_econometrics_4_cw/)

## Complete Project Structure
```
SW-econometrics-exercises/
├── Chapters/
│   └── Chapter4/
│       ├── common-requirements.txt            # General requirements
│       ├── Python code/                # Python implementation
│       │   ├── Earnings_and_Height_Python.ipynb
│       │   └── requirements.txt       # Python-specific requirements
│       ├── R \ code/                   # R implementation (note escaped space)
│       │   ├── Earnings_and_Height_R.ipynb
│       │   ├── install_R_packages.R
│       │   └── requirements.txt       # R-specific requirements
│       └── Used data and given exercise/  # Data and instructions
│           ├── Earnings and Height Exercise.pdf
│           ├── Earnings_and_Height_Description.pdf
│           ├── Earnings_and_Height.ods
│           ├── Earnings_and_Height.xlsx
│           ├── Page 1.png
│           └── Page 2.png
├── config/
│   └── jupyter_notebook_config.py      # Jupyter configuration
└── README.md                           # This documentation
```

## Project Overview
This repository contains implementations of econometrics exercises from Chapter 4 of Stock and Watson's textbook. The main exercise focuses on analyzing the relationship between earnings and height using data from the US National Health Interview Survey (1994).

## Environment Setup

### Common Requirements
1. Jupyter Notebook (`pip install notebook`)
2. Apply Jupyter configuration (see below)

### Python Setup
1. Install Python 3.6+
2. Install requirements:
```bash
pip install -r "Chapters/Chapter4/Python \ code/requirements.txt"
```

### R Setup
1. Install R (https://cran.r-project.org/)
2. Install packages (note escaped space):
```bash
Rscript "Chapters/Chapter4/R \ code/install_R_packages.R"
```
3. Verify kernel:
```R
IRkernel::installspec(user = FALSE)
```

## Jupyter Notebook Configuration
Configure using either:
1. Copy config file:
```bash
mkdir -p ~/.jupyter
cp config/jupyter_notebook_config.py ~/.jupyter/
```
2. Or use config flag:
```bash
jupyter notebook --config=config/jupyter_notebook_config.py
```

Includes:
- Automatic output resizing
- Increased rate limits
- Auto-scrolling

## Working with the Exercises
1. Launch Jupyter:
```bash
jupyter notebook
```
2. Open either:
   - R notebook (`Earnings_and_Height_R.ipynb`) a bit less extensive in detail
   - Python notebook (`Earnings_and_Height_Python.ipynb`)
3. Follow instructions from "Earnings and Height Exercise.pdf"

## Expected Results
- Scatterplot with horizontal lines (earnings brackets)
- Regression showing:
  - Initial positive height coefficient
  - Reduced coefficient when controlling for education
- Gender differences in results

## Data Files
Available in:
- OpenDocument (.ods)
- Excel (.xlsx)

Variables include:
- age, earnings, education, height
- marital status, occupation, race/ethnicity
- region, sex, weight
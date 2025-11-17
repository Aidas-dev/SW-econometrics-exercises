# SW-econometrics-exercises

This repository holds completed empirical exercises from "Introduction to Econometrics, 4th Edition" by Stock and Watson.  
Link to site: [Stock and Watson website](https://media.pearsoncmg.com/ph/bp/bp_stock_econometrics_4_cw/)

---

## Project Overview

This repository implements econometrics exercises from Stock and Watson's textbook, demonstrating key concepts through practical analysis of real-world datasets. Each chapter focuses on different econometric techniques and datasets.

---

### Chapter 4: Earnings and Height

Analyzes the relationship between earnings and height using data from the US National Health Interview Survey (1994). Key concepts:  
- **Multiple regression analysis**  
- **Omitted variable bias**  
- **Perfect multicollinearity analysis**  
- **Interpretation of regression coefficients**  

---

### Chapter 5: Birthweight and Smoking

Examines the effect of smoking and other variables on birthweight using data from the National Natality-Mortality Detail File for births in Pennsylvania in 1989. Key concepts:  
- **Causal inference**  
- **Confidence intervals, robustness**  
- **Ommited variable bias**  
- **Multiple regression analysis**  

---

## Complete Project Structure

```
SW-econometrics-exercises/
├── Chapters/
│   ├── Chapter4/
│   │   ├── common-requirements.txt            # General requirements
│   │   ├── environment.yml                   # Conda environment file
│   │   ├── Python code/                      # Python implementation
│   │   │   ├── Earnings_and_Height_Python.ipynb
│   │   │   └── requirements.txt             # Python-specific requirements
│   │   ├── R code/                          # R implementation
│   │   │   ├── Earnings_and_Height_R.ipynb
│   │   │   └── install_R_packages.R
│   │   └── Used data and given exercise/     # Data and instructions
│   │       ├── Earnings and Height Exercise.pdf
│   │       ├── Earnings_and_Height_Description.pdf
│   │       ├── Earnings_and_Height.ods
│   │       ├── Earnings_and_Height.xlsx
│   │       ├── Page 1.png
│   │       └── Page 2.png
│   └── Chapter5/
│       ├── common-requirements.txt            # General requirements
│       ├── environment.yml                   # Conda environment file
│       ├── Python code/                      # Python implementation
│       │   ├── Birthweight_and_Smoking_Python.ipynb
│       │   └── requirements.txt             # Python-specific requirements
│       ├── R code/                          # R implementation
│       │   ├── Birthweight_and_Smoking_R.ipynb
│       │   └── install_R_packages.R
│       └── Used data and given exercise/     # Data and instructions
│           ├── Birthweight_and_Smoking_Exercise.pdf
│           ├── Birthweight_Smoking_Description.pdf
│           ├── birthweight_smoking.ods
│           ├── birthweight_smoking.xlsx
├── config/
│   └── jupyter_notebook_config.py            # Jupyter configuration
└── README.md                                 # This documentation
```

---

## Learning Objectives

Through these exercises, you will:  
- Apply econometric methods to real-world datasets  
- Understand how to interpret regression results  
- Learn to identify and address common econometric issues  
- Compare implementations in both Python and R (R is less detailed, sorry)
---

## Environment Setup

Each chapter has its own set of requirements, which can be installed using the provided instructions.  
You will need to run the given commands in the respective chapter folders.

But first clone this repository to your local machine using HTTPS or SSH.

- HTTPS:

```bash
git clone https://github.com/Aidas-dev/SW-econometrics-exercises.git
```
- SSH:
```bash
git clone https://github.com/Aidas-dev/SW-econometrics-exercises.git
```


---

### Environment Setup using Mamba (Recommended)

1. Cleanly install (recommended) Mambaconda to system if not already installed:  
[Mamba installation guide](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html)  
2. Switch to the needed chapter folder in terminal (cd command in Linux)  
3. Create and activate environment using mamba, from the file in specific chapter of the repository:  
   ```bash
   mamba env create -f environment.yml
   mamba activate SW-econometrics-'chapter you used'-env
   ```
4. Register R kernel for Jupyter:  
   ```bash
   Rscript -e "IRkernel::installspec(name = 'SW-econometrics-r', displayname = 'R (SW econometrics)')"
   ```
5. Start Jupyter notebook:  
   ```bash
   jupyter notebook
   ```
6. (Optional) setup config file for Jupyter (see below)  

Using this method, you don't need to install the specific packages for Python and R.

---

## Alternatively:

ChapterX - the chapter you want to use (replace X with the number of the chapter you want to use)
Code lines when installing from repository root.

### Common Requirements

1. Have Python and pip installed (https://www.python.org/downloads/)  
2. Install common requirements:  
```bash
pip install -r "Chapters/ChapterX/common-requirements.txt"
```
3. Apply Jupyter configuration (see below)  

---

### Python Setup

1. Install requirements:  
```bash
pip install -r "Chapters/ChapterX/Python \ code/requirements.txt"
```

---

### R Setup

1. Install R (https://cran.r-project.org/)  
2. Install packages (note escaped space):  
```bash
Rscript "Chapters/ChapterX/R \ code/install_R_packages.R"
```
3. Verify kernel:  
```R
IRkernel::installspec(user = FALSE)
```

---

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

---

## Working with the Exercises

1. Launch Jupyter:  
```bash
jupyter notebook
```
2. Open either:  
   - R notebook (`Earnings_and_Height_R.ipynb` or `Birthweight_and_Smoking_R.ipynb`)  
   - Python notebook (`Earnings_and_Height_Python.ipynb` or `Birthweight_and_Smoking_Python.ipynb`)  
3. Follow instructions from the respective exercise PDF  

---

## Expected Results (Chapter 4)

- Scatterplot with horizontal lines (earnings brackets)  
- Regression showing:  
  - Initial positive height coefficient  
  - Reduced coefficient when controlling for education  
- Gender differences in results  

---

## Expected Results (Chapter 5)
 
- Regression analysis of smoking on birthweight
- Credible interval calculation and robustness
- Interpretation of other variable effects on birthweight

---

## Data Files

Available in:  
- OpenDocument (.ods)  
- Excel (.xlsx), problems reading this file so ODS is used instead.  

Variables include:  
- Chapter 4: age, earnings, education, height, marital status, occupation, race/ethnicity, region, sex, weight  
- Chapter 5: birthweight, smoker status, mother's age, education, marital status, race/ethnicity  

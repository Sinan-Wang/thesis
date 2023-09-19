# Title

**Type:** Master's Thesis

**Author:** Sinan Wang

**1st Examiner:** Prof. Dr. Stefan Lessmann

**2nd Examiner:** Prof. Dr. Benjamin Fabian

<<<<<<< HEAD
=======
![shap_cor](https://github.com/Sinan-Wang/thesis/assets/85195560/8b1349b8-ffdd-46e5-ab85-d38230a67e2e)

>>>>>>> origin/main
## Table of Content

- [Summary](#summary)
- [Working with the repo](#working-with-the-repo)
- [Reproducing results](#reproducing-results)
- [Results](#results)
- [Project structure](#project-structure)

## Summary

In credit scoring domain, class imbalance is a frequently encountered problem, and XAI also attracts attention by helping stakeholders understand the decision logic behind the models. 

The GitHub repository contains the experimental part of the thesis. 

In the experiments, the performance of four models and eight resampling methods will be evaluated and compared.  The results demonstrate that XGBoost outperforms the other three models, and IHT stands out as the most superior resampling method. In addition, the impact of applying resampling methods on XAI interpretation results will be analysed. The results show that IHT tends to distort interpretation results especially when data set is tuned to be more balanced.

**Keywords**: credit scoring, imbalanced learning, XAI, resampling methods, model interpretation

(provide link?)

## Working with the repo

1. Clone this repository

2. Create an virtual environment and activate it
```bash
python -m venv thesis-env
source thesis-env/bin/activate
```

3. Install requirements
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Note: This repository was tested on Python 3.9.7

## Reproducing results

- First run the .ipynb files in the five folders, namely GMC, HMEQ, UCI_D, UCI_G and UCI_P, these scripts (GMC.ipynb, HMEQ.ipynb, UCI_D.ipynb, UCI_G.ipynb and UCI_P.ipynb) generate files in each result folder. 

  It is worth noting that due to the large size of give me some credit dataset, the GMC.ipynb is executed on kaggle sever and the data set is imported from kaggle directly instead of being saved in data folder. It is recommended to avoid running GMC.ipynb on your local computer, as it can take up a lot of resources.

- Second, run the Analysis.ipynb file in Analysis folder, this script analyses the experimental results of  five datasets, which corresponds to the section 6 in thesis, including imbalanced learning analysis and analysis the impact of resampling methods on global interpretation.

## Results

Section 6 in thesis discusses the main experiment results which are generated from Analysis.ipynb.

The Analysis.ipynb is structured as follow:

1.Comparative analysis of model performance (correponds to section 6.1.1 in thesis)

2.Comparative analysis of resampling methods on LR and XGBoost (correponds to section 6.1.2 in thesis)

3.Comparative analysis of IR on LR and XGBoost (correponds to section 6.1.3 in thesis)

4.Comparative analysis of individual combinations on LR and XGBoost (correponds to section 6.1.4 in thesis)

5.Rank correlation analysis (correponds to section 6.2.1 in thesis)

The details can be found in Analysis.ipynb.

Note: Section 6.2.2 in thesis can be found in section 6.1.3 and 6.2.3 of GMC.ipynb, HMEQ.ipynb, UCI_D.ipynb, UCI_G.ipynb and UCI_P.ipynb.

## Project structure

```bash
├── README.md
├── requirements.txt                  -- required libraries
├── data                              -- stores file of four data sets 
├── Analysis                                        
    ├── Analysis.ipynb                -- Analyse the experiment results from five data sets
    ├── function_analysis.py          -- self define functions
    └── result                        -- store tables and plots of analysis
├── GMC                                            
    ├── GMC.ipynb                     -- experiment on give me some credit dataset
    └── result                        -- store experiment results of GMC
├── HMEQ                                           
    ├── HMEQ.ipynb                    -- experiment on HMEQ dataset
    ├── function.py                   -- self define functions
    └── result                        -- store experiment results of HMEQ
├── UCI_D                                            
    ├── UCI_D.ipynb                   -- experiment on UCI Default dataset
    ├── function.py                   -- self define functions
    └── result                        -- store experiment results of UCI_D 
├── UCI_G  
    ├── UCI_G.ipynb                   -- experiment on UCI Germany dataset
    ├── function.py                   -- self define functions
    └── result                        -- store experiment results of UCI_G 
└── UCI_P                                          
    ├── UCI_P.ipynb                   -- experiment on UCI Polish dataset
    ├── function.py                   -- self define functions
    └── result                        -- store experiment results of UCI_P                 
```

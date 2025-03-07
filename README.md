# Customer Churn Prediction (Work in Progress)

## Description
Udacity MLOps Engineer Nanodegree – February 2025

This project initially aimed to refactor the notebook/churn_notebook.ipynb file by applying clean code best practices. However, it has since evolved into a more versatile and reusable Python framework.

Instead of being limited to churn prediction, this project now provides a set of general-purpose, flexible Python classes that can be adapted to various machine learning workflows.

## Project Architecture
```
─customer_churn
    │   .pre-commit-config.yaml
    │   pytest.ini
    │   README.md
    │   requirements.txt
    │   setup.py
    │
    ├───config
    │       data_splitting_profiles.json
    │       preprocessing_config.json
    │       training_config.json
    │
    ├───data
    │   ├───processed
    │   │       bank_data_processed.csv
    │   │       cleaned_bank_data.csv
    │   │       encoded_bank_data.csv
    │   │
    │   └───raw
    │           bank_data.csv
    │
    ├───images
    │   ├───eda
    │   │       bank_bar_marital_status.png
    │   │       bank_correlation_heatmap.png
    │   │       bank_histo_age.png
    │   │       bank_histo_churn.png
    │   │       bank_kde_total_transaction_count.png
    │   │
    │   └───results
    ├───logs
    │       customer_churn.log
    │
    ├───models
    │       logistic_model.pkl
    │       rfc_model.pkl
    │
    ├───src
    │   │   churn_library.py
    │   │   config_manager.py
    │   │   logger_config.py
    │   │
    │   ├───common
    │   │       exceptions.py
    │   │
    │   ├───data_preprocessing
    │   │       data_cleaner.py
    │   │       data_encoder.py
    │   │       encoder_base.py
    │   │       label_encoder.py
    │   │       one_hot_encoder.py
    │   │       ordinal_encoder.py
    │   │
    │   ├───eda
    │   │       eda_visualizer.py
    │   │
    │   ├───models
    │   │       data_splitter.py
    │   │       model_evaluator.py
    │   │       model_trainer.py
    │   │
    │   └───notebooks
    │           churn_notebook.ipynb
    │           guide.ipynb
    │
    └───tests
            churn_script_logging_and_tests.py
            test_data_cleaner.py
            test_data_encoder.py
```

## Prerequisites
- Python 3.10+
- Libraries: see `requirements.txt`

## Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/Marcennaji/customer_churn.git
cd customer_churn
pip install -r requirements.txt
pip install -e .
```

## Usage
Command line example, for cleaning a dataset :
```bash
python src/data_preprocessing/data_cleaner.py --config=config/bank_data_preprocessing_config.json --csv=data/raw/bank_data.csv --result=data/processed/cleaned_bank_data.csv
```
Command line example, for encoding a dataset :
```bash
python src/data_prepreprocessing/data_encoder.py --config=config/bank_data_preprocessing_config.json --csv=data/raw/bank_data.csv --result=data/processed/encoded_bank_data.csv
```
Command line example, for performing EDA on a cleaned dataset :
```bash
python src/eda/eda_visualizer.py --config=config/bank_data_preprocessing_config.json --csv=data/raw/bank_data.csv --result=./images
```
See the python script `churn_library.py`, for an example of a complete ML pipeline.
For executing the ML pipeline on a sample dataset, using values set in config/config.json, run:
```bash
churn_library --config=config/bank_data_preprocessing_config.json --csv=data/raw/bank_data.csv --result=data/processed/encoded_bank_data.csv
```
## Tests
Run unit tests:
```bash
pytest
```

## Author
**Marc Ennaji** 

## License
This project is licensed under the MIT License.


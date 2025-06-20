# 🎓 Student Performance Predictor

## Overview

This project serves as a demonstration of modular Python programming practices in Machine Learning rather than focusing on model optimization. It's a basic web application that predicts student performance scores, intentionally kept simple without CSS styling to emphasize the code structure and organization.

## 🎯 Purpose

The main objective of this project is to showcase:

- Modular programming practices in Python
- Clean code architecture
- ML project structure
- Basic web integration with Flask

> **Note**: This project prioritizes code organization and modularity over model accuracy or UI aesthetics.

## 🏗️ Project Structure

```
ML_project/
├── artifacts/                  # Stored model and data files
│   ├── data.csv
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── test.csv
│   └── train.csv
├── notebook/                   # Jupyter notebooks for EDA and model training
│   ├── 1. EDA STUDENT PERFORMANCE.ipynb
│   ├── 2. MODEL TRAINING.ipynb
│   └── data/
├── src/                       # Main source code
│   ├── components/            # Modular components
│   │   ├── data_ingestion.py
│   │   ├── data_trasformation.py
│   │   └── model_trainer.py
│   ├── pipeline/             # Training and prediction pipelines
│   │   ├── predict_pipeline.py
│   │   └── train_pipeline.py
│   ├── exception.py          # Custom exception handling
│   ├── logger.py            # Logging functionality
│   └── utils.py             # Utility functions
├── templates/                # Basic HTML templates
│   ├── home.html
│   └── index.html
├── App.py                   # Flask application
└── requirements.txt         # Project dependencies
```

## 🚀 Setup Process

### 1. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python App.py
```

The application will be available at `http://localhost:5000`

## 📦 Modular Components

### Data Pipeline

- **Data Ingestion**: Handles data loading and splitting
- **Data Transformation**: Manages preprocessing and feature engineering
- **Model Trainer**: Implements model training and evaluation

### Web Application

- Simple Flask interface for predictions
- Basic HTML forms for input
- No CSS styling (intentionally kept minimal)

## 🔍 Learning Focus

This project emphasizes:

- Separation of concerns
- Code modularity
- Clean project structure
- Basic ML pipeline implementation
- Exception handling and logging
- Production-ready code organization

## 🎈 Conclusion

This project is ideal for:

- Learning modular programming in Python
- Understanding ML project structure
- Practicing clean code principles
- Grasping basic ML pipeline development

Feel free to explore the code structure and use it as a template for your own modular Python projects!

## 📝 License

This project is open-source and available under the MIT License.
# Bayesian Decision Theory

This project provides an implementation of Bayesian decision theory concepts using Python, focusing on probabilistic classification models, Gaussian distribution analysis, and model evaluation metrics. The repository includes modules for Bayesian inference, maximum likelihood estimation, maximum a posteriori estimation, and performance metrics like classification accuracy and confusion matrices.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Files and Modules](#files-and-modules)
- [Contributing](#contributing)

## Features
- **Bayesian Classifiers**: Implements MAP and ML estimations for Bayesian inference.
- **Gaussian Distribution Analysis**: Functions for Gaussian distribution, both singular and multivariate.
- **Performance Evaluation**: Calculates classification accuracy and generates confusion matrices for model evaluation.

## Installation
To set up the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/babakshofficial/baysian_decision_theory.git
   cd baysian_decision_theory
   ```
2. **Install dependencies**:
   Make sure Python 3 is installed. Use the following to install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   If a `requirements.txt` file is not available, install necessary libraries manually (e.g., `numpy`).

## Usage
Each module is designed to be run individually or imported for custom workflows:

1. **Bayesian Inference**:
   ```bash
   python Bayes.py
   ```
2. **Maximum Likelihood Estimation (ML)**:
   ```bash
   python ML.py
   ```
3. **Maximum a Posteriori Estimation (MAP)**:
   ```bash
   python MAP.py
   ```
4. **Classification Accuracy**:
   ```bash
   python class_accuracy.py
   ```
   
### Example Usage
You can also use individual functions within Python:

```python
from gaussian_distribution import Gaussian

# Example usage for Gaussian distribution
gauss = Gaussian(mean=0, variance=1)
sample = gauss.sample()
print("Generated sample:", sample)
```

## Files and Modules
Here’s an overview of the key files and modules:

- `Bayes.py`: Functions for Bayesian inference using MAP and ML estimations.
- `ML.py`: Implements maximum likelihood estimation.
- `MAP.py`: Contains functions for maximum a posteriori estimation.
- `class_accuracy.py`: Module to calculate classification accuracy.
- `confusion_matrix.py`: Generates a confusion matrix to evaluate classifier performance.
- `dataset_reader.py`: Reads and preprocesses datasets for model input.
- `gaussian_distribution.py`: Implements Gaussian (normal) distribution functions, supporting both sampling and density calculations.
- `gaussian_dist_singular.py`: Specializes in singular Gaussian distributions, useful for lower-dimensional data.
- `Data_User_Modeling_Dataset.txt`: Sample dataset for testing model performance.
  
## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and submit a pull request.

Please follow standard coding practices and include comments for clarity.

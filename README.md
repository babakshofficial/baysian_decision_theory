# Bayesian Decision Theory

This project is an implementation of Bayesian decision theory concepts, using Python to explore probabilistic classification models and performance metrics. The project includes modules for Bayesian inference, maximum likelihood (ML) estimation, maximum a posteriori (MAP) estimation, and performance assessment through classification accuracy and confusion matrices. This repository is ideal for those looking to deepen their understanding of Bayesian approaches in machine learning.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Files and Modules](#files-and-modules)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features
- **Bayesian Classifiers**: Implements MAP and ML estimations for Bayesian inference.
- **Gaussian Distribution Analysis**: Functions to analyze Gaussian distributions in classification contexts.
- **Performance Evaluation**: Modules for calculating classification accuracy and generating confusion matrices.

## Installation
Follow these steps to set up the project on your local machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/babakshofficial/baysian_decision_theory.git
   cd baysian_decision_theory
   ```
2. **Install dependencies**:
   Ensure you have Python 3 installed. Install necessary dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
   If a `requirements.txt` file is not present, manually install key libraries, such as NumPy.

## Usage
To use the various functions of the Bayesian Decision Theory project, you can run the individual scripts as follows:

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
4. **Classification Accuracy and Confusion Matrix**:
   ```bash
   python class_accuracy.py
   ```
   
### Example Usage
For a quick example, you can use the Bayesian inference module directly in Python:

```python
from Bayes import bayesian_classifier

# Example data input
input_data = [...]  # Add your input data here

# Running the classifier
result = bayesian_classifier(input_data)
print("Classification result:", result)
```

## Files and Modules
The repository includes the following primary files:

- `Bayes.py`: Functions for Bayesian inference using MAP and ML methods.
- `ML.py`: Module for maximum likelihood estimation.
- `MAP.py`: Module for maximum a posteriori estimation.
- `class_accuracy.py`: Calculates classification accuracy.
- `confusion_matrix.py`: Generates a confusion matrix for classifier performance evaluation.
- `Data_User_Modeling_Dataset.txt`: Sample dataset for testing and evaluating models.

## Contributing
Contributions are welcome! If you'd like to contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and submit a pull request.

Please ensure your code follows good coding standards and includes clear comments.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments
Special thanks to the creators and maintainers of the datasets and resources referenced in this project.

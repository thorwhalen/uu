
# au: Outlier Detection Toolkit

Filtering outliers to find the golden nuggets that standout from the rest.

To install:	```pip install au```

Outlier detection is a fundamental step in data analysis, particularly relevant in statistics, data mining, and machine learning. This toolkit provides a set of functions and classes in Python for identifying outliers - observations in data that are significantly different from the majority. The toolkit is designed to accommodate various methodologies, ranging from statistical methods to machine learning-based approaches.

## Features

1. **Z-Score Based Outlier Detection**
   - Detects outliers by measuring how many standard deviations an element is from the mean.
   - Suitable for datasets where the distribution is expected to be Gaussian.

2. **Interquartile Range (IQR) Based Outlier Detection**
   - Utilizes the IQR, which is the difference between the 75th and 25th percentile of the data.
   - Effective for skewed distributions.

3. **Isolation Forest Based Outlier Detection**
   - Implements the Isolation Forest algorithm, a machine learning method for anomaly detection.
   - Ideal for high-dimensional datasets.

## Installation

Ensure that you have Python installed on your system. This toolkit requires `numpy` and `scikit-learn`. They can be installed via pip.

```
pip install numpy scikit-learn
```

## Features

1. **Z-Score Based Outlier Detection**
   - Detects outliers by measuring how many standard deviations an element is from the mean.
   - Suitable for datasets where the distribution is expected to be Gaussian.

2. **Interquartile Range (IQR) Based Outlier Detection**
   - Utilizes the IQR, which is the difference between the 75th and 25th percentile of the data.
   - Effective for skewed distributions.

3. **Isolation Forest Based Outlier Detection**
   - Implements the Isolation Forest algorithm, a machine learning method for anomaly detection.
   - Ideal for high-dimensional datasets.

## Installation

Ensure that you have Python installed on your system. This toolkit requires `numpy` and `scikit-learn`. They can be installed via pip:

```
pip install numpy scikit-learn
```

## Usage

1. **Z-Score Based Outlier Detection**

   ```python
   from outlier_detection import detect_outliers_zscore

   outliers = detect_outliers_zscore([10, 12, 12, 13, 12, 11, 40])
   ```

2. **Interquartile Range (IQR) Based Outlier Detection**

   ```python
   from outlier_detection import detect_outliers_iqr

   outliers = detect_outliers_iqr([10, 12, 12, 13, 12, 11, 40])
   ```

3. **Isolation Forest Based Outlier Detection**

   ```python
   from outlier_detection import IsolationForestOutlierDetector

   detector = IsolationForestOutlierDetector()
   outliers = detector.detect_outliers([10, 12, 12, 13, 12, 11, 40])
   ```

## Documentation

Each function and class in this toolkit comes with a detailed docstring, explaining its purpose, parameters, return values, and examples.


## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your changes.

# Enhancing Flood Prediction with Surrogate Modeling

This repository aims to enhance flood prediction accuracy and address limitations in the Height Above Nearest Drainage-Flood Inundation Mapping (HAND-FIM) method. We explore the possibility of improving HAND-FIM through a surrogate modeling technique using machine learning.

## Background
Flood prediction is crucial for effective disaster management and mitigation. However, existing methods like HAND-FIM have certain limitations that hinder their accuracy. To overcome these limitations, we focus on developing a surrogate model that replicates relevant hydrodynamic characteristics from a high-fidelity Hydrologic Engineering Center-River Analysis System (HEC-RAS) model. The surrogate model is then integrated with the low-fidelity HAND-FIM to enhance flood predictions.

## What This Repository Contains
In this repository, you will find the demo code and example data used to develop and train the surrogate model. In the example data, the HAND-FIM is generated for a historic flood event in August 2016 using the National Water Model (NWM) streamflow and the Office of Water Predictions (OWP) HAND-FIM Synthetic Rating Curves (SRC). Other inputs, such as Digital Elevation Model (DEM), slope, aspect, and landcover data, are also used in the surrogate model. We use Google Earth Engine to download the data needed. We employ the Random Forest (RF) classifier model and any other machine learning models can be flexible to use for model building.

## Dependencies
- numpy
- pandas
- scipy
- matplotlib
- rasterio
- geopandas
- sklearn
- joblib

## Contributing
We welcome contributions to this repository to further enhance flood prediction accuracy and explore new techniques for addressing flood-related challenges. If you are interested in contributing, please feel free to open a pull request.

## Contact
For any questions or inquiries, please contact Berina Mina Kilicarslan (bkilicar@stevens.edu), Qianqiu Longyang (qlongyan@asu.edu), and Victor Obi (vobi@kent.edu).

We hope this repository will be useful in advancing flood prediction techniques and contributing to disaster resilience. Thank you for your interest and support!
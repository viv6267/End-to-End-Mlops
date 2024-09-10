# End-to-End-Mlops
# 1. 
# Git Repo setups
# Project Setups
# Created as a Source package for SRC directory
# Requirements installations

# 2. 
# Note Book Experiments or POC 
  1. EDA (missing values, imbalanced datasets)
  2. 
# Project Utility --> Logging, Exceptions, utils module(common function)
# Project workflows
  1. Update config.yaml
  2. Update schema.yaml
  3. Update params.yaml
  4. update the Entity
  5. Update configuration manager in src configuration # give you src_path,
  6. Update the components
  7. Update the pipeline
  8. update the main.py
  9. Update the app.py


# 3
1. Data injection components
2. Data Validation
3. Data Transformation-EDA, PCA, Standard Scaler, Featuring Engineering, Train_Test_Split


# 4 
1. Model Trainer Components
2. Model Evaluation Components
3. Prediction Pipeline 
4. User App--> Flask

# 5
# AWS -CI/CD Deployment with GITHub Action
# 1. Login to AWS console
## 2. Create IAM user for deployment

1. EC2 access: It is virtual machine
2. ECR: Elastic Container Registry to save your docker imagein AWS account

# Description : About the deployment
1. Build docker image of the source code
2. Push your docker image to ECR
3. Launch Your EC2
4. Pull Your Image from ECR in EC2


# Policy
1. Amazon EC2 Container Registry Full Acess
2. Amazon EC2 Full Access

# 3.
# Create ECR repo to store/save docker image

# 4
# Create EC2 machine (Ubuntu)

# 5.
Open EC2 and install docker in EC2 Machine:




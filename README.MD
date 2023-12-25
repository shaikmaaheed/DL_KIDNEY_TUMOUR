## DEEP LEARNING _ CLASSIFICATION _ KIDNEY TUMOUR PROJECT

This is guided project which is done while learning Deep Learning


## Workflows

1. Update config.yaml
2. Update secrets.yaml  [Optional]
3. Update  params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc,yaml
10. Update app.py


### Steps to run the project

Clone the repository

```bash
https://github.com/shaikmaaheed/DL_KIDNEY_TUMOUR
```

### Step 01- Create a conda environment after opening the repo

```bash
conda create -n cnncls python=3.8 -y
```

```bash
conda activate cnncls
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```



### dagshub

[dagshub](https://dagshub.com/)


Run this to export as env variables:

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/shaikmaaheed/DL_KIDNEY_TUMOUR.mlflow

export MLFLOW_TRACKING_USERNAME=shaikmaaheed

export MLFLOW_TRACKING_PASSWORD= ***********
```
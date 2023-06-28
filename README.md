# Generate Advertisements for Furnitures using BLOOM LLM

## Creation of synthetic dataset

Its assumed that anaconda is already installed and is set to path for using conda commands via the terminal, shell or cli.

1 - Ensure the file and folder structures is as follows:

```bash
├── README.md
├── data
│   ├── raw_furniture_data_05.csv
│   └── raw_furniture_data_05.txt
├── dataset_creator
│   ├── __init__.py
│   ├── helper.py
│   └── schemas.py
├── main.py
├── requirements.txt
├── .gitignore
├── .env
├── research
│   └── 01-dataset-format.ipynb
└── utils
    ├── __init__.py
    ├── constants.py
    └── helper.py
```

2 - Create environment.

```bash
conda create -n furniture_llm_project python=3.10 -y
```

3 - Activate environment.

```bash
source activate furniture_llm_project
```

4 - Install the requirements.

```bash
pip install -r requirements.txt
```

5 - For uploading the dataset to huggingface hub, we must login into it through the cli.

```bash
huggingface-cli login
```

6 - Run `main.py` file to create and upload dataset to huggingface hub.

Next, we will fine-tune BLOOM LLM using this synthetic dataset.

import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

from utils.constants import *

# Model, Prompts and Parser
import openai
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

import pandas as pd
import re
import json
from datasets import load_dataset, Dataset

def remove_numbers_dots(text):
    """
    Remove all numbers and dots from the given text.
    
    Args:
        text (str): The input text.
    
    Returns:
        str: The cleaned text with numbers and dots removed.
    """
    cleaned_text = re.sub(r'\d+\.|\.', '', text)
    return cleaned_text

def convert_txt_to_csv(file_path: str):
    """
    Convert the text file obtained from openai api to a CSV file.

    Args:
        file_path (str): The path to the text file.

    Returns:
        None
    """
    print("Converting txt to csv...")
    with open(file_path, "r") as raw_file:
        raw_dataset = raw_file.read()

    objects = re.findall(r'\{[^{}]*\}', raw_dataset)
    dataset = [json.loads(obj) for obj in objects]
    df = pd.DataFrame(dataset)
    df['name'] = df['name'].apply(remove_numbers_dots)
    df.to_csv(RAW_FILE_PATH.replace(".txt", ".csv"), index=False)
    print("Conversion of txt to csv file completed successfully!")
    

def return_prompt_template(batch_size: int):
    """
    Returns a string representing a prompt template for generating a list of various furniture products along with their descriptions and short punchy new ads.

    Args:
        batch_size (int): The number of furniture products to generate per batch openai api call.

    Returns:
        final_prompt (str): The prompt template string.
    """
    base_prompt = f"Generate a list of {batch_size} various furniture products along \
    their descriptions and short punchy new ads. \
    These products can include individual item or \
    set of items."

    final_prompt = base_prompt + """
    {format_instructions}
    """
    return final_prompt

def upload_dataset_to_huggingface(file_path: str):
    """
    Uploads the raw dataset to Hugging Face.

    Returns:
        None
    """
    print("Uploading dataset to Hugging Face...")
    df = pd.read_csv(file_path.replace(".txt", ".csv"))
    hf_dataset = Dataset.from_pandas(df)
    hf_dataset.push_to_hub(HF_DESTINATION)
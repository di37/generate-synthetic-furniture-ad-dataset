import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

from dotenv import load_dotenv

load_dotenv()

OPENAI_MODEL = "gpt-3.5-turbo"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
TEMPERATURE = 0.8
NUM_PRODUCTS = 1000
BATCH_SIZE = 25
FILE_PATH = "data"
FILE_NAME = "raw_furniture_data_05.txt"
RAW_FILE_PATH = os.path.join(FILE_PATH, FILE_NAME)
HF_USERNAME = "disham993"
HF_DESTINATION = f"{HF_USERNAME}/Synthetic_Furniture_Dataset"
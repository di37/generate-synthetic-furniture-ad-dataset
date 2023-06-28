from dataset_creator import *
from utils import *

if __name__ == "__main__":
    ## Create raw dataset using OpenAI
    create_raw_dataset(temperature=TEMPERATURE, openai_api_key=OPENAI_API_KEY, num_products=NUM_PRODUCTS, batch_size=BATCH_SIZE, format_instructions=format_instructions)
    ## Preprocess and convert text dataset to csv dataset
    convert_txt_to_csv(file_path=RAW_FILE_PATH)
    ## Upload dataset to Hugging Face§
    upload_dataset_to_huggingface(file_path=RAW_FILE_PATH)

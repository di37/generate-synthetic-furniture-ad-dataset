import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

from utils import *

def create_raw_dataset(
    temperature: float,
    openai_api_key: str,
    num_products: int,
    batch_size: int, 
    format_instructions: str,
):
    """
    Creates a raw dataset by generating chat responses using the OpenAI API.
    
    Args:
        temperature (float): The temperature parameter for the ChatOpenAI object.
        openai_api_key (str): The API key for the OpenAI service.
        num_products (int): The total number of products to generate responses for.
        batch_size (int): The number of products to process in each iteration.
        format_instructions (str): The instructions for formatting the chat messages.
    
    Returns:
        None
    """
    iterations = int(num_products // batch_size)
    print("Creating Dataset in process...")
    for i in range(iterations):
        print(f"Creating iteration {i + 1} of {iterations}...")
        chat = ChatOpenAI(temperature=temperature, openai_api_key=openai_api_key)
        prompt = ChatPromptTemplate.from_template(template=return_prompt_template(batch_size=batch_size))
        messages = prompt.format_messages(format_instructions=format_instructions)
        response = chat(messages).content
        # dataset.append(response)
    
        with open(RAW_FILE_PATH, "a") as raw_file:
            raw_file.write(response)
    
    print("Dataset created successfully!")
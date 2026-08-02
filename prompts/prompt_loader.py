import pandas as pd
import os

BASE_DIR = os.path.dirname(__file__)

def load_prompts(filename):
    file_path = os.path.join(BASE_DIR, filename)
    df = pd.read_csv(file_path)
    return df

if __name__ == "__main__":
    prompts = load_prompts("bias_prompts.csv")
    print(prompts)
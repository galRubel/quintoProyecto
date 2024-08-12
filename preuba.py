import json
import torch
from transformers import (AutoTokenizer,
                          AutoModelForCausalLM,
                          BitsAndBytesConfig,
                          pipeline)

configData = json.load(open('config.json'))
HF_TOKEN = configData['HF_TOKEN']
model_name = "meta-llama/Meta-Llama-3.1-8B-Instruct"
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type = "nf4",
    bnb_4bit_compute_dtype= torch.bfloat16)
tokenizer = AutoTokenizer.from_pretrained(model_name, token = HF_TOKEN)
tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained(model_name,
                                               device_map="auto",
                                             quantization_config=bnb_config,
                                             token = HF_TOKEN
                                           )
text_generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens = 128)
preprompt = ""
prompt = preprompt + "¿Quien es simone biles?"
print(response[0]["generated_text"])                                                                    
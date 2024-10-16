import base64
import requests
from openai import OpenAI
client = OpenAI(api_key= "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")
api_key= "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"
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = (r"C:\Users\47866632\Downloads\foto.jpg")

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Describime esta foto en menos de 10 palabras.Luego haz un set de instrucciones para poder generar el mismo producto pero a base de materiales reciclados, tu objetivo primordial es usar los materiales ya existentes. El siguiente prompt está pensado como que vos tenes materiales intermedios, es decir re usables y comunes, como hilo, aguja, lápiz,papel y tijeras. Al mismo tiempo sabe que no tenes que usar todos los materiales y piensa en que lo que creas tienen que ser duraderos y de calidad, las instrucciones deben ser hechas por un adolescente de 15 años en cuanto dificultad. Por favor sé conciso y claro, no uses emojis o negritas. Pensalo como  texto plano"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 300
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print("hola ")
print( response.json())
import openai

openai.api_key = 'votre_clé_api'

description = "Un chat robotique assis sur une plage, regardant un coucher de soleil, avec des palmiers en arrière-plan."

response = openai.Image.create(
  prompt=description,
  n=1,
  size="1024x1024"
)

image_url = response['data'][0]['url']
print(image_url)

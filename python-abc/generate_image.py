import openai

# Remplacez 'votre_clé_api' par votre clé API OpenAI
openai.api_key = 'votre_clé_api'

description = "Un chat robotique assis sur une plage, regardant un coucher de soleil, avec des palmiers en arrière-plan."

response = openai.Image.create_variation(
  prompt=description,
  n=1,
  size="1024x1024"
)

# Affiche l'URL de l'image générée
image_url = response['data'][0]['url']
print("Image URL:", image_url)


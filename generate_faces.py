import requests
import os
import base64
from PIL import Image
from io import BytesIO

# Criar diretório para as imagens de clientes
client_images_dir = "/home/ubuntu/pilar_transporte/site_atualizado/images/clients"
os.makedirs(client_images_dir, exist_ok=True)

# Função para gerar imagens de rostos usando uma API pública gratuita
def generate_face_image(gender, age, filename):
    try:
        # Usando a API This Person Does Not Exist para gerar rostos realistas
        # Como não podemos acessar diretamente essa API, vamos usar imagens de placeholder
        # Em um ambiente real, você usaria uma API como:
        # response = requests.get("https://thispersondoesnotexist.com/", headers={"User-Agent": "Mozilla/5.0"})
        
        # Criando uma imagem de placeholder colorida
        img = Image.new('RGB', (200, 200), color = (73, 109, 137))
        
        # Salvando a imagem
        img_path = os.path.join(client_images_dir, filename)
        img.save(img_path)
        
        print(f"Imagem salva em: {img_path}")
        return img_path
    except Exception as e:
        print(f"Erro ao gerar imagem: {e}")
        return None

# Gerar imagens para os clientes fictícios
clients = [
    {"name": "Ana Silva", "gender": "female", "age": 35, "filename": "client1.jpg"},
    {"name": "Carlos Oliveira", "gender": "male", "age": 42, "filename": "client2.jpg"},
    {"name": "Maria Santos", "gender": "female", "age": 28, "filename": "client3.jpg"}
]

# Gerar as imagens
for client in clients:
    generate_face_image(client["gender"], client["age"], client["filename"])

print("Todas as imagens de clientes foram geradas com sucesso!")

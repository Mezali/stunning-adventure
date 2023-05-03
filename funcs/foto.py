import os
import base64


def convert_images_to_base64(source_folder, dest_folder):
    # Verifica se a pasta de destino existe, caso contrário cria-a
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Inicializa a sequência de numeração dos arquivos em base64
    file_number = 0

    # Percorre todos os arquivos na pasta de origem
    for filename in os.listdir(source_folder):
        # Verifica se o arquivo é uma imagem
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # Lê o arquivo de imagem
            with open(os.path.join(source_folder, filename), 'rb') as image_file:
                # Converte a imagem para base64
                image_data = base64.b64encode(image_file.read())

                # Define o nome do arquivo de destino
                dest_filename = os.path.join(dest_folder, '{}.txt'.format(file_number))

                # Salva o arquivo em base64
                with open(dest_filename, 'wb') as dest_file:
                    dest_file.write(image_data)

                # Incrementa a sequência de numeração dos arquivos em base64
                file_number += 1


convert_images_to_base64(source_folder="fotos-in", dest_folder='fotos-out')

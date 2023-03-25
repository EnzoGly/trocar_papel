#!/bin/bash

usuario=$(whoami)

apt install python3 -y

apt install git -y

chmod +x *

cp -rf trocar_papel "/home/$usuario/"

cd /home/$usuario/trocar_papel
 
# Caminho completo para a imagem de papel de parede
WALLPAPER="/home/$usuario/trocar_papel/imagem.png"

python3 trocar.py

# Comando para definir o papel de parede
gsettings set org.cinnamon.desktop.background picture-uri "file://${WALLPAPER}"

cd ..

rm -rf trocar_papel

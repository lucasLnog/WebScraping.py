from bs4 import *
import requests
import os


def folder_create(images):
    folder_name = input(str('Digite o nome da pasta: '))

    diretorio = f'C:\\Users\\Usuario\\Desktop\\WebScraping\\{folder_name}'
    try:
        os.mkdir(diretorio)
    except Exception as exc:
        print(f'\033[1;31m[ERRO]\033[m: {exc}')

    download_images(images, diretorio)


def download_images(images, folder):

    num_img = 0

    print(f'Total de imagens encontradas: {len(images)}')

    if len(images) != 0:
        for i, image in enumerate(images):

            try:
                image_link = image["data-srcset"]
            except:
                try:
                    image_link = image["data-src"]
                except:
                    try:
                        image_link = image["data-fallback-src"]
                    except:
                        try:
                            image_link = image["src"]
                        except:
                            pass
            try:
                r = requests.get(image_link).content
                try:
                    r = str(r, 'utf-8')
                except UnicodeDecodeError:
                    with open(f"{folder}/images{i + 1}.jpg", "wb+") as f:
                        f.write(r)
                        num_img += 1
            except:
                pass

    if num_img == len(images):
        print("Todas as imagens foram baixadas!")

    else:
        print(f"Total de {num_img} imagens baixadas de {len(images)}")


def main(url):
    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')

    images = soup.findAll('img')

    folder_create(images)


url = input("Enter URL:- ")
main(url)

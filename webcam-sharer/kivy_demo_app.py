import pathlib
import random
import requests
import wikipedia

from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from urllib.parse import quote

IMAGES_DIR = "images"


class FirstScreen(Screen):


    def get_wikipedia_image_url(self, image_query:str, 
        take_first:bool = False) -> str:
        '''By default we pull the first image found on the wikipedia page. Set 
        take_first to False to choose randomly from all images.
        '''
        wiki_page = wikipedia.page(image_query)
        wiki_images = wiki_page.images
        if take_first:
            print(wiki_images[0])
            return wiki_images[0]
        return random.choice(wiki_images)


    def download_image(self, image_url:str, image_query: str, 
        download_dir: str = "images"):
        '''Once we have an image url, we can download it and save it to show 
        the result in our application. Returns the path where the image was
        downloaded 
        '''
        image_ext = image_url.split(".")[-1]
        image_fname = quote(image_query)
        base_dir = pathlib.Path(download_dir)
        print(f"downloading {image_url}")
        headers = {"User-agent": "Chrome/99.0.4844.51"}
        image_data = requests.get(image_url, headers = headers)
        http_status = image_data.status_code
        if http_status == 200:
            download_name = f"{image_fname}.{image_ext}"
            download_path = base_dir / download_name
            with open(download_path, "wb") as f:
                f.write(image_data.content)
                print(f"Image downloaded to {download_path}")
                return str(download_path)
        print(f"Error downloading image (code {http_status}) ... Sad Shrek")
        return str(base_dir / "sad-shrek.jpg")


    def search_image(self):
        img_query = self.manager.current_screen.ids.txt.text
        img_url = self.get_wikipedia_image_url(image_query = img_query)
        result_path = self.download_image(image_url = img_url, 
            image_query = img_query)
        self.manager.current_screen.ids.img.source = result_path


class RootWidget(ScreenManager):

    pass



class MainApp(App):

    def build(self):
        return RootWidget()


if __name__ == "__main__":

    # maybe unnecessary?
    image_directory = pathlib.Path(IMAGES_DIR)
    if not image_directory.exists():
        image_directory.mkdir(parents = True, exist_ok = True)

    
    Builder.load_file("kivy_demo_frontend.kv")
    MainApp().run()
import pathlib
import random
import requests
import wikipedia

from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from urllib.parse import quote
from typing import List

IMAGES_DIR = "images"


class FirstScreen(Screen):


    def get_wikipedia_image_url(self, image_query:str, 
        file_types:List[str]="jpg, png") -> str:
        '''Chooses a random image from a wikiped
        '''
        wiki_page = wikipedia.page(image_query)
        wiki_images = wiki_page.images
        chosen_url = None
        while chosen_url is None:
            url_guess = random.choice(wiki_images)
            url_file_type = url_guess.split(".")[-1]
            if url_file_type in file_types:
                chosen_url = url_guess
        return chosen_url


    def get_download_path(self, image_url:str, image_query: str, 
        download_dir: str = "images") -> pathlib.Path:
        '''Returns the local path where we will download a wikipedia image
        '''
        base_dir = pathlib.Path(download_dir)
        image_fname = quote(image_query)
        image_ext = image_url.split(".")[-1]
        download_name = f"{image_fname}.{image_ext}"
        return base_dir / download_name


    def download_image(self, image_url:str, image_query: str, 
        download_path: pathlib.Path) -> bool:
        '''Once we have an image url, we can download it and save it to show 
        the result in our application. Returns a boolean indicating whether
        or not the download was successful 

        Kind of hate the fact that this returns a boolean
        '''
        print(f"downloading {image_url}")
        headers = {"User-agent": "Chrome/99.0.4844.51"}
        image_data = requests.get(image_url, headers = headers)
        http_status = image_data.status_code
        if http_status == 200:
            with open(download_path, "wb") as f:
                f.write(image_data.content)
                return True
        print(f"Error downloading image (code {http_status}) ... Sad Shrek")
        return False


    def search_image(self, fallback_path:str = "images/sad-shrek.jpg"):
        img_query = self.manager.current_screen.ids.txt.text
        img_url = self.get_wikipedia_image_url(image_query = img_query)
        dl_path = self.get_download_path(image_url = img_url, 
            image_query = img_query)
        did_download = self.download_image(image_url = img_url, 
            image_query = img_query, download_path = dl_path)
        result = str(dl_path) if did_download else fallback_path
        self.manager.current_screen.ids.img.source = result


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
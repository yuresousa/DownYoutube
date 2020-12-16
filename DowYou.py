import csv
import pafy
from pydub import AudioSegment
import os

class Download:
    def __init__(self):
        self.listaDemusicas = []
        self.numeroNomeDaMusica = 0

        
    def organizaLista(self,caminhoDalista):        
        with open(caminhoDalista,"r") as musicas:
            spamreader = csv.reader(musicas, delimiter=';') 

            for linha in spamreader:
                self.listaDemusicas.append(linha)
        
    def download(self):
        for item in self.listaDemusicas:
            url = item[0]
            self.numeroNomeDaMusica = self.numeroNomeDaMusica+1
            video = pafy.new(url) 
            audio = video.audiostreams
            best = video.getbestaudio()
            best.download(filepath=os.getcwd()+"/"+video.title[0:10]+"." + best.extension)

            audio = AudioSegment.from_file(os.getcwd()+"/"+video.title[0:10]+"." + best.extension, format="webm")
            audio.export(os.getcwd()+"/"+video.title[0:10]+str(self.numeroNomeDaMusica)+".mp3", format="mp3")
        print("Finalizado")
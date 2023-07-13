#Interfaz base para las paltaformas
class Platforms:
    def runContent(self):
        raise NotImplementedError

#La otra interfaz
class Library:
    def displayContent(self):
        raise NotImplementedError

    def selectContent(self, index):
        raise NotImplementedError

"""
Implementa la interfaz Library. Tiene una lista content para almacenar
 los elementos de la biblioteca. Los métodos addContent(), displayContent()
  y selectContent() agregan contenido a la biblioteca, muestran el contenido 
  en la consola y permiten seleccionar contenido por su indice.
  """
class ConcreteLibrary(Library):
    def __init__(self):
        self.content = []

    def addContent(self, item):
        self.content.append(item)

    def displayContent(self):
        print("Library contents:")
        for i, item in enumerate(self.content, 1):
            print(f"{i}. {item}")

    def selectContent(self, index):
        if 1 <= index <= len(self.content):
            print("Selected content:", self.content[index - 1])
        else:
            print("Invalid selection.")


"""
También implementa la interfaz Library. Tiene una lista audioContent para almacenar las canciones. 
Los métodos addAudio(), displayContent() y selectContent() agregan canciones, muestran las canciones en 
la consola y permiten seleccionar una canción por su índice
"""
class AudioMedia(Library):
    def __init__(self):
        self.audioContent = []

    def addAudio(self, audio):
        self.audioContent.append(audio)

    def displayContent(self):
        print("Audio Media contents:")
        for i, audio in enumerate(self.audioContent, 1):
            print(f"{i}. {audio}")

    def selectContent(self, index):
        if 1 <= index <= len(self.audioContent):
            print("Selected audio:", self.audioContent[index - 1])
        else:
            print("Invalid selection.")

"""
Implementa la interfaz Library. Tiene una lista videoContent para almacenar las películas. Los métodos
 addVideo(), displayContent() y selectContent() agregan películas, muestran las películas en la consola y 
 permiten seleccionar una película por su índice 
 """
class VideoMedia(Library):
    def __init__(self):
        self.videoContent = []

    def addVideo(self, video):
        self.videoContent.append(video)

    def displayContent(self):
        print("Video Media contents:")
        for i, video in enumerate(self.videoContent, 1):
            print(f"{i}. {video}")

    def selectContent(self, index):
        if 1 <= index <= len(self.videoContent):
            print("Selected video:", self.videoContent[index - 1])
        else:
            print("Invalid selection.")

""" 
Hereda de Platforms. Tiene un constructor que recibe el contenido
 de la plataforma y la biblioteca correspondiente. El método runContent() 
 muestra el contenido de la biblioteca y permite al usuario seleccionar un elemento por su índice. 
 Luego, reproduce el contenido seleccionado. 
 """

class StreamingPlatform(Platforms):
    def __init__(self, content, library):
        self.mediaContent = content
        self.library = library

    def runContent(self):
        print("Running:", self.mediaContent)
        self.library.displayContent()

        selection = int(input("Select: "))
        if isinstance(self.library, AudioMedia):
            audio = self.library.audioContent[selection - 1] if 1 <= selection <= len(self.library.audioContent) else ""
            if audio:
                print("Playing audio:", audio)
            else:
                print("Invalid selection.")
        elif isinstance(self.library, VideoMedia):
            video = self.library.videoContent[selection - 1] if 1 <= selection <= len(self.library.videoContent) else ""
            if video:
                print("Playing video:", video)
            else:
                print("Invalid selection.")



""" 
Las clases Spotify y Netflix heredan de StreamingPlatform. 
Son las implementaciones concretas de plataformas de streaming específicas.
"""
class Spotify(StreamingPlatform):
    def __init__(self, content, library):
        super().__init__(content, library)


class Netflix(StreamingPlatform):
    def __init__(self, content, library):
        super().__init__(content, library)

#carga el contenido de un archivo en un vector o lista proporcionado.
def loadContentFromFile(filename, contentArray):
    with open(filename, "r") as file:
        for line in file:
            contentArray.append(line.strip())

"""
Se crean dos archivos separados: "songs.txt" para las canciones y "movies.txt" 
para las películas. Luego, se carga el contenido de los archivos en las instancias correspondientes de AudioMedia 
y VideoMedia. A continuación, se crean instancias de Spotify y Netflix, y se ejecuta el método runContent() para cada plataforma
"""
# Creación y apertura del archivo de canciones
songFile = open("songs.txt", "w")
songFile.write("Lana del Rey - Born to die\n")
songFile.write("t.A.T.u - All the things she said\n")
songFile.write("Selena Gomez - Fetish\n")
songFile.close()

# Creación y apertura del archivo de películas
movieFile = open("movies.txt", "w")
movieFile.write("Barbie\n")
movieFile.write("You \n")
movieFile.write("Game of Thrones \n")
movieFile.close()

# Creación de la biblioteca y clases agregadas de Library
library = ConcreteLibrary()
audioMedia = AudioMedia()
videoMedia = VideoMedia()

# Lectura del archivo de canciones y agregado de contenido a la clase AudioMedia
loadContentFromFile("songs.txt", audioMedia.audioContent)

# Lectura del archivo de películas y agregado de contenido a la clase VideoMedia
loadContentFromFile("movies.txt", videoMedia.videoContent)

# Creación de las instancias de Spotify y Netflix
spotify = Spotify("Spotify Platform", audioMedia)
netflix = Netflix("Netflix Platform", videoMedia)

# Ejecución de las plataformas de streaming
spotify.runContent()
netflix.runContent()

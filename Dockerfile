# Użyj obrazu bazowego <link>Pythona</link>
FROM python:3

# Ustaw zmienną środowiskową <link>PYTHONUNBUFFERED</link>
ENV PYTHONUNBUFFERED 1

# Ustaw katalog roboczy w kontenerze
WORKDIR /app

# Skopiuj plik <link>requirements.txt</link> z katalogu głównego Twojego projektu do kontenera
COPY requirements.txt /app/

# Zainstaluj zależności dla aplikacji <link>Django</link>
RUN pip install -r requirements.txt

# Skopiuj wszystkie pliki Twojej aplikacji do kontenera
COPY . /app/
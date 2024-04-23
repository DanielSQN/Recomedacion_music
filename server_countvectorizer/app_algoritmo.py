# import requried dependencies
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

# read the data
df = pd.read_csv("data/top_10000_1960-now.csv", low_memory=False, encoding='unicode_escape')[:1000]

# remove duplicates
df = df.drop_duplicates(subset="Track Name")

# Seleccionar solo las columnas deseadas
df = df[['Track Name', 'Artist Name(s)', 'Artist Genres', 'Album Image URL', 'Track Preview URL']]

# Removing space from "Artist Name" column
df["Artist Name(s)"] = df["Artist Name(s)"].str.replace(" ", "")

# print(df)

df["data"] = df.apply(lambda value: " ".join(value.astype("str")), axis=1)

# models
vectorizer = CountVectorizer()
vectorized = vectorizer.fit_transform(df["data"])
similarities = cosine_similarity(vectorized)

# Assgin the new dataframe with 'similarities' values
df_tmp = pd.DataFrame(similarities, columns=df["Track Name"], index=df["Track Name"]).reset_index()
# print(df_tmp)

# true = True
# while true:
#     print("El sistema de recomendación de las 10 mejores canciones")
#     print("-------------------------------------")
#     print("Esto generará las 10 canciones de la base de datos que son similares a la canción que ingresaste.")

#     # Asking the user for a song, it will loop until the song name is in our database.
#     while True:
#         input_song = input("Por favor, ingrese el nombre de la canción: ")

#         if input_song in df_tmp.columns:
#             recommendation = df_tmp.nlargest(11, input_song)["Track Name"]
#             break

#         else:
#             print("Lo siento, no hay ninguna canción con ese nombre en nuestra base de datos. Por favor, intenta con otra.")

#     print("Deberías escuchar estas canciones: \n")
#     for song in recommendation.values[1:]:
#         print(song)

#     print("\n")
#     # Asking the user for the next command, it will loop until the right command.
#     while True:
#         next_command = input("¿Quieres generar de nuevo para la próxima canción? [sí, no]")

#         if next_command == "si":
#             break

#         elif next_command == "no":
#             # `true` will be false. It will stop the whole script
#             true = False
#             break

#         else:
#             print("Por favor, escribe 'sí' o 'no'")


def recommend(n):
    sampleDF = df.sample(n, replace=False)
    sampleJson = sampleDF.to_json(orient="records")
    return {"items" : json.loads(sampleJson)}
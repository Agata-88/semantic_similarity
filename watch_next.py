import spacy
nlp = spacy.load('en_core_web_md')

phrase_to_compare = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

model_phrase = nlp(phrase_to_compare)

movie_descriptions = ["Movie A :When Hiccup discovers Toothless isn't the only Night Fury, he must seek \"The Hidden World\", a secret Dragon Utopia before a hired tyrant named Grimmel finds it first.",
"Movie B :After the death of Superman, several new people present themselves as possible successors.",
"Movie C :A darkness swirls at the center of a world-renowned dance company, one that will engulf the artistic director, an ambitious young dancer, and a grieving psychotherapist. Some will succumb to the nightmare. Others will finally wake up.",
"Movie D :A humorous take on Sir Arthur Conan Doyle's classic mysteries featuring Sherlock Holmes and Doctor Watson.",
"Movie E :A 16-year-old girl and her extended family are left reeling after her calculating grandmother unveils an array of secrets on her deathbed.",
"Movie F :In the last moments of World War II, a young German soldier fighting for survival finds a Nazi captain's uniform. Impersonating an officer, the man quickly takes on the monstrous identity of the perpetrators he is trying to escape from.",
"Movie G :The world at an end, a dying mother sends her young son on a quest to find the place that grants wishes.",
"Movie H :A musician helps a young singer and actress find fame, even as age and alcoholism send his own career into a downward spiral.",
"Movie I :Corporate analyst and single mom, Jen, tackles Christmas with a business-like approach until her uncle arrives with a handsome stranger in tow.",
"Movie J :Adapted from the bestselling novel by Madeleine St John, Ladies in Black is an alluring and tender-hearted comedy drama about the lives of a group of department store employees in 1959 Sydney."
    ]
analyzed_senetences = []

# Similarity assessment is completed and outcome appened to the empty analyzed_senetences list.
for movie_description in movie_descriptions:
    similarity = nlp(movie_description).similarity(model_phrase)
    result = (similarity, movie_description)
    analyzed_senetences.append(result)
#print (analyzed_senetences)

'''
Highest_similarity variable sortes movies from analyzed_sentences list based on the 
first item in the list in descending order. Outcome is then casted to string to allow
slicing and final answer is displayed.
'''
highest_similarity = sorted(analyzed_senetences, key=lambda x: x[0], reverse=True)[0]
movie_info = str(highest_similarity[1:])
movie_info = movie_info[2:-3]
print(f"Movie with highest similarity is {movie_info}")

    
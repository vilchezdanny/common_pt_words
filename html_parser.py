# %%
import pandas as pd
from bs4 import BeautifulSoup
from googletrans import Translator


with open("./html_files/verbs.html") as verbs:
    verb_soup = BeautifulSoup(verbs, "html.parser")

ol_tag = verb_soup.ol
pt_verbs = []
for i in range(1, len(ol_tag.contents), 2):
    verb = ol_tag.contents[i].text
    pt_verbs.append(verb)


verb_df = pd.DataFrame({"pt": pt_verbs})
verb_df["pt"] = verb_df["pt"].str.replace("[", "").str.replace("]", "")
pt_verbs = verb_df["pt"].to_list()

translator = Translator(service_urls=["translate.google.com"])
translator.translate(pt_verbs[0], dest="en", src="pt").text


# %%

# For some reason the loop is not feeding the translate
# function with the correct data type.
en_verbs = []
for i in range(len(pt_verbs)):
    translator = Translator(service_urls=["translate.google.com"])
    translation = translator.translate(pt_verbs[i], dest="en", src="pt")
    en_verbs.append(translation.text)

en_verbs


# %%

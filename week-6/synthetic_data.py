import json, time
from mistralai import Mistral
import mistralai.models.sdkerror as MistralError
import pandas as pd

api_key = json.load(open("apikeys.json", "r"))["Mistral"]
client = Mistral(api_key=api_key)

def mispell(query: str, n = 1):
    try: # Try to query the Mistral LLM
        response = client.chat.complete(
            model="mistral-medium-latest",
            messages=[{"role": "user", "content": f"Return {n} mispelled versions of the following text: '{query}'. Return only the mispelled versions separated by new lines and nothing else."}]
        )
        return response.choices[0].message.content.replace("\n\n", "\n").split("\n")
    except MistralError.SDKError: # Because I'm using the free tier the service capacity may be exceeded, in that case try again
        return mispell(query=query, n = n)

queries = pd.read_csv("week-6/web_search_queries.csv")["Query"].tolist()
mispelled = dict.fromkeys(queries)
for k in mispelled.keys():
    mispelled[k] = mispell(k, 5)

open("week-6/mispelledQueries.json", "w").write(json.dumps(mispelled))
# Task: implement a method, that will take a query string as input and produce N misspelling variants of the query.
# These variants with typos will be used to test a search engine quality.
# Example
# Query: machine learning applications
# Possible Misspellings:
# "machin learning applications" (missing "e" in "machine")
# "mashine learning applications" (phonetically similar spelling of "machine")
# "machine lerning aplications" (missing "a" in "learning" and "p" in "applications")
# "machin lerning aplications" (combining multiple typos)
# "mahcine learing aplication" (transposed letters in "machine" and typos in "learning" and "applications")
#
# Questions:
# 1. Does the search engine produce the same results for all the variants?
# 2. Do all variants make sense?
# 3. How to improve robustness of the method, for example, skip known abbreviations, like JFK or NBC.
# 4. Can you test multiple LLMs and figure out which one is the best?
# 5. Do the misspellings capture a variety of error types (phonetic, omission, transposition, repetition)?
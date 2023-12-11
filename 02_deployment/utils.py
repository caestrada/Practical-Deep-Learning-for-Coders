from duckduckgo_search import ddg_images, DDGS
from fastcore.all import *

# Using duckduckgo_search library instead of bing since i don't have to add an api key.
def search_images_ddg(term, max_images=200):
    print(f"Searching for '{term}'")
    # return L(ddg_images(term, max_results=max_images)).itemgot('image')
    return L(DDGS().images(term, max_results=max_images)).itemgot('image')

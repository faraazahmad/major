import wikipediaapi
import pandas as pd


wiki_wiki = wikipediaapi.Wikipedia('hi')
page_py = wiki_wiki.page('ईस्ट_इण्डिया_कम्पनी')
body = page_py.text.replace('\n', '').replace('==', '').replace('\u200d', '').replace('।', '')

def print_links(page,body):
    links=[]
    for link in page.links:
        if body.find(link) != -1:
            links.append(link)

    return links
link_list=print_links(page_py,body)

def print_langlinks(page):
        langlinks = page.langlinks
        
        for k in sorted(langlinks.keys()):
            v = langlinks[k]
            if(v.language=='en'):
                return v.title
            
        return "Page does not exist"

def word_list(page):
	x=[]
	for page in link_list:
    	page_1 = wiki_wiki.page(page)
    	y=print_langlinks(page_1)
    	x.append([page,y])

    return x

list=word_list(link_list)
df=pd.DataFrame(list)
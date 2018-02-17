import dblp

def author_check(authors):
    publications = 0
    for author in authors:
        publications = author_lookup(author) + publications
    return publications

def author_lookup(author):
    author = dblp.search(author)
    return len(michael.publications)


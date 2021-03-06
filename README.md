
# Shrink 

![preview](res/pre.png)

## Idea
For this project, we decided to address the problem of consuming the plethora of technology around us. We attempted and will continue working on a chrome extension that helps users view summaries of Articles as well as a calculated credibility rating based on the a standard set for by standford at https://credibility.stanford.edu/guidelines/index.html. We attempted to reduce the amount of computations in our servers and creations of already established technologies by taking advangtage of already curated API's for NLP (natural language processing) and easy of submission to websites like hackernews and twitter. 

## Technologies Used
- Digital Ocean
- MongoDB
- Python3 API's
	- newspaper https://github.com/codelucas/newspaper
	- gunicorn http://docs.gunicorn.org/en/stable/
	- scholar.py https://github.com/ckreibich/scholar.py
	- Language-Check https://github.com/myint/language-check
	- ScraPY NLP Library
- Nginx
- Google

## Future Goals of this Work
- [ ]	Complete the integration of social media sharing and crowdsource curation of popular summaries
- [ ] 	Ability to hover over links and summarize web content
- [ ] 	Summarize more intelligently
- [ ]	Bookmarking with history browsing tree (Building graphs based on history)
- [ ]	Peer reviewing (Potential crowdsourcing element)

Resources:
### Backend
- https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-with-http-2-support-on-ubuntu-16-04 
- https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-14-04
### NLP Resources
- https://github.com/dipanjanS/text-analytics-with-python

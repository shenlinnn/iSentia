import pymongo

def search_article(keyword):
    ## compose MongoDB URI, db name and collection name
    mongo_uri = "mongodb://shenlin92:shenlin921002@aws-us-east-1-portal.23.dblayer.com:17212/iSentia"
    mongo_db = "iSentia"
    collection_name = 'Articles'

    ## connect to the db
    client = pymongo.MongoClient(mongo_uri, ssl_ca_certs="./iSentia/cert.pem")
    db = client[mongo_db]
    collection = db[collection_name]
    ## search all stored articles by the keyword in title
    search_result = list(collection.find({'title': {"$regex": keyword}}))
    ## print the title and url
    for i in search_result:
        print {'title': i[u'title'],'url': i[u'link']}


###### Testing #######
# search_article('Donald Trump')
# {'url': u'https://www.theguardian.com/us-news/2017/jan/15/the-seven-faces-of-donald-trump-a-psychologists-view', 'title': u'The seven faces of Donald Trump \u2013 a psychologist\u2019s view'}
# {'url': u'https://www.theguardian.com/science/political-science/2016/nov/11/they-may-not-like-it-but-scientists-must-work-with-donald-trump', 'title': u'They may not like it, but scientists must work with Donald Trump'}
# {'url': u'https://www.theguardian.com/us-news/2016/nov/17/climate-change-a-chinese-plot-beijing-gives-donald-trump-a-history-lesson', 'title': u'Climate change a Chinese hoax? Beijing gives Donald Trump a lesson in history'}
# {'url': u'https://www.theguardian.com/music/2017/mar/15/snoop-dogg-owes-apology-donald-trump-lawyer-lavender-video-badbadnotgood', 'title': u'Snoop Dogg attacked by Donald Trump over Lavender video'}
# {'url': u'https://www.theguardian.com/books/2017/mar/01/alec-baldwin-trump-book-cant-spell-america-without-me', 'title': u'Alec Baldwin to co-write satirical book in character of Donald Trump'}
# {'url': u'https://www.theguardian.com/sport/2017/feb/28/rory-mcilroy-us-president-donald-trump-golf', 'title': u'Rory McIlroy: I talked golf not politics during round with Donald Trump'}


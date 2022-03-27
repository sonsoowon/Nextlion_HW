def extract_info(webtoon_list):
    result = []
    
    for item in webtoon_list:
        title = item.find("dt").find("a").string
        writer = item.find("dd", {"class":"desc"}).find("a").text
        rating = item.find("div", {"class":"rating_type"}).find("strong").text

        result.append({'title':title, 'writer':writer, 'rating':rating})

    return result
import requests
api_key='1f546d75494e4b98818ee22f0685cda2'
while True:
    
    options = {
    1: "technology",
    2: "sports",
    3: "business",
    4: "health",
    5: "science",
    6: "exit"

    }

    selected = int(input("Choose a topic:\n1. Technology\n2. Sports\n3. Business\n4. Health\n5. Science\n6.exit\n "))

# Use get() to handle invalid input, default to 'general'
    keyword = options.get(selected, "general")

    print("🔍 Fetching the latest news... Please wait.\n")

    if keyword== 'exit':
        print('exiting the news reader have a ammazing day')
        break
    choice=input(''' type '1' for top head lines or '2' for every thing you want know :''')

    if choice == '1':
        url=f'https://newsapi.org/v2/top-headlines?q={keyword}&sortBy=publishedAt&Language=en&apiKey={api_key}'
        print(' getting you top head-lines')

    elif choice == '2':
        url=f'https://newsapi.org/v2/everything?q={keyword}&sortBy=publishedAt&Language=en&apiKey={api_key}'
        print(' news is getting ready got you in seconds')
    else:
        print(' invalid choice .please enter 1 or 2')
        continue
    

        
    response=requests.get(url)
    data=response.json()
    articles=data.get('articles',[])
    if not articles:
        print(f'''no recent news found for '{keyword}' . try other keyword.\n''')
        continue
    print(f'\nTop news about {keyword}:\n')
    for i, article in enumerate(data['articles'][:5],start=1):
        print(f'{i}.{article['title']}')
        print(f'    {article['description']}')
        print(f'    {article['url']}')
        print(f'    {article['publishedAt']}')

    print('^'*60 + '\n')
        

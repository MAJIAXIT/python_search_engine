# python_search_engine

## Usage
  
To use all modules run from terminal in project folder:
```
pip install -r requirements.txt
```
create `directories` folder

## Work

The `crawler` module - collect all data from page and subpages of entered domen, analyze the content from html data and write it into the data.txt file of local domen directory folder.

The `searcher` module - index the pages in data.txt file, make search with entered string and rank the results. Returns the list of relevant search results.

The `console_client` is the console app that helps user to interact with `crawler` and `searcher` modules using their functions. This app has the full acces to the `crawler` and `searcher` modules.

The `bot_searcher` is the telegram bot based on aiogram library. From this bot user only can search in the previously collected data.
To use `bot_searcher` you should create the `config.py` file and put `bot_token = '<token>'` with your bot token into it.

## Crawler block diagram
![crawler_block_diagram](https://user-images.githubusercontent.com/76401858/167364551-95b69cb1-b62b-4a97-89dd-2f0fcc4cf590.png)


## Searcher block diagram
![searcher_block_diagram](https://user-images.githubusercontent.com/76401858/167364602-5bc9b9c4-7fb6-4e6e-affd-a5ceb763df25.png)

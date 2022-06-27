# python_search_engine

## Usage

To use all modules run following command from terminal in project folder:

```
pip install -r requirements.txt
```

## Work

- `crawler` module - collect all data from page and subpages of entered domain, analyze the content on webpage and write it into the data.txt file of local domain folder.

- `searcher` module - indexes the pages in the data.txt file, searches for the entered string and rank the results. Returns a list of relevant search results.

- `console_client` - the console app that helps user to interact with `crawler` and `searcher` modules. This application has the full acces to the `crawler` and `searcher` modules.

- `bot_searcher` - telegram bot based on the aiogram library. With this bot, the user can only search in previously collected domains.
To use `bot_searcher`, you must create a `config.py` file and put `bot_token = '<token>'` into it with your bot token.

## Crawler block diagram
![crawler_block_diagram](https://user-images.githubusercontent.com/76401858/167364551-95b69cb1-b62b-4a97-89dd-2f0fcc4cf590.png)


## Searcher block diagram
![searcher_block_diagram](https://user-images.githubusercontent.com/76401858/167364602-5bc9b9c4-7fb6-4e6e-affd-a5ceb763df25.png)

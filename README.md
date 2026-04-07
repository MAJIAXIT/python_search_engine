<div align="center">
  <a href="#ru">🇷🇺 Русский</a> &nbsp;|&nbsp; <a href="#en">🇬🇧 English</a>
</div>

---

<a name="ru"></a>

# Python Search Engine

Легковесная поисковая система с открытым исходным кодом на Python: веб-краулер, полнотекстовый индексатор, ранжирование результатов и Telegram-бот.

Написана в одиночку за 72 часа на **VI Открытом IT-чемпионате (Хакатон)** — **2-е место** в номинации *Разработка поисковой системы с открытым исходным кодом*, оценка судей **293/300**.

## Награды

**VI Открытый IT-чемпионат, 2022** — Хакатон, номинация: *Разработка поисковой системы с открытым исходным кодом*

- Оценка: **293 / 300**
- Место: **2-е место** (специальный приз от спонсоров)
- 170+ участников из России и других стран (Барнаул, Иркутск, Челябинск, Германия, Финляндия)
- Организован при участии IT-ПАРК; спонсоры: Сбербанк, Ростелеком, R-Style Softlab, Транснефть и другие

| Ссылка | Описание |
|--------|----------|
| [Пост о хакатоне](https://vk.com/wall-58525095_4941) | Публикация IT-ПАРК с результатами и участниками |
| [Список победителей](https://vk.com/@open_it_2022-pobediteli) | Официальная статья со всеми победителями |

## Модули

- **`crawler`** — обходит все страницы и подстраницы указанного домена, анализирует содержимое и сохраняет результаты в файл `data.txt` в локальную папку домена.

- **`searcher`** — индексирует страницы из `data.txt`, ищет по запросу и возвращает ранжированный список релевантных результатов.

- **`console_client`** — консольное приложение с полным доступом к модулям `crawler` и `searcher`.

- **`bot_searcher`** — Telegram-бот на базе [aiogram](https://github.com/aiogram/aiogram). Позволяет искать по ранее собранным доменам.  
  Для использования: создайте файл `config.py` и добавьте `bot_token = '<ваш_токен>'`.

## Установка

```bash
pip install -r requirements.txt
```

## Архитектура

### Схема краулера
![crawler_block_diagram](https://user-images.githubusercontent.com/76401858/179345221-f3d7dee6-cef2-4110-8a72-403871e1832a.png)

### Схема поисковика
![searcher_block_diagram](https://user-images.githubusercontent.com/76401858/176031830-38e1ceff-628b-4f37-ba96-751538d97f5a.png)

---

<div align="center">
  <a href="#ru">🇷🇺 Русский</a> &nbsp;|&nbsp; <a href="#en">🇬🇧 English</a>
</div>

---

<a name="en"></a>

# Python Search Engine

A lightweight open-source search engine built in Python, featuring a web crawler, full-text indexer, ranked search results, and a Telegram bot interface.

Built solo in 72 hours at the **VI Open IT Championship (Hackathon)** — awarded **2nd place** in the *Open-Source Search Engine Development* track with a score of **293/300**.

## Recognition

**VI Open IT Championship, 2022** — Hackathon track: *Open-Source Search Engine Development*

- Score: **293 / 300**
- Place: **2nd place** (special prize from sponsors)
- 170+ participants from Russia and abroad (Barnaul, Irkutsk, Chelyabinsk, Germany, Finland)
- Organized with support from IT-PARK; sponsored by Sberbank, Rostelecom, R-Style Softlab, Transneft and others

| Link | Description |
|------|-------------|
| [Post about the hackathon](https://vk.com/wall-58525095_4941) | IT-PARK announcement with results and participants |
| [Winners list](https://vk.com/@open_it_2022-pobediteli) | Official article with all winners |

## Modules

- **`crawler`** — crawls all pages and subpages of a given domain, analyzes content, and writes results to `data.txt` in a local domain folder.

- **`searcher`** — indexes pages from `data.txt`, searches for a query string, and returns a ranked list of relevant results.

- **`console_client`** — CLI application providing full access to the `crawler` and `searcher` modules.

- **`bot_searcher`** — Telegram bot built on [aiogram](https://github.com/aiogram/aiogram). Allows users to search across previously crawled domains.  
  To use: create a `config.py` file with `bot_token = '<your_token>'`.

## Setup

```bash
pip install -r requirements.txt
```

## Architecture

### Crawler block diagram
![crawler_block_diagram](https://user-images.githubusercontent.com/76401858/179345221-f3d7dee6-cef2-4110-8a72-403871e1832a.png)

### Searcher block diagram
![searcher_block_diagram](https://user-images.githubusercontent.com/76401858/176031830-38e1ceff-628b-4f37-ba96-751538d97f5a.png)

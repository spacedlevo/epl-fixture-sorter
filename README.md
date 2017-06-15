# EPL Fixture Downloader and Organiser

This script is designed to scrape the fixtures from the [official EPL](https://www.premierleague.com)
 website. It will download the full HTML from the page using BeautifulSoup and then
 with regular expressions, extract the information required. The fixtures will then be placed into
 text files per round.

 This was designed to scrape data that was needed for another project.

## Basic Usage
In order to allow this script to be used each season I haven't hard coded in the website or season.
Therefore it will require two arguments;

* page_id which is the id of the page with the fixtures on, needed to complete the URL
* season this variable will be used to create a folder to keep the fixtures seperated into seasons

For the latest season the page id is 408956

```
python download_fixtures.py [page_id] [season]
```

Place the script where you will want the fixtures downloaded. The script will then create a folder for fixtures and then season where the text files will be held.

*Only been tested on Linux*

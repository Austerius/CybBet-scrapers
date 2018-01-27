import scrapy
import datetime
""" Spider for scraping esport data from betting site cybbet.com using scrapy with css selectors(for educational purposes)
    To run this script, you'll need to install scrapy packet first.
    On a Windows machine, you'll also need to install appropriate C++ SDK to run 'Twisted' (check a documentation) 
    Create scrapy project and put this script into 'spiders' folder.
    Use command 'scrapy crawl cybbet' from the command line to start the crawler(you need to be in the scrapy
     project directory).
    To save scraped data into .csv file - uncomment section of code with 'custom_settings' definition. 
"""


class CybBet(scrapy.spiders.CrawlSpider):

    name = 'cybbet'
    start_urls = ['https://cybbet.com/']

    # saving scraped data to .csv file. Comment this to simply print results into terminal window
    # custom_settings = {
    #     "FEED_FORMAT": "csv",
    #     "FEED_URI": "bets.csv"
    # }
    current_time = datetime.datetime.utcnow()

    def parse(self, response):
        # delete .noResult in following paths to parse all data from bets table
        game = response.css("tr.gt-row.process.noResult::attr(data-game-category-alias)").extract()
        date = response.css("tr.gt-row.process.noResult::attr(data-time-event-full)").extract()
        player1 = response.css("tr.gt-row.process.noResult td.gt-team div.team-name.team-name-first span.team-name-text::text").extract()
        odds1 = response.css("tr.gt-row.process.noResult td.gt-team a.gt-inner.team1 div.price span::text").extract()
        player2 = response.css("tr.gt-row.process.noResult td.gt-team div.team-name.team-name-second span.team-name-text::text").extract()
        odds2 = response.css("tr.gt-row.process.noResult td.gt-team a.gt-inner.team2 div.price span::text").extract()

        for item in zip(game, date, player1, odds1, player2, odds2):
            # converting date string to datetime format
            temp_date = datetime.datetime.strptime(item[1], "%a, %d %b %Y %H:%M:%S")
            # it seems, site showing date in UTC(0) format
            # we scrape only games, we can still bet on(comment 'if' statement to scrape games 'in progress')
            if self.current_time > temp_date:
                continue
            # striping spaces from bet-rate values
            temp_odds1 = float(item[3].strip())
            temp_odds2 = float(item[5].strip())
            info = {
                'game': item[0],
                'date': temp_date,
                'player1': item[2],
                'odds1': temp_odds1,
                'player2': item[4],
                'odds2': temp_odds2,
            }
            yield info

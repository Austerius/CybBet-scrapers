from bs4 import BeautifulSoup
import requests
import datetime
import shlex
import sys

""" This script will scrape game's data from betting site: cybbet.com/ 
    Mind, that scraper was built for educational purposes.
    'cybbet_scraper' script using combination of 'BeautifulSoup' + 'requests' for scraping data. 
    So, before running it - make sure that you have 'bs4' and 'requests' packets installed.
    You can run this script from command line with parameter 'show' to list scraped data
    directly into terminal window (also command 'help' to check all available options).
    After importing 'cybbet_scraper' into your own script - run 'cybbet_spider()' function to 
    collect data from the site(or test file). Returning data type - dictionary of lists of dictionaries:
    {'name of the 1st esport': [{'time': event time, 'player1': name of the first player, 
                                'player2': name of the second player, 'odds1': bet odds on the first player,
                                'odds2': bet odds on the second player},
                                {another game information},],
     'name of the 2nd esport': [{}, {}, ], 
     ..............................................
    }
    Script scrapes only event's data on which we can still bet on(but you can comment/uncomment necessary
     sections to scrape all available data)   
    """


# script author - Alexander Shums'kii
# https://github.com/Austerius
def cybbet_spider(show=False):
    source_code = requests.get("https://cybbet.com/")
    info_dict = {}  # here we will save parsed data
    if source_code.status_code == 200:
        bs = BeautifulSoup(source_code.text, 'html.parser')
        # extracting events with css selector
        events_block = bs.select('tr.gt-row.process')
        # print(events_block[0])
        current_time = datetime.datetime.utcnow()
        for event in events_block:
            date_string = event['data-time-event-full']
            # converting string time to datetime UTC format
            event_date = datetime.datetime.strptime(date_string, "%a, %d %b %Y %H:%M:%S")
            # here we scrape only events we still can bid on( delete 'if' statement for scraping all events)
            if current_time > event_date:
                continue
            game = event['data-game-category-alias']  # name of the game
            player1 = event.select_one('a.gt-inner.team1 span.team-name-text').get_text()  # first player's name
            odds1 = event.select_one('a.gt-inner.team1 div.price span').get_text()
            odds1 = float(odds1.strip())  # bet rate for the first player
            player2 = event.select_one('a.gt-inner.team2 span.team-name-text').get_text()  # second player's name
            odds2 = event.select_one('a.gt-inner.team2 div.price span').get_text()  # bet rate for the second player
            odds2 = float(odds2.strip())

            temp_dict = {'time': event_date, 'player1': player1, 'player2': player2,
                         'odds1': odds1, 'odds2': odds2}
            try:
                info_dict[game].append(temp_dict)
            except KeyError:
                info_dict[game] = [temp_dict]

            if show:
                print(game)
                print(event_date)
                print("{0}   {1}:{2}   {3}".format(player1, odds1, odds2, player2))
                print("-"*40)
    return info_dict


if __name__ == "__main__":
    show = False
    try:
        command = shlex.quote(sys.argv[1])
        if command.lower() == "show":
            show = True
        if command.lower() == "help":
            print("Keywords:")
            print("show - print scrapped data")
            print("help - print info about available commands")
            sys.exit(0)
    except IndexError:
        pass
    cybbet_spider(show=show)

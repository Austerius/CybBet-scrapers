# CybBet-scrapers
<p>Two scripts for gathering betting data from site: <i>CybBet.com</i>. First script - '<i>cybbet.py</i>' - using scrapy 
to acquire data, 
when second - '<i>cybbet_scraper.py</i>' - using combination of BeautifulSoup + requests.</p>
<h3>cybbet.py</h3>
<p>Spider for scraping esport data from betting site cybbet.com using <b>scrapy</b> with css selectors(<b>for educational purposes</b>).</p>
    <p>To run this script, you'll need to install scrapy packet first.
    On a Windows machine, you'll also need to install appropriate C++ SDK to run 'Twisted' (check a documentation).</p> 
    <p><b>Create scrapy project</b> and put this script into '<i>spiders</i>' folder.</p>
    <p>Use command '<i>scrapy crawl cybbet</i>' from the command line to start the crawler(you need to be in the scrapy
     project directory).</p>
    <p>To save scraped data into <i>.csv</i> file - uncomment section of code with 'custom_settings' definition.</p> 
<h3>cybbet_scraper.py</h3>
<p>This script will scrape game's data from betting site: cybbet.com/</p> 
    <p>Mind, that scraper was built for educational purposes.</p>
    <p>'<i>cybbet_scraper</i>' script using combination of <b>'BeautifulSoup' + 'requests'</b> for scraping data. 
    So, before running it - make sure that you have '<i>bs4</i>' and '<i>requests</i>' packets installed.</p>
    <p>You can run this script <b>from command line</b> with parameter '<i>show</i>' to list scraped data
    directly into terminal window (also, command '<i>help</i>' to check all available options).</p>
    <p>After importing 'cybbet_scraper' into your own script - run 'cybbet_spider()' function to 
    collect data from the site. <b>Returning data type</b> - dictionary of lists of dictionaries:</p>
    <p>{</br>
    '<i>name of the 1st esport'</i>: [{'<i>time</i>': event time, '<i>player1</i>': name of the first player,</br> 
                                '<i>player2</i>': name of the second player, '<i>odds1</i>': bet odds on the first player,</br>
                                '<i>odds2</i>': bet odds on the second player},</br>
                                {another game information},],</br>
     '<i>name of the 2nd esport</i>': [{}, {}, ],</br> 
     ..............................................</br>
    }</p>
    <p>Script scrapes only event's data on which we can still bet on(but you can comment/uncomment necessary
     sections to scrape all available data).</p>   

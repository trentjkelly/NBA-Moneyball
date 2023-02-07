# NBA "Moneyball" - Statistics Predictor

Like from the film "Moneyball", it calculates the most important NBA stats weighted on their effect on win percentage.

## Description

Grabs current NBA data from each team on ESPN's statistics page and weights each stat against the win percentage to determine the most important statistics for predicting wins in the current regular season. Each of the statistics comes with a "score" to show how much more they were to predict wins than other statistics. Any time the program is run, it will run the algorithm based on updated season data.

## Getting Started

### Dependencies

Libraries Needed:
* BeautifulSoup4

Languages:
* Python3

### Installing

Download the three files including "main.py", "team.py", and "webscraping.py". Make sure they are located in the same directory. Make sure Python3 is installed on your computer, and BeautifulSoup4 has been installed.

If you haven't downloaded bs4:
```
pip install beautifulsoup4
```
or if you use pip3:
```
pip3 install beautifulsoup4
```

### Executing program

In the terminal, navigate to the directory containing the files and enter:
```
python3 main.py
```
Give the code time to run, it parses through a lot of data.

## Author

Trent Kelly 
trentjkelly@outlook.com

## Version History

* 1.0 
    * Initial Release
    * Shows top statistic indicators & their weighting

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

Inspiration:
* ["Moneyball" - Film](https://www.sonypictures.com/movies/moneyball)
Sources:
* [Statistics](https://www.espn.com/nba/stats)

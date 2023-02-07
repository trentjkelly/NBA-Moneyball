# Copyright (c) 2023, Trent Kelly
# All rights reserved.

# This source code is licensed under the MIT-style license found in the
# LICENSE file in the root directory of this source tree. 

import bs4
from bs4 import BeautifulSoup
import requests

# Gets the main content from the page
def getMainContent(url):
    html_text = requests.get(url).content
    soup = BeautifulSoup(html_text, 'lxml')
    mainDiv = soup.find('div', class_='Wrapper Card__Content')
    return mainDiv

# 
# Webscraping for Team class:
# 

def get_team_record(url):
    html_text = requests.get(url).content
    soup = BeautifulSoup(html_text, 'lxml')
    header = soup.select('div.StickyContainer > div.ResponsiveWrapper')[0]
    record = header.li.text
    return record

def get_team_ast_to(mainDiv, rowNum):
    selector = 'div > div:nth-child(5) > div.flex > div > div.Table__Scroller > table > tbody > tr:nth-child(' + rowNum + ') > td:nth-child(13) > span'
    ast_to_list = mainDiv.select(selector)
    ast_to = ast_to_list[0].text
    return ast_to

def get_team_reb(mainDiv, rowNum):
    selector = 'div > div:nth-child(5) > div.flex > div > div.Table__Scroller > table > tbody > tr:nth-child(' + rowNum + ') > td:nth-child(7) > span'
    reb_list = mainDiv.select(selector)
    reb = reb_list[0].text
    return reb

def get_team_blk(mainDiv, rowNum):
    selector = 'div > div:nth-child(5) > div.flex > div > div.Table__Scroller > table > tbody > tr:nth-child(' + rowNum + ') > td:nth-child(10)'
    blk_list = mainDiv.select(selector)
    blk = blk_list[0].text
    return blk

def get_team_stl(mainDiv, rowNum):
    selector = 'div > div:nth-child(5) > div.flex > div > div.Table__Scroller > table > tbody > tr:nth-child(' + rowNum + ') > td:nth-child(9) > span'
    stl_list = mainDiv.select(selector)
    stl = stl_list[0].text
    return stl

def get_team_fgp(mainDiv, rowNum):
    selector = 'div > div:nth-child(6) > div.flex > div > div.Table__Scroller > table > tbody > tr:nth-child(' + rowNum + ') > td:nth-child(3) > span'
    fgp_list = mainDiv.select(selector)
    fgp = fgp_list[0].text
    return fgp

def get_team_three_pp(mainDiv, rowNum):
    selector = 'div > div:nth-child(6) > div.flex > div > div.Table__Scroller > table > tbody > tr:nth-child(' + rowNum + ') > td:nth-child(6) > span'
    three_pp_list = mainDiv.select(selector)
    three_pp = three_pp_list[0].text
    return three_pp

def get_team_ftp(mainDiv, rowNum):
    selector = 'div > div:nth-child(6) > div.flex > div > div.Table__Scroller > table > tbody > tr:nth-child(' + rowNum + ') > td:nth-child(9) > span'
    ftp_list = mainDiv.select(selector)
    ftp = ftp_list[0].text
    return ftp

def get_team_sc_eff(mainDiv, rowNum):
    selector = 'div > div:nth-child(6) > div.flex > div > div.Table__Scroller > table > tbody > tr:nth-child(' + rowNum + ') > td:nth-child(13) > span'
    sc_eff_list = mainDiv.select(selector)
    sc_eff = sc_eff_list[0].text
    return sc_eff

def get_team_sh_eff(mainDiv, rowNum):
    selector = 'div > div:nth-child(6) > div.flex > div > div.Table__Scroller > table > tbody > tr:nth-child(' + rowNum + ') > td:nth-child(14) > span'
    sh_eff_list = mainDiv.select(selector)
    sh_eff = sh_eff_list[0].text
    return sh_eff

def get_num_players(mainDiv):
    table = mainDiv.select('div > div:nth-child(5) > div.flex > div > div.Table__Scroller > table > tbody')
    rows = table[0].find_all('tr')
    numPlayers = len(rows) - 1
    return numPlayers
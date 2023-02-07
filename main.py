# Copyright (c) 2023, Trent Kelly
# All rights reserved.

# This source code is licensed under the MIT-style license found in the
# LICENSE file in the root directory of this source tree. 

import team
import webscraping

def populateTeams():
    teams = [] # Contains Team Objects

    # Instantiate all teams
    atlanta = team.Team('atlanta', 'https://www.espn.com/nba/team/stats/_/name/atl')
    boston = team.Team('boston', 'https://www.espn.com/nba/team/stats/_/name/bos')
    brooklyn = team.Team('brooklyn', 'https://www.espn.com/nba/team/stats/_/name/bkn')
    charlotte = team.Team('charlotte', 'https://www.espn.com/nba/team/stats/_/name/cha')
    chicago = team.Team('chicago', 'https://www.espn.com/nba/team/stats/_/name/chi')
    cleveland = team.Team('cleveland', 'https://www.espn.com/nba/team/stats/_/name/cle')
    dallas = team.Team('dallas', 'https://www.espn.com/nba/team/stats/_/name/dal')
    denver = team.Team('denver', 'https://www.espn.com/nba/team/stats/_/name/den')
    detroit = team.Team('detroit', 'https://www.espn.com/nba/team/stats/_/name/det')
    goldenState = team.Team('goldenState', 'https://www.espn.com/nba/team/stats/_/name/gs')
    houston = team.Team('houston', 'https://www.espn.com/nba/team/stats/_/name/hou')
    indiana = team.Team('indiana', 'https://www.espn.com/nba/team/stats/_/name/ind')
    lac = team.Team('lac', 'https://www.espn.com/nba/team/stats/_/name/lac')
    lal = team.Team('lal', 'https://www.espn.com/nba/team/stats/_/name/lal')
    memphis = team.Team('memphis', 'https://www.espn.com/nba/team/stats/_/name/mem')
    miami = team.Team('miami', 'https://www.espn.com/nba/team/stats/_/name/mia')
    milwaukee = team.Team('milwaukee', 'https://www.espn.com/nba/team/stats/_/name/mil')
    minnesota = team.Team('minnesota', 'https://www.espn.com/nba/team/stats/_/name/min')
    newOrleans = team.Team('newOrleans', 'https://www.espn.com/nba/team/stats/_/name/no')
    newYork = team.Team('newYork', 'https://www.espn.com/nba/team/stats/_/name/ny')
    oklahomaCity = team.Team('oklahomaCity', 'https://www.espn.com/nba/team/stats/_/name/okc')
    orlando = team.Team('orlando', 'https://www.espn.com/nba/team/stats/_/name/orl')
    philadelphia = team.Team('philadelphia', 'https://www.espn.com/nba/team/stats/_/name/phi')
    phoenix = team.Team('phoenix', 'https://www.espn.com/nba/team/stats/_/name/phx')
    portland = team.Team('portland', 'https://www.espn.com/nba/team/stats/_/name/por')
    sacramento = team.Team('sacramento', 'https://www.espn.com/nba/team/stats/_/name/sac')
    sanAntonio = team.Team('sanAntonio', 'https://www.espn.com/nba/team/stats/_/name/sa')
    toronto = team.Team('toronto', 'https://www.espn.com/nba/team/stats/_/name/tor')
    utah = team.Team('utah', 'https://www.espn.com/nba/team/stats/_/name/utah')
    washington = team.Team('washington', 'https://www.espn.com/nba/team/stats/_/name/wsh')
    #Add teams to teams list
    teams.append(atlanta)
    teams.append(boston)
    teams.append(brooklyn)
    teams.append(charlotte)
    teams.append(chicago)
    teams.append(cleveland)
    teams.append(dallas)
    teams.append(denver)
    teams.append(detroit)
    teams.append(goldenState)
    teams.append(houston)
    teams.append(indiana)
    teams.append(lac)
    teams.append(lal)
    teams.append(memphis)
    teams.append(miami)
    teams.append(milwaukee)
    teams.append(minnesota)
    teams.append(newOrleans)
    teams.append(newYork)
    teams.append(oklahomaCity)
    teams.append(orlando)
    teams.append(philadelphia)
    teams.append(phoenix)
    teams.append(portland)
    teams.append(sacramento)
    teams.append(sanAntonio)
    teams.append(toronto)
    teams.append(utah)
    teams.append(washington)

    return teams

def modifyTeamStats(teams):
    # Individual team check:
    # website = teams[5].get_website()
    # mainDiv = webscraping.getMainContent(website)
    # print(teams[5].get_name())
    # webscraping.get_num_players(mainDiv)

    for t in teams:
        website = t.get_website()
        mainDiv = webscraping.getMainContent(website)

        numRows = webscraping.get_num_players(mainDiv)
        t.set_num_players(numRows)
        numRows = str((numRows + 1))
        
        t.set_ast_to(webscraping.get_team_ast_to(mainDiv, numRows))
        t.set_fgp(webscraping.get_team_fgp(mainDiv, numRows))
        t.set_three_pp(webscraping.get_team_three_pp(mainDiv, numRows))
        t.set_ftp(webscraping.get_team_ftp(mainDiv, numRows))
        t.set_sc_eff(webscraping.get_team_sc_eff(mainDiv, numRows))
        t.set_sh_eff(webscraping.get_team_sh_eff(mainDiv, numRows))
        t.set_reb(webscraping.get_team_reb(mainDiv, numRows))
        t.set_blk(webscraping.get_team_blk(mainDiv, numRows))
        t.set_stl(webscraping.get_team_stl(mainDiv, numRows))
        t.set_win_pct(webscraping.get_team_record(website))

def getAverageStats(teams):

    averageStats = {
        'ast_to': 0.0,
        'fgp': 0.0,
        'three_pp': 0.0,
        'ftp': 0.0,
        'sc_eff': 0.0,
        'sh_eff': 0.0,
        'reb': 0.0,
        'blk': 0.0,
        'stl': 0.0
    }

    for t in teams:
        averageStats['ast_to'] += float(t.get_ast_to())
        averageStats['fgp'] += float(t.get_fgp())
        averageStats['three_pp'] += float(t.get_three_pp())
        averageStats['ftp'] += float(t.get_ftp())
        averageStats['sc_eff'] += float(t.get_sc_eff())
        averageStats['sh_eff'] += float(t.get_sh_eff())
        averageStats['reb'] += float(t.get_reb())
        averageStats['blk'] += float(t.get_blk())
        averageStats['stl'] += float(t.get_stl())

    for s in averageStats:
        averageStats[s] /= 30
        averageStats[s] = round(averageStats[s], 3)

    return averageStats

def statWeightTeam(team, statName, averageStats):
    averageStat = averageStats[statName]
    teamStat = float(team.statNameToFunction(statName))
    statWeight = teamStat / averageStat
    statWeight = abs(1 - statWeight) # Determine how far it deviates from 1
    return statWeight

def statPredictability(teams, statName, averageStats):
    total = 0
    for t in teams:
        recordWeight = t.get_win_pct() - 0.5
        total += (recordWeight * statWeightTeam(t,statName,averageStats))
    return round(total, 5)

def getPredictorStats(teams, averageStats):

    ast_to = statPredictability(teams, 'ast_to', averageStats)
    fgp = statPredictability(teams, 'fgp', averageStats)
    three_pp = statPredictability(teams, 'three_pp', averageStats)
    ftp = statPredictability(teams, 'ftp', averageStats)
    sc_eff = statPredictability(teams, 'sc_eff', averageStats)
    sh_eff = statPredictability(teams, 'sh_eff', averageStats)
    reb = statPredictability(teams, 'reb', averageStats)
    blk = statPredictability(teams, 'blk', averageStats)
    stl = statPredictability(teams, 'stl', averageStats)

    # In reverse order bc want to look them up by number, and get the stat
    predictorStats = {
        ast_to: 'ast_to',
        fgp: 'fgp',
        three_pp: 'three_pp',
        ftp: 'ftp',
        sc_eff: 'sc_eff',
        sh_eff: 'sh_eff',
        reb: 'reb',
        blk: 'blk',
        stl: 'stl'
    }

    return predictorStats

def bestPredictorStats(teams):
    averageStats = getAverageStats(teams)
    predictorStats = getPredictorStats(teams, averageStats)
    orderPredictorStats = []

    for s in predictorStats.keys():
        orderPredictorStats.append(s)

    orderPredictorStats.sort(reverse=True)

    # Top 5 predictor stats in order
    myStr = 'Top 5 predictor stats and respective weighting:\n'
    myStr += predictorStats[orderPredictorStats[0]] + ': ' + str(orderPredictorStats[0]) + ' \n'
    myStr += predictorStats[orderPredictorStats[1]] + ': ' + str(orderPredictorStats[1]) + ' \n'
    myStr += predictorStats[orderPredictorStats[2]] + ': ' + str(orderPredictorStats[2]) + ' \n'
    myStr += predictorStats[orderPredictorStats[3]] + ': ' + str(orderPredictorStats[3]) + ' \n'
    myStr += predictorStats[orderPredictorStats[4]] + ': ' + str(orderPredictorStats[4])
    print(myStr)

def main():
    teams = populateTeams()
    modifyTeamStats(teams)
    predictorStats = bestPredictorStats(teams)

if __name__ == '__main__':
    main()
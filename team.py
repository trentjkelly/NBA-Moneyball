# Copyright (c) 2023, Trent Kelly
# All rights reserved.

# This source code is licensed under the MIT-style license found in the
# LICENSE file in the root directory of this source tree. 

class Team:

    def __init__(self, name, website):
        self.name = name
        self.website = website
        self.num_players = 0
        # Metric for weighting
        self.win_pct = 0
        # Stats chosen for player/stats predictability
        self.ast_to = 0
        self.fgp = 0
        self.three_pp = 0
        self.ftp = 0
        self.sc_eff = 0
        self.sh_eff= 0
        self.reb = 0
        self.blk = 0
        self.stl = 0

    def print_team(self):
        teamstr = ''
        teamstr += 'name: ' + self.name + '\n'
        teamstr += 'number of players: ' + str(self.num_players) + '\n'
        teamstr += 'win percentage: ' + str(self.win_pct) + '\n'
        teamstr += 'assist to turnover ratio: ' + str(self.ast_to) + '\n'
        teamstr += 'fg percentage: ' + str(self.fgp) + '\n'
        teamstr += '3p percantage: ' + str(self.three_pp) + '\n'
        teamstr += 'free throw percentage: ' + str(self.ftp) + '\n'
        teamstr += 'scoring efficiency: ' + str(self.sc_eff) + '\n'
        teamstr += 'shooting efficiency: ' + str(self.sh_eff) + '\n'
        teamstr += 'rebounds: ' + str(self.reb) + '\n'
        teamstr += 'blocks: ' + str(self.blk) + '\n'
        teamstr += 'steals: ' + str(self.stl) + '\n'
        print(teamstr)

    def set_num_players(self, num_players):
        self.num_players = num_players

    def get_num_players(self):
        return self.num_players

    def get_name(self):
        return self.name

    def get_website(self):
        return self.website

    def get_win_pct(self):
        return self.win_pct

    def set_win_pct(self, win_pct):
        splitW = win_pct.split('-')
        wins = int(splitW[0])
        losses = int(splitW[1])

        total = wins + losses
        percentage = (wins / total)

        self.win_pct = round(percentage, 3)

    def get_ast_to(self):
        return self.ast_to

    def set_ast_to(self, ast_to):
        self.ast_to = ast_to

    def get_fgp(self):
        return self.fgp

    def set_fgp(self, fgp):
        self.fgp = fgp

    def get_three_pp(self):
        return self.three_pp

    def set_three_pp(self, three_pp):
        self.three_pp = three_pp

    def get_ftp(self):
        return self.ftp

    def set_ftp(self, ftp):
        self.ftp = ftp

    def get_sc_eff(self):
        return self.sc_eff

    def set_sc_eff(self, sc_eff):
        self.sc_eff = sc_eff

    def get_sh_eff(self):
        return self.sh_eff

    def set_sh_eff(self, sh_eff):
        self.sh_eff = sh_eff

    def get_reb(self):
        return self.reb

    def set_reb(self, reb):
        self.reb = reb

    def get_blk(self):
        return self.blk

    def set_blk(self, blk):
        self.blk = blk

    def get_stl(self):
        return self.stl

    def set_stl(self, stl):
        self.stl = stl

    def statNameToFunction(self, name):
        if(name == 'ast_to'):
            return self.get_ast_to()
        elif (name == 'fgp'):
            return self.get_fgp()
        elif (name == 'three_pp'):
            return self.get_three_pp()
        elif (name == 'ftp'):
            return self.get_ftp()
        elif (name == 'sc_eff'):
            return self.get_sc_eff()
        elif (name == 'sh_eff'):
            return self.get_sh_eff()
        elif (name == 'reb'):
            return self.get_reb()
        elif (name == 'blk'):
            return self.get_blk()
        elif (name == 'stl'):
            return self.get_stl()
import numpy as np
import pandas as pd
import re

def pd_df(matn):
    ust = ['PERIOD','REMAINING_SEC','RELEVANT_TEAM','AWAY_TEAM',
    'HOME_TEAM','AWAY_SCORE','HOME_SCORE','DESCRIPTION']
    df = pd.read_csv(matn, names=ust, sep='|')
    return df

def players_names(DESCRIPTION):
    players = []
    for matn in DESCRIPTION:
        names = re.findall(r"(.?['.']\s[A-Z]?[a-z][A-Z]*[öa-z]+)", matn)
        for name in names:
           players.append(name)

    return pd.unique(players)

def dfdan_df(df):
    ustun = ['Team', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%',
            'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST',
            'STL', 'BLK', 'TOV', 'PF','PTS']
    df2 = pd.DataFrame(index=players_names(df['DESCRIPTION']), columns=ustun)
    df2.index.rename('Players', inplace=True)
    df2.fillna(0, inplace=True)
    return df2

def full_df(df, df2):

    P3 = re.compile(r"(.?['.']\s[A-Z]?[a-z][A-Z]*[öa-z]+) makes 3-pt")
    PA3 = re.compile(r"(.?['.']\s[A-Z]?[a-z][A-Z]*[öa-z]+) misses 3-pt")
    FG = re.compile(r"(.?['.']\s[A-Z]?[a-z][A-Z]*[öa-z]+) makes 2-pt")
    FGA = re.compile(r"(.?['.']\s[A-Z]?[a-z][A-Z]*[öa-z]+) misses 2-pt")
    TOV = re.compile(r"Turnover by (.?['.']\s[A-Z]?[a-z][A-Z]*[öa-z]+)")
    ORB = re.compile(r"Offensive rebound by (.?['.']\s[A-Z]?[a-z][A-Z]*[öa-z]+)")
    DRB = re.compile(r"Defensive rebound by (.?['.']\s[A-Z]?[a-z][A-Z]*[öa-z]+)")
    PF = re.compile(r"Personal foul by (.?['.']\s[A-Z]?[a-z][A-Z]*[öa-z]+)")
    FT = re.compile(r"(.?['.']\s[A-Z]?[a-z][A-Z]*[öa-z]+) makes free throw")
    FTA = re.compile(r"(.?['.']\s[A-Z]?[a-z][A-Z]*[öa-z]+) misses free throw ")
    AST = re.compile(r"assist by (.?['.']\s[A-Z]?[a-z][A-Z]*[öa-z]+)")
    STL = re.compile(r"steal by (.?['.']\s[A-Z]?[a-z][A-Z]*[öa-z]+)")
    BLK = re.compile(r"block by (.?['.']\s[A-Z]?[a-z][A-Z]*[öa-z]+)")

    for ind in df.index:
      txt = df['DESCRIPTION'][ind]

      if P3.search(txt):
          df2.at[P3.search(txt).group(1), '3P'] += 1
          df2.at[P3.search(txt).group(1), '3PA'] += 1
          df2.at[P3.search(txt).group(1), 'Team'] = df['RELEVANT_TEAM'][ind]


      elif PA3.search(txt):
          df2.at[PA3.search(txt).group(1), '3PA'] += 1
          df2.at[PA3.search(txt).group(1), 'Team'] = df['RELEVANT_TEAM'][ind]

      elif FG.search(txt):
          df2.at[FG.search(txt).group(1), 'FG'] += 1
          df2.at[FG.search(txt).group(1), 'FGA'] += 1
          df2.at[FG.search(txt).group(1), 'Team'] = df['RELEVANT_TEAM'][ind]

      elif FGA.search(txt):
          df2.at[FGA.search(txt).group(1), 'FGA'] += 1
          df2.at[FGA.search(txt).group(1), 'Team'] = df['RELEVANT_TEAM'][ind]

      elif FT.search(txt):
          df2.at[FT.search(txt).group(1), 'FT'] += 1
          df2.at[FT.search(txt).group(1), 'FTA'] += 1
          df2.at[FT.search(txt).group(1), 'Team'] = df['RELEVANT_TEAM'][ind]

      elif FTA.search(txt):
          df2.at[FTA.search(txt).group(1), 'FTA'] += 1
          df2.at[FTA.search(txt).group(1), 'Team'] = df['RELEVANT_TEAM'][ind]

      elif ORB.search(txt):
          df2.at[ORB.search(txt).group(1), 'ORB'] += 1

      elif DRB.search(txt):
          df2.at[DRB.search(txt).group(1), 'DRB'] += 1
          df2.at[DRB.search(txt).group(1), 'Team'] = df['RELEVANT_TEAM'][ind]
      elif TOV.search(txt):
          df2.at[TOV.search(txt).group(1), 'TOV'] += 1
          df2.at[TOV.search(txt).group(1), 'Team'] = df['RELEVANT_TEAM'][ind]

      elif PF.search(txt):
          df2.at[PF.search(txt).group(1), 'PF'] += 1

      if AST.search(txt):
          df2.at[AST.search(txt).group(1), 'AST'] += 1
          df2.at[AST.search(txt).group(1), 'Team'] = df['RELEVANT_TEAM'][ind]

      elif STL.search(txt):
          df2.at[STL.search(txt).group(1), 'STL'] += 1
          df2.at[STL.search(txt).group(1), 'Team'] = df['RELEVANT_TEAM'][ind]

      elif BLK.search(txt):
          df2.at[BLK.search(txt).group(1), 'BLK'] += 1
          df2.at[BLK.search(txt).group(1), 'Team'] = df['RELEVANT_TEAM'][ind]

    df2['FG%'] = df2['FG']/df2['FGA']
    df2['3P%'] = df2['3P']/df2['3PA']
    df2['FT%'] = df2['FT']/df2['FTA']
    df2['TRB'] = df2['ORB']+df2['DRB']
    df2['PTS'] = (df2['FG'] * 2) + (df2['3P'] * 3) + df2['FT']

    df2.fillna(0, inplace=True)
    return df2

def teams(df):
    home_team = df['HOME_TEAM'][0]
    away_team = df['AWAY_TEAM'][0]
    h_a_teams = [home_team, away_team]
    return h_a_teams

def to_dict(df, teams):
    df1 = df[df['Team'] == teams[0]]
    hplayers = list (df1.index.values)
    hFG = list (df1['FG'].values)
    hFGA = list (df1['FGA'].values)
    hFGF = list (df1['FG%'].values)
    hP3 = list(df1['3P'].values)
    hPA3 = list (df1['3PA'].values)
    hP3F = list (df1['3P%'].values)
    hFT = list (df1['FT'].values)
    hFTA = list (df1['FTA'].values)
    hFTF = list (df1['FT%'].values)
    hORB = list (df1['ORB'].values)
    hDRB = list (df1['DRB'].values)
    hTRB = list (df1['TRB'].values)
    hAST = list (df1['AST'].values)
    hSTL = list (df1['STL'].values)
    hBLK = list (df1['BLK'].values)
    hTOV = list (df1['TOV'].values)
    hPF = list (df1['PF'].values)
    hPTS = list (df1['PTS'].values)

    df = df[df['Team'] == teams[1]]
    aplayers = list (df.index.unique())
    aFG = list (df['FG'].values)
    aFGA = list (df['FGA'].values)
    aFGF = list (df['FG%'].values)
    aP3 = list (df['3P'].values)
    aPA3 = list (df['3PA'].values)
    aP3F = list (df['3P%'].values)
    aFT = list (df['FT'].values)
    aFTA = list (df['FTA'].values)
    aFTF = list (df['FT%'].values)
    aORB = list (df['ORB'].values)
    aDRB = list (df['DRB'].values)
    aTRB = list (df['TRB'].values)
    aAST = list (df['AST'].values)
    aSTL = list (df['STL'].values)
    aBLK = list (df['BLK'].values)
    aTOV = list (df['TOV'].values)
    aPF = list (df['PF'].values)
    aPTS = list (df['PTS'].values)

    HDATA = {"player_name": hplayers, "FG": hFG, "FGA": hFGA, "FG%": hFGF, "3P": hP3, "3PA": hPA3, "3P%": hP3F, "FT": hFT, "FTA": hFTA, "FT%": hFTF, "ORB": hORB, "DRB": hDRB, "TRB": hTRB, "AST": hAST, "STL": hSTL, "BLK": hBLK, "TOV": hTOV, "PF": hPF, "PTS": hPTS}
    ADATA = {"player_name": aplayers, "FG": aFG, "FGA": aFGA, "FG%": aFGF, "3P": aP3, "3PA": aPA3, "3P%": aP3F, "FT": aFT, "FTA": aFTA, "FT%": aFTF, "ORB": aORB, "DRB": aDRB, "TRB": aTRB, "AST": aAST, "STL": aSTL, "BLK": aBLK, "TOV": aTOV, "PF": aPF, "PTS": hPTS}
    javob = {"home_team": {"name": teams[0], "players_data": HDATA}, "away_team": {"name": teams[1], "players_data": ADATA}}
    return javob

def analyse_nba_game(play_by_play_moves):
    df = pd_df(play_by_play_moves)
    df2 = dfdan_df(df)
    jadval = full_df(df, df2)
    jamoalar = teams(df)
    javob = to_dict(jadval, jamoalar)
    return javob

def print_nba_game_stats(team_dict):
        
    umumiy = []
    x = 0
    for k, v in team_dict.items():
        qator = []
        qator.append(k)
        umumiy.append(qator)
        for val in v:
            umumiy[x].append(val)
        if x > 0:
            umumiy[x].append(sum(umumiy[x][1:]))
        else:
            umumiy[x].append('Team Totals')
        x += 1

      
    for x in range(len(umumiy)):
        for qator in umumiy:
            if len(qator) <= x:
                break
            print(qator[x], end='\t')
        if len(qator) < x:
            break
        
        print('\n')
        
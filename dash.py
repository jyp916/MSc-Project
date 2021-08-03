#!/usr/bin/env python
# coding: utf-8

# In[1]:


import psutil
import time
import os
import pandas as pd
import numpy as np
from pyecharts.globals import CurrentConfig, NotebookType
# CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB
from pyecharts.charts import Bar, Line, Pie, Timeline, Tab, Page
from pyecharts import options as opts
from pyecharts.globals import ThemeType

pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 500)
from pyecharts.commons.utils import JsCode
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts

# In[2]:


# person
start = time.clock()
data_person_115_1 = pd.read_csv("data/115_1_5_person.csv")
data_person_115_2 = pd.read_csv("data/115_7_8_person.csv")
data_person_134_1 = pd.read_csv("data/134_1_5_person.csv")
data_person_134_2 = pd.read_csv("data/134_7_8_person.csv")
data_person_148_1 = pd.read_csv("data/148_1_5_person.csv")
data_person_148_2 = pd.read_csv("data/148_7_8_person.csv")

data_person_115_1["年份"] = "2019"
data_person_115_2["年份"] = "2019"
data_person_134_1["年份"] = "2020"
data_person_134_2["年份"] = "2020"
data_person_148_1["年份"] = "2021"
data_person_148_2["年份"] = "2021"

data_person = pd.concat([data_person_115_1, data_person_115_2,
                         data_person_134_1, data_person_134_2,
                         data_person_148_1, data_person_148_2]).reset_index(drop=True)

# In[3]:


# check if there is null value in this table
sum(data_person.isnull().sum())

# In[4]:


# delete all the axis with every value in null
data_person.dropna(axis=0, how='all')

# In[5]:


# check the data type of this table and
data_person.dtypes.value_counts()

# In[6]:


data_person.shape

# In[7]:


# hero
data_hero_115_1 = pd.read_csv("data/115_1_5_hero.csv")
data_hero_115_2 = pd.read_csv("data/115_7_8_hero.csv")
data_hero_134_1 = pd.read_csv("data/134_1_5_hero.csv")
data_hero_134_2 = pd.read_csv("data/134_7_8_hero.csv")
data_hero_148_1 = pd.read_csv("data/148_1_5_hero.csv")
data_hero_148_2 = pd.read_csv("data/148_7_8_hero.csv")

data_hero_115_1["年份"] = "2019"
data_hero_115_2["年份"] = "2019"
data_hero_134_1["年份"] = "2020"
data_hero_134_2["年份"] = "2020"
data_hero_148_1["年份"] = "2021"
data_hero_148_2["年份"] = "2021"

data_hero = pd.concat([data_hero_115_1, data_hero_115_2,
                       data_hero_134_1, data_hero_134_2,
                       data_hero_148_1, data_hero_148_2]).reset_index(drop=True)

# In[8]:


data_hero.shape

# In[9]:


# check if there is null value in this table
sum(data_hero.isnull().sum())

# In[10]:


# delete all the axis with every value in null
data_hero.dropna(axis=0, how='all')

# In[11]:


# team
data_team_115_1 = pd.read_csv("data/115_1_5_team.csv", encoding="gbk")
data_team_115_2 = pd.read_csv("data/115_7_8_team.csv", encoding="gbk")
data_team_134_1 = pd.read_csv("data/134_1_5_team.csv", encoding="gbk")
data_team_134_2 = pd.read_csv("data/134_7_8_team.csv", encoding="gbk")
data_team_148_1 = pd.read_csv("data/148_1_5_team.csv", encoding="gbk")
data_team_148_2 = pd.read_csv("data/148_7_8_team.csv", encoding="gbk")

data_team_115_1["年份"] = "2019"
data_team_115_2["年份"] = "2019"
data_team_134_1["年份"] = "2020"
data_team_134_2["年份"] = "2020"
data_team_148_1["年份"] = "2021"
data_team_148_2["年份"] = "2021"

data_team = pd.concat([data_team_115_1, data_team_115_2,
                       data_team_134_1, data_team_134_2,
                       data_team_148_1, data_team_148_2]).reset_index(drop=True)

# In[12]:


data_team.shape

# In[13]:


# check if there is null value in this table
sum(data_team.isnull().sum())

# In[14]:


data_team.head(10)

# In[15]:


# Bar chart to show the top 10 teams with the higest win rate along with their number of
# victory and defeat.
colors = ["#5793f3", "#d14a61", "green"]
tl1 = Timeline()
for i in ["2019", "2020", "2021"]:
    table2 = data_team[["sTeamName", "iAppearancesFrequency", "iWin", "iLoss", "年份"]]
    table2.columns = ["队名", "总场次", "Victory", "Defeat", "年份"]
    table2 = table2[table2.年份 == i].reset_index(drop=True)
    table2 = pd.pivot_table(table2, index="队名", values=["总场次", "Victory", "Defeat"], aggfunc="sum").reset_index()
    table2["胜率"] = round(table2["Victory"] / table2["总场次"], 2) * 100
    table2["胜率"] = table2["胜率"].astype(int)
    table2 = table2.sort_values("胜率", ascending=True)
    table2 = table2.reset_index(drop=True).head(10)

    bar2 = (
        Bar()
            .add_xaxis(xaxis_data=table2.队名.tolist())
            .add_yaxis(
            series_name="Win Rate(%)",
            y_axis=table2.胜率.tolist(),
            itemstyle_opts=opts.ItemStyleOpts(color=colors[2], opacity=0.7)
        )
            .add_yaxis(
            series_name="Victory(The Nmber of Match)",
            y_axis=table2.Victory.tolist(),
            itemstyle_opts=opts.ItemStyleOpts(color=colors[1], opacity=0.7)
        )
            .add_yaxis(
            series_name="Defeat(The Nmber of Match)",
            y_axis=table2.Defeat.tolist(),
            itemstyle_opts=opts.ItemStyleOpts(color=colors[0], opacity=0.7)
        )
            .reversal_axis()
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                             itemstyle_opts={"normal": {"barBorderRadius": [30, 30, 30, 30]}})
            .set_global_opts(
            toolbox_opts=opts.ToolboxOpts(
                pos_top="top",
                pos_left="right",
                feature={"saveAsImage": {},
                         "magicType": {"show": True, "type": ["line", "bar"]},
                         "dataView": {}})
        )
    )
    tl1.add(bar2, i)
tl1.render("p1.html")

# In[16]:


# pie chart to show the team with the highest win rate
fn = """
    function(params) {
        if(params.name == 'Number of Victory')
            return params.name + ' : ' + params.value;
        return ''
    }
    """


def new_label_opts():
    return opts.LabelOpts(formatter=JsCode(fn), position="center")


tl2 = Timeline()
for i in ["2019", "2020", "2021"]:
    table2 = data_team[["sTeamName", "iAppearancesFrequency", "iWin", "iLoss", "年份"]]
    table2.columns = ["队名", "总场次", "Victory", "Defeat", "年份"]
    table2 = table2[table2.年份 == i].reset_index(drop=True)
    table2 = pd.pivot_table(table2, index="队名", values=["总场次", "Victory", "Defeat"], aggfunc="sum").reset_index()
    table2["胜率"] = round(table2["Victory"] / table2["总场次"], 2) * 100
    table2["胜率"] = table2["胜率"].astype(int)
    table2 = table2.sort_values("胜率", ascending=True)
    table2 = table2.reset_index(drop=True).head(10)
    a = table2.总场次[9]
    b = table2.Victory[9]
    pie1 = (
        Pie()
            .add(
            "",
            [['Total Matches', int(a)], ['Number of Victory', int(b)]],
            radius=[75, 90],
            label_opts=new_label_opts(),
        )
            .set_colors(["blue", "silver"])
            .set_global_opts(
            legend_opts=opts.LegendOpts(is_show=False),
            title_opts=opts.TitleOpts(
                title=["   %s \n The Highest Win Rate" % table2.队名[9]],
                pos_left="center",
                title_textstyle_opts=opts.TextStyleOpts(color="black"),
            )
        )
    )
    tl2.add(pie1, i)
tl2.render("p2.html")

# In[17]:


# pie chart to show the team with the highest number of kill from 2019-2021
tl3 = Timeline()
for i in ["2019", "2020", "2021"]:
    table3 = data_team[["sTeamName", "iKill", "iDeath", "年份"]]
    table3 = table3[table3.年份 == i].reset_index(drop=True)
    table3 = pd.pivot_table(table3, index="sTeamName", values=["iKill", "iDeath"], aggfunc="sum").reset_index()
    table3 = table3.sort_values("iKill", ascending=False)
    table3 = table3.reset_index(drop=True)
    table3.head(1)

    b = table3.iKill[0]
    a = table3.iDeath[0]

    fn = """
    function(params) {
        if(params.name == 'Kills')
            return params.name + ' : ' + params.value;
        return ''
    }
    """

    pie2 = (
        Pie()
            .add(
            "",
            [['Kills', int(b)], ['Total Death', int(a)]],
            radius=[75, 90],
            label_opts=new_label_opts(),
        )
            .set_colors(["skyblue", "silver"])
            .set_global_opts(
            legend_opts=opts.LegendOpts(is_show=False),
            title_opts=opts.TitleOpts(
                title=["   %s \n The Highest Kills" % table3.sTeamName[0]],
                pos_left="center",
                title_textstyle_opts=opts.TextStyleOpts(color="black"),
            )
        )
    )
    tl3.add(pie2, i)
tl3.render("p3.html")

# In[18]:


# pie chart to show the team with the highest gold from 2019-2021
tl4 = Timeline()
for i in ["2019", "2020", "2021"]:
    table4 = data_team[["sTeamName", "sAveragingGold", "年份"]]
    table4 = table4[table4.年份 == i].reset_index(drop=True)
    table4 = pd.pivot_table(table4, index="sTeamName", values=["sAveragingGold"], aggfunc="mean").reset_index()
    table4 = table4.sort_values("sAveragingGold", ascending=False)
    table4 = table4.reset_index(drop=True)
    table4 = table4.head(10)

    b = table4.sAveragingGold[0]
    a = table4.sAveragingGold.sum()

    fn = """
    function(params) {
        if(params.name == 'Average amount')
            return params.name + ' : ' + params.value;
        return ''
    }
    """

    pie3 = (
        Pie()
            .add(
            "",
            [['Average amount', int(b)], ['Total amount of top ten teams', int(a)]],
            radius=[75, 90],
            label_opts=new_label_opts(),
        )
            .set_colors(["darkturquoise", "silver"])
            .set_global_opts(
            legend_opts=opts.LegendOpts(is_show=False),
            title_opts=opts.TitleOpts(
                title=["   %s \n The Highest of Average amount" % table4.sTeamName[0]],
                pos_left="center",
                title_textstyle_opts=opts.TextStyleOpts(color="black"),
            )
        )
    )
    tl4.add(pie3, i)
tl4.render("p4.html")

# In[19]:


# pie chart to show the team which got the most time of dragons from 2019-2021

tl5 = Timeline()
for i in ["2019", "2020", "2021"]:
    table5 = data_team[["sTeamName", "sAveragingSmallDragon", "年份"]]
    table5 = table5[table5.年份 == i].reset_index(drop=True)
    table5 = pd.pivot_table(table5, index="sTeamName", values=["sAveragingSmallDragon"], aggfunc="mean").reset_index()
    table5 = table5.sort_values("sAveragingSmallDragon", ascending=False)
    table5 = table5.reset_index(drop=True)
    table5 = table5.head(10)

    b = table5.sAveragingSmallDragon[0]
    a = table5.sAveragingSmallDragon.sum()

    fn = """
    function(params) {
        if(params.name == 'Dragons Per Match')
            return params.name + ' : ' + params.value;
        return ''
    }
    """

    pie4 = (
        Pie()
            .add(
            "",
            [['Dragons Per Match', round(b, 2)], ['Sum of dragons per match of the top ten teams', round(a, 2)]],
            radius=[75, 90],
            label_opts=new_label_opts(),
        )
            .set_colors(["hotpink", "silver"])
            .set_global_opts(
            legend_opts=opts.LegendOpts(is_show=False),
            title_opts=opts.TitleOpts(
                title=["   %s \n The Most Dragons Per Match" % table5.sTeamName[0]],
                pos_left="center",
                title_textstyle_opts=opts.TextStyleOpts(color="black"),
            )
        )
    )
    tl5.add(pie4, i)
tl5.render("p5.html")

# In[20]:


# pie chart to show the team which got the most time of baron dragon from 2019-2021

tl6 = Timeline()
for i in ["2019", "2020", "2021"]:
    table6 = data_team[["sTeamName", "sAveragingBigDragon", "年份"]]
    table6 = table6[table6.年份 == i].reset_index(drop=True)
    table6 = pd.pivot_table(table6, index="sTeamName", values=["sAveragingBigDragon"], aggfunc="mean").reset_index()
    table6 = table6.sort_values("sAveragingBigDragon", ascending=False)
    table6 = table6.reset_index(drop=True)
    table6 = table6.head(10)

    b = table6.sAveragingBigDragon[0]
    a = table6.sAveragingBigDragon.sum()

    fn = """
    function(params) {
        if(params.name == 'Barons Per Match')
            return params.name + ' : ' + params.value;
        return ''
    }
    """

    pie5 = (
        Pie()
            .add(
            "",
            [['Barons Per Match', round(b, 2)], ['Sum of Barons per match of the top ten teams', round(a, 2)]],
            radius=[75, 90],
            label_opts=new_label_opts(),
        )
            .set_colors(["orangered", "silver"])
            .set_global_opts(
            legend_opts=opts.LegendOpts(is_show=False),
            title_opts=opts.TitleOpts(
                title=["   %s \n The Most Barons Per Match" % table6.sTeamName[0]],
                pos_left="center",
                title_textstyle_opts=opts.TextStyleOpts(color="black"),
            )
        )
    )
    tl6.add(pie5, i)
tl6.render("p6.html")

# In[21]:


# rose pie chart to show the players who got the most time of MVP from 2019-2021
tl7 = Timeline()

for i in ["2019", "2020", "2021"]:
    table7 = data_person[["sMemberName", "iMVPFrequency", "年份"]]
    table7 = pd.pivot_table(table7, index=["sMemberName", "年份"],
                            values="iMVPFrequency", aggfunc="mean").reset_index()
    table7 = table7[table7.年份 == i].reset_index(drop=True)
    table7 = table7.sort_values("iMVPFrequency", ascending=False)
    table7 = table7.reset_index(drop=True)
    table7.iMVPFrequency = table7.iMVPFrequency.astype(int)
    table7 = table7.head(5)

    pie6 = (
        Pie()
            .add(
            "",
            [list(z) for z in zip(table7["sMemberName"], table7.iMVPFrequency.tolist())],
            radius=["30%", "75%"],
            rosetype="area",
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="The Players of Top 5"),
                             )
    )
    tl7.add(pie6, i)
tl7.render("p7.html")

# In[22]:


# Bar chart to show the 15 minutes' gold difference of all teams from 2019-2021
teamdata1 = pd.read_csv("oraclelixir2019-2021/LPL 2019 Spring Playoff.csv")
teamdata2 = pd.read_csv("oraclelixir2019-2021/LPL 2019 Spring.csv")
teamdata3 = pd.read_csv("oraclelixir2019-2021/LPL 2019 Summer Playoffs.csv")
teamdata4 = pd.read_csv("oraclelixir2019-2021/LPL 2019 Summer.csv")
teamdata5 = pd.read_csv("oraclelixir2019-2021/LPL 2020 Spring Playoffs.csv")
teamdata6 = pd.read_csv("oraclelixir2019-2021/LPL 2020 Spring.csv")
teamdata7 = pd.read_csv("oraclelixir2019-2021/LPL 2020 Summer Playoffs.csv")
teamdata8 = pd.read_csv("oraclelixir2019-2021/LPL 2020 Summer.csv")
teamdata9 = pd.read_csv("oraclelixir2019-2021/LPL 2021 Spring Playoffs.csv")
teamdata10 = pd.read_csv("oraclelixir2019-2021/LPL 2021 Spring.csv")
teamdata11 = pd.read_csv("oraclelixir2019-2021/LPL 2021 Summer.csv")

teamdata1["年份"] = "2019"
teamdata2["年份"] = "2019"
teamdata3["年份"] = "2019"
teamdata4["年份"] = "2019"
teamdata5["年份"] = "2020"
teamdata6["年份"] = "2020"
teamdata7["年份"] = "2020"
teamdata8["年份"] = "2020"
teamdata9["年份"] = "2021"
teamdata10["年份"] = "2021"
teamdata11["年份"] = "2021"

teamdata = pd.concat([teamdata1, teamdata2, teamdata3, teamdata4, teamdata5,
                      teamdata6, teamdata7, teamdata8, teamdata9, teamdata10,
                      teamdata11]).reset_index(drop=True)

teamdata = teamdata[["Team", "GD15", "年份"]]
teamdata = pd.pivot_table(teamdata, index=["Team", "年份"], values="GD15", aggfunc="mean").reset_index()
dict = {'Bilibili Gaming': "BLG",
        'Dominus Esports': "DMO",
        'EDward Gaming': "EDG",
        'FunPlus Phoenix': "FPX",
        'Invictus Gaming': "IG",
        'JD Gaming': "JDG",
        'LGD Gaming': "LGD",
        'LNG Esports': "LNG",
        'Oh My God': "OMG",
        'Rare Atom': "RA",
        'Rogue Warriors': "RW",
        'Royal Never Give Up': "RNG",
        'SinoDragon Gaming': "SDG",
        'Snake Esports': "Snake",
        'Suning': "SN",
        'Team WE': "WE",
        'ThunderTalk Gaming': "TT",
        'Top Esports': "TES",
        'Topsports Gaming': "TOP",
        'Vici Gaming': "VG",
        'Victory Five': "V5",
        'eStar': "ES"}

teamdata["队名"] = teamdata.Team.map(dict)

tl8 = Timeline()
for i in ["2019", "2020", "2021"]:
    teamdata_table = teamdata[teamdata.年份 == i].reset_index(drop=True)
    teamdata_table = teamdata_table.sort_values(["GD15"], ascending=True)
    teamdata_table.GD15 = teamdata_table.GD15.astype(int)

    bar_final = (
        Bar()
            .add_xaxis(xaxis_data=teamdata_table.队名.tolist())
            .add_yaxis(
            series_name="Gold Difference in 15 minutes",
            y_axis=teamdata_table.GD15.tolist(),
            itemstyle_opts=opts.ItemStyleOpts(color="blue", opacity=0.7))
            .reversal_axis()
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                             itemstyle_opts={"normal": {"barBorderRadius": [30, 30, 30, 30]}})

    )
    tl8.add(bar_final, i)
tl8.render("p8.html")

# In[23]:


# table to show the players with the best performance from 2019-2021
table_person = pd.pivot_table(data_person, index=["Name", "年份"],
                              values=["iKill", "iAssists", "iDeath", "iKDA"],
                              aggfunc="mean").reset_index()
table_person = table_person[table_person.年份 == "2019"].reset_index(drop=True)
table_person = table_person.sort_values("iKill", ascending=False).reset_index(drop=True)
best_kill = table_person[["Name", "iKill"]].reset_index(drop=True)
best_kill = best_kill.head(1)
table_person = table_person.sort_values("iAssists", ascending=False).reset_index(drop=True)
best_ass = table_person[["Name", "iAssists"]].reset_index(drop=True)
best_ass = best_ass.head(1)
table_person = table_person.sort_values("iKDA", ascending=False).reset_index(drop=True)
best_KDA = table_person[["Name", "iKDA"]].reset_index(drop=True)
best_KDA = best_KDA.head(1)
table_person = table_person.sort_values("iDeath", ascending=False).reset_index(drop=True)
best_Death = table_person[["Name", "iDeath"]].reset_index(drop=True)
best_Death = best_Death.head(1)

table_dash = pd.DataFrame({"选手": ["", "", ""],
                           "表现": ["The Most Kills", "The Most Assists", "The Highest KDA"],
                           "数据": ["", "", ""]})
table_dash.loc[0, "选手"] = best_kill.loc[0, "Name"]
table_dash.loc[0, "数据"] = "Kills:%d" % int(best_kill.loc[0, "iKill"])
table_dash.loc[1, "选手"] = best_ass.loc[0, "Name"]
table_dash.loc[1, "数据"] = "Assists:%d" % int(best_ass.loc[0, "iAssists"])
table_dash.loc[2, "选手"] = best_KDA.loc[0, "Name"]
table_dash.loc[2, "数据"] = "KDA:%d" % round(best_KDA.loc[0, "iKDA"], 2)
record_2019 = table_dash
record_2019["年份"] = "2019"

table_person = pd.pivot_table(data_person, index=["Name", "年份"],
                              values=["iKill", "iAssists", "iDeath", "iKDA"],
                              aggfunc="mean").reset_index()
table_person = table_person[table_person.年份 == "2020"].reset_index(drop=True)
table_person = table_person.sort_values("iKill", ascending=False).reset_index(drop=True)
best_kill = table_person[["Name", "iKill"]].reset_index(drop=True)
best_kill = best_kill.head(1)
table_person = table_person.sort_values("iAssists", ascending=False).reset_index(drop=True)
best_ass = table_person[["Name", "iAssists"]].reset_index(drop=True)
best_ass = best_ass.head(1)
table_person = table_person.sort_values("iKDA", ascending=False).reset_index(drop=True)
best_KDA = table_person[["Name", "iKDA"]].reset_index(drop=True)
best_KDA = best_KDA.head(1)
table_person = table_person.sort_values("iDeath", ascending=False).reset_index(drop=True)
best_Death = table_person[["Name", "iDeath"]].reset_index(drop=True)
best_Death = best_Death.head(1)
table_dash = pd.DataFrame({"选手": ["", "", ""],
                           "表现": ["The Most Kills", "The Most Assists", "The Highest KDA"],
                           "数据": ["", "", ""]})
table_dash.loc[0, "选手"] = best_kill.loc[0, "Name"]
table_dash.loc[0, "数据"] = "Kills:%d" % int(best_kill.loc[0, "iKill"])
table_dash.loc[1, "选手"] = best_ass.loc[0, "Name"]
table_dash.loc[1, "数据"] = "Assists:%d" % int(best_ass.loc[0, "iAssists"])
table_dash.loc[2, "选手"] = best_KDA.loc[0, "Name"]
table_dash.loc[2, "数据"] = "KDA:%d" % round(best_KDA.loc[0, "iKDA"], 2)
record_2020 = table_dash
record_2020["年份"] = "2020"

table_person = pd.pivot_table(data_person, index=["Name", "年份"],
                              values=["iKill", "iAssists", "iDeath", "iKDA"],
                              aggfunc="mean").reset_index()
table_person = table_person[table_person.年份 == "2021"].reset_index(drop=True)
table_person = table_person.sort_values("iKill", ascending=False).reset_index(drop=True)
best_kill = table_person[["Name", "iKill"]].reset_index(drop=True)
best_kill = best_kill.head(1)
table_person = table_person.sort_values("iAssists", ascending=False).reset_index(drop=True)
best_ass = table_person[["Name", "iAssists"]].reset_index(drop=True)
best_ass = best_ass.head(1)
table_person = table_person.sort_values("iKDA", ascending=False).reset_index(drop=True)
best_KDA = table_person[["Name", "iKDA"]].reset_index(drop=True)
best_KDA = best_KDA.head(1)
table_person = table_person.sort_values("iDeath", ascending=False).reset_index(drop=True)
best_Death = table_person[["Name", "iDeath"]].reset_index(drop=True)
best_Death = best_Death.head(1)
table_dash = pd.DataFrame({"选手": ["", "", ""],
                           "表现": ["The Most Kills", "The Most Assists", "The Highest KDA"],
                           "数据": ["", "", ""]})
table_dash.loc[0, "选手"] = best_kill.loc[0, "Name"]
table_dash.loc[0, "数据"] = "Kills:%d" % int(best_kill.loc[0, "iKill"])
table_dash.loc[1, "选手"] = best_ass.loc[0, "Name"]
table_dash.loc[1, "数据"] = "Assists:%d" % int(best_ass.loc[0, "iAssists"])
table_dash.loc[2, "选手"] = best_KDA.loc[0, "Name"]
table_dash.loc[2, "数据"] = "KDA:%d" % round(best_KDA.loc[0, "iKDA"], 4)

record_2021 = table_dash
record_2021["年份"] = "2021"
total_table = pd.concat([record_2019, record_2020, record_2021]).reset_index(drop=True)
total_table = total_table[["年份", "选手", "表现", "数据"]]
total_table.columns = ["Year", "Players", "Performance", "Data"]
table = Table()
headers = total_table.columns.tolist()
rows = total_table.values
table.add(headers, rows)
table.set_global_opts(
    title_opts=ComponentTitleOpts(title="Data of The Most Outstanding Players Each Year"),
)

table.render("table.html")

# In[24]:


# multi-y axis bar chart to show the specific players' performance from 2019-2021 with
# selection tabs
data_person_table1 = pd.pivot_table(data_person, index=["年份", "Name"],
                                    values=["iKill", "iAssists", "iDeath", "iKDA", "sAveragingOfferedRate"],
                                    aggfunc="mean").reset_index()
data_person_table1.columns = ["年份", "选手名", "助攻", "死亡数", "KDA", "击杀数", "参团率"]
data_person_table1.助攻 = data_person_table1.助攻.astype(int)
data_person_table1.死亡数 = data_person_table1.死亡数.astype(int)
data_person_table1.击杀数 = data_person_table1.击杀数.astype(int)
data_person_table1.参团率 = data_person_table1.参团率 * 100
data_person_table1.参团率 = data_person_table1.参团率.astype(int)
data_person_table1.KDA = list(map(lambda x: round(x, 2), data_person_table1.KDA))

tab = Tab()
namelist = ["Doinb", "Karsa", "Xiaohu", "Rookie", "Xiaohu", "Lwx", "TheShy", "Ning",
            "JackeyLove", "GALA", "Khan", "huanfeng", "Viper", "Nuguri"]
for i in namelist:
    data_person_table = data_person[data_person.Name == i].reset_index(drop=True)
    data_person_table1 = pd.pivot_table(data_person_table, index=["年份", "Name"],
                                        values=["iKill", "iAssists", "iDeath", "iKDA", "sAveragingOfferedRate"],
                                        aggfunc="mean").reset_index()
    data_person_table1.columns = ["年份", "Players", "助攻", "死亡数", "KDA", "击杀数", "参团率"]
    data_person_table1.助攻 = data_person_table1.助攻.astype(int)
    data_person_table1.死亡数 = data_person_table1.死亡数.astype(int)
    data_person_table1.击杀数 = data_person_table1.击杀数.astype(int)
    data_person_table1.参团率 = data_person_table1.参团率 * 100
    data_person_table1.参团率 = data_person_table1.参团率.astype(int)
    data_person_table1.KDA = list(map(lambda x: round(x, 2), data_person_table1.KDA))
    data_person_table1.columns = ["Year", "Players", "Assists", "Deaths", "KDA", "Kills", "Average Participation Rate"]

    colors = ["#5793f3", "#d14a61", "#675bba", "green", "red"]
    x_data = data_person_table1.Year.drop_duplicates().tolist()

    bar = (
        Bar()
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(
            series_name="Kills",
            y_axis=data_person_table1.Kills.tolist(),
            yaxis_index=2,
            color=colors[1],
        )
            .add_yaxis(
            series_name="Assists", y_axis=data_person_table1.Assists.tolist(), yaxis_index=2, color=colors[0]
        )
            .add_yaxis(
            series_name="Deaths", y_axis=data_person_table1.Deaths.tolist(), yaxis_index=2, color=colors[2]
        )
            .add_yaxis(
            series_name="KDA", y_axis=data_person_table1.KDA.tolist(), yaxis_index=1, color=colors[3]
        )
            .add_yaxis(
            series_name="Average Participation Rate",
            y_axis=data_person_table1["Average Participation Rate"].tolist(), yaxis_index=0, color=colors[4]
        )
            .extend_axis(
            yaxis=opts.AxisOpts(
                name="KDA",
                type_="value",
                min_=0,
                max_=10,
                position="right",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="black")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} "),
            )
        )
            .extend_axis(
            yaxis=opts.AxisOpts(
                type_="value",
                name="The Number",
                min_=0,
                max_=round(data_person_table1[["Kills", "Assists", "Deaths"]].values.max() * 1.2 / 100, 0) * 100,
                position="left",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="black")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} 个"),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
                ),
            )
        )
            .set_global_opts(
            yaxis_opts=opts.AxisOpts(
                type_="value",
                name="    AP Rate",
                min_=0,
                max_=100,
                position="right",
                offset=40,
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="black")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} %"),
            ),
            toolbox_opts=opts.ToolboxOpts(
                pos_top="top",
                pos_left="right",
                feature={"saveAsImage": {},
                         "magicType": {"show": True, "type": ["line", "bar"]},
                         "dataView": {}}

            ),
            title_opts=opts.TitleOpts(title="      %s" % data_person_table1.Players[0])
        )
    )
    tab.add(bar, data_person_table1.Players[0])
tab.render("tab.html")

# In[25]:


# table to show the top 3 popular champions chose by players from 2019-2021 with
# selection tab.
herodata = pd.read_csv("data/hero_data.csv", encoding="gbk")
temp_table = data_person[["sMemberName", "iPosition"]]
temp_table.columns = ["sOftenMemberName", "iPosition"]
data_hero1 = data_hero.merge(temp_table, on="sOftenMemberName", how="left")

hero_table = pd.pivot_table(data_hero1, index=["年份", "iPosition", "iChampionId"],
                            values=["sAveragingPick", "sAveragingBan", "sAveragingWin", "iAppearancesFrequency"],
                            aggfunc="mean").reset_index()

hero_table = hero_table.sort_values(["年份", "iPosition", "iAppearancesFrequency"], ascending=False).reset_index(
    drop=True)
hero_table_copy = hero_table.copy()
E = None
for i in hero_table_copy.iPosition.drop_duplicates().tolist():
    hero_table = hero_table_copy[hero_table_copy.iPosition == i].reset_index(drop=True)
    hero_table_2021 = hero_table[hero_table.年份 == "2021"].reset_index(drop=True)
    hero_table_2021 = hero_table_2021.head(3)
    hero_table_2020 = hero_table[hero_table.年份 == "2020"].reset_index(drop=True)
    hero_table_2020 = hero_table_2020.head(3)
    hero_table_2019 = hero_table[hero_table.年份 == "2019"].reset_index(drop=True)
    hero_table_2019 = hero_table_2019.head(3)
    hero_table = pd.concat([hero_table_2019, hero_table_2020, hero_table_2021]).reset_index(drop=True)
    E = pd.concat([E, hero_table]).reset_index(drop=True)

herodata = herodata[["heroId", "alias"]]
herodata.columns = ["iChampionId", "Name"]
E = E.merge(herodata, how="left", on="iChampionId")
E.loc[0, "Name"] = "THE WANDERING CARETAKER Bard"

dict_position = {"辅助": "Support",
                 "上单": "Top",
                 "打野": "Jungle",
                 "中单": "Middle",
                 "ADC": "Bottom"}
E.iPosition = E.iPosition.map(dict_position)
tab2 = Tab()
namelist = E.iPosition.drop_duplicates().tolist()
for i in namelist:
    E2 = E[E.iPosition == i].reset_index(drop=True)
    E2["Rank"] = ["N0.1", "NO.2", "NO.3", "N0.1", "NO.2", "NO.3", "N0.1", "NO.2", "NO.3"]
    E2 = E2[["年份", "Rank", "Name", "sAveragingPick", "sAveragingWin", "sAveragingBan"]]
    E2.columns = ["Year", "Rank", "Hero", "Pick Rate", "Win Rate", "Ban Rate"]
    E2["Pick Rate"] = list(map(lambda x: str(round(x * 100, 2)) + '%', E2["Pick Rate"]))
    E2["Win Rate"] = list(map(lambda x: str(round(x * 100, 2)) + '%', E2["Win Rate"]))
    E2["Ban Rate"] = list(map(lambda x: str(round(x * 100, 2)) + '%', E2["Ban Rate"]))
    table2 = Table()
    headers = E2.columns.tolist()
    rows = E2.values
    table2.add(headers, rows)
    table2.set_global_opts(
        title_opts=ComponentTitleOpts(title="Popular champions by position")
    )
    tab2.add(table2, i)
tab2.render("table2.html")


# In[26]:


# initial integration of all charts.
def page_draggable_layout():
    page = Page(layout=Page.DraggablePageLayout)
    page.add(
        tl1,
        tl2,
        tl3,
        tl4,
        tl5,
        tl6,
        tl7,
        tl8,
        table
    )
    page.render("LOL_index.html")


if __name__ == "__main__":
    page_draggable_layout()

# In[27]:

end = time.clock()
Page.save_resize_html("LOL_index.html", cfg_file='chart_config.json')

# In[28]:


info = psutil.virtual_memory()
totalMemory = info.total
memoryUsed = info.used
memoryPercentage = info.percent
cpuTimes = psutil.cpu_times()
cpuPercentage = psutil.cpu_percent()

print('Running time: %s Seconds' % (end - start) + "\n"
      "Total memory:", str(totalMemory) + "\n"
      + "Memory used:", str(memoryUsed) + "\n"
      + "Percentage of memory:", str(info.percent) + '%' + "\n"
      + "CPU time:", str(cpuTimes) + "\n"
      + "CPU percentage", str(cpuPercentage) + '%')

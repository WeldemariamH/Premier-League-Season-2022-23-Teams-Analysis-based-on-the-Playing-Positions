#!/usr/bin/env python
# coding: utf-8

# In[51]:


import pandas as pd
import os


# In[ ]:


######Importing the files


# In[52]:


Defense_data= pd.read_csv(r'D:\Data Analytics project\Premier league 2022-2023\PremierLeaguePlayerDefenseStats22-23.csv',header=0)


# In[53]:


GCA_data= pd.read_csv(r'D:\Data Analytics project\Premier league 2022-2023\PremierLeaguePlayerGCAStats22-23.csv',header=0)


# In[54]:


Passing_data= pd.read_csv(r'D:\Data Analytics project\Premier league 2022-2023\PremierLeaguePlayerPassingStats22-23.csv',header=0)


# In[55]:


Possession_data= pd.read_csv(r'D:\Data Analytics project\Premier league 2022-2023\PremierLeaguePlayerPossessionStats22-23.csv',header=0)


# In[56]:


Shooting_data= pd.read_csv(r'D:\Data Analytics project\Premier league 2022-2023\PremierLeaguePlayerShootingStats22-23.csv',header=0)


# In[57]:


All_aspects_data=pd.read_csv(r'D:\Data Analytics project\Premier league 2022-2023\PremierLeaguePlayerStats22-23.csv',header=0)


# In[ ]:


####Renaming the column of the data frames and check them 


# In[59]:


Defense_data=Defense_data.rename(columns={'player':'Player','Nation':'Nation','Pos':'Position','Squad':'Team','Age':'Age','Born':'Born','90s':'Minutes played divided by 90','Tkl':'Number of players tackled','TklW':'Tackles Won','Def 3rd':'Tackles in defensive 1/3','Mid 3rd':'Tackles in middle 1/3','att 3rd':'Tackles in attacking 1/3','TKI':'Number of dribblers tackled','Att':'Number of unsuccessful challenges plus number of dribblers tackled','Tkl%':'% of dribblers tackled','Lost':'Number of unsucessful attempts to challenge a dribbling player','Blocks':'Number of times blocking the ball by standing in its path','Sh':'Number of times blocking a shot by standing in its path','Pass':'Number of times blocking a pass by standing in its path','Int':'Interceptions','Tkl+Int':'Number of players tackled plus number of interceptions','Clr':'Clearances','Err':'Mistakes leading to an opponents shot'})


# In[60]:


Defense_data.head()


# In[61]:


GCA_data=GCA_data.rename(columns={'player':'Player','Nation':'Nation','Pos':'Position','Squad':'Team','Age':'Age','Born':'Born','90s':'Minutes played divided by 90','SCA':'Shot-Creating Actions','SCA90':'Shot-Creating Actions per 90 minutes','PassLive':'Completed live-ball passes that lead to a shot attempt','PassDead':'Completed dead-ball passes that lead to a shot attempt','To':'Successful take-ons that lead to a shot attempt','Sh':'Shots that lead to another shot attempt','Fld':'Fouls drawn that lead to a shot attempt','Def':'Defensive actions that lead to a shot attempt','GCA':'Goal-Creating Actions','GCA90':'Goal-Creating Actions per 90 minutes','PassLive':'Completed live-ball passes that lead to a goal','PassDead':'Completed dead-ball passes that lead to a goal Includes free kicks corner kicks kick offs throw-ins and goal kicks','TO':'Successful take-ons that lead to a goal','Sh':'Shots that lead to another goal-scoring shot','Fld':'Fouls drawn that lead to a goal','Def':'Defensive actions that lead to a goal'})


# In[62]:


GCA_data.head()


# In[63]:


Passing_data=Passing_data.rename(columns={'player':'Player','Nation':'Nation','Pos':'Position','Squad':'Team','Age':'Age','Born':'Born','90s':'Minutes played divided by 90','Cmp':'90s played Minutes played divided by 90','Att':'Passes Attempted','Cmp%':'Pass Completion Percentage','TotDist':'Total distance in yards that completed passes have traveled in any direction','PrgDist':'Progressive Passing Distance','Cmp':'Short Passes Completed','Att':'Short Passes Attempted','Cmp%':'Short Pass Completion Percentage','Cmp':'Medium Passes Completed','Att':'Medium Passes Attempted','Cmp%':'Medium Pass Completion Percentage','Cmp':'Long Passes Completed','Att':'Long Passes Attempted','Cmp%':'Long Pass Completion Percentage','Ast':'Assists','xAG':'xG which follows a pass that assists a shot','xA':'Expected Assists','A-xAG':'Assists minus Expected Goals Assisted','KP':'Key Passes','1/3/2023':'Passes into Final Third','PPA':'Passes into Penalty Area','CrsPA':'Crosses into Penalty Area','PrgP':'Progressive Passes'})


# In[64]:


Passing_data.head()


# In[65]:


Possession_data=Possession_data.rename(columns={'player':'Player','Nation':'Nation','Pos':'Position','Squad':'Team','Age':'Age','Born':'Born','90s':'Minutes played divided by 90','Touches':'Touches','Def Pen':'Touches in defensive penalty area','Def 3rd':'Touches in defensive 1/3','Mid 3rd':'Touches in middle 1/3','Att 3rd':'Touches in attacking 1/3','Att Pen':'Touches in attacking penalty area','Live':'Live-ball touches','Att':'Take-Ons Attempted','Succ':'Successful Take-Ons','Succ%':'Successful Take-On %','Tkld':'Times Tackled During Take-On','Tkld%':'Tackled During Take-On Percentage','Carries':'Carries','TotDist':'Total Carrying Distance','PrgDist':'Progressive Carrying Distance','PrgC':'Progressive Carries','1/3/2023':'Carries into Final Third','CPA':'Carries into Penalty Area','Mis':'Miscontrols','Dis':'Dispossessed','Rec':'Passes Received','PrgR':'Progressive Passes Rec'})


# In[66]:


Possession_data.head()


# In[67]:


Shooting_data=Shooting_data.rename(columns={'player':'Player','Nation':'Nation','Pos':'Position','Squad':'Team','Age':'Age','Born':'Born','90s':'Minutes played divided by 90','Gls':'Goals scored','Sh':'Total shots','SoT':'Shots on target','SoT%':'Shots on target %','Sh/90':'Shots Total per 90 minutes','SoT/90':'Shots on target per 90 minutes','G/Sh':'Goals per shot','G/SoT':'Goals per shot on target','Dist':'Average Shot Distance','FK':'Shots from free kicks','PK':'Penalty Kicks Scored','PKatt':'Penalty Kicks Attempted','xG':'Expected Goals','npxG':'Non-Penalty xG','npxG/Sh':'Non-Penalty Expected Goals per shot','G-xG':'Goals minus Expected Goals','np:G-xG':'Non-Penalty Goals minus Non-Penalty Expected Goals'})


# In[68]:


Shooting_data.head()


# In[69]:


All_aspects_data=All_aspects_data.rename(columns={'player':'Player','Nation':'Nation','Pos':'Position','Squad':'Team','Age':'Age','Born':'Born','MP':'Matches played','Starts':'Games started','Min':'Minutes played','90s':'Minutes divided by 90','Gls':'Goals','Ast':'Assists','G+A':'Goals and Assists','npGls':'Non-Penalty Goals','PK':'Penalty Kicks Scored','PKatt':'Penalty Kicks Attempted','CrdY':'Yellow Cards','Red Cards':'Medium Pass Completion Percentage','xG':'Expected Goals','npxG':'Expected Goals','xAG':'Expected Assisted Goals','npxG+xAG':'Non-Penalty Expected Goals plus Assisted Goals','PrgC':'Progressive Carries','PrgP':'Progressive Passes','PrgR':'Progressive Passes Received','Glsp90':'Goals Scored per 90 minutes','Astp90':'Assists per 90 minutes','G+Ap90':'Goals and Assists per 90 minutes','npGlsp90':'Non-Penalty Goals per 90 minutes','npGlsAstp90':'Non-Penalty Goals and Assists per 90 minutes','xGp90':'Expected Goals per 90 minutes','xAGp90':'Expected Assisted Goals per 90 minutes','xG+xAGp90':'Expected Goals plus Assisted Goals per 90 minutes','npxGp90':'Non-Penalty Expected Goals per 90 minutes','npxG+xAGp90':'Non-Penalty Expected Goals plus Assisted Goals per 90 minutes'})


# In[70]:


All_aspects_data.head()


# In[71]:


Shooting_data.info()


# In[ ]:





# In[72]:


Shooting_data.head()


# In[ ]:


##### Pulling out the data for the defensive players in each dataframe and merge them together


# In[73]:


Defense_Df=Defense_data[Defense_data['Position']=='DF']
GCA_Df=GCA_data[GCA_data['Position']=='DF']
Passing_Df=Passing_data[Passing_data['Position']=='DF']
Possession_Df=Possession_data[Possession_data['Position']=='DF']
Shooting_Df=Shooting_data[Shooting_data['Position']=='DF']
All_aspects_Df=All_aspects_data[All_aspects_data['Position']=='DF']

Defence=pd.merge(Defense_Df,GCA_data,on='Player',how='inner')
Defence=pd.merge(Defence,Passing_Df,on='Player',how='inner')
Defence=pd.merge(Defence,Possession_Df,on='Player',how='inner')
Defence=pd.merge(Defence,Shooting_Df,on='Player',how='inner')
Defence=pd.merge(Defence,All_aspects_Df,on='Player',how='inner')


# In[74]:


Defence.head()


# In[75]:


Defence.info()


# In[ ]:


###Pulling out the data for the Goal Keepers in each dataframe and merge them together


# In[76]:


Defense_Gk=Defense_data[Defense_data['Position']=='GK']
GCA_Gk=GCA_data[GCA_data['Position']=='GK']
Passing_Gk=Passing_data[Passing_data['Position']=='Gk']
Possession_Gk=Possession_data[Possession_data['Position']=='GK']
Shooting_Gk=Shooting_data[Shooting_data['Position']=='GK']
All_aspects_Gk=All_aspects_data[All_aspects_data['Position']=='GK']

Goal_Keeper=pd.merge(Defense_Gk,GCA_Gk,on='Player',how='inner')
Goal_Kepper=pd.merge(Goal_Keeper,Passing_Gk,on='Player',how='inner')
Goal_Keeper=pd.merge(Goal_Keeper,Possession_Gk,on='Player',how='inner')
Goal_Keeper=pd.merge(Goal_Keeper,Shooting_Gk,on='Player',how='inner')
Goal_Keeper=pd.merge(Goal_Keeper,All_aspects_Gk,on='Player',how='inner')


# In[77]:


Goal_Keeper.head()


# In[ ]:


###Pulling out the data for the Midfielders in each dataframe and merge them together


# In[78]:


Defense_Mf=Defense_data[Defense_data['Position']=='MF']
GCA_Mf=GCA_data[GCA_data['Position']=='MF']
Passing_Mf=Passing_data[Passing_data['Position']=='MF']
Possession_Mf=Possession_data[Possession_data['Position']=='MF']
Shooting_Mf=Shooting_data[Shooting_data['Position']=='MF']
All_aspects_Mf=All_aspects_data[All_aspects_data['Position']=='MF']

Mid_Field=pd.merge(Defense_Mf,GCA_data,on='Player',how='inner')
Mid_Field=pd.merge(Mid_Field,Passing_Mf,on='Player',how='inner')
Mid_Field=pd.merge(Mid_Field,Possession_Mf,on='Player',how='inner')
Mid_Field=pd.merge(Mid_Field,Shooting_Mf,on='Player',how='inner')
Mid_Field=pd.merge(Mid_Field,All_aspects_Mf,on='Player',how='inner')


# In[79]:


Mid_Field.info()


# In[ ]:


###Pulling out the data for the Forwar players in each dataframe and merge them together


# In[80]:


Defense_Fw=Defense_data[Defense_data['Position']=='FW']
GCA_Fw=GCA_data[GCA_data['Position']=='FW']
Passing_Fw=Passing_data[Passing_data['Position']=='FW']
Possession_Fw=Possession_data[Possession_data['Position']=='FW']
Shooting_Fw=Shooting_data[Shooting_data['Position']=='FW']
All_aspects_Fw=All_aspects_data[All_aspects_data['Position']=='FW']

Forward=pd.merge(Defense_Fw,GCA_Fw,on='Player',how='inner')
Forward=pd.merge(Forward,Passing_Fw,on='Player',how='inner')
Forward=pd.merge(Forward,Possession_Fw,on='Player',how='inner')
Forward=pd.merge(Forward,Shooting_Fw,on='Player',how='inner')
Forward=pd.merge(Forward,All_aspects_Fw,on='Player',how='inner')


# In[81]:


Forward.info()


# In[82]:


###Pulling out the data for the defensive Midfielders in each dataframe and merge them together


# In[83]:


Defence_DifensiveMidfield = Defense_data[Defense_data['Position'].isin(['DF,MF', 'MF,DF'])]
GCA_DifensiveMidfield=GCA_data[GCA_data['Position'].isin(['DF,MF', 'MF,DF'])]
Passing_DifensiveMidfield=Passing_data[Passing_data['Position'].isin(['DF,MF', 'MF,DF'])]
Possession_DifensiveMidfield=Possession_data[Possession_data['Position'].isin(['DF,MF', 'MF,DF'])]
Shooting_DifensiveMidfield=Shooting_data[Shooting_data['Position'].isin(['DF,MF', 'MF,DF'])]
All_aspects_DifensiveMidfield=All_aspects_data[All_aspects_data['Position'].isin(['DF,MF', 'MF,DF'])]

DifensiveMidfield=pd.merge(Defence_DifensiveMidfield,GCA_DifensiveMidfield,on='Player',how='inner')
DifensiveMidfield=pd.merge(DifensiveMidfield,Passing_DifensiveMidfield,on='Player',how='inner')
DifensiveMidfield=pd.merge(DifensiveMidfield,Possession_DifensiveMidfield,on='Player',how='inner')
DifensiveMidfield=pd.merge(DifensiveMidfield,Shooting_DifensiveMidfield,on='Player',how='inner')
DifensiveMidfield=pd.merge(DifensiveMidfield,All_aspects_DifensiveMidfield,on='Player',how='inner')


# In[84]:


DifensiveMidfield.head()


# In[ ]:


###Pulling out the data for the Attacking Midfielders in each dataframe and merge them together


# In[85]:


Defence_DifensiveMidfield = Defense_data[Defense_data['Position'].isin(['FW,MF', 'MF,FW'])]
GCA_DifensiveMidfield=GCA_data[GCA_data['Position'].isin(['FW,MF', 'MF,FW'])]
Passing_DifensiveMidfield=Passing_data[Passing_data['Position'].isin(['FW,MF', 'MF,FW'])]
Possession_DifensiveMidfield=Possession_data[Possession_data['Position'].isin(['FW,MF', 'MF,FW'])]
Shooting_DifensiveMidfield=Shooting_data[Shooting_data['Position'].isin(['FW,MF', 'MF,FW'])]
All_aspects_DifensiveMidfield=All_aspects_data[All_aspects_data['Position'].isin(['FW,MF', 'MF,FW'])]

AttackingMidfield=pd.merge(Defence_DifensiveMidfield,GCA_DifensiveMidfield,on='Player',how='inner')
AttackingMidfield=pd.merge(AttackingMidfield,Passing_DifensiveMidfield,on='Player',how='inner')
AttackingMidfield=pd.merge(AttackingMidfield,Possession_DifensiveMidfield,on='Player',how='inner')
AttackingMidfield=pd.merge(AttackingMidfield,Shooting_DifensiveMidfield,on='Player',how='inner')
AttackingMidfield=pd.merge(AttackingMidfield,All_aspects_DifensiveMidfield,on='Player',how='inner')


# In[86]:


AttackingMidfield.head()


# In[ ]:


###Exporting all the 6 merged files as a csv file


# In[87]:


Defence.to_csv('D:\Data Analytics project\Premier league 2022-2023\Defence_data.csv')
Goal_Keeper.to_csv('D:\Data Analytics project\Premier league 2022-2023\Goalkeepers_Data.csv')
Mid_Field.to_csv('D:\Data Analytics project\Premier league 2022-2023\Midfield_data.csv')
Forward.to_csv('D:\Data Analytics project\Premier league 2022-2023\Forward_data.csv')
DifensiveMidfield.to_csv('D:\Data Analytics project\Premier league 2022-2023\DifensiveMidfield_data.csv')
AttackingMidfield.to_csv('D:\Data Analytics project\Premier league 2022-2023\AttackingMidfield_data.csv')


# In[ ]:





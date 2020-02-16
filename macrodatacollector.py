# -*- coding: utf-8 -*-
"""
A script for monitoring macro data and housing market metircs  
"""
import sqlite3
from pandas.io.sql import read_sql #read_frame,
import pandas as pd
import numpy as np
import datetime as dt
from utils import datekeyRange #datekeyDifference
sDefaultDBPath = None #EABSMACRO_PATH
from macrodataqueries import sqlquery

class MacroHousingDataManager:
    """
    A class handles all sorts of calculations for 
    the European housing markets. 
    """
    def __init__(self, query, var='hpi'):
        self.query = query
        conn = sqlite3.connect(sDefaultDBPath) #detec_type=sqlite3.PARSE_DECLTYPES
        if conn:
            self.res = read_sql(self.query%(var,), conn)
        else:
            conn.row_factory = sqlite3.Row
            self.res = read_sql(self.query%(var,), conn) #load hpi value into data container

    def datekeyToDate(self, datekey):
        """turns datekey (int: YYYYMM) or a list of datekeys into datetime.date
        """
        if isinstance(datekey, (tuple, list, np.ndarray)):
            return [self.datekeyToDate(dk) for dk in datekey]
        else:
            return dt.date(datekey // 100, datekey % 100, 1)

    def calculateNormalizedHPIatPeak(self, dictPerf):
        """House price index rebased to 100 at its peak values
        """
        df = self.res
        for countrycode, dd in df.groupby(['countrycode']):
            ndf = dd.set_index(dd['datekey'])
            newvalues = ndf['value'] / ndf['value'].max() * 100
            ndf['normalised_hpi'] = newvalues
            
            # handle two or more peak values 
            max_date = ndf.iloc[np.where(ndf['value'] == ndf['value'].max())]['datekey'].values
            if len(max_date) > 1:
                max_date = self.datekeyToDate(int(max_date[0]))
            else:
                max_date = self.datekeyToDate(int(max_date))
            
            minDate = ndf.index[0]
            maxDate = ndf.index[-1]
            fullIndex = datekeyRange(minDate, maxDate, step=1)
            ndf = ndf.reindex(index=fullIndex)
            ndf = ndf.interpolate()
            
            ldates = self.datekeyToDate(ndf.index.tolist())
            xaxis = [(d - max_date).days / 30 for d in ldates]
            
            ndf['indices'] = xaxis
            tempdict = dict(zip(ndf['indices'], ndf['normalised_hpi']))
            dictPerf[(countrycode, 'House Price Indices relative to Peak')] = tempdict
            return dictPerf
        
    def interpoloateHPIvalues(self, dictPerf):
        '''interpolate the raw HPI values'''
        df = self.res
        for countrycode, dd in df.groupby(['country_code']):
            dd = dd.sort_index(by='datekey')
            dd = dd.set_index(df['datekey'])
            fullindex = datekeyRange(dd.index[0], dd.index[-1], step=1)
            dd = dd.reindex(index=fullindex)
            dd = dd.interpolate()
            tempdict = dict(zip(dd.index, dd['value']))
            dictPerf[(countrycode, 'House Price Indices')] = tempdict
        return dictPerf
    
    def calculateNominalGrowthRate(self, dictPerf):
        '''Nominal House Price Growth Rate'''
        df = self.res
        for countrycode, dd in df.groupby(['country_code']):
            dd = dd.set_index(dd['datekey'])
            dd = self.calculateGrowthRateValue(dd)
            tempdict = dict(zip(dd['datekey'], dd['growth_date']))
            dictPerf[(countrycode, 'Nominal House Price Growth')] = tempdict
        return dictPerf

    def calculateGrowthRateValue(self, df):
        tempcontainer = {}
        fullindex = datekeyRange(df.index[0], df.index[-1], step=1)
        df = df.reindex(index=fullindex)
        df = df.interpolate()
        df = df.sort_index(ascending=False)
        for ii in df.index:
            currentdt = ii
            year  = currentdt // 100 
            month = currentdt % 100
            previousdt = 100 * (year-1) + month
            if previousdt in df.index.tolist():
                diff = df.loc[currentdt, 'value'] - df.loc[previousdt, 'value']
                gr = 100 * (diff) / df.loc[currentdt, 'value']
                tempcontainer[currentdt] = gr
        newdf = pd.DataFrame(tempcontainer.items(), columns=['datekey', 'growth_rate'])
        newdf = newdf.sort_index(by='datekey')
        return newdf
    
    def loadMacrodataFromDB(self, query, vn):
        '''load macro data from database''' #TODO: revise again
        conn = sqlite3.connect(sDefaultDBPath) #detec_type=sqlite3.PARSE_DECLTYPES
        conn.row_factory = sqlite3.Row
        res = read_sql(self.query%(vn,), conn)
        return res
        
    def calculateRealPriceGrowth(self, dictPerf):
        '''Real House Price Growth Rate'''
        df = self.res
        df_cpi = self.loadMacrodataFromDB(sqlquery, 'cpi').groupby(['country_code'])
        for countrycode, dd in df.groupby(['country_code']):
            cpi = df_cpi.get_group(countrycode)
            hpi = dd.set_index(dd['datekey'])
            cpi = cpi.set_index(cpi['datekey'])
            real_hpi = 100 * hpi['value'] / cpi['value']
            
            dRealHPI = {'real_hpi': real_hpi}
            ndf = pd.DataFrame(dRealHPI)
            minDate = ndf.index[0]
            maxDate = ndf.index[-1]
            fullIndex = datekeyRange(minDate, maxDate, step=1)
            ndf = ndf.reindex(index=fullIndex)
            ndf = ndf.interpolate()
            
            ndf = ndf.sort_index(ascending=False)
            tempcontainer = {}
            currentdt = ndf.first_valid_index()
            for ii in ndf.index:
                year  = currentdt // 100
                month = currentdt % 100
                previousdt = 100 * (year - 1) + month
                if previousdt in (ndf.index.tolist()):
                    gr = 100 * ((ndf.loc[currentdt, 'real_hpi'] - ndf.loc[previousdt, 'real_hpi']) / 
                                ndf.loc[previousdt, 'real_hpi'])
                    tempcontainer[currentdt] = gr
                    
            rate_df = pd.DataFrame(tempcontainer.items(), columns=['datekey', 'growth_rate'])
            rate_df = rate_df.sort_index(by='datekey')
            tempdict = dict(zip(rate_df['datekey'], rate_df['growth_rate']))
            dictPerf = [(countrycode, 'Real House Price Growth')] = tempdict
        return dictPerf
            
    def test(self):
        print("Unfinished And Will Continue!")
    
if __name__ == '__main__':
    tt = MacroHousingDataManager(sqlquery)
    print(tt.test())

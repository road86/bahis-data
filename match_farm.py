import pandas as pd
import seaborn as sns

farms_bahis = pd.read_csv('./output/formdata_Farm_Assessment_Monitoring.csv')
farms_csv = pd.read_csv('./input/Farm assessments BAHIS Aug2017-Mar2022.csv')

farms_bahis=farms_bahis[farms_bahis['report_type']=='First assessment report']
farms_csv=farms_csv[farms_csv['report_type']=='First assessment report']

farms_bahis = farms_bahis.drop_duplicates(subset=['farm_id'], keep='last')
farms_csv = farms_csv.drop_duplicates(subset=['farm_id'], keep='last')

farms_match = pd.merge(farms_bahis,farms_csv,on='farm_id',how='outer',suffixes=['_bahis','_excel'],indicator=True)

farms_match = farms_match.reindex(columns=sorted(list(farms_match.columns)))

farms_match.to_csv('./output/farms_matched.csv')

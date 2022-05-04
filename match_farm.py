import pandas as pd

farms_bahis = pd.read_csv('./output/formdata_Farm_Assessment_Monitoring.csv')
farms_csv = pd.read_csv('./input/Farm assessments BAHIS Aug2017-Mar2022.csv')

farms_match = pd.merge(farms_bahis,farms_csv,on='farm_id',how='outer',suffixes=['bahis','excel'],indicator=True)

farms_match.to_csv('./output/farms_matched.csv')

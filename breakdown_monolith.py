import pandas as pd
import json

#formadata table from static BAHIS (aka V1) database
static = pd.read_csv('input/static.csv')
nodata=len(static)

#column 'form_name' says which form data given row contains
rowif = 0
for fm in static['form_name'].unique():
    print(f'Processing {fm}')
    # if fm!='Farm Assessment Monitoring':
    #     continue

    f1 = static[static['form_name']==fm]

    #create an empty dataframe for form named {fm}
    for row, val in f1.iterrows():
        c2 = list(json.loads(val['datajson']).keys())
        f2 = pd.DataFrame(columns=c2)
        break

    #fill in data stored in json in column {datajson}
    #create a list of json values
    jlist = []
    for row, val in f1.iterrows():
        jlist.append(json.loads(val['datajson']))

    f2 = pd.json_normalize(jlist)

    fm = fm.replace(' ','_')
    f2.to_csv(f'output/formdata_{fm}.csv')

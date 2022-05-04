import pandas as pd
import json

#formadata table from static BAHIS (aka V1) database
static = pd.read_csv('input/static.csv')
nodata=len(static)

#column 'form_name' says which form data given row contains
rowif = 0
for fm in static['form_name'].unique():
    print(f'Processing {fm}')
    if fm!='Farm Assessment Monitoring':
        continue

    f1 = static[static['form_name']==fm]

    #create an empty dataframe for form named {fm}
    for row, val in f1.iterrows():
        c2 = list(json.loads(val['datajson']).keys())
        f2 = pd.DataFrame(columns=c2)
        break

    #fill in data stored in json in column {datajson}
    for row, val in f1.iterrows():
        newrow = json.loads(val['datajson'])
        f2 = pd.concat([f2,
                   pd.DataFrame.from_dict(newrow,orient='index').transpose()
                   ], ignore_index=True)
        perc = rowif/nodata
        print(f'{rowif} of {nodata}, {perc:0.2f}')
        rowif = rowif + 1

    fm = fm.replace(' ','_')
    f2.to_csv(f'output/formdata_{fm}.csv')

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#text = pd.read_csv('/Users/Dovla/Desktop/Priv/Fax/DMT/HW1/aggText.tsv', sep='\t')
#title = pd.read_csv('/Users/Dovla/Desktop/Priv/Fax/DMT/HW1/aggTitle.tsv', sep='\t')

import sys
import pandas as pd

text = pd.read_csv(sys.argv[1], sep='\t')
title = pd.read_csv(sys.argv[2], sep='\t')
#v2 topK from GroundTruth
combine = pd.merge(text, title, how='outer', on=['Query_ID','Doc_ID'])
combine = combine.fillna(0)
combine['Final_Score'] = combine['Score_x'] + 2*combine['Score_y']
combine = combine.sort_index(by=['Query_ID', 'Final_Score'], ascending=[True, False])

groundTruth = pd.read_csv('/Users/Dovla/Desktop/Priv/Fax/DMT/HW1/Cranfield_DATASET/cran_Ground_Truth.tsv', sep = '\t')

temp1 = pd.DataFrame(groundTruth.groupby('Query_id').agg('count')).to_dict()
temp1 = temp1['Relevant_Doc_id']
temp1

final = combine.groupby('Query_ID').apply(lambda dfg: dfg.nlargest(temp1[dfg.name],'Final_Score')).reset_index(drop=True)
final = final.loc[:,['Query_ID', 'Doc_ID','Final_Score']]
final['Rank'] = final.groupby(['Query_ID'])['Final_Score'].rank(method = 'first', ascending = False)
final
final.to_csv('aggTextTitle.tsv', sep='\t', index=False, columns = ['Query_ID','Doc_ID', 'Rank', 'Score'])

#final.to_csv('/Users/Dovla/Dropbox/Fax/DMT/HW1/aggTextTitleTest.tsv', sep='\t', index=False, columns = ['Query_ID','Doc_ID', 'Rank', 'Score'])

#v1 top-200
#combined1 = pd.merge(text, title, how='outer', on=['Query_ID', 'Doc_ID'])
#combined1 = combined1.fillna(0)
#combined1['Score'] = combined1.Score_x + (combined1.Score_y * 2)
#combinedSorted1 = combined1.sort_values(['Query_ID', 'Score'], ascending=[1, 0])
#comb1test = combinedSorted1.groupby('Query_ID').head(200).reset_index(drop=True)
#comb1test['Rank'] = comb1test.groupby(['Query_ID'])['Score'].rank(method = 'first',ascending=False)
#comb1test.to_csv('/Users/Dovla/Dropbox/Fax/DMT/HW1/resTest1.tsv', sep='\t', index=False, columns = ['Query_ID','Doc_ID', 'Rank', 'Score'])

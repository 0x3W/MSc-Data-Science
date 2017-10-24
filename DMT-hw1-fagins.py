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


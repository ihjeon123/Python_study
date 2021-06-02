def information_gain(col):
    import pandas  as  pd
    import  numpy  as  np
    skin = pd.read_csv("c:\\data\\skin.csv")
    column_names = skin.columns[ 3 : -1 ]
    column_names
    x = skin['cupon_react']
    ct = pd.crosstab( x, skin[col], margins= True)
    values = np.unique(  skin[col].values )
    before  =  [ ct.loc[i]['All'] / ct.loc['All']['All']  for  i  in  values ]
    before_entropy =  np.sum( [- i * np.log2(i) for  i  in before] )
    
    after = [ ct[j][i]/ct['All'][i]  for  j in values for i in  values ]
    after_entropy =before[0] * np.sum([-i*np.log2(i) for  i  in after[0:2]]) + \
                        before[1] * np.sum([-i*np.log2(i) for  i  in after[2: ]])
    
    return  before_entropy - after_entropy

for i in skin.columns[3:6]:
    print('{0} : {1}'.format(i, information_gain(i)))





def elimin_outliers(df,list_col ):
    
    '''elimina outliers baseado no intervalo interquartil
    
    Input:
    list_col: lista com colunas para a eliminação
    '''
    
    
    #elimina pontos outliers
    df_semOut= df.copy()

    #elimina linhas da df
    for col in list_col:    
        
        # calculo de IQR
        Q1 = df_semOut[col].quantile(0.25)
        Q3 = df_semOut[col].quantile(0.75)
        IQR = Q3 - Q1
   
        frac=1.5
        serieBool=(df_semOut[col]<(Q1-frac*IQR))\
               |(df_semOut[col]>(Q3+frac*IQR))    
    
    
        #elimina linhas fora do intervalo acima
        df_semOut=df_semOut[~serieBool]   
    

    #numero de linhas eliminadas:
    nLinha_elim= len(df)-len(df_semOut)
    fracElim=nLinha_elim/len(df)
    
    return(nLinha_elim, fracElim, df_semOut)  

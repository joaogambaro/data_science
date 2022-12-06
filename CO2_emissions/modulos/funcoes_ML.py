import pandas as pd


def results_CV_organizado(search, set_params=False):

    '''
    Organiza o resultado da grid search. Retorna um dataframe com informações
    relevantes e com nomes mais amigávies

    Inputs:
    "search": objeto da cross validadtin treinada

    Output:
    "df_results": dataframe com os resultados organizados
    '''

    df_results = pd.DataFrame(search.cv_results_)


    # Colunas slecionadas	
    if set_params:
        columns=['mean_test_score','std_test_score','params']
    else:
        columns=['mean_test_score','std_test_score']	
	
    param_lista=[var for var in df_results.columns if var[0:5]=="param" and var!= "params"]
    split_lista=[var for var in df_results.columns if var[0:5]=="split"]
    colunas_sel=columns+param_lista+split_lista

    # Nome para renomear as colunas
    if set_params:
        colunms_rename=['mean_score','std_score', 'params']
        param_rename=[var[6:] for var in param_lista]
        split_rename=[var[0:6]+"_score" for var in split_lista]
        colunas_rename=colunms_rename+param_rename+split_rename
    else:
        colunms_rename=['mean_score','std_score']
        param_rename=[var[6:] for var in param_lista]
        split_rename=[var[0:6]+"_score" for var in split_lista]
        colunas_rename=colunms_rename+param_rename+split_rename


		
    #seleciona e renomeia as colunas
    df_results = df_results[colunas_sel]
    df_results.columns=colunas_rename

    return(df_results)



def results_CV_organizado_metricas_adici(search, muda_sinal_metrica=True, set_params=False):

    """
    Retorna um dataframe com formato amigável dos resultados da cross validation
    com duas colunas adicionais relativas a novas métricas criadas para a seleção
    de hiperparâmetros

    Inputs:
    "search": objeto da cross validation treinada
    "muda_sinal_metrica": muda o sinal da métrica retornada pala CV. É útil pois
                        a CV realiza um processo de minimização e por isto altera
                        o sinal de algumas métricas

    Output:
    "df_results": dataframe com os resultados organizados
    """

    # df com resultados organizados
    df_results=results_CV_organizado(search, set_params=set_params)

    # coluna com "split*"
    split_lista=[var for var in df_results.columns if var[0:5]=="split"]

    # muda o sinal da métrica(algumas métricas tem sinal negativo devido a CV)
    if muda_sinal_metrica:
        df_results['mean_score']=df_results['mean_score']*(-1)        
        df_results[split_lista]=df_results[split_lista]*(-1)

    #adiciona novas métricas
    df_results["mean_std"]=df_results[['mean_score', 'std_score' ]].sum(axis=1)
    df_results["pior_score"]=df_results[split_lista].min(axis=1)

    return(df_results)



def seleciona_resultados(search):

    """
    Retorna os melhores resultados de acordo duas métricas:
        Metrica A - menor valore de media+std
        Metrica B - menor dos piores scores da CV

    Inputs:
    "search": objeto da cross validation treinada

    Outputs:
    "[A,B]": melhores valores para as métricas A e B
    "[param_A, param_B]": lista com os parâmetros que levaram aos menores valores
	"""
	
	#resultados organizados
    df_results=results_CV_organizado_metricas_adici(search, muda_sinal_metrica=True,set_params=True)
	

    # melhores valores e parametros
    A=df_results["mean_std"].min()
    B=df_results["pior_score"].min()

    param_A=df_results[df_results["mean_std"]==A]['params'].to_list()[0]
    param_B=df_results[df_results["pior_score"]==B]['params'].to_list()[0]

    return([A,B], [param_A, param_B])





import csv
import os

def adiciona_resultado_CSV(file_path=None,file_path_seg=None, data_line=None, header=None):

    '''
    Obs:
     - so é possível adicionar um título quando o arquivo está vazio. Se tentar adic.
       com o arquivo contendo dados o título não é escrito no codigo
     - se o titulo não for forncido os dados são escritos em um arquivo sem titulo

     - e segundo arquivo pode ser iniciado depois que o primeiro ja contém dados e de
       de forma diferente (com ou sem titulo), mas este não é o propósido da funcao
    '''

    # escreve no arquivo principal
    with open(file_path, 'a') as arq:
        if os.stat(file_path).st_size == 0:

            #quando o arquivo esta vazio
            if header!=None:
                # escreve o título e os dados
                writer = csv.writer(arq)
                writer.writerow(header)
                writer.writerow(data_line)
            else:
                # escreve somente os dados
                writer = csv.writer(arq)
                writer.writerow(data_line)
        else:
            #quando o arquivo não esta vazio
            # escreve os dados
            writer = csv.writer(arq)
            writer.writerow(data_line)

        #Obs: usando open com 'with' não precisa fechar o arquivo

    # escreve no arquivo de segurança
    if(file_path_seg!=None):
        with open(file_path_seg, 'a') as arq:
            if os.stat(file_path_seg).st_size == 0:
                if header!=None:
                    # escreve o título e os dados
                    writer = csv.writer(arq)
                    writer.writerow(header)
                    writer.writerow(data_line)
                else:
                    # escreve somente os dados
                    writer = csv.writer(arq)
                    writer.writerow(data_line)
            else:
                # escreve os dados
                writer = csv.writer(arq)
                writer.writerow(data_line)


from sklearn import metrics
import joblib

def treina_modelo(X_train, y_train, modelo, kargs=None,
                  nome_mod=None, path_mod=None, salva_mod=False):
    '''
    Treina um modelo e salva o modelo treinado
    '''

    modelo.set_params(**kargs)
    modelo.fit(X_train, y_train)

	#salva o modelo treinado
    if salva_mod:
        joblib.dump(modelo, str(path_mod)+"/"+nome_mod+'.joblib')

    return(modelo)





def gera_linha_de_dados_CV(X_train, y_train, X_test,y_test, resultados=None,
                           A_clu='?', B_clus='?', modelo=None,nome_mod=None,
                           path_mod=None, salva_mod=False):
    '''
    Gera uma linha de dado para ser armazenada no arquivo .csv

    Output:
    retorna uma tupla onde o pirmeiro valor é uma lista com os títulos e o segundo
    são os dados
    '''

	# teste scores
    teste_score=[]
    for i in [0,1]:

        # dicionário com os hip.
        kargs=resultados[1][i][0]
        modelo = treina_modelo(X_train, y_train,
                 modelo,
                 nome_mod=nome_mod+"_scr_"+str(i),
                 path_mod=path_mod,
                 kargs=kargs,
                 salva_mod=salva_mod)

        # faz previsão
        y_hat=modelo.predict(X_test)
        teste_score.append(metrics.mean_squared_error(y_hat,y_test,squared=False))


    # formato:("titulo", "dados")
    L=[('nome_modelo', nome_mod),
	   ('A',resultados[0][0]),
	   ('B',resultados[0][1]),
	   ('teste_A',teste_score[0]),
	   ('teste_B',teste_score[1]),
	   ('A_clu', '?'),
	   ('B_clus','?'),
	   ('params_A',resultados[1][0][0]),
	   ('params_B',resultados[1][1][0])]

    return([var[0] for var in L], [var[1] for var in L])



# seleciona o objeto da cros. val.
def get_rand_search(pipe_search_CV):    
    """
    Para um pipeline cujo último elemento é um algoritimo
    de 'tunning hiperperemeters', este método retorna o
    objeto responsável pelo ajuste no pipeline.
    
    Outpu:
     objeto com random search CV
    """  
    # seleciona o último elemento do pipeline
    return(pipe_search_CV.steps[-1][1])



def get_model(pipe_search_CV):    
    """
    Retorna o modelo para estimações considerado no pipeline
    com a redom search cv
    
    Output:
     modelo estimador com random search CV
    """  
    # seleciona o último elemento do pipeline
    return(pipe_search_CV.steps[-1][1].estimator)



from sklearn.pipeline import Pipeline

def make_best_pipeline(pipe_search_CV, params, rand_state=1000):

    '''
    A parti do objeto pra tunning hip. ('pipe_search_CV'), gera um pipeline
    com todas as etapas de transoformação nos primeiros passos e no último
    passo é o colocado o modelo estimador usado no C.V. com o parâmetros 
    fornecidos. 

    Os parâmtetros fornecidos são escolhidos a partir dos resultados da CV.
    '''
    
    # seleciona os primeiros passos do pipeline
    steps_pipe = pipe_search_CV.steps[0:-1]
    
    # adc. seed nos params
    params['random_state']=rand_state    
    
    # adiciona o ultimo passo como o modelos do CV
    nome = "modelo"   
    modelo = pipe_search_CV[-1]\
            .estimator\
            .set_params(**params)
    
    steps_pipe.append((nome,modelo))
    
    #retorna o pipeline    
    return(Pipeline(steps_pipe))






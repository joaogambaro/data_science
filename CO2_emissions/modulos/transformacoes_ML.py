

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import LabelEncoder



class Mapeamento(BaseEstimator, TransformerMixin):

    '''
    Realiza a codificação de variáveis categóricas em variáveis numéricas.
    A codificação feita é do tipo 'label encoder'
'   '''
    
    def __init__(self):
        self.leb_enc_list=[]
        self.vars_cat=[]
        
    def fit(self, X):
        
        # seleciona variáveis categóricas e numéricas
        self.vars_cat = [var for var in X.columns if X[var].dtype == 'O']
        self.vars_cat.append("Cylinders")       
        
        # fit
        for cat in self.vars_cat:
            le = LabelEncoder().fit(X[cat])            
            
            #armazena método treinado
            self.leb_enc_list.append(le)
            
        return self
    

    def transform(self, X):    
        
        X_aux=X.copy()
        
        # faz a transformação               
        for cat, le in zip(self.vars_cat, self.leb_enc_list):
            X_aux[cat] = le.transform(X[cat])
        
        return(X_aux)






from sklearn.cluster import KMeans
import numpy as np

class AdicionaColClusters(BaseEstimator, TransformerMixin):
    
    '''
    Adiciona os números dos clusters obtidos pelo algorítimo
    kMeans no dataset. O dataset resultante pode ser usado em
    em um modelos de previsão. 
    
    Esta classe foi feita pensando em ser utiliada em pipelines
    para treinamentos de modelos    
    '''
    
    def __init__(self, k=3, rand=1000):
        self.kmeans = []
        self.k = k
        self.rand = rand

        
    def fit(self, X, y=None):
      
        model = KMeans(n_clusters=self.k, random_state=self.rand)        
        self.kmeans = model.fit(X)        
        return self
    

    def transform(self, X):    
        
        X_aux=X.copy()
               
        # adiciona coluna com clusters
        X_aux=np.column_stack((X_aux, self.kmeans.predict(X_aux)))
        
        #X_aux.insert(0,                 # posição da coluna
        #    "k_"+str(self.k),           # nome da coluna
        #    self.kmeans.predict(X_aux)  # vator com valores
        #    )       
               
        return(X_aux)

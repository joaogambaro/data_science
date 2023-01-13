

#-----------------------------------------------------------
#   Funções para gráficos de rosca
#-----------------------------------------------------------

import matplotlib.pyplot as plt


def formata_string(lis_values, d1=1, d2=1):    
    '''
    Função para formatar string para os resultados 
    num gráfico de pizza ou rosca
    '''
    
    def formata_string_aux(n_porcent):
        
        # transforma a porcentgem em numero
        total = sum(lis_values)        
        n = int(round(n_porcent * total / 100.0))
        
        # retorna a porcentagem e o numero
        return f'{round(n_porcent,d1)}%\n({round(n,d2)})'   
    
    # retorna a funcão 'formata_string' configurada com d1,d2 e lis_values
    return formata_string_aux



def plot_rosca_agg(ax=None,
                   data=None,
                   col_agg=None,   
                   paleta=None,
                   d=1,
                   tam_letra=40,
                   fracCirculo=0.8,
                   f_textCentr=0.6,
                   showCount=False):
    
    # gera dados e labels
    dados = df[col_agg].value_counts().values
    labels = df[col_agg].value_counts().index.to_list()
    
    
    # define se mostra porcentagem com numeros(padrao é só porcentagem)
    func=lambda x: f'{round(x,d)}%'
    if showCount:
        func = formata_string(dados, d1=1, d2=1)
        
    
    # plota grafico de pizza   
    ax.pie(dados,
            labels = labels,  
            colors = paleta,
            textprops = {"fontsize": tam_letra},            
            wedgeprops = {"ec": "white","linewidth":0}, 
            pctdistance = f_textCentr, # distância dos numeros interno ao centro
            startangle= 0,        # ângulo do primeiro traço
            radius =1.0,          # define raio da pizza(1 pq faz analogia com 100%)
            labeldistance = 1.1,  # distancia dos rótulos para o disco   
            counterclock=True,    # sentido de rotação para a construção do gráfico
            autopct= func,        # formata texto com com numeros        
            )
    
    # desenha um circulo interno branco
    center_circle = plt.Circle((0, 0), fracCirculo, color='white') 
    ax.add_artist(center_circle)
    ax.axis('equal')   
    
    
def plot_rosca(ax=None,
               listaVal=None,
               rotulosVal=None,   
               paleta=None,
               d=1,
               tam_letra=40,
               fracCirculo=0.8,
               f_textCentr= 0.6,
               startangle=0,
               showCount=False):
    
    
    # define se mostra porcentagem com numeros(padrao é só porcentagem)
    func=lambda x: f'{round(x,d)}%'
    if showCount:
        func = formata_string(listaVal, d1=1, d2=1)
        
    
    # plota grafico de pizza   
    ax.pie(listaVal,
           labels = rotulosVal,  
           colors = paleta,
           textprops = {"fontsize": tam_letra},            
           wedgeprops = {"ec": "white","linewidth":0},
           pctdistance = f_textCentr, # distância dos numeros interno ao centro
           startangle= startangle, # ângulo do primeiro traço
           radius =1.0,          # define raio da pizza(1 pq faz analogia com 100%)
           labeldistance = 1.1,  # distancia dos rótulos para o disco   
           counterclock=True,    # sentido de rotação para a construção do gráfico
           autopct= func        # formata texto com com numeros        
          )
    
    # desenha um circulo interno branco
    center_circle = plt.Circle((0, 0), fracCirculo, color='white') 
    ax.add_artist(center_circle)
    ax.axis('equal') 

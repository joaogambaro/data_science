




class pdr_class:
    def __init__(self):
        # estilos e cores
        self.estilos_sns=['white', 'whitegrid']
        self.paletas=['magma','crest', 'mako', 'PuBuGn_r']
        self.cores_barras=['#000080', '#4682B4', '#008B8B', '#66CDAA']
        self.cores_texto = ['#000000']
        self.cores_eixos= ['#cccccc']
        self.cores_ticks= ['#cccccc']


        # tamanhos das letras (calculada como f_*dy)
        self.f_titulo = 0.35
        self.f_numeros_barras = 0.25
        self.f_ticks_x = 0.3
        self.f_ticks_y = 0.3

        # distancia do texto a barra
        # Obs: esta distância é calcuda como:
        # f_texto_bar*(comprimento da primeira barra no gráfico)
        self.f_texto_bar = 0.02



# instancia da classe com padrões
pdr = pdr_class()

# casas decimais numeros
def num_dec(num, d=1):
    if d==0:
        text = '{:,.0f}'.format(num)
    elif d==1:
        text = '{:,.1f}'.format(num)
    elif d==2:
        text = '{:,.2f}'.format(num)
    elif d==3:
        text = '{:,.3f}'.format(num)
    elif d==4:
        text = '{:,.4f}'.format(num)
    return(text)


def porcent_dec(num, d=1):
    if d==0:
        text = '{:,.0f}%'.format(num)
    elif d==1:
        text = '{:,.1f}%'.format(num)
    elif d==2:
        text = '{:,.2f}%'.format(num)
    elif d==3:
        text = '{:,.3f}%'.format(num)
    elif d==4:
        text = '{:,.4f}%'.format(num)
    return(text)

def num_porcent_dec(num, d=1):
    '''
    Escrever funcao para plotar numero e porcentagem ex. 123.2(45.3%), ambos
    com casas decimais
    '''



def _dl(ax, barras_vert=True):
    '''
    Retorna um parâmetro usado para ajustar o tamanho das letras
    nos graficos de barras. O parâmero em questão consiste na
    largura do gráfico dividido pelo número de barras plotadas.
    O tamanho das letras é proporcional a este parâmetro
    '''
    if barras_vert:
        # para gráfico com barras verticais
        return(ax.bbox.width/len(ax.patches))
    else:
        # para gráfico com barras horizontais
        return(ax.bbox.height/len(ax.patches))



def eixos_barplot_vertical(ax,titulo):
    '''
    Configura os eixos dos gráficos
    '''

    # parametro para ajuste do tamanho das letras
    dl= _dl(ax)

    # nomes e tilulo
    ax.set_ylabel("")
    ax.set_xlabel("")
    ax.set_title(titulo, size = pdr.f_titulo*dl)

    # definições dos eixos
    ax.spines[['right','top']].set_visible(False)
    ax.spines[['bottom','left']].set_color(pdr.cores_ticks[0])

    # marcações nos eixos
    ax.tick_params(axis ='x', labelrotation = 90,
                   labelsize=pdr.f_ticks_x * dl)
    ax.tick_params(axis='y', labelrotation = 0,
                   labelsize = pdr.f_ticks_y* dl)
    ax.tick_params(bottom=True, color=pdr.cores_ticks[0]) #mostra as marcações dos ticks
    ax.tick_params(left=True, color=pdr.cores_ticks[0]) #mostra as marcações dos ticks

def eixos_barplot_horizontal(ax,titulo):

    # parametro para ajuste do tamanho das letras
    dl= _dl(ax)

    # nomes e tilulo
    ax.set_ylabel("")
    ax.set_xlabel("")
    ax.set_title(titulo, size = pdr.f_titulo*dl)

    # definições dos eixos
    ax.spines[['top','right','bottom']].set_visible(False)
    ax.spines['left'].set_color(pdr.cores_ticks[0])

    # marcações nos eixos
    ax.tick_params(axis='y', labelrotation=0, labelsize=pdr.f_ticks_x * dl)
    ax.tick_params(left=True, color=pdr.cores_ticks[0]) #mostra as marcações dos ticks
    ax.set_xticks([])


def numeros_barras_verticais(ax, dy=None,f_texto_bar=None,f_numeros_barras=None,
                cor_texto=None, d=1, is_percent=False):
    '''
    Escreve os números equivalentes as alturas das barras em cima das
    barras
    '''
    # parametro para ajuste do tamanho das letras
    dl=_dl(ax)

    # fracao para calculo de dy(distancia da barra ao texto)
    if f_texto_bar==None:
        f_texto_bar= pdr.f_texto_bar

    #calculo de dy
    if dy==None:
        dy= f_texto_bar*(ax.patches[0].get_height())

    # fracao para definir o tamanho da letra
    if f_numeros_barras==None:
        f_numeros_barras = pdr.f_numeros_barras

    # cor do texto
    if cor_texto==None:
        cor_texto = pdr.cores_texto[0]

    # configurações texto
    kargs = {
        'fontsize': f_numeros_barras * dl,
        'color':    cor_texto,
        'ha':       'center',
    }

    # escreva os textos nas barras
    for p in ax.patches:

        # coordenadas do texto
        x = p.get_center()[0]
        y = p.get_height()+dy

        if is_percent==False:
            # texto como numero decimal
            ax.annotate( num_dec(p.get_height(),d=d), (x, y), **kargs)
        else:
            # texto como porcentagem
            ax.annotate( porcent_dec(p.get_height(),d=d), (x, y), **kargs)

    return(dy)


def numeros_barras_horizontais(ax,dx=None,f_texto_bar=None,f_numeros_barras=None,
                                cor_texto=None, d=1, is_percent=False):
    '''
    Escreve os números equivalentes aos comprimentos das barras no canto
    das barras
    '''

    # parametro para ajuste do tamanho das letras
    dl=_dl(ax)

    # fracao para calculo de dx(distancia da barra ao texto)
    if f_texto_bar==None:
        f_texto_bar= pdr.f_texto_bar

    #calculo de dx
    if dx==None:
        dx= f_texto_bar* (ax.patches[0].get_width())


    # fracao para definir o tamanho da letra
    if f_numeros_barras==None:
        f_numeros_barras = pdr.f_numeros_barras

    # cor do texto
    if cor_texto==None:
        cor_texto = pdr.cores_texto[0]


    # configurações texto
    kargs = {
        'fontsize': f_numeros_barras * dl,
        'color':    cor_texto,
        'va':       'center'
    }


    # escreve os textos nas barras
    for p in ax.patches:

        # coordenadas do texto
        y = p.get_center()[1]
        x = p.get_width() +dx

        if is_percent==False:
            # texto como numero decimal
            ax.annotate( num_dec(p.get_width(),d=d), (x, y), **kargs)
        else:
            # texto como porcentagem
            ax.annotate( porcent_dec(p.get_width(),d=d),(x, y), **kargs)

    return(dx)


def muda_limites_eixo_y(ax, y_min=None, y_max=None,tipo_aumento=0, frac=0.1):
    '''
    Muda os limites dos gráficos com o objetivo de melhorar a aparência
    da figura.

    Esta função amplia o eixo y. Para a amplicação é calculada a diferença
    entre o mínimo e máximo original (chamada de dy). A ampliação é feita
    adicionando uma fração de dy (frac*dy) aos limites do eixo y do gráfico.

    Args:
        frac: fração de 'dy' para aumento do limite superior do eixo y
    '''

    # limites no aixo x
    if y_min==None:
        y_min, y_max = ax.get_ylim()

    # variação no eixo
    dy= frac*(y_max-y_min)

    # aumenta os limites
    if tipo_aumento==0:
        ax.set_ylim([y_min, y_max+dy])
    elif tipo_aumento==1:
        ax.set_ylim([y_min-dy , y_max])
    elif tipo_aumento==2:
        ax.set_ylim([y_min-dy , y_max+dy])

    # retorna limites antigos
    return(y_min, y_max)


def muda_limites_eixo_x(ax, x_min=None, x_max=None,tipo_aumento=0, frac=0.1):
    '''
    Muda os limites dos gráficos com o objetivo de melhorar a aparência
    da figura.

    Esta função amplia o eixo x. Para a amplicação é calculada a diferença
    entre o mínimo e máximo original (chamada de dx). A ampliação é feita
    adicionando uma fração de dx (frac*dx) aos limites do eixo x do gráfico

    Args:
        frac: fração de 'dx' para aumento do limite superior do eixo x
    '''

    # limites no aixo x
    if x_min==None:
        x_min, x_max = ax.get_xlim()

    # variação no eixo
    dx= frac*(x_max-x_min)

    # aumenta os limites
    if tipo_aumento==0:
        ax.set_xlim([x_min, x_max+dx])
    elif tipo_aumento==1:
        ax.set_xlim([x_min-dx , x_max])
    elif tipo_aumento==2:
        ax.set_xlim([x_min-dx , x_max+dx])

    # retorna limites antigos
    return(x_min, x_max)




#------------------------------------------------------------------------
#   Funções para montar as figuras
#-------------------------------------------------------------------

import seaborn as sns

def bar_plot_freqModels(ax, df, x=None, y=None, y_min=None,y_max=None,
                        dy=None, titulo=None):
    '''
    Plota graficos para a análise do modelos mais prequentes na amostra
    '''

    # plota barra as barras
    sns.set_theme(style=pdr.estilos_sns[0])
    sns.barplot(x=x, y=y, data=df, ax=ax, palette=pdr.paletas[0])

    # coloca num. nas barras e muda limites dos eixos
    h=numeros_barras_verticais(ax,dy=dy)
    y_lims = muda_limites_eixo_y(ax,y_min=y_min,y_max=y_max)

    # considera a configuração padrão para os eixos
    eixos_barplot_vertical(ax,titulo)

    return(y_lims,h)


def bar_plot_model_make(ax, df, dx=None, d=1, is_percent=False,
                        texto_float=True, x=None, y=None, titulo=None):

    #plota as barras
    sns.set_theme(style=pdr.estilos_sns[0])
    sns.barplot(x=x, y=y, data=df, ax=ax, palette= pdr.paletas[0])

    # coloca num. nas barras e muda limites dos eixos
    numeros_barras_horizontais(ax, f_numeros_barras=1.2, d=d, is_percent=is_percent)
    muda_limites_eixo_x(ax, frac=0.2)

    # eixos
    ax.set_ylabel("")
    ax.set_xlabel("")
    ax.set_title(titulo, size=14)
    ax.tick_params(axis='y', labelrotation=0, labelsize=10)
    ax.spines[['top','right','bottom']].set_visible(False)
    ax.spines['left'].set_color('#cccccc')
    ax.tick_params(left=True, color='#cccccc') #mostra as marcações dos ticks
    ax.set_xticks([])


def plot_fuel_consume(ax,
                      df_mean_fuel,
                      col_name=None,
                      n=10,
                      is_head=True,
                      dx=None,
                      x_min=None,
                      x_max=None,
                      titulo="",
                      color='#4B0082'):

    # estilo white
    sns.set_theme(style= pdr.estilos_sns[0])

    # parametros do barplot
    kargs={'linewidth': 0.5,
           'edgecolor': "#000000",
           'color': color
          }

    # plota as barras
    if(is_head):
        sns.barplot(ax=ax, data=df_mean_fuel.head(n),
                    x=col_name, y="Model",
                    **kargs)
    else:
        sns.barplot(ax=ax, data= df_mean_fuel.tail(n),
                    x=col_name, y="Model",
                    **kargs)


    # escreve numero nas barras e muda limites dos eixos
    dx= numeros_barras_horizontais(ax,f_numeros_barras=None,dx=dx, d=2)
    x_lims= muda_limites_eixo_x(ax, x_min=x_min, x_max=x_max,frac=0.3)

    # nomes e titulo
    ax.set_title(titulo, size=28)
    ax.set_ylabel("")
    ax.set_xlabel("")
    #eixos
    ax.spines[['top','right']].set_visible(False)
    ax.spines[['left','bottom']].set_color(pdr.cores_eixos[0])
    #ticks
    ax.set_xticks([])
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelrotation=0, labelsize=10)
    ax.tick_params(left=True)      #mostra as marcações dos ticks

    return(x_lims,dx)



def plot_kde(ax, df, x_col=None, col_hue=None, palette=None):

    sns.set_theme(style= pdr.estilos_sns[0])
    sns.kdeplot(data=df,
                x=x_col,
                hue=col_hue,
                ax=ax,
                alpha=.5,
                linewidth=1,
                palette=palette,
                fill=True,
                common_norm=False)

    # muda limites nos gráficos
    muda_limites_eixo_y(ax, frac=0.2)

    # titulo e nomes
    ax.set_title("Distribição: "+x_col, size=24)
    ax.set_xlabel(x_col,size=20)
    ax.set_ylabel("")
    # eixos
    ax.spines[['top','right']].set_visible(False)
    # ticks
    ax.tick_params(axis='x', labelsize=20)
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(left=True)      #mostra os traços
    ax.tick_params(bottom=True)    #mostra os traços





def bar_plot_kde(ax, df_inp, x_col=None, y_col=None, palette=None,
             y_min=None, y_max=None):

    # monta a figura
    sns.set_theme(style= pdr.estilos_sns[0])
    sns.barplot(data=df_inp,
                x=x_col,
                y=y_col,
                estimator='mean',
                errorbar=None,
                ax=ax,
                palette=palette
               )

    # muda limites nos gráficos
    muda_limites_eixo_y(ax, y_min=y_min, y_max=y_max, frac=0.2)
    muda_limites_eixo_x(ax, tipo_aumento=2, frac=0.2)

    # titulo e nomes
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_title("Media de "+y_col, size=24)
    # eixos
    ax.spines[['top','right','left']].set_visible(False)
    # ticks
    ax.set_yticks([])
    ax.tick_params(axis='x', labelsize=0.09*_dl(ax))
    ax.tick_params(axis='y', labelsize=0.09*_dl(ax))



def hist_var_num(ax,df,col):
    '''Plota um histograma para uma variável númerica
    
    Args:
        ax: eixo da figura onde será plotado o histograma
        df: dataframe com os dados
        col: coluna do dataframe
    
    '''
    sns.set_theme(style="white")
    sns.histplot(data=df,
                x=col,
                bins=13,             #bins=np.arange(0, 9, 0.5)            
                element= "bars",     #bars,poly
                kde=True,                
                line_kws={'linewidth':1.8},                  
                edgecolor="white",
                color='#1360ac',   #"#49389C",
                ax=ax)
    
    # muda limites nos gráficos
    muda_limites_eixo_y(ax, frac=0.2)
    muda_limites_eixo_x(ax, frac=0.15)
    
        
    ax.set_title("Hist.: "+col, size=22)  #fontweight='bold'
    ax.tick_params(axis='x', labelsize=16, labelrotation=0, color='#cccccc')
    ax.tick_params(axis='y', labelsize=16, labelrotation=0, color='#cccccc')
    ax.set_ylabel("")
    ax.set_xlabel(col,size=18)
    ax.spines[['top','right']].set_visible(False)
    ax.spines[['left','bottom']].set_color('#cccccc')
    ax.tick_params(left=True, color='#cccccc')
    ax.tick_params(bottom=True, color='#cccccc')




def plot_tSNE(ax,data=None, hue=None,
              title='colocar titulo',
              palette='mako' ):
    '''
    Plota os resultados de da transformação t-SNE e colore os 
    pontos de acordo com as categóricas definidas em 'hue'
    
    Inputs:
    df_cluster: dataframe com os dados dos dataset e colunas
                adicionais para armazenar as coordenadas obtidas 
                pala t-SNE.
    hue: variável categórica usada para colorir os pontos.
    '''    
    
    sns.scatterplot(x="tSNE_x",
                    y="tSNE_y",
                    hue=hue,
                    data=data,
                    ax=ax,
                    palette=palette)
    
    ax.legend(title=title,bbox_to_anchor=(1.0, 1.0, 0.20, 0))
    ax.set_title("Rótulos: "+title, size=17)




def plot_line_metrica_models(ax, data, y_inp=None, x_inp=None):
    
    '''
    Plota a métrica dos modelos em um gráfico de linhas    
    
    Ref. para o desenho das setas:
    [1]:https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch
    [2]:https://matplotlib.org/stable/gallery/text_labels_and_annotations/annotate_transform.html#sphx-glr-gallery-text-labels-and-annotations-annotate-transform-py
    [3]:https://matplotlib.org/stable/gallery/text_labels_and_annotations/fancyarrow_demo.html            
    '''    
    

    #defina o eixo X
    if x_inp==None:
        x_inp=[x for x in range(len(data))]
    
    #plota o gráfico
    sns.set_theme(style="white")
    sns.lineplot(        
        data=data,
        y=y_inp,
        x=x_inp,
        ax=ax,
        linewidth=1.3,
        color='#191970', #'#000080'
        marker='o',
        markersize=5,      
    )
    
    
    # rotina para escrever as anotações    
    for p in ax.lines:
        
        # coordenadas dos pontos
        [x_pts,y_pts]= p.get_data()
        
        # para as anotações
        for i in range(x_inp[-1],0,-8):            
            
            # coordenadas do texto
            x_in = x_pts[i]
            y_in = y_pts[i]    
    
            # monta o texto 
            nome_mod = data["Modelos"].iloc[i]
            nome_crit = data["criterio_sel_CV"].iloc[i]
            texto = nome_mod+"\n("+nome_crit+")"
            
            # configurações da caixa e seta
            bbox=dict(boxstyle="round4", pad=1, edgecolor="k",
                      facecolor="w", linewidth=0.5)
            arrowprops=dict(arrowstyle='->',color='k',
                            shrinkB=30.0)
                          
            
            #faz a anotação           
            ax.annotate(texto,
                        xy=(x_in, y_in),
                        xytext=(x_in+0.6,y_in+1.7),
                        color='k',
                        size=7,
                        ha='center',
                        arrowprops=arrowprops,      
                        bbox=bbox
                       )
        
            
        # escreve os numeros
        dy=0.2
        for x, y in zip(x_pts,y_pts):       
            
            ax.annotate(num_dec(y,2),
                        size=7,
                        xy=(x, y+dy),                        
                        ha='center',
                        rotation=30)    
    
    # muda limites nos gráficos
    muda_limites_eixo_y(ax, frac=0.2)    
    

    # titulo e nomes
    ax.set_xlabel("Modelos", size=12)
    ax.set_ylabel(y_inp, size=12)
    ax.set_title("Métrica: "+y_inp, size=15)
    # eixos
    ax.spines[['top','right']].set_visible(False)
    ax.spines[['left','bottom']].set_color('#cccccc')    
    # ticks   
    ax.tick_params(left=True, labelsize=10, color='#cccccc')
    ax.tick_params(bottom=True, labelsize=10, color='#cccccc')







# --- Funções no módulo-----

# --- para barras verticais ----
'''
num_barras_verticais(ax, f_texto_bar=0.025, f_tam_letra=0.25,cor_texto='#000000',
                     d=1, rotation=0, ds=None)

porc_barras_verticais(ax, sum_tot=None, f_texto_bar=0.025, f_tam_letra=0.25,
                      cor_texto='#000000', d=1, rotation=0, ds=None)

porc_num_bar_verticais(ax, sum_tot=None,  f_texto_bar=0.025,  f_tam_letra=0.25,
                      d_porc=1,  d_num=1,  org_texto=1, cor_texto='#000000',
                      rotation=0, ds=None )
'''
# --- para barras horizontais ----
'''
num_barras_horizontais(ax, f_texto_bar=0.025, f_tam_letra=0.25, cor_texto='#000000',
                       d=1, rotation=0, ds=None)

porc_barras_horizontais(ax, sum_tot=None, f_texto_bar=0.025, f_tam_letra=0.25,
                        cor_texto='#000000', d=1, rotation=0, ds=None)

porc_num_bar_horizontal(ax, sum_tot=None, f_texto_bar=0.025, f_tam_letra=0.25,
                       d_porc=1, d_num=1, org_texto=1, cor_texto='#000000',
                       rotation=0, ds=None)
'''
# --- para linhas ----
'''
num_graf_linhas(ax,f_tam_letra=0.02,f_texto_linha=0.025,cor_texto='#000000',
                    d=1, rotation=0, ds=None)
'''



def _k(ax):
    '''Retorna a lagura da caixa do gráfico em pixels. Este valor é usado        
       para definir os tamnhos das letras,  largura das linhas, etc
    '''
    return(ax.bbox.width)


# casas decimais numeros
def num_dec(num, d=1):
    '''
    Escreve um número com 'd'' casas decimais
    '''
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
    '''
    Escreve uma porcentagem com 'd'' casas decimais
    '''
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



#-------------------------------------------------------------
#   Funçoes para incluir números nos graficos #-------------------------------------------------------------



def num_barras_verticais(ax,
                         f_texto_bar=0.025,
                         f_tam_letra=0.02,
                         cor_texto='#000000',
                         d=1,
                         rotation=0,
                         ds=None):
    '''
    Escreve os números em cima das barras
    
    Args:
    'h_texto_bar': fracao para calcular a posicao do texto a partir da barra. 
        A posicao é calculada com a média da maior e da menor barra vezes esta
        fração   
    'f_tam_letra': fração usada para calcular o tamnho da fonte das anotações.
        O tamanho da fonte é esta fração vezes o tamanho da maior barra    
    'd': número de casas decimais do numero das barras
    'dh':(USADO PARA UNIR GRAFICOS CORRELACIONADOS). É a altura de estabelecida para as
        anotações em cima da barra. Para unir dois ou mais gráficos este valor é estabelecido
        por um gráfico enterior

    Outputs:
    'dh': distância das anotações para as barras. Este retorno é usado para unir 2
        ou mais gráficos        
    '''
    
    # distancia do texto para a barra
    if(ds == None):
        ds = f_texto_bar*(ax.patches[0].get_height()\
                     + ax.patches[-1].get_height())/2
       
    
    # configurações texto
    kargs = dict(fontsize=f_tam_letra * _k(ax),
                 color=cor_texto,
                 ha='center')

    # escreve os textos nas barras
    for p in ax.patches:

        # coordenadas do texto
        x = p.get_center()[0]
        y = p.get_height()+ds
       
        ax.annotate(num_dec(p.get_height(),d=d),
                    (x, y),
                    rotation=rotation,
                    **kargs)
        
    return(ds)



def porc_barras_verticais(ax,
                          sum_tot=None,
                          f_texto_bar=0.025,
                          f_tam_letra=0.02,
                          cor_texto='#000000',
                          d=1,
                          rotation=0,
                          ds=None):

    '''
    Escreve as porcentagens em cima das barras
    
    Args:
    'sum_tot': número equivalente a soma dos valores de todas as barras.
        Este valor deve ser calculado previamenete e passada para a função
    'h_texto_bar': fracao para calcular a posicao do texto a partir da barra. 
        A posicao é calculada com a média da maior e da menor barra vezes esta
        fração   
    'f_tam_letra': fração usada para calcular o tamnho da fonte das anotações.
        O tamanho da fonte é esta fração vezes o tamanho da maior barra
    'd': número de casas decimais da porcentagem
    'dh':(USADO PARA UNIR GRAFICOS CORRELACIONADOS). É a altura de estabelecida para as
        anotações em cima da barra. Para unir dois ou mais gráficos este valor é estabelecido
        por um gráfico enterior

    Outputs:
    'dh': distância das anotações para as barras. Este retorno é usado para unir 2
        ou mais gráficos        
    '''

    

    # distancia do texto para a barra
    if(ds == None):
        ds = f_texto_bar*(ax.patches[0].get_height()\
                     + ax.patches[-1].get_height())/2

    

  
    # configurações texto
    kargs = dict(fontsize=f_tam_letra * _k(ax),
                 color=cor_texto,
                 ha='center')

    # escreve os textos nas barras
    for p in ax.patches:

        # coordenadas do texto
        x = p.get_center()[0]
        y = p.get_height()
        
        porc= (y/sum_tot)*100
       
        ax.annotate(porcent_dec(porc, d=d),
                    (x, y+ds),
                    rotation=rotation, 
                    **kargs)
        
    return(ds)



def porc_num_bar_verticais(ax, sum_tot=None,  f_texto_bar=0.025,  f_tam_letra=0.02,
                      d_porc=1,  d_num=1,  org_texto=0, cor_texto='#000000',
                      rotation=0, ds=None):
    '''
    Escreve os números e as porcentagens em cima das barras
    
    Args:
    'sum_tot': número equivalente a soma dos valores de todas as barras.
        Este valor deve ser calculado previamenete e passada para a função
    'h_texto_bar': fracao para calcular a posicao do texto a partir da barra. 
        A posicao é calculada com a média da maior e da menor barra vezes esta
        fração   
    'f_tam_letra': fração usada para calcular o tamnho da fonte das anotações.
        O tamanho da fonte é esta fração vezes o tamanho da maior barra
    'd_porc': número de casas decimais da porcentagem
    'd_num': número de casas decimais do numero das barras
    'org_texto': numero que define a organização das anotações:
        0-> escreve numero em cima e porcentagem a baixo
        1-> escreve porcentagem em cima e número a baixo
    'rotation': rotação das anotações
    'dh':(USADO PARA UNIR GRAFICOS CORRELACIONADOS). É a altura de estabelecida para as
        anotações em cima da barra. Para unir dois ou mais gráficos este valor é estabelecido
        por um gráfico enterior

    Outputs:
    'dh': distância das anotações para as barras. Este retorno é usado para unir 2
        ou mais gráficos        
    '''
    
    
    # distancia do texto para a barra
    if(ds == None):
        ds = f_texto_bar*(ax.patches[0].get_height()\
                     + ax.patches[-1].get_height())/2
       
    
    # configurações texto
    kargs = dict(fontsize=f_tam_letra * _k(ax),
                 color=cor_texto,
                 ha='center')

    # escreve os textos nas barras
    for p in ax.patches:

        # coordenadas do texto
        x = p.get_center()[0]
        y = p.get_height()
        
        # calcula a porcentagem
        porc= (y/sum_tot)*100  
        
        # monta o texto
        if org_texto==0:
            texto=  num_dec(p.get_height(),d=d_num)+'\n'+\
                    porcent_dec(porc, d=d_porc)
        elif org_texto==1:
            texto=  porcent_dec(porc, d=d_porc)+'\n'+\
                    num_dec(p.get_height(),d=d_num)

       
        # escreve na figura
        ax.annotate(texto,
                    (x, y+ds),
                    rotation=rotation,
                    **kargs)
    
    # retorna 'dh' para graficos correlaciondados
    return(ds)




def num_barras_horizontais(ax,
                           f_texto_bar=0.025,
                           f_tam_letra=0.02,
                           cor_texto='#000000',
                           d=1,
                           rotation=0,
                           ds=None):
    
    '''
    Escreve os números equivalentes aos comprimentos das barras no canto
    das barras
    '''
    
   # distancia do texto para a barra
    if(ds == None):
        ds = f_texto_bar*(ax.patches[0].get_width()\
                     + ax.patches[-1].get_width())/2
        
   
    # configurações texto
    kargs = dict(fontsize = f_tam_letra * _k(ax),
                 color=cor_texto,
                 va='center')     #va ->vertical aligment


    # escreve os textos nas barras
    for p in ax.patches:

        # coordenadas do texto
        y = p.get_center()[1]
        x = p.get_width() + ds  
        
        ax.annotate(num_dec(p.get_width(),d=d),
                    (x, y),
                    rotation=rotation,
                    **kargs)
        
    return(ds)



def porc_barras_horizontais(ax,                                
                                 sum_tot=None,
                                 f_texto_bar=0.025,
                                 f_tam_letra=0.02,
                                 cor_texto='#000000',
                                 d=1,
                                 rotation=0,
                                 ds=None):

    '''
    Escreve as porcentagens em cima das barras
    
    Args:
    'sum_tot': número equivalente a soma dos valores de todas as barras.
        Este valor deve ser calculado previamenete e passada para a função
    'h_texto_bar': fracao para calcular a posicao do texto a partir da barra. 
        A posicao é calculada com a média da maior e da menor barra vezes esta
        fração   
    'f_tam_letra': fração usada para calcular o tamnho da fonte das anotações.
        O tamanho da fonte é esta fração vezes o tamanho da maior barra
    'd': número de casas decimais da porcentagem
    'dh':(USADO PARA UNIR GRAFICOS CORRELACIONADOS). É a altura de estabelecida para as
        anotações em cima da barra. Para unir dois ou mais gráficos este valor é estabelecido
        por um gráfico enterior

    Outputs:
    'dh': distância das anotações para as barras. Este retorno é usado para unir 2
        ou mais gráficos        
    '''

    

    # distancia do texto para a barra
    if(ds == None):
        ds = f_texto_bar*(ax.patches[0].get_width()\
                     + ax.patches[-1].get_width())/2   

  
    # configurações texto
    kargs = dict(fontsize=f_tam_letra * _k(ax),
                 color=cor_texto,
                 va='center')   #va ->vertical aligment

    # escreve os textos nas barras
    for p in ax.patches:

        # coordenadas do texto
        y = p.get_center()[1]
        x = p.get_width()
                
        porc= (x/sum_tot)*100
       
        ax.annotate(porcent_dec(porc, d=d),
                    (x+ds, y),
                    rotation=rotation, 
                    **kargs)
        
    return(ds)



def porc_num_bar_horizontais(ax, 
                       sum_tot=None,
                       f_texto_bar=0.025,
                       f_tam_letra=0.02,
                       d_porc=1,
                       d_num=1,
                       org_texto=1,
                       cor_texto='#000000',
                       rotation=0,
                       ds=None,):
    '''
    Escreve os números e as porcentagens ao lado das barras
    
    Args:
    'sum_tot': número equivalente a soma dos valores de todas as barras.
        Este valor deve ser calculado previamenete e passada para a função
    'f_texto_bar': fracao para calcular a posição do texto a partir da barra. 
        A posicao é calculada com a média da maior e da menor barra multiplicada 
        por esta fração   
    'f_tam_letra': fração usada para calcular o tamnho da fonte das anotações.
        O tamanho da fonte é esta fração vezes o tamanho da maior barra
    'd_porc': número de casas decimais da porcentagem
    'd_num': número de casas decimais do numero das barras
    'org_texto': numero que define a organização das anotações:
        0-> escreve numero em cima e porcentagem a baixo
        1-> escreve porcentagem em cima e número a baixo
        2-> escreve numero e porcentagem na mesma linha como: num(porc)
        3-> escreve numero e porcentagem na mesma linha como: porc(num)
    'rotation': rotação das anotações
    'ds': distância entre as barras e o texto. É usado para unir 2 ou mais gráficos

    Outputs:
    'ds': distância entre as barras e o texto. É usado para unir 2 ou mais gráficos        
    '''
 
    # distancia do texto para a barra
    if(ds == None):
        ds = f_texto_bar*(ax.patches[0].get_height()\
                     + ax.patches[-1].get_height())/2
       
    
    # configurações texto
    kargs = dict(fontsize=f_tam_letra * _k(ax),
                 color=cor_texto,
                 va='center')   #va-> vertical aligment

    # escreve os textos nas barras
    for p in ax.patches:

        # coordenadas do texto
        y = p.get_center()[1]
        x = p.get_width()
                
        porc= (x/sum_tot)*100
        
        
        # monta o texto
        if org_texto==0:
            # formato 0: num
            #            porc             
            texto = num_dec(p.get_width(),d=d_num)+'\n'+\
                    porcent_dec(porc, d=d_porc)
            
        elif org_texto==1:
            # formato 1: porc
            #            num             
            texto = porcent_dec(porc, d=d_porc)+'\n'+\
                    num_dec(p.get_width(),d=d_num)
            
        elif org_texto==2:
            #formato 2: num(porc)
            texto = num_dec(p.get_width(),d=d_num)+' ('+\
                    porcent_dec(porc, d=d_porc)+')'
                
        elif org_texto==3:
            #formato 3: porc(num)            
            texto = porcent_dec(porc, d=d_porc)+' ('+\
                    num_dec(p.get_width(),d=d_num)+')'
            

        # escreve na figura
        ax.annotate(texto,
                    (x+ds, y),
                    rotation=rotation, 
                    **kargs)
    
    
    # retorna 'dh' para graficos correlaciondados
    return(ds)




def num_graf_linhas(ax,
                    f_tam_letra=0.02,
                    f_texto_linha=0.025,
                    cor_texto='#000000',
                    d=1,
                    rotation=0,
                    ds=None):
    
    '''Escreve os valores numéricos de um gráficos de linha como anotação
       em cima das linhas
    '''
    
    # distancia da texto para a linha
    if ds==None:
        # coordenadas y dos pontos da linha
        coordY = ax.lines[0].get_data()[1]    
        # calcula o ds
        ds= f_texto_linha*(coordY.max()+coordY.min())/2 
        
        
    # configurações texto
    kargs = dict(fontsize= f_tam_letra*_k(ax),        #f_tam_letra * _dl(ax),
                 color=cor_texto,
                 ha='center',
                 rotation=rotation)

        
    # escrever as anotações
    for p in ax.lines:
        
        # coordenadas dos pontos
        [x_pts,y_pts]= p.get_data()        
        
        # escreve os numeros
        for x, y in zip(x_pts,y_pts):
            ax.annotate(num_dec(y , d=d),
                        xy=(x, y+ds),
                        **kargs
                       )
    return(ds)




#------------------------------------------------------------------
#   Funçoes para incluir anotações com informações nos gráficos
#------------------------------------------------------------------



def anotacoes_box_texto(ax,texto1=None,
                        texto2=None,
                        x_in=None,
                        y_in=None,                        
                        numLetra=0.04,
                        c_FaceBox="#d8e6db",
                        c_EdgeBox="k",
                        c_LetraBox='#191970',
                        c_LetraTexto='gray',
                        boxstyle='round4',
                        f_textos=18):
    
    '''   
    Faz anotações em gráficos dividindo as anotações em duas partes um quadro
    com um texto e um texto livre abaixo do quadro. Esta função é útil para
    colocar informações adicionais nos gráficos
        As coordenadas do texto são definidas no input. A função foi escrita
    de forma que aumentando o tamanho da letra, todos os compoenentes da
    anotação também aumentam mantendo todas as proporções
    
    ax: eixo do gráficos
    texto1: texto dentro da caixa
    texto2: texto fora da caixa
    x_in: coordenada x do texto
    y_in: coordenada y do texto
    numLetra: tamanho da letra
    c_FaceBox: cor interna da caixa
    c_EdgeBox: cor da borda da caixa
    c_LetraBox: cor da letra do texto da caixa
    c_LetraTexto: cor da letra do texto fora da caixa
    boxstyle: estilo da caixa. Dois valores ficam bons('square', 'round4')   
    f_textos -> fração relacionada com as distâncias dos textos
                quanto maior este valor maior as distâncias 
                entre os textos
    '''       
        
    
    # configurações da caixa
    bbox=dict(boxstyle=boxstyle,  #"square" (outra opção)
              pad=1,              #define se quadro pe proximo ou distente do texto 
              edgecolor = c_EdgeBox,
              facecolor = c_FaceBox,
              linewidth=0.0005*_k(ax))
            

    # escreve o primeiro texto (texto na caixa)
    ax.annotate(texto1,
                xy=(x_in, y_in),
                xycoords='axes fraction',  #coordenadas definidas for frações dos eixos
                color = c_LetraBox, 
                size=numLetra*_k(ax),                
                bbox=bbox,
                ha = 'center',    #alinhamento horizontal
                va = 'bottom',    #alinhamento vertical            
                )
    
    
    
    #--- Calculo das coordendas do segundo texto--

    # limites dos eixos
    lim_y= ax.get_ylim()
    dy=lim_y[1]-lim_y[0] 
    
    # coordenadas do segundo texto
    x_in = x_in
    y_in = y_in - (f_textos*(dy/ax.bbox.height))/dy
    
    # opções para o cálculi de y_in(não funcionam muito bem)
    #y_in = y_in - 0.04*dy              #invariável à escala
    #y_in = y_in - 100 /ax.bbox.height  #invariável a altura da fig
    

    # --- escreve o segundo texto ---
    ax.annotate(texto2,
                 xy = (x_in, y_in),                 
                 xycoords='axes fraction',  #coordenadas definidas for frações dos eixos
                 color = c_LetraTexto,
                 size = numLetra*_k(ax),
                 ha = 'center', #alinhamento horizontal
                 va = 'top',    #alinhamento vertical            
               )
    
    
    
    

    

def anotacoes_texto_box(ax,
                        texto1=None,
                        texto2=None,
                        x_in=None,
                        y_in=None,
                        numLetra=0.04,
                        c_FaceBox="#d8e6db",
                        c_EdgeBox="k",
                        c_LetraBox='#191970',
                        c_LetraTexto='gray',
                        boxstyle='round4',
                        f_textos=18):

                        
    '''
    Faz anotações em gráficos dividindo as anotações em duas partes um texto
    livre (sem caixa) e um texto abaixo dentro de uma caixa. Esta função é 
    útil para colocar informações adicionais nos gráficos.
        As coordenadas do texto são definidas no input. A função foi escrita
    de forma que aumentando o tamanho da letra, todos os compoenentes da
    anotação também aumentam mantendo todas as proporções.
    
    ax: eixo do gráficos
    texto1: texto dentro da caixa
    texto2: texto fora da caixa
    x_in: coordenada x do texto
    y_in: coordenada y do texto
    numLetra: tamanho da letra
    c_FaceBox: cor interna da caixa
    c_EdgeBox: cor da borda da caixa
    c_LetraBox: cor da letra do texto da caixa
    c_LetraTexto: cor da letra do texto fora da caixa
    boxstyle: estilo da caixa. Dois valores ficam bons('square', 'round4')
    f_textos: fração relacionada com as distâncias dos textos
                quanto maior este valor maior as distâncias 
                entre os textos  
    '''  
      
        
    # escreve o primeiro texto
    ax.annotate(texto1,
                 xy=(x_in, y_in),
                 xycoords='axes fraction',  #coordenadas definidas for frações dos eixos
                 color = c_LetraTexto, 
                 size=numLetra*_k(ax),
                 ha='center',
                 va = 'bottom',  #alinhamento vertical 
                 )

    
    
    #--- Calculo das coordendas do segundo texto---
    
     # limites dos eixos
    lim_y= ax.get_ylim()
    dy=lim_y[1]-lim_y[0] 
    
    # coordenadas do segundo texto
    x_in = x_in
    y_in = y_in - (f_textos*(dy/ax.bbox.height))/dy
    #y_in = y_in - (f_textos*(dy/ax.bbox.height))/dy
    
    # opções para o cálculi de y_in
    #y_in = y_in - 0.04*dy              #invariável à escala
    #y_in = y_in - 100 /ax.bbox.height  #invariável a altura da fig
    
    
    # configurações da caixa
    bbox=dict(boxstyle=boxstyle,
              pad=1,              #define se quadro pe proximo ou distente do texto 
              edgecolor = c_EdgeBox,
              facecolor = c_FaceBox,
              linewidth=0.0005*_k(ax))

    # escreve o segundo texto
    ax.annotate(texto2,
                xy = (x_in, y_in),
                xycoords='axes fraction',  #coordenadas definidas for frações dos eixos
                color = c_LetraBox,
                size = numLetra*_k(ax),
                ha = 'center', #alinhamento horizontal
                va = 'top',    #alinhamento vertical  
                bbox=bbox)
    




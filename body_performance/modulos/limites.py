
# --- Funções no módulo-----

# muda_limites_eixo_y(ax, frac=0.1, tipo_aumento=0, ylims=None):

# muda_limites_eixo_x(ax, frac=0.1, tipo_aumento=0, xlims=None):



def get_lims(df, col):
    '''
    Obtémos limites de referêcia a aprtir dos limites dos dados. Quando chamados
    os métodos 'muda_limites_*' diretamente estes valores de referência são calculados
    a partir do gráfico que já esta plotado. Na maioria das vezes charmar 'muda_limites*'
    diretamente ja funcioana, mas as vezes, isto deixo o gráfico com velores menores cortado.
    Neste casos é necessário calcula os limites a partir dos dados e deve ser usada está
    função.Nestes casos o retorno desta funçao deve ser fornecido para o campo 'ylims'
    (ou 'xlims') do método 'muda_limites_eixo_y'(ou 'muda_limites_eixo_x')
    '''
    lims=[ df[col].min(), df[col].max()]
    return( lims)



def muda_limites_eixo_y(ax, frac=0.1, tipo_aumento=0, ylims=None):
    '''
    Muda os limites dos gráficos com o objetivo de melhorar a aparência
    da figura.

    Esta função amplia o eixo y. Para a amplicação é calculada a diferença
    entre o mínimo e máximo original (chamada de dy). A ampliação é feita
    adicionando uma fração de dy (frac*dy) aos limites do eixo y do gráfico.

    Args:
        frac: fração de 'dy' para aumento do limite superior do eixo y
    '''

    # obtém os limites em y
    if ylims==None:
        ylims = ax.get_ylim()

    # variação no eixo
    dy= frac*(ylims[1]-ylims[0])

    # aumenta os limites
    if tipo_aumento==0:
        ax.set_ylim([ylims[0], ylims[1]+dy])
    elif tipo_aumento==1:
        ax.set_ylim([ylims[0]-dy , ylims[1]])
    elif tipo_aumento==2:
        ax.set_ylim([ylims[0]-dy , ylims[1]+dy])

    # retorna limites antigos
    return(ylims)





def muda_limites_eixo_x(ax,
                        frac=0.1,
                        tipo_aumento=0,
                        xlims=None):
                        
    '''
    Muda os limites dos gráficos com o objetivo de melhorar a aparência
    da figura.

    Esta função amplia o eixo x. Para a amplicação é calculada a diferença
    entre o mínimo e máximo original (chamada de dx). A ampliação é feita
    adicionando uma fração de dx (frac*dx) aos limites do eixo x do gráfico

    Args:
        frac: fração de 'dx' para aumento do limite superior do eixo x
    '''

    # obtém os limites em x
    if xlims==None:
        xlims = ax.get_xlim()
        
    # variação no eixo
    dx= frac*(xlims[1]-xlims[0])
    
    
    # aumenta os limites
    if tipo_aumento==0:
        ax.set_xlim([xlims[0], xlims[1]+dx])
    elif tipo_aumento==1:
        ax.set_xlim([xlims[0]-dx , xlims[1]])
    elif tipo_aumento==2:
        ax.set_xlim([xlims[0]-dx , xlims[1]+dx])    
        

    # retorna limites antigos
    return(xlims)



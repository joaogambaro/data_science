

#Funções definidas

# def _k(ax)
# set_axes_1(ax, titulo, xlabel, ylabel)
# set_axes_2(ax, titulo, xlabel, ylabel)








# --------------------------------------------------
#    Tema e eixos
# --------------------------------------------------

# sns.set_theme(style='white')
# cor_titulo= '#898d8f'
# cor_eixos= 'k'
# cor_nomes= 'k'
# cor_rotulos= 'k'


# -------------------------------------------------
#   Esquema de cores
# -------------------------------------------------

import seaborn as sns

# -- paletas: paletas multicores:
pm_1 =['#00076f','#44008b','#9f45b0','#e54ed0', '#ffe4f2']  #(5 cores)
pm_2 =['#004c4c','#6c1b8f','#1b1c6b','#d8e6db','#facdd0','#bcf7ed','#f5e9e9' ] #(7 cores)
pm_3 ='Accent'   #(n cores)

# -- Platetas: monocor
pmo_1 = lambda n: sns.color_palette("blend:#004c4c,#bcf7ed",n)
pmo_2 = lambda n: sns.color_palette("blend:#6c1b8f,#bcf7ed",n)
pmo_3 = lambda n: sns.color_palette("blend:#1b1c6b,#facdd0",n)
    
# -- cores
#Cores 1:
c1_normal='#008080'                  #normal
c1_forte = '#004c4c'
c1_fraca = '#d8e6db'
c1_curinga ='#191970'
c1_contraste =  [c1_forte , '#bcf7ed']   #contraste
c1_enfase = [c1_fraca,  '#191970']   #enfase

#Cores 2: 
c2_normal='#d0b6db'                        #normal
c2_forte='#6c1b8f' 
c2_fraca= '#f5e9e9'
c2_curinga='#008080'
c2_contraste= [c2_forte, '#bcf7ed']    #contraste
c2_enfase =   [c2_fraca, '#008080']      #enfase

#Cores 3:
c3_normal='#1b1c6b'                         #normal
c3_forte='#1b1c6b'
c3_fraca='#facdd0'
c3_contraste= [c3_forte,'#f5e9e9']
c3_enfase= [c3_fraca, c3_normal]


# ----------------------------------------
#   eixos 
# ----------------------------------------


# parâmetro para definir tamanhos
def _k(ax):
    return(ax.bbox.width)



# eixos para para 1 divisão

def set_axes_1(ax, titulo='titulo_1',xlabel='xlabel', ylabel='ylabel' ):
    
    # cores
    cor_titulo= '#898d8f'
    cor_eixos= '#cccccc'
    cor_nomes= 'k'
    cor_rotulos= 'k'
    
    # fracões para definir tamanhos
    # nomes
    fti=0.020       # titulo
    fx=0.015       # label x
    fy=0.015       # label y
    f_d=0.008       # distancia nome do rótulo ao eixo
    
    # ticks
    ftk_ls=0.015    # tick labelsize
    ftk_l=0.005      # tick length
    ftk_w=0.0005     # tick width
    
    # nomes
    ax.set_title(titulo, color=cor_titulo, size = fti*_k(ax))
    ax.set_ylabel(ylabel, color=cor_nomes, labelpad=f_d*_k(ax), 
                  size = fx*_k(ax))
    ax.set_xlabel(xlabel, color=cor_nomes, labelpad=f_d*_k(ax),
                  size = fy*_k(ax))
    # eixos
    ax.spines[['top','right']].set_visible(False)
    ax.spines[['left','bottom']].set_color(cor_eixos)
    # ticks
    ax.tick_params(left=True,bottom=True,
                   color= cor_eixos,
                   colors= cor_rotulos,
                   
                   labelsize = ftk_ls *_k(ax),
                   length = ftk_l *_k(ax),
                   width = ftk_w *_k(ax),                  
                   )



# eixos par para 2 divisões

def set_axes_2(ax, titulo='Titulo_1',xlabel='xlabel', ylabel='ylabel'):
    
    # cores
    cor_titulo= '#898d8f'
    cor_eixos= '#cccccc'
    cor_nomes= 'k'
    cor_rotulos= 'k'
    
    # fracões para definir tamanhos
    # nomes
    fti=0.04       # titulo
    fx=0.037       # label x
    fy=0.037       # label y
    f_d=0.015       # distancia nome do rótulo ao eixo
    
    # ticks
    ftk_ls=0.032   # tick labelsize
    ftk_l=0.02     # tick length
    ftk_w=0.003    # tick width
    
    
    # nomes
    ax.set_title(titulo, color=cor_titulo, size = fti*_k(ax))
    ax.set_ylabel(ylabel, color=cor_nomes,labelpad=f_d*_k(ax),
                  size = fx*_k(ax))
    ax.set_xlabel(xlabel, color=cor_nomes,labelpad=f_d*_k(ax),
                  size = fy*_k(ax))
    # eixos
    ax.spines[['top','right']].set_visible(False)
    ax.spines[['left','bottom']].set_color(cor_eixos)
    # ticks
    ax.tick_params(left=True,bottom=True,
                   color=cor_eixos,
                   colors= cor_rotulos,
                   
                   labelsize = ftk_ls *_k(ax),
                   length = ftk_l *_k(ax),
                   width = ftk_w *_k(ax),                  
                   )


   



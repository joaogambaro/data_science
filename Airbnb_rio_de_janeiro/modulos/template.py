

#Funções definidas

# def _k(ax)
# set_axes_1(ax, titulo, xlabel, ylabel)
# set_axes_2(ax, titulo, xlabel, ylabel)




# --------------------------------------------------
#    Tema e eixos
# --------------------------------------------------

# sns.set_theme(style='white')
# cor_titulo= '#8c8c8f'
# cor_eixos= 'k'
# cor_nomes= 'k'
# cor_rotulos= 'k'




# -------------------------------------------------
#   Esquema de cores
# -------------------------------------------------
import seaborn as sns


# -- paletas: paletas multicores
pm_1 = ['#10A19D', '#540375','#FF7000','#FFBF00', '#2192FF']  #(5 cores)
pm_2 = ['#382266','#ed2f2f','#97aabf','#FF7000', '#f7f7d5','#4FA095','#6D67E4']  #(7cores)
pm_3 = 'Accent'   #(n cores)


# -- Paletas: monocor
pmo_1 = lambda n: sns.color_palette("blend:#EB455F,#2B3467",n)
pmo_2 = lambda n: sns.color_palette("blend:#153462,#4FA095",n)
pmo_3 = lambda n: sns.color_palette("blend:#453C67,#6D67E4",n)
pal_4 = lambda n: sns.color_palette("blend:#97aabf,#f7f7d5",n)
    

# -- cores
#Cores 1:
c1_normal='#512f94'
c1_forte = '#382266'
c1_fraca = '#97aabf'
c1_contraste='#ed2f2f'
c1_curinga ='#191970'
c1_vet_contra = [c1_forte, c1_contraste]
c1_vet_enfase = [c1_fraca, c1_curinga] 


#Cores 2: 
c2_normal='#f05456'              
c2_forte='#8c010b' 
c2_fraca= '#f7f7d5'
c2_contraste='#aba6a6'
c2_curinga='#382266'
c2_vet_contra=   [c2_forte, c2_contraste] 
c2_vet_enfase =  [c2_fraca, c2_curinga]      


#Cores 3:
c3_normal='#4FA095'                        
c3_forte='#153462'
c3_fraca='#bdf2c3'
c3_contraste='#f5c898'
c3_curinga='#090247'
c3_vet_contra= [c3_forte, c3_contraste]
c3_vet_enfase= [c3_fraca, c3_curinga]


# ----------------------------------------
#   eixos 
# ----------------------------------------

#Os nomes são baseados na divisão da aréa de gráficos em partes no eixo x 

#set_axes_32 --> pega 3 partes de uma divisão em 3
#set_axes_31 --> pega 1 parte de uma divisão em 3
#set_axes_1  --> pega uma parte inteira (3 partes de 3 ou 2 partes de 2)
#set_axes_2  --> pega 2 partes de uma divisao em 2



# parâmetro para definir tamanhos
def _k(ax):
    return(ax.bbox.width)

def set_axes_32(ax, titulo='titulo_1',xlabel=None, ylabel=None ):
    
    # cores
    cor_titulo= '#8c8c8f'
    cor_eixos= 'k'
    cor_nomes= 'k'
    cor_rotulos= 'k'
    
    # fracões para definir tamanhos
    # nomes
    fti=0.021       # titulo
    fx=0.017       # label x
    fy=fx           # label y
    f_d=0.008       # distancia nome do rótulo ao eixo
    
    # ticks
    ftk_ls=0.016    # tick labelsize
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
                   color=cor_eixos,
                   colors= cor_rotulos,
                   
                   labelsize = ftk_ls *_k(ax),
                   length = ftk_l *_k(ax),
                   width = ftk_w *_k(ax),                  
                   )

def set_axes_31(ax, titulo='titulo_1',xlabel=None, ylabel=None ):
    
    # cores
    cor_titulo= '#8c8c8f'
    cor_eixos= 'k'
    cor_nomes= 'k'
    cor_rotulos= 'k'
    
    # fracões para definir tamanhos
    # nomes
    fti=0.047       # titulo
    fx=0.036        # label x
    fy=fx           # label y
    f_d=0.018       # distancia nome do rótulo ao eixo
    
    # ticks
    ftk_ls=0.035    # tick labelsize
    ftk_l=0.015      # tick length
    ftk_w=0.0015     # tick width
    
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
                   color=cor_eixos,
                   colors= cor_rotulos,
                   
                   labelsize = ftk_ls *_k(ax),
                   length = ftk_l *_k(ax),
                   width = ftk_w *_k(ax),                  
                   )



def set_axes_1(ax, titulo='titulo_1',xlabel=None, ylabel=None ):
    
    # cores
    cor_titulo= '#8c8c8f'
    cor_eixos= 'k'
    cor_nomes= 'k'
    cor_rotulos= 'k'
    
    # fracões para definir tamanhos
    # nomes
    fti=0.014       # titulo
    fx=0.012        # label x
    fy=fx           # label y
    f_d=0.008       # distancia nome do rótulo ao eixo
    
    # ticks
    ftk_ls=0.011    # tick labelsize
    ftk_l=0.004      # tick length
    ftk_w=0.001     # tick width
    
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
                   color=cor_eixos,
                   colors= cor_rotulos,
                   
                   labelsize = ftk_ls *_k(ax),
                   length = ftk_l *_k(ax),
                   width = ftk_w *_k(ax),                  
                   )


def set_axes_2(ax, titulo='titulo_1',xlabel=None, ylabel=None ):
    
    # cores
    cor_titulo= '#8c8c8f'
    cor_eixos= 'k'
    cor_nomes= 'k'
    cor_rotulos= 'k'
    
    # fracões para definir tamanhos
    # nomes
    fti=0.03       # titulo
    fx=0.0225       # label x
    fy=fx           # label y
    f_d=0.012       # distancia nome do rótulo ao eixo
    
    # ticks
    ftk_ls=0.023    # tick labelsize
    ftk_l=0.007      # tick length
    ftk_w=0.001     # tick width
    
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
                   color=cor_eixos,
                   colors= cor_rotulos,
                   
                   labelsize = ftk_ls *_k(ax),
                   length = ftk_l *_k(ax),
                   width = ftk_w *_k(ax),                  
                   )

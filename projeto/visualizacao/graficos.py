import plotly.graph_objects as go
from django.shortcuts import render
import plotly.offline as opy
import plotly.graph_objs as go
from plotly.offline import plot
import pandas as pd
import plotly.express as px
import pycountry

"""
def plot_series_temperatura():
    # Dados fornecidos
    years = list(range(1961, 2023))
    temperatures = [0.167, -0.184, 0.158, -0.213, -0.075, 0.044, 0.073, -0.409, 0.331, 0.13, -0.134, 0.114, 0.443, -0.179,
                -0.14, -0.185, 0.252, 0.03, 0.017, 0.313, 0.191, 0.277, 0.471, 0.294, 0.092, 0.285, 0.722, 0.461, 0.13,
                0.435, 0.468, 0.403, 0.495, 0.608, 0.799, 0.504, 0.671, 1.234, 0.523, 0.495, 0.746, 1.052, 0.927, 0.768,
                1.085, 0.77, 0.969, 0.731, 0.969, 1.112, 0.814, 1.023, 0.922, 1.153, 1.516, 1.457, 1.363, 1.148, 1.517,
                1.477, 1.154, 0.926]

    # Criar o gráfico interativo
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=temperatures, mode='lines+markers'))

    # Configurar o layout do gráfico
    fig.update_layout(
        plot_bgcolor='green',
        title='Mudança de temperatura no Brasil',
        xaxis=dict(title='Ano'),
        yaxis=dict(title='Mudança de temperatura (°C)')
    )

    # Exibir o gráfico interativo
    fig.show()
    

    div = opy.plot(fig, auto_open=False, output_type='div')

    return div"""

def mudanca_temperatura_brasil():
    # Dados fornecidos
    years = list(range(1961, 2023))
    temperatures = [0.167, -0.184, 0.158, -0.213, -0.075, 0.044, 0.073, -0.409, 0.331, 0.13, -0.134, 0.114, 0.443, -0.179,
                -0.14, -0.185, 0.252, 0.03, 0.017, 0.313, 0.191, 0.277, 0.471, 0.294, 0.092, 0.285, 0.722, 0.461, 0.13,
                0.435, 0.468, 0.403, 0.495, 0.608, 0.799, 0.504, 0.671, 1.234, 0.523, 0.495, 0.746, 1.052, 0.927, 0.768,
                1.085, 0.77, 0.969, 0.731, 0.969, 1.112, 0.814, 1.023, 0.922, 1.153, 1.516, 1.457, 1.363, 1.148, 1.517,
                1.477, 1.154, 0.926]

    # Criar o gráfico interativo
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=temperatures, mode='lines+markers'))

    # Configurar o layout do gráfico
    fig.update_layout(
        plot_bgcolor='grey',
        
        title='Mudança de temperatura no Brasil',
        xaxis=dict(title='Ano'),
        yaxis=dict(title='Mudança de temperatura (°C)')
    )
    fig.update_traces(line=dict(color='black'))
    # Converter o gráfico em HTML
    div = plot(fig, output_type='div')

    return div



def co2_emissions():  

    # Dados de emissão de CO2
    years = list(range(1990, 2022))
    emissions = [1.31313162278407, 1.3400291104962, 1.33331845207455, 1.35861090138514, 1.38213969207396, 1.47560355931892,
                1.58045379755498, 1.6691806384565, 1.6989442995386, 1.73476944842688, 1.78349954728882, 1.79211171672668,
                1.76065069014316, 1.7018519889237, 1.77844124428615, 1.77566238713021, 1.77747742696957, 1.847975735626,
                1.93921475496659, 1.79932762776072, 2.02660515963729, 2.11067771312325, 2.27141718351636,
                2.41344604124948, 2.51459146813631, 2.36536013363926, 2.16125936406967, 2.18937093870573,
                2.0649751983417, 2.05067522030747]

    # Criar figura Plotly
    #fig = go.Figure()
    fig = go.Figure(data=go.Scatter(x=years, y=emissions, mode='markers+lines'))

    # Configurar layout do gráfico
    fig.update_layout(
        title='Emissões de CO2 no Brasil 1995 a 2020',
        xaxis_title='Ano',
        yaxis_title='Emissões de CO2',
        hovermode='closest'
    )

    # Adicionar interação ao passar o mouse sobre os pontos
    fig.update_traces(hovertemplate='Ano: %{x}<br>Emissões de CO2: %{y}')

    # Exibir gráfico interativo
    #fig.show()

    div = plot(fig, output_type='div')
    
    return div




def desmatamento():

    # Dados de emissões de CO2 por ano
    years = list(range(1988, 2023))
    acre = [620, 540, 550, 380, 400, 482, 482, 1208, 433, 358, 536, 441, 547, 419, 883, 1078, 728, 592, 398, 184, 254, 167, 259, 280, 305, 221, 309, 264, 372, 257, 444, 682, 706, 889, 847]
    amazonas = [1510, 1180, 520, 980, 799, 370, 370, 2114, 1023, 589, 670, 720, 612, 634, 885, 1558, 1232, 775, 788, 610, 604, 405, 595, 502, 523, 583, 500, 712, 1129, 1001, 1045, 1434, 1512, 2306, 2607]
    amapa = [60, 130, 250, 410, 36, 0, 0, 9, 0, 18, 30, 0, 0, 7, 0, 25, 46, 33, 30, 39, 100, 70, 53, 66, 27, 23, 31, 25, 17, 24, 32, 24, 17, 6]
    maranhao = [2450, 1420, 1100, 670, 1135, 372, 372, 1745, 1061, 409, 1012, 1230, 1065, 958, 1085, 993, 755, 922, 674, 631, 1271, 828, 712, 396, 269, 403, 257, 209, 258, 265, 253, 237, 336, 350, 282]
    mato_grosso = [5140, 5960, 4020, 2840, 4674, 6220, 6220, 10391, 6543, 5271, 6466, 6963, 6369, 7703, 7892, 10405, 11814, 7145, 4333, 2678, 3258, 1049, 871, 1120, 757, 1139, 1075, 1601, 1489, 1561, 1490, 1702, 1779, 2213, 1906]
    para = [6990, 5750, 4890, 3780, 3787, 4284, 4284, 7845, 6135, 4139, 5829, 5111, 6671, 5237, 7510, 7145, 8870, 5899, 5659, 5526, 5607, 4281, 3770, 3008, 1741, 2346, 1887, 2153, 2992, 2433, 2744, 4172, 4899, 5238, 4141]
    rondonia = [2340, 1430, 1670, 1110, 2265, 2595, 2595, 4730, 2432, 1986, 2041, 2358, 2465, 2673, 3099, 3597, 3858, 3244, 2049, 1611, 1136, 482, 435, 865, 773, 932, 684, 1030, 1376, 1243, 1316, 1257, 1273, 1673, 1512]
    roraima = [290, 630, 150, 420, 281, 240, 240, 220, 214, 184, 223, 220, 253, 345, 84, 439, 311, 133, 231, 309, 574, 121, 256, 141, 124, 170, 219, 156, 202, 132, 195, 590, 297, 315, 240]
    tocantins = [1650, 730, 580, 440, 409, 333, 333, 797, 320, 273, 576, 216, 244, 189, 212, 156, 158, 271, 124, 63, 107, 61, 49, 40, 52, 74, 50, 57, 58, 31, 25, 23, 25, 37, 27]

    # Criar o gráfico
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=acre, name='Acre'))
    fig.add_trace(go.Scatter(x=years, y=amazonas, name='Amazonas'))
    fig.add_trace(go.Scatter(x=years, y=amapa, name='Amapá'))
    fig.add_trace(go.Scatter(x=years, y=maranhao, name='Maranhão'))
    fig.add_trace(go.Scatter(x=years, y=mato_grosso, name='Mato Grosso'))
    fig.add_trace(go.Scatter(x=years, y=para, name='Pará'))
    fig.add_trace(go.Scatter(x=years, y=rondonia, name='Rondônia'))
    fig.add_trace(go.Scatter(x=years, y=roraima, name='Roraima'))
    fig.add_trace(go.Scatter(x=years, y=tocantins, name='Tocantins'))

    # Personalizar o layout do gráfico
    fig.update_layout(
        plot_bgcolor='lightgray',
        title='Desmatamento florestal no Brasil',
        xaxis_title='Ano',
        yaxis_title='km²',
        legend_title='Estado'
    )

    # Exibir o gráfico
    #fig.show()
    return fig.to_html()
    #div = plot(fig, output_type='div')
    #return div






def barras():
        # Leitura do arquivo CSV
    data = pd.read_csv('/home/netune/Documents/UFMG/VD/PPGCC_visualizacao_dados/projeto/visualizacao/dados/co2_emissions_kt_by_country.csv')

    # Cálculo do total por país
    total_por_pais = data.groupby('country_name')['value'].sum().reset_index()

    # Ordenação em ordem decrescente pelo total
    total_por_pais = total_por_pais.sort_values('value', ascending=False)

    # Seleção dos 5 maiores valores com country_name não repetido
    top_5 = total_por_pais.drop_duplicates(subset='country_name').head(5)

    # Obtenção dos URLs das bandeiras para cada país
    flags_urls = []
    for country_name in top_5['country_name']:
        try:
            country = pycountry.countries.get(name=country_name)
            flag_url = f"https://flagcdn.com/w20/{country.alpha_2.lower()}.png"
            flags_urls.append(flag_url)
        except AttributeError:
            flags_urls.append('')

    # Criação do gráfico de barras interativo com bandeiras
    fig = px.bar(top_5, x='country_name', y='value', title='Top 5 Países com Maior Total de CO2 Emissões',
                hover_data=['value'], color='country_name')

    # Adição das bandeiras como imagens das barras
    fig.update_layout(images=[dict(source=url, x=x_val, y=y_val, sizex=0.15, sizey=0.15, xanchor='center', yanchor='bottom')
                            for url, x_val, y_val in zip(flags_urls, top_5['country_name'], top_5['value'])])

    # Ajuste das configurações do layout
    fig.update_layout(yaxis_title='Total de CO2 Emissões', xaxis_tickangle=-45, showlegend=False)

    # Exibição do gráfico
    #fig.show()

    return fig.to_html()
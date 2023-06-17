from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


from .graficos import mudanca_temperatura_brasil, co2_emissions, desmatamento, barras

import plotly.graph_objs as go
from plotly.offline import plot








def graficos(request): # pega o grafico do arquivo codigo_graficos/graficos.py da função mudanca_temperatura_brasil()
    graph_temperature_brazil = mudanca_temperatura_brasil()
    graph_co2_emissions_brazil = co2_emissions()
    graph_desmatamento_brazil = desmatamento()
    graph_paises_barra = barras()

    context = {
       'temperatura':graph_temperature_brazil,
       'co2':graph_co2_emissions_brazil,
       'desmatamento_brazil':graph_desmatamento_brazil,
       'barras': graph_paises_barra
       
    }
   
    return render(request, 'graficos.html', context)


def aluno(request):
    return render(request, 'aluno.html')

def fonte(request):
    return render(request, 'fonte.html')




"""def co2_emissions_view(request):
    # Dados de emissão de CO2
    years = list(range(1990, 2022))
    emissions = [1.31313162278407, 1.3400291104962, 1.33331845207455, 1.35861090138514, 1.38213969207396, 1.47560355931892,
                1.58045379755498, 1.6691806384565, 1.6989442995386, 1.73476944842688, 1.78349954728882, 1.79211171672668,
                1.76065069014316, 1.7018519889237, 1.77844124428615, 1.77566238713021, 1.77747742696957, 1.847975735626,
                1.93921475496659, 1.79932762776072, 2.02660515963729, 2.11067771312325, 2.27141718351636,
                2.41344604124948, 2.51459146813631, 2.36536013363926, 2.16125936406967, 2.18937093870573,
                2.0649751983417, 2.05067522030747]

    # Criar figura Plotly
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

    # Renderizar o gráfico como HTML e passá-lo para o contexto
    div = plot(fig, output_type='div')
    context = {'plot_div': div}

    # Renderizar a página HTML com o gráfico
    return render(request, 'graficos.html', context)"""

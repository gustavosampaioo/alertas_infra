import streamlit as st
from datetime import datetime, time
import pytz
import pyperclip

# Função para gerar o texto
def gerar_texto(setor, prioridade, data_inicio, hora_inicio, data_fim, hora_fim, descricao, numero_os, motivo, extras, cidade, regioes_selecionadas):
    descricao_texto = descricao_map[descricao]
    texto_descricao = descricao_texto.replace("BAIRROS E CIDADE", "\n".join([f"- {regiao} ({cidade})" for regiao in regioes_selecionadas]))
    
    texto_gerado = (f"[{prioridade}][{setor}][DATA DE INÍCIO E HORA ({data_inicio} {hora_inicio})]"
                    f"[DATA DE FIM E HORA ({data_fim} {hora_fim})][{texto_descricao}]\n"
                    f"£Nº DA OS: £({numero_os})\n"
                    f"£REGIÃO:£({', '.join(regioes_selecionadas)} - {cidade})\n"
                    f"£MOTIVO:£({motivo})\n"
                    f"£INFORMAÇÕES COMPLEMENTARES:£({extras})")
    
    return texto_gerado

# Dicionários e listas de dados
descricao_map = {
    "Manutenção Programada": "Prezado cliente, informamos que identificamos um rompimento de fibra que está afetando a conexão nos bairros:\nBAIRROS E CIDADE\nO setor responsável já está atuando para resolver o problema o mais breve possível. Pedimos que não mexa nos equipamentos, pois a conexão será restabelecida automaticamente assim que o nosso serviço for normalizado.\nAgradecemos a sua compreensão.",
    "Falha Técnica": "Prezado cliente, informamos que identificamos um rompimento de fibra que está afetando a conexão nos bairros:\nBAIRROS E CIDADE\nO setor responsável já está atuando para resolver o problema o mais breve possível. Pedimos que não mexa nos equipamentos, pois a conexão será restabelecida automaticamente assim que o nosso serviço for normalizado.\nAgradecemos a sua compreensão.",
    "Corte na Fibra": "Prezado cliente, informamos que identificamos um rompimento de fibra que está afetando a conexão nos bairros:\nBAIRROS E CIDADE\nO setor responsável já está atuando para resolver o problema o mais breve possível. Pedimos que não mexa nos equipamentos, pois a conexão será restabelecida automaticamente assim que o nosso serviço for normalizado.\nAgradecemos a sua compreensão.",
    "Condições Adversas": "Prezado cliente, informamos que identificamos um rompimento de fibra que está afetando a conexão nos bairros:\nBAIRROS E CIDADE\nO setor responsável já está atuando para resolver o problema o mais breve possível. Pedimos que não mexa nos equipamentos, pois a conexão será restabelecida automaticamente assim que o nosso serviço for normalizado.\nAgradecemos a sua compreensão.",
    "Obra Local": "Prezado cliente, informamos que identificamos um rompimento de fibra que está afetando a conexão nos bairros:\nBAIRROS E CIDADE\nO setor responsável já está atuando para resolver o problema o mais breve possível. Pedimos que não mexa nos equipamentos, pois a conexão será restabelecida automaticamente assim que o nosso serviço for normalizado.\nAgradecemos a sua compreensão.",
    "Atualização de Rede": "Prezado cliente, informamos que identificamos um rompimento de fibra que está afetando a conexão nos bairros:\nBAIRROS E CIDADE\nO setor responsável já está atuando para resolver o problema o mais breve possível. Pedimos que não mexa nos equipamentos, pois a conexão será restabelecida automaticamente assim que o nosso serviço for normalizado.\nAgradecemos a sua compreensão."
}

motivo_map = {
    "Manutenção Programada": ["Ampliação de Portas de Atendimento Na CTO", "Redução de portas de atendimento na CTO", "PORTA LOS"],
    "Falha Técnica": ["Atenuação de fibra ótica - Sinal Atenuado"],
    "Corte na Fibra": ["Acidente de Trânsito", "Vandalismo", "Poda de árvores", "CTO LOS"],
    "Condições Adversas": ["Fogo nos postes", "Postes quebrados", "Fortes Chuvas na Região", "Árvores caídas"],
    "Obra Local": ["Troca de postes"],
    "Atualização de Rede": ["Manutenção Preventiva", "Manutenção Programada na Madrugada - CEO'S, DIO'S, POP"]
}

regioes_por_cidade = {
    "TERESINA-PI": [
        "ACARAPE", "AEROPORTO", "AGUA MINERAL", "ALTO ALEGRE", "ANGELICA", "ANGELIM", 
        "AREIAS", "AROEIRAS", "ARVORES VERDES", "BEIRA RIO", "BELA VISTA", 
        "BOM JESUS", "BOM PRINCIPIO", "BR343", "BRASILAR", "BUENOS AIRES", 
        "CABRAL", "CAMPESTRE", "CATARINA", "CENTRO", "CHAPADINHA","CIDADE INDUSTRIAL",
        "CIDADE JARDIM", "CIDADE NOVA", "COLORADO", "COMPRIDA", 
        "CRISTO REI", "DISTRITO INDUSTRIAL", "ESPLANADA", "EXTREMA", 
        "FÁTIMA", "FLOR DO CAMPO", "FREI SERAFIM", "GURUPI", "HORTO", 
        "ILHOTAS", "ININGA", "ITAPERU", "ITARARÉ", "JACINTA ANDRADE", 
        "JARDIM EUROPA", "JOQUEI", "LIVRAMENTO", "LOURIVAL PARENTE", 
        "MACAÚBA", "MAFRENSE", "MAFUÁ", "MARQUÊS", "MATADOURO", "MATINHA", 
        "MEMORARE", "MONTE ALEGRE", "MONTE CASTELO", "MONTE VERDE", 
        "MOCAMBINHO", "MORADA DO SOL", "MORADA NOVA", "MORRO DA ESPERANÇA", 
        "MORROS", "NOVA BRASILIA", "NOIVOS", "NOSSA SENHORA DAS GRAÇAS", 
        "NOVO HORIZONTE", "NOVO URUGUAI","OLARIAS", "PARQUE ALVORADA", "PARQUE IDEAL", 
        "PARQUE INDUSTRIAL", "PARQUE JACINTA", "PARQUE JULIANA", 
        "PARQUE PIAUÍ", "PARQUE POTI", "PARQUE SÃO JOÃO", "PARQUE SUL", 
        "PEDRA MIÚDA", "PEDRA MOLE", "PIÇARRA", "PIÇARREIRA", "PIO XII", 
        "PLANALTO", "PIRAJÁ", "PORENQUANTO", "PORTAL DA ALEGRIA", 
        "PORTO DO CENTRO", "POTY VELHO", "POVOADO CACIMBA VELHA", "POVOADO SOINHO", "PRIMAVERA", "PROMORAR", 
        "REAL COPAGRE", "RECANTO DAS PALMEIRAS", "REDENÇÃO", "REDONDA", 
        "RENASCENÇA", "SACI", "SAMAPI", "SANTA CRUZ", "SANTA ISABEL", 
        "SANTA LIA", "SANTA LUZIA", "SANTA MARIA", "SANTA ROSA", 
        "SANTO ANTÔNIO", "SATÉLITE", "SÃO CRISTOVÃO", "SÃO JOÃO", 
        "SÃO JOAQUIM", "SÃO LORENÇO", "SÃO PEDRO", "SÃO RAIMUNDO", 
        "SÃO SEBASTIÃO", "SOCOPO", "TABAJARAS", "TABULETA", "TANCREDO NEVES", 
        "TODOS OS SANTOS", "TRÊS ANDARES", "TRIUNFO", "URUGUAI", 
        "USINA SANTANA", "VALE DO GAVIÃO", "VALE QUEM TEM", "VERDE LAR", 
        "VERDE CAP", "VERMELHA", "VILA OPERÁRIA", "VILA SÃO FRANCISCO", 
        "ZOOBOTÂNICO",
    ],
    "ALTO ALEGRE-MA": ["ALTO ALEGRE"],
    "ALTOS-PI": ["ALTOS"],
    "BACABAL-MA": ["BACABAL"],
    "BARRAS-PI": ["BARRAS"],
    "BATALHA-PI": ["BATALHA"],
    "CAMPO MAIOR-PI": ["CAMPO MAIOR"],
    "CODÓ-MA": ["CODO"],
    "COIVARAS-PI": ["COIVARAS"],
    "COROATÁ-MA": ["COROATA"],
    "ESPERANTINA-PI": ["ESPERANTINA"],
    "ITAPECURU MIRIM-MA": ["ITAPECURU MIRIM"],
    "JOSÉ DE FREITAS-PI": ["JOSE DE FREITAS"],
    "LAGOA SECA-PI": ["LAGOA SECA"],
    "MATIAS OLIMPIO-PI": ["MATIAS OLIMPIO"],
    "MIGUEL ALVES-PI": ["MIGUEL ALVES"],
    "PIRACURUCA-PI": ["PIRACURUCÁ"],
    "PIRIPIRI-PI": ["PIRIPIRI"],
    "SÃO MATEUS-MA": ["SÃO MATEUS"],
    "TIMBIRAS-MA": ["TIMBIRAS"],
    "TIMON-MA": ["TIMON"],
    "UNIÃO-PI": ["UNIÃO"],
}

# Configuração da interface no Streamlit
st.title("Gerador de Alerta")

# Setor
setor = st.selectbox("Setor:", ["INFRA"])

# Prioridade
prioridade = st.selectbox("Prioridade:", ["BAIXA", "MÉDIA", "ALTA", "URGENTE"])

# Data e Hora de Início
col1, col2 = st.columns(2)
with col1:
    data_inicio = st.date_input("Data de Início:", datetime.now(pytz.timezone('America/Sao_Paulo')).date())
with col2:
    hora_inicio = st.time_input("Hora de Início:", time(0, 0))

# Data e Hora de Fim
col3, col4 = st.columns(2)
with col3:
    data_fim = st.date_input("Data de Fim:", datetime.now(pytz.timezone('America/Sao_Paulo')).date())
with col4:
    hora_fim = st.time_input("Hora de Fim:", time(0, 0))

# Descrição
descricao = st.selectbox("Descrição:", list(descricao_map.keys()))

# Motivo
motivo = st.selectbox("Motivo:", motivo_map.get(descricao, []))

# Cidade
cidade = st.selectbox("Cidade:", list(regioes_por_cidade.keys()))

# Regiões
regioes_selecionadas = st.multiselect("Regiões:", regioes_por_cidade.get(cidade, []))

# Número da OS
numero_os = st.text_input("Número da OS:")

# Informações Complementares
extras = st.text_input("Informações Complementares:")

if st.button("Gerar Texto"):
    texto_gerado = gerar_texto(setor, prioridade, 
                               data_inicio.strftime("%d/%m/%Y"), hora_inicio.strftime("%H:%M"), 
                               data_fim.strftime("%d/%m/%Y"), hora_fim.strftime("%H:%M"), 
                               descricao, numero_os, motivo, extras, cidade, regioes_selecionadas)
    
    st.session_state.historico.insert(0, texto_gerado)  # Adiciona no início da lista
    st.success("Texto gerado e salvo no histórico!")

st.subheader("Histórico de Textos")
for i, item in enumerate(st.session_state.historico):
    with st.expander(f"Texto {i+1}"):
        st.text_area("", item, height=100, key=f"text_{i}")
        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"Editar {i}"):
                st.session_state.historico.pop(i)
                st.experimental_rerun()
        with col2:
            if st.button(f"Excluir {i}"):
                st.session_state.historico.pop(i)
                st.experimental_rerun()


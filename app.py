import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Configurazione pagina
st.set_page_config(
    page_title="Quantum Tech Revolution",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Titolo e introduzione
st.title("🔬 Quantum Tech Revolution")
st.markdown("""
### Esplora la connessione tra scoperte quantistiche e tecnologie quotidiane
Questa dashboard interattiva mostra come le scoperte teoriche della fisica quantistica
hanno portato allo sviluppo di tecnologie che usiamo ogni giorno.
""")

# Creiamo i dataset

# Scoperte quantistiche
quantum_discoveries = {
    'anno': [1900, 1913, 1925, 1927, 1935, 1947, 1957, 1981, 1994, 2012],
    'scoperta': [
        'Teoria dei Quanti (Planck)', 
        'Modello atomico di Bohr', 
        'Meccanica Quantistica (Schrödinger, Heisenberg)', 
        'Principio di Indeterminazione', 
        'Paradosso EPR (Entanglement)', 
        'Elettrodinamica Quantistica', 
        'Teoria BCS della Superconduttività', 
        'Quantum Computing (Feynman)',
        'Algoritmo di Shor',
        'Bosone di Higgs'
    ],
    'importanza': [95, 80, 100, 90, 85, 75, 70, 95, 80, 90],
    'descrizione': [
        'Planck scopre che l\'energia è quantizzata in pacchetti discreti.',
        'Bohr descrive gli elettroni come occupanti orbite specifiche attorno al nucleo.',
        'Formulazione matematica completa della meccanica quantistica.',
        'Heisenberg stabilisce che non si possono conoscere contemporaneamente posizione e velocità.',
        'Einstein, Podolsky e Rosen descrivono il fenomeno dell\'entanglement quantistico.',
        'Teoria che unisce meccanica quantistica ed elettromagnetismo.',
        'Teoria che spiega la superconduttività attraverso coppie di elettroni.',
        'Feynman propone l\'idea di usare sistemi quantistici per calcoli.',
        'Algoritmo quantistico per la fattorizzazione di numeri grandi.',
        'Rilevamento della particella che conferisce massa.'
    ]
}

# Tecnologie derivate
quantum_tech = {
    'anno': [1947, 1958, 1960, 1970, 1985, 2000, 2010, 2015, 2019, 2022],
    'tecnologia': [
        'Transistor', 
        'Circuito Integrato', 
        'Laser', 
        'MRI (Risonanza Magnetica)', 
        'Microscopi a Effetto Tunnel', 
        'LED Quantici (QLED)', 
        'Sensori Quantistici', 
        'Comunicazione Quantistica Sicura', 
        'Computer Quantistico (Google)',
        'Simulatori Quantistici'
    ],
    'impatto_economico_mld': [1000, 900, 500, 400, 50, 300, 100, 80, 50, 30],
    'settore': [
        'Elettronica', 
        'Elettronica', 
        'Vari', 
        'Medicina', 
        'Ricerca', 
        'Display', 
        'Sensori', 
        'Sicurezza', 
        'Calcolo',
        'Ricerca'
    ],
    'scoperta_correlata': [
        'Meccanica Quantistica', 
        'Meccanica Quantistica',
        'Meccanica Quantistica',
        'Meccanica Quantistica',
        'Effetto Tunnel',
        'Meccanica Quantistica',
        'Entanglement',
        'Entanglement',
        'Quantum Computing (Feynman)',
        'Quantum Computing (Feynman)'
    ],
    'dispositivi_quotidiani': [
        'Smartphone, computer, elettrodomestici', 
        'Tutti i dispositivi elettronici moderni',
        'Lettori CD/DVD, scanner, puntatori',
        'Ospedali, centri diagnostici',
        'Laboratori di ricerca avanzata',
        'TV, monitor, smartphone',
        'Orologi atomici, sensori di gravità',
        'Reti di comunicazione sicura',
        'Sistemi di calcolo specializzati',
        'Laboratori di ricerca'
    ]
}

# Convertiamo in DataFrame pandas
df_discoveries = pd.DataFrame(quantum_discoveries)
df_tech = pd.DataFrame(quantum_tech)

# Analizziamo il tempo medio tra scoperta teorica e applicazione
# Creiamo un dataframe con alcune corrispondenze dirette
quantum_impact = pd.DataFrame({
    'scoperta': ['Meccanica Quantistica (Schrödinger, Heisenberg)', 'Principio di Indeterminazione', 
                'Paradosso EPR (Entanglement)', 'Teoria BCS della Superconduttività', 
                'Quantum Computing (Feynman)'],
    'anno_scoperta': [1925, 1927, 1935, 1957, 1981],
    'tecnologia': ['Transistor', 'Microscopi a Effetto Tunnel', 'Comunicazione Quantistica Sicura', 
                  'Superconduttori commerciali', 'Computer Quantistico (Google)'],
    'anno_tecnologia': [1947, 1985, 2015, 1986, 2019]
})

# Calcoliamo gli anni di ritardo
quantum_impact['anni_ritardo'] = quantum_impact['anno_tecnologia'] - quantum_impact['anno_scoperta']

# Sidebar con informazioni e opzioni
st.sidebar.title("Esplora la Dashboard")
st.sidebar.info("Questa dashboard è stata creata per mostrare il legame tra fisica quantistica e tecnologia moderna.")
view_option = st.sidebar.selectbox(
    "Scegli una visualizzazione:",
    ["Timeline Storica", "Impatto Economico", "Applicazioni Quotidiane", "Tempo di Sviluppo", "Dettagli Tecnologie"]
)

# Contenuto principale basato sulla scelta
if view_option == "Timeline Storica":
    st.header("Timeline delle Scoperte Quantistiche e Tecnologie Derivate")
    st.markdown("""
    Questa visualizzazione mostra quando sono avvenute le principali scoperte quantistiche (in blu)
    e quando sono state sviluppate le tecnologie correlate (in rosso).
    La dimensione dei punti rappresenta l'importanza della scoperta o l'impatto economico della tecnologia.
    """)
    
    # Timeline interattiva con Plotly
    fig = go.Figure()

    # Aggiungiamo le scoperte quantistiche
    fig.add_trace(go.Scatter(
        x=df_discoveries['anno'],
        y=[1] * len(df_discoveries),
        mode='markers',
        marker=dict(
            size=df_discoveries['importanza']/2,
            color='blue',
            opacity=0.7
        ),
        text=df_discoveries['scoperta'],
        hovertemplate='<b>%{text}</b><br>Anno: %{x}<br>Descrizione: ' + df_discoveries['descrizione'],
        name='Scoperte Quantistiche'
    ))

    # Aggiungiamo le tecnologie derivate
    fig.add_trace(go.Scatter(
        x=df_tech['anno'],
        y=[0] * len(df_tech),
        mode='markers',
        marker=dict(
            size=df_tech['impatto_economico_mld']/20,
            color='red',
            opacity=0.7
        ),
        text=df_tech['tecnologia'],
        hovertemplate='<b>%{text}</b><br>Anno: %{x}<br>Settore: ' + df_tech['settore'] + '<br>Dispositivi: ' + df_tech['dispositivi_quotidiani'],
        name='Tecnologie Derivate'
    ))

    # Personalizziamo il layout
    fig.update_layout(
        xaxis_title='Anno',
        yaxis=dict(
            ticktext=['Tecnologie', 'Scoperte'],
            tickvals=[0, 1],
            range=[-0.5, 1.5]
        ),
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)
    
    with st.expander("Dettagli delle Scoperte Scientifiche"):
        for i, row in df_discoveries.iterrows():
            st.markdown(f"**{row['scoperta']} ({row['anno']})**")
            st.write(row['descrizione'])
            st.markdown("---")

elif view_option == "Impatto Economico":
    st.header("Impatto Economico delle Tecnologie Quantistiche")
    st.markdown("""
    Questa visualizzazione mostra l'impatto economico stimato delle tecnologie
    derivate dalla fisica quantistica, suddiviso per settore.
    """)
    
    # Impatto economico per settore
    impact_by_sector = df_tech.groupby('settore')['impatto_economico_mld'].sum().reset_index()
    impact_by_sector = impact_by_sector.sort_values('impatto_economico_mld', ascending=False)

    fig = px.bar(
        impact_by_sector, 
        x='settore', 
        y='impatto_economico_mld',
        labels={'impatto_economico_mld': 'Impatto Economico (Miliardi $)', 'settore': 'Settore'},
        color='impatto_economico_mld',
        color_continuous_scale='Viridis',
        text_auto=True
    )

    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)
    
    # Dettagli per ogni settore
    selected_sector = st.selectbox("Seleziona un settore per vedere i dettagli:", impact_by_sector['settore'].tolist())
    
    sector_techs = df_tech[df_tech['settore'] == selected_sector]
    st.markdown(f"### Tecnologie nel settore {selected_sector}")
    
    for i, row in sector_techs.iterrows():
        st.markdown(f"**{row['tecnologia']} ({row['anno']})**")
        st.write(f"Impatto economico: ${row['impatto_economico_mld']} miliardi")
        st.write(f"Dispositivi: {row['dispositivi_quotidiani']}")
        st.markdown("---")

elif view_option == "Applicazioni Quotidiane":
    st.header("Tecnologie Quantistiche nella Vita Quotidiana")
    st.markdown("""
    Questa visualizzazione mostra come le tecnologie quantistiche
    sono presenti nei dispositivi che usiamo ogni giorno.
    """)
    
    # Dati per applicazioni quotidiane
    tech_devices = pd.DataFrame({
        'Categoria': ['Elettronica di consumo', 'Medicina', 'Telecomunicazioni', 'Sicurezza', 'Energia'],
        'Tecnologie Quantistiche Utilizzate': ['Transistor, Circuiti Integrati, QLED', 'MRI, Sensori Quantistici', 
                                              'Laser, Comunicazione Quantistica', 'Crittografia Quantistica', 
                                              'Celle Solari Quantistiche'],
        'Percentuale Prodotti': [85, 45, 60, 25, 30],
        'Esempio Dispositivo': ['Smartphone', 'Scanner MRI', 'Fibra Ottica', 'Sistemi di sicurezza bancari', 'Pannelli solari avanzati']
    })

    fig = px.bar(
        tech_devices,
        x='Categoria',
        y='Percentuale Prodotti',
        color='Percentuale Prodotti',
        text='Percentuale Prodotti',
        title='Percentuale di Prodotti che Utilizzano Tecnologie Quantistiche per Categoria',
        hover_data=['Tecnologie Quantistiche Utilizzate', 'Esempio Dispositivo'],
        color_continuous_scale='Bluered'
    )

    st.plotly_chart(fig, use_container_width=True)
    
    # Esempi di tecnologie nella vita quotidiana
    st.subheader("Esempi nella vita quotidiana")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 📱 Smartphone")
        st.markdown("""
        - **Transistor**: Processori basati su effetti quantistici
        - **LED e QLED**: Display a tecnologia quantistica
        - **GPS**: Utilizza orologi atomici basati su principi quantistici
        """)
    
    with col2:
        st.markdown("### 💻 Computer")
        st.markdown("""
        - **Memoria**: Basata su storage di carica elettronica
        - **Laser**: Lettori ottici basati su effetti quantistici
        - **Hard Disk**: GMR (Giant Magnetoresistance) basata su spin quantistico
        """)
    
    with col3:
        st.markdown("### 🏥 Medicina")
        st.markdown("""
        - **MRI**: Risonanza magnetica basata su spin nucleare
        - **PET**: Tomografia a emissione di positroni
        - **Laser chirurgici**: Basati su emissione stimolata quantistica
        """)

elif view_option == "Tempo di Sviluppo":
    st.header("Tempo tra Scoperta Quantistica e Applicazione Tecnologica")
    st.markdown("""
    Questa visualizzazione mostra quanto tempo è passato tra una scoperta teorica
    e la sua prima applicazione tecnologica significativa.
    """)
    
    # Visualizziamo il ritardo
    fig = px.bar(
        quantum_impact,
        x='scoperta',
        y='anni_ritardo',
        color='anni_ritardo',
        text='anni_ritardo',
        labels={'scoperta': 'Scoperta Quantistica', 'anni_ritardo': 'Anni di Ritardo'},
        color_continuous_scale='Viridis'
    )

    st.plotly_chart(fig, use_container_width=True)
    
    # Mostriamo i dettagli in una tabella
    st.subheader("Dettagli Scoperta-Applicazione")
    
    # Aggiungiamo colonne leggibili
    quantum_impact_display = quantum_impact.copy()
    quantum_impact_display['Scoperta → Tecnologia'] = quantum_impact_display.apply(
        lambda row: f"{row['scoperta']} → {row['tecnologia']}", axis=1
    )
    quantum_impact_display['Periodo'] = quantum_impact_display.apply(
        lambda row: f"{row['anno_scoperta']} → {row['anno_tecnologia']}", axis=1
    )
    
    st.dataframe(
        quantum_impact_display[['Scoperta → Tecnologia', 'Periodo', 'anni_ritardo']].rename(
            columns={'anni_ritardo': 'Anni Trascorsi'}
        ),
        use_container_width=True
    )
    
    # Calcoliamo e mostriamo la media
    media_anni = quantum_impact['anni_ritardo'].mean()
    st.info(f"📊 **Dato rilevante**: In media, ci vogliono **{media_anni:.1f} anni** per trasformare una scoperta quantistica in tecnologia applicata.")

else:  # Dettagli Tecnologie
    st.header("Dettagli delle Tecnologie Quantistiche")
    st.markdown("""
    Questa sezione permette di esplorare in dettaglio ciascuna tecnologia quantistica,
    la sua origine, impatto economico e applicazioni quotidiane.
    """)
    
    selected_tech = st.selectbox("Seleziona una tecnologia:", df_tech['tecnologia'].tolist())
    
    tech_details = df_tech[df_tech['tecnologia'] == selected_tech].iloc[0]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(tech_details['tecnologia'])
        st.markdown(f"**Anno di sviluppo:** {tech_details['anno']}")
        st.markdown(f"**Settore principale:** {tech_details['settore']}")
        st.markdown(f"**Impatto economico stimato:** ${tech_details['impatto_economico_mld']} miliardi")
        st.markdown(f"**Scoperta quantistica correlata:** {tech_details['scoperta_correlata']}")
    
    with col2:
        st.subheader("Applicazioni nella vita quotidiana")
        st.markdown(f"**Dispositivi:** {tech_details['dispositivi_quotidiani']}")
        
        # Aggiungiamo un fatto curioso per ogni tecnologia
        tech_facts = {
            'Transistor': "I processori dei moderni smartphone contengono miliardi di transistor, ciascuno delle dimensioni di pochi nanometri.",
            'Circuito Integrato': "Il primo circuito integrato conteneva solo un transistor, un resistore e un condensatore. Oggi ne contengono miliardi.",
            'Laser': "Il termine LASER è in realtà un acronimo per 'Light Amplification by Stimulated Emission of Radiation'.",
            'MRI (Risonanza Magnetica)': "Un tipico scanner MRI utilizza magneti 60.000 volte più potenti del campo magnetico terrestre.",
            'Microscopi a Effetto Tunnel': "Questi microscopi possono visualizzare singoli atomi sfruttando l'effetto tunnel quantistico.",
            'LED Quantici (QLED)': "I QLED utilizzano nanocristalli (quantum dots) di dimensioni comprese tra 2 e 10 nanometri.",
            'Sensori Quantistici': "I sensori basati sul diamante possono rilevare campi magnetici generati da singole cellule.",
            'Comunicazione Quantistica Sicura': "Grazie all'entanglement, qualsiasi tentativo di intercettazione viene immediatamente rilevato.",
            'Computer Quantistico (Google)': "Nel 2019, il computer quantistico di Google ha completato in 200 secondi un calcolo che avrebbe richiesto 10.000 anni al supercomputer più potente.",
            'Simulatori Quantistici': "I simulatori quantistici permettono di studiare sistemi complessi impossibili da modellare con computer tradizionali."
        }
        
        st.info(f"**Lo sapevi?** {tech_facts.get(selected_tech, '')}")

# Footer
st.markdown("---")
st.markdown("Dashboard creata per scopi didattici | Quantum Tech Revolution | 2025")

import streamlit as st
# Lehe seadistamine
st.set_page_config(
    page_title="Kickboxing Payment Tracker",
    page_icon="🥊",
    layout="wide"
)
# Äpi kujundus
st.markdown("""
<style>
    .stApp {
        background-color: #10151F;
        color: #F8FAFC;
    }

    .block-container {
        max-width: 1150px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3 {
        color: #FFFFFF !important;
        letter-spacing: -0.5px;
    }

    h1 {
        font-size: 2.5rem !important;
    }

    p, label {
        color: #E2E8F0 !important;
    }

    div[data-testid="stWidgetLabel"] p {
        color: #CBD5E1 !important;
        font-weight: 500;
    }

    div[data-baseweb="select"] > div,
    div[data-baseweb="input"] > div {
        background-color: #1D2532 !important;
        border: 1px solid #364152 !important;
        border-radius: 12px !important;
        color: #FFFFFF !important;
    }

    div[data-baseweb="select"] *,
    div[data-baseweb="input"] input {
        color: #FFFFFF !important;
    }

    div[data-testid="stMetric"] {
        background-color: #1D2532;
        border: 1px solid #364152;
        padding: 20px;
        border-radius: 16px;
    }

    div[data-testid="stMetricValue"] {
        color: #FFFFFF;
        font-weight: 700;
    }

    div.stButton > button,
    div.stFormSubmitButton > button {
        border-radius: 10px;
        border: 1px solid #475569;
        font-weight: 600;
    }

    div.stButton > button:hover,
    div.stFormSubmitButton > button:hover {
        border-color: #E63946;
        color: #E63946;
    }

    hr {
        border-color: #364152;
    }

/* Sisestuskastide tume taust */
div[data-testid="stSelectbox"] div[data-baseweb="select"] > div,
div[data-testid="stNumberInput"] div[data-baseweb="input"] > div,
div[data-testid="stTextInput"] div[data-baseweb="input"] > div {
    background-color: #1D2532 !important;
    border: 1px solid #364152 !important;
    border-radius: 12px !important;
}

/* Sisestuskastide tekst */
div[data-testid="stSelectbox"] div[data-baseweb="select"] *,
div[data-testid="stNumberInput"] input,
div[data-testid="stTextInput"] input {
    color: #FFFFFF !important;
}

/* Õpilase lisamise nupp */
div[data-testid="stFormSubmitButton"] button {
    background-color: #E63946 !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
}

/* Nupp hiirega peale minnes */
div[data-testid="stFormSubmitButton"] button:hover {
    background-color: #C92C39 !important;
    color: #FFFFFF !important;
}/* Valikukastide loetav tekst */
div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
    background-color: #F8FAFC !important;
}

div[data-testid="stSelectbox"] div[data-baseweb="select"] * {
    color: #1E293B !important;
}

/* Aasta sisestuskasti tekst */
div[data-testid="stNumberInput"] input {
    color: #1E293B !important;
    -webkit-text-fill-color: #1E293B !important;
}

/* Õpilase nime sisestuskasti tekst */
div[data-testid="stTextInput"] input {
    color: #1E293B !important;
    -webkit-text-fill-color: #1E293B !important;
}/* Valikukastide loetav tekst */
div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
    background-color: #F8FAFC !important;
}

div[data-testid="stSelectbox"] div[data-baseweb="select"] * {
    color: #1E293B !important;
}

/* Aasta sisestuskasti tekst */
div[data-testid="stNumberInput"] input {
    color: #1E293B !important;
    -webkit-text-fill-color: #1E293B !important;
}

/* Õpilase nime sisestuskasti tekst */
div[data-testid="stTextInput"] input {
    color: #1E293B !important;
    -webkit-text-fill-color: #1E293B !important;
}/* Õpilaste kaardid */
div[data-testid="stVerticalBlockBorderWrapper"] > div {
    border-color: #303A49;
    border-radius: 16px;
}

/* Prügikasti nupud */
div.stButton > button {
    transition: all 0.2s ease;
}

div.stButton > button:hover {
    border-color: #E63946;
    background-color: #2A1B25;
    color: #FF5B67;
}

/* Linnukese värv */
div[data-testid="stCheckbox"] input:checked {
    accent-color: #22C55E;
}/* Vähem tühja ruumi elementide vahel */
.stVerticalBlock {
    gap: 0.6rem;
}

/* Väiksemad pealkirjad */
h1 {
    font-size: 2rem !important;
    margin-bottom: 0.3rem !important;
}

h2, h3 {
    font-size: 1.35rem !important;
    margin-top: 0.5rem !important;
    margin-bottom: 0.3rem !important;
}

/* Vähem ruumi lehe ülaosas */
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
}

/* Kompaktsemad sisestuskastid */
div[data-testid="stTextInput"] input {
    min-height: 2.5rem;
}/* Peidame Streamliti ülemise tööriistariba */
header[data-testid="stHeader"] {
    display: none;
}

/* Jätame lehe ülaossa natuke ruumi */
.block-container {
    padding-top: 1.5rem !important;
}/* Filtri nuppude tekst */
div[data-testid="stSegmentedControl"] button {
    color: #111827 !important;
}

/* Valitud filtri nupp */
div[data-testid="stSegmentedControl"] button[aria-pressed="true"] {
    background-color: #e93449 !important;
    color: white !important;
}/* Filtri nuppude tekst */
div[data-testid="stSegmentedControl"] button,
div[data-testid="stSegmentedControl"] label,
div[data-testid="stSegmentedControl"] p {
    color: #111827 !important;
}

/* Valitud nupp */
div[data-testid="stSegmentedControl"] button[aria-pressed="true"] {
    background-color: #e93449 !important;
    color: white !important;
}/* Õpilaste filtri nupud */
div[data-testid="stSegmentedControl"] button {
    background-color: #202938 !important;
    color: #ffffff !important;
    border: 1px solid #39465a !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
}

/* Valitud filtrinupp */
div[data-testid="stSegmentedControl"] button[aria-checked="true"],
div[data-testid="stSegmentedControl"] button[aria-pressed="true"] {
    background-color: #e93448 !important;
    color: #ffffff !important;
    border-color: #e93448 !important;
}

/* Hiirega nupule liikudes */
div[data-testid="stSegmentedControl"] button:hover {
    background-color: #38465a !important;
    color: #ffffff !important;
}
</style>
""", unsafe_allow_html=True)
import psycopg
from datetime import date

# Loome ühenduse andmebaasiga
def loo_uhendus():
    return psycopg.connect(st.secrets["DATABASE_URL"])

# Loome andmebaasi tabelid
def loo_tabelid():
    uhendus = loo_uhendus()
    cursor = uhendus.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS kickboxing.opilased (
            id INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
            nimi TEXT NOT NULL,
            grupp TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS kickboxing.maksed (
            opilase_id INTEGER NOT NULL,
            kuu TEXT NOT NULL,
            makstud INTEGER NOT NULL DEFAULT 0,
            PRIMARY KEY (opilase_id, kuu),
            FOREIGN KEY (opilase_id)
                REFERENCES kickboxing.opilased(id)
        )
    """)

    uhendus.commit()
    uhendus.close()
# Käivitame tabelite loomise
loo_tabelid()
# Salvestame uue õpilase andmebaasi
# Salvestame uue õpilase Supabase'i andmebaasi
def lisa_opilane(nimi, grupp):
    uhendus = loo_uhendus()
    cursor = uhendus.cursor()

    cursor.execute(
        "INSERT INTO kickboxing.opilased (nimi, grupp) VALUES (%s, %s)",
        (nimi, grupp)
    )

    uhendus.commit()
    uhendus.close()
    # Loeme õpilased Supabase'i andmebaasist
def leia_opilased(grupp):
    uhendus = loo_uhendus()
    cursor = uhendus.cursor()

    cursor.execute(
        "SELECT id, nimi FROM kickboxing.opilased WHERE grupp = %s",
        (grupp,)
    )

    opilased = cursor.fetchall()
    uhendus.close()

    return opilased

# Salvestame õpilase makse Supabase'i
def salvesta_makse(opilase_id, kuu, makstud):
    uhendus = loo_uhendus()
    cursor = uhendus.cursor()

    cursor.execute("""
        INSERT INTO kickboxing.maksed (opilase_id, kuu, makstud)
        VALUES (%s, %s, %s)
        ON CONFLICT (opilase_id, kuu)
        DO UPDATE SET makstud = EXCLUDED.makstud
    """, (opilase_id, kuu, int(makstud)))

    uhendus.commit()
    uhendus.close()


# Kontrollime Supabase'ist, kas õpilane on maksnud
def kontrolli_makset(opilase_id, kuu):
    uhendus = loo_uhendus()
    cursor = uhendus.cursor()

    cursor.execute(
        "SELECT makstud FROM kickboxing.maksed WHERE opilase_id = %s AND kuu = %s",
        (opilase_id, kuu)
    )

    tulemus = cursor.fetchone()
    uhendus.close()

    return bool(tulemus[0]) if tulemus else False

# Kustutame õpilase ja tema maksed Supabase'ist
def kustuta_opilane(opilase_id):
    uhendus = loo_uhendus()
    cursor = uhendus.cursor()

    cursor.execute(
        "DELETE FROM kickboxing.maksed WHERE opilase_id = %s",
        (opilase_id,)
    )

    cursor.execute(
        "DELETE FROM kickboxing.opilased WHERE id = %s",
        (opilase_id,)
    )

    uhendus.commit()
    uhendus.close()






st.title("🥊 KICKBOXING")
st.caption("PAYMENT TRACKER | Treeningtasude haldamine")
# Treeninggrupi ja perioodi valimine
st.subheader("🥊 Maksete haldamine")

grupid = ["Noored", "Täiskasvanud"]

kuu_nimed = [
    "Jaanuar", "Veebruar", "Märts", "Aprill",
    "Mai", "Juuni", "Juuli", "August",
    "September", "Oktoober", "November", "Detsember"
]

veerg_grupp, veerg_kuu, veerg_aasta = st.columns([2, 2, 1])

with veerg_grupp:
    valitud_grupp = st.selectbox(
        "Treeninggrupp",
        grupid
    )

with veerg_kuu:
    kuu = st.selectbox(
        "Kuu",
        range(1, 13),
        index=date.today().month - 1,
        format_func=lambda x: kuu_nimed[x - 1]
    )

with veerg_aasta:
    aasta = st.number_input(
        "Aasta",
        min_value=2025,
        max_value=2100,
        value=date.today().year
    )

valitud_kuu = f"{aasta}-{kuu:02d}"

# Kõikide gruppide kuutasu
kuutasu = 50.0

# Loome õpilaste nimekirja
if "opilased" not in st.session_state:
    st.session_state.opilased = []

with st.expander("➕ Lisa uus õpilane"):
    with st.form("opilase_lisamine", clear_on_submit=True):
        nimi = st.text_input(
            "Õpilase nimi",
            placeholder="Sisesta ees- ja perekonnanimi"
        )

        lisa_nupp = st.form_submit_button("➕ Lisa õpilane")

        if lisa_nupp:
            if nimi.strip():
                lisa_opilane(nimi.strip(), valitud_grupp)
                st.success(f"Õpilane {nimi} lisatud!")
            else:
                st.warning("Palun sisesta õpilase nimi!")
# Õpilaste filtreerimine makse staatuse järgi

filter_valik = st.radio(
    "Õpilaste filter",
    ["Kõik", "Makstud", "Maksmata"],
    horizontal=True
)
andmebaasi_opilased = leia_opilased(valitud_grupp)
filtreeritud_opilased = []

for opilase_id, opilase_nimi in andmebaasi_opilased:
    makstud = kontrolli_makset(opilase_id, valitud_kuu)

    if filter_valik == "Kõik":
        filtreeritud_opilased.append((opilase_id, opilase_nimi))

    elif filter_valik == "Makstud" and makstud:
        filtreeritud_opilased.append((opilase_id, opilase_nimi))

    elif filter_valik == "Maksmata" and not makstud:
        filtreeritud_opilased.append((opilase_id, opilase_nimi))
# Õpilaste otsimine nime järgi
otsing = st.text_input(
    "🔎 Otsi õpilast",
    placeholder="Sisesta õpilase nimi..."
)

naidatavad_opilased = [
    opilane for opilane in filtreeritud_opilased
    if otsing.lower() in opilane[1].lower()
]
for opilase_id, opilase_nimi in naidatavad_opilased:
    with st.container(border=True, height="content"):
        veerg1, veerg2, veerg3 = st.columns([3, 2, 1])

        with veerg1:
            st.write("🥊", opilase_nimi)

        with veerg2:
            linnuke, staatus, tyhi = st.columns(
    [0.5, 2, 1],
    vertical_alignment="center",
    gap="small"
)

            with linnuke:
                makstud = st.checkbox(
                    "Makstud",
                    value=kontrolli_makset(opilase_id, valitud_kuu),
                    key=f"makse_{opilase_id}_{valitud_kuu}",
                    label_visibility="collapsed"
                )

            salvesta_makse(opilase_id, valitud_kuu, makstud)

            with staatus:
                if makstud:
                    st.markdown(":green[**● Makstud**]")
                else:
                    st.markdown(":red[**● Maksmata**]")


        with veerg3:
            if st.button("🗑️", key=f"kustuta_{opilase_id}", type="tertiary"):
                st.session_state.kustutatav_id = opilase_id
                st.rerun()

        # Kustutamise kinnitamine
        if st.session_state.get("kustutatav_id") == opilase_id:
            st.warning(
                f"Kas oled kindel, et soovid kustutada õpilase {opilase_nimi}?"
            )

            jah, ei = st.columns(2)

            with jah:
                if st.button("✅", key=f"jah_{opilase_id}"):
                    kustuta_opilane(opilase_id)
                    st.session_state.kustutatav_id = None
                    st.rerun()

            with ei:
                if st.button("❌", key=f"ei_{opilase_id}"):
                    st.session_state.kustutatav_id = None
                    st.rerun()


# Maksete kokkuvõtte arvutamine
makstud_arv = sum(
    1 for opilase_id, nimi in andmebaasi_opilased
    if kontrolli_makset(opilase_id, valitud_kuu)
)

maksmata_arv = len(andmebaasi_opilased) - makstud_arv

# Arvutame treeningtasude summad
kuutasu = 50

laekunud = makstud_arv * kuutasu
laekumata = maksmata_arv * kuutasu
kokku = len(andmebaasi_opilased) * kuutasu

# Rahaline kokkuvõte
st.subheader("💶 Rahaline kokkuvõte")

veerg1, veerg2, veerg3 = st.columns(3)

with veerg1:
    st.metric("💰 Laekunud", f"{laekunud:.2f} €")

with veerg2:
    st.metric("❌ Laekumata", f"{laekumata:.2f} €")

with veerg3:
    st.metric("📊 Kokku oodatav", f"{kokku:.2f} €")


# Funktsioon maksmata õpilaste leidmiseks
def leia_volglased(opilased, kuu):
    volglased = []

    for opilase_id, nimi in opilased:
        if not kontrolli_makset(opilase_id, kuu):
            volglased.append(nimi)

    return volglased


# Maksmata õpilaste nimekiri
st.subheader("❌ Maksmata õpilased")

volglased = leia_volglased(andmebaasi_opilased, valitud_kuu)

if len(volglased) == 0:
    st.success("🎉 Kõik selle grupi õpilased on maksnud!")
else:
    for nimi in volglased:
        with st.container(border=True):
            veerg_nimi, veerg_summa = st.columns([3, 1])

            with veerg_nimi:
                st.write("🔴", nimi)

            with veerg_summa:
                st.markdown(":red[**50 € tasumata**]")


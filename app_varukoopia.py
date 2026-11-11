import streamlit as st

st.title("🥊 Kickboxing Payment Tracker")

st.write("Tere tulemast treeningtasude haldamise programmi!")

st.subheader("Treeninggrupid")

grupid = ["Lapsed", "Noored", "Täiskasvanud", "Võistlejad"]

valitud_grupp = st.selectbox("Vali treeninggrupp:", grupid)

st.write("Valitud grupp:", valitud_grupp)
from datetime import date

st.subheader("Maksete kuu")

kuu = st.selectbox(
    "Vali kuu:",
    range(1, 13),
    index=date.today().month - 1,
    format_func=lambda x: [
        "Jaanuar", "Veebruar", "Märts", "Aprill",
        "Mai", "Juuni", "Juuli", "August",
        "September", "Oktoober", "November", "Detsember"
    ][x - 1]
)

aasta = st.number_input(
    "Vali aasta:",
    min_value=2025,
    max_value=2100,
    value=date.today().year
)

valitud_kuu = f"{aasta}-{kuu:02d}"

# Loome õpilaste nimekirja
if "opilased" not in st.session_state:
    st.session_state.opilased = []

st.subheader("Õpilaste lisamine")

nimi = st.text_input("Sisesta õpilase nimi:")

if st.button("Lisa õpilane"):
    if nimi.strip():
        uus_opilane = {
            "nimi": nimi.strip(),
            "grupp": valitud_grupp,
            "makstud": False
        }

        st.session_state.opilased.append(uus_opilane)
        st.success(f"Õpilane {nimi} lisatud!")
    else:
        st.warning("Palun sisesta õpilase nimi!")

# Kuvame õpilaste nimekirja
st.subheader("Õpilaste nimekiri")

for i, opilane in enumerate(st.session_state.opilased):
    if opilane["grupp"] == valitud_grupp:

        veerg1, veerg2, veerg3 = st.columns([3, 2, 1])

        with veerg1:
            st.write("🥊", opilane["nimi"])

        with veerg2:
            if "maksed" not in opilane:
                opilane["maksed"] = {}

            makstud = st.checkbox(
                "Makstud",
                value=opilane["maksed"].get(valitud_kuu, False),
                key=f"makse_{i}_{valitud_kuu}"
            )

            st.session_state.opilased[i]["maksed"][valitud_kuu] = makstud


        with veerg3:
            if st.button("🗑️", key=f"kustuta_{i}"):
                st.session_state.opilased.pop(i)
                st.rerun()

# Maksete kokkuvõte
st.subheader("Maksete kokkuvõte")

grupi_opilased = [
    opilane for opilane in st.session_state.opilased
    if opilane["grupp"] == valitud_grupp
]

makstud_arv = sum(
    1 for opilane in grupi_opilased
    if opilane.get("maksed", {}).get(valitud_kuu, False)
)

maksmata_arv = len(grupi_opilased) - makstud_arv

st.write("✅ Makstud:", makstud_arv)
st.write("❌ Maksmata:", maksmata_arv)

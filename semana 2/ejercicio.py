listaDinosaurios=[
    {
        "nombre": "Tyrannosaurus Rex",
        "periodo": "Cretácico",
        "alimentacion": "Carnívoro",
        "tamaño": "Grande"
    },
    {
        "nombre": "Triceratops",
        "periodo": "Cretácico",
        "alimentacion": "Herbívoro",
        "tamaño": "Grande"
    },
    {
        "nombre": "Velociraptor",
        "periodo": "Cretácico",
        "alimentacion": "Carnívoro",
        "tamaño": "Pequeño"
    },
    {
        "nombre": "Stegosaurus",
        "periodo": "Jurásico",
        "alimentacion": "Herbívoro",
        "tamaño": "Grande"
    },
    {
        "nombre": "Allosaurus",
        "periodo": "Jurásico",
        "alimentacion": "Carnívoro",
        "tamaño": "Grande"
    },
    {
        "nombre": "Brachiosaurus",
        "periodo": "Jurásico",
        "alimentacion": "Herbívoro",
        "tamaño": "Grande"
    },
    {
        "nombre": "Spinosaurus",
        "periodo": "Cretácico",
        "alimentacion": "Carnívoro",
        "tamaño": "Grande"
    },
    {
        "nombre": "Ankylosaurus",
        "periodo": "Cretácico",
        "alimentacion": "Herbívoro",
        "tamaño": "Grande"
    },
    {
        "nombre": "Pteranodon",
        "periodo": "Cretácico",
        "alimentacion": "Carnívoro",
        "tamaño": "Mediano"
    },
    {
        "nombre": "Diplodocus",
        "periodo": "Jurásico",
        "alimentacion": "Herbívoro",
        "tamaño": "Grande"
    },
    {
        "nombre": "Gallimimus",
        "periodo": "Cretácico",
        "alimentacion": "Herbívoro",
        "tamaño": "Mediano"
    },
    {
        "nombre": "Parasaurolophus",
        "periodo": "Cretácico",
        "alimentacion": "Herbívoro",
        "tamaño": "Grande"
    },
    {
        "nombre": "Irritator",
        "periodo": "Cretácico",
        "alimentacion": "Carnívoro",
        "tamaño": "Mediano"
    },
    {
        "nombre": "Carnotaurus",
        "periodo": "Cretácico",
        "alimentacion": "Carnívoro",
        "tamaño": "Grande"
    },
    {
        "nombre": "Pachycephalosaurus",
        "periodo": "Cretácico",
        "alimentacion": "Herbívoro",
        "tamaño": "Mediano"
    },
    {
        "nombre": "Therizinosaurus",
        "periodo": "Cretácico",
        "alimentacion": "Herbívoro",
        "tamaño": "Grande"
    },
    {
        "nombre": "Oviraptor",
        "periodo": "Cretácico",
        "alimentacion": "Omnívoro",
        "tamaño": "Pequeño"
    },
    {
        "nombre": "Compsognathus",
        "periodo": "Jurásico",
        "alimentacion": "Carnívoro",
        "tamaño": "Pequeño"
    },
    {
        "nombre": "Mamenchisaurus",
        "periodo": "Jurásico",
        "alimentacion": "Herbívoro",
        "tamaño": "Grande"
    },
    {
        "nombre": "Deinonychus",
        "periodo": "Cretácico",
        "alimentacion": "Carnívoro",
        "tamaño": "Mediano"
    },
    {
        "nombre": "Baryonyx",
        "periodo": "Cretácico",
        "alimentacion": "Carnívoro",
        "tamaño": "Mediano"
    },
    {
        "nombre": "Iguanodon",
        "periodo": "Cretácico",
        "alimentacion": "Herbívoro",
        "tamaño": "Grande"
    },
    {
        "nombre": "Pachyrhinosaurus",
        "periodo": "Cretácico",
        "alimentacion": "Herbívoro",
        "tamaño": "Grande"
    },
    {
        "nombre": "Theropoda",
        "periodo": "Jurásico",
        "alimentacion": "Carnívoro",
        "tamaño": "Mediano"
    }
]
switcher = {
    1: "Tyrannosaurus Rex",
    2: "Triceratops",
    3: "Velociraptor",
    4: "Stegosaurus",
    5: "Allosaurus",
    6: "Brachiosaurus",
    7: "Spinosaurus",
    8: "Ankylosaurus",
    9: "Pteranodon",
    10: "Diplodocus",
    11: "Gallimimus",
    12: "Parasaurolophus",
    13: "Irritator",
    14: "Carnotaurus",
    15: "Pachycephalosaurus",
    16: "Therizinosaurus",
    17: "Oviraptor",
    18: "Compsognathus",
    19: "Mamenchisaurus",
    20: "Deinonychus",
    21: "Baryonyx",
    22: "Iguanodon",
    23: "Pachyrhinosaurus",
    24: "Theropoda"
}
import streamlit as st

st.set_page_config(page_title="Explorador de dinosaurios", page_icon="🦖")
st.title("Explorador de dinosaurios")
st.write("Selecciona un número para consultar la información del dinosaurio.")

input_number = st.number_input(
    "Número del dinosaurio",
    min_value=1,
    max_value=len(switcher),
    value=1,
    step=1,
)

dinosaurio_nombre = switcher[input_number]
dinosaurio_encontrado = next(
    (
        dinosaurio
        for dinosaurio in listaDinosaurios
        if dinosaurio["nombre"] == dinosaurio_nombre
    ),
    None,
)

if dinosaurio_encontrado:
    st.subheader(dinosaurio_encontrado["nombre"])
    st.write(f"**Periodo:** {dinosaurio_encontrado['periodo']}")
    st.write(f"**Alimentación:** {dinosaurio_encontrado['alimentacion']}")
    st.write(f"**Tamaño:** {dinosaurio_encontrado['tamaño']}")
else:
    st.error("Dinosaurio no encontrado.")

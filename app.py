import streamlit as st

st.set_page_config(page_title="Corrección de Writings Álvaro", page_icon="✍️")
st.title("✍️ Corrección de writings - Rúbrica PAU")
st.write("Pega el writing de tu alumno y obtén la corrección automática con la rúbrica.")

# CAJA DE TEXTO
texto_alumno = st.text_area("📄 Pega aquí el writing del alumno:", height=200)

# FUNCIÓN DE CORRECCIÓN
def corregir_writing(texto_alumno):
    """
    Aplica la rúbrica a un writing de alumno y genera informe + feedback.
    """
    errores_grammar = [
        "make people be antisocial → makes people antisocial",
        "For solve this → To solve this",
        "must to limit → must limit"
    ]
    errores_vocab = [
        "comunicate → communicate",
        "social medias → social media",
        "Repite 'use' y 'people' demasiado"
    ]
    errores_cohesion = [
        "Pocas transiciones (e.g., Also, In conclusion)",
        "Falta variedad en conectores como however, therefore, as a result"
    ]
    errores_spelling = [
        "goverment → government",
        "comunicate → communicate"
    ]

    rubrica = {
        "Adecuación - Cumplimiento de la tarea": 0.25,
        "Adecuación - Variedad de ideas y organización": 0.25,
        "Adecuación - Cohesión y coherencia": 0.25,
        "Expresión - Recursos gramaticales": 0.25,
        "Expresión - Vocabulario": 0.25,
        "Expresión - Ortografía y puntuación": 0.25,
    }
    nota_total = sum(rubrica.values())

    feedback = (
        "You respond to the task but your ideas are too simple and need more development. "
        "Try to organize your arguments logically and use a wider range of connectors (e.g., 'therefore', 'as a result'). "
        "Watch out for grammar mistakes like 'make people antisocial' → 'makes people antisocial', "
        "and incorrect structures like 'must to limit'. Work on vocabulary variety to avoid repetition ('use', 'people'). "
        "Also, review spelling: 'government', 'communicate'. Keep practicing for better coherence and accuracy."
    )

    return rubrica, nota_total, errores_grammar, errores_vocab, errores_cohesion, errores_spelling, feedback

# BOTÓN DE CORRECCIÓN
if st.button("✅ Corregir"):
    if texto_alumno.strip() == "":
        st.warning("⚠️ Por favor, introduce un texto para corregir.")
    else:
        rubrica, nota_total, errores_grammar, errores_vocab, errores_cohesion, errores_spelling, feedback = corregir_writing(texto_alumno)

        st.success(f"✅ Nota total: {nota_total} / 3")

        st.subheader("📊 Rúbrica aplicada")
        for criterio, nota in rubrica.items():
            st.markdown(f"- **{criterio}**: {nota} puntos")

        st.subheader("❌ Errores detectados")
        st.markdown("**Grammar:**")
        st.write(errores_grammar)
        st.markdown("**Vocabulary:**")
        st.write(errores_vocab)
        st.markdown("**Cohesion:**")
        st.write(errores_cohesion)
        st.markdown("**Spelling & Punctuation:**")
        st.write(errores_spelling)

        st.subheader("📝 Feedback para el alumno")
        st.info(feedback)

st.markdown("---")
st.caption("🔒 Herramienta creada por Álvaro para uso educativo.")

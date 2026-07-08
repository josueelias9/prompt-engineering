import os
import requests
import streamlit as st

OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://ollama:11434")
DEFAULT_MODEL = os.environ.get("LLM_MODEL", "llama3.2")

st.set_page_config(page_title="Prompt Runner", page_icon="🧠", layout="centered")
st.title("🧠 Prompt Runner")
st.caption("Consulta directa al modelo — sin memoria, sin historial.")

# ── Sidebar: model config ──────────────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Configuración")
    model = st.text_input("Modelo", value=DEFAULT_MODEL)
    temperature = st.slider(
        "Temperatura",
        min_value=0.0,
        max_value=2.0,
        value=0.7,
        step=0.05,
        help="Valores bajos → respuestas más deterministas. Valores altos → más creatividad.",
    )
    max_tokens = st.number_input(
        "Máx. tokens", min_value=64, max_value=8192, value=1024, step=64
    )
    top_k = st.slider(
        "Top-K",
        min_value=1,
        max_value=200,
        value=40,
        step=1,
        help="Limita la selección a los K tokens más probables. Menor → más enfocado.",
    )
    top_p = st.slider(
        "Top-P (nucleus)",
        min_value=0.0,
        max_value=1.0,
        value=0.9,
        step=0.01,
        help="Masa de probabilidad acumulada considerada. Menor → más determinista.",
    )

# ── Main: prompt input ─────────────────────────────────────────────────────────
prompt = st.text_area(
    "Prompt",
    placeholder="Escribe aquí tu instrucción o pregunta...",
    height=200,
)

run = st.button("Ejecutar ▶", type="primary", use_container_width=True)

if run:
    if not prompt.strip():
        st.warning("El prompt no puede estar vacío.")
    else:
        with st.spinner("Consultando el modelo..."):
            try:
                response = requests.post(
                    f"{OLLAMA_HOST}/api/generate",
                    json={
                        "model": model,
                        "prompt": prompt,
                        "stream": False,
                        "options": {
                            "temperature": temperature,
                            "top_k": top_k,
                            "top_p": top_p,
                            "num_predict": max_tokens,
                        },
                    },
                    timeout=120,
                )
                response.raise_for_status()
                data = response.json()
                answer = data.get("response", "")

                st.divider()
                st.subheader("Respuesta")
                st.markdown(answer)

                with st.expander("Métricas"):
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Tokens evaluados", data.get("eval_count", "—"))
                    col2.metric("Tokens prompt", data.get("prompt_eval_count", "—"))
                    col3.metric(
                        "Tiempo total (s)",
                        round(data.get("total_duration", 0) / 1e9, 2),
                    )

            except requests.exceptions.ConnectionError:
                st.error(
                    f"No se pudo conectar a Ollama en `{OLLAMA_HOST}`. "
                    "Verifica que el servicio esté corriendo."
                )
            except requests.exceptions.HTTPError as e:
                st.error(f"Error HTTP: {e.response.status_code} — {e.response.text}")
            except Exception as e:
                st.error(f"Error inesperado: {e}")

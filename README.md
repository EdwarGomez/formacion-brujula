# 🧭 Formación Brújula IA · Grupo LEMCO

Aplicación interactiva y material de formación para Champions y Líderes de **Grupo LEMCO** (Challenger S.A.S, Grupo Sky, Hotel Habitel).

---

## 📚 Contenido de la Capacitación (13 Módulos)

1. **Panorama e Introducción a la IA:** Contexto global y hoja de ruta de adopción.
2. **Qué es y qué NO es IA Generativa:** Modelos fundacionales de punta (Claude Sonnet 5.5, GPT-6.1 Sol, Gemini 4 Argon, Amazon Nova) vs. Aprendizaje Automático Tradicional.
3. **Cómo funciona un LLM por dentro:** Tokenización en español, embeddings vectoriales y mecanismo de atención (Query, Key, Value).
4. **Limitaciones Reales y Mitigación:** Alucinaciones estadísticas, corte de conocimiento y arquitecturas RAG / Fine-Tuning.
5. **Casos Reales: Proyecto Brújula:** Demostraciones aplicadas a manufactura, logística WMS y hotelería.
6. **IA Responsable y Ley 1581 de 2012:** Privacidad, datos sensibles y lista de verificación previa a la ejecución de prompts.
7. **Matriz Viabilidad × Impacto:** Evaluador interactivo en vivo con diagnóstico y catalogación por cuadrantes.
8. **Técnicas de Prompting Efectivo:** Zero-Shot, Few-Shot delimitado, Chain-of-Thought, System Prompts y Prompt Chaining.
9. **Ingeniería de Contexto e Instrucciones Estructuradas:** Metodología DAIR.AI, delimitadores XML, esquema JSON tipado y supresión de alucinaciones.
10. **Taller en Vivo — Framework CERO:** Constructor interactivo y medidor de calidad del prompt (*Contexto, Especificidad, Rol, Output*).
11. **Buenas Prácticas y Errores Comunes:** Espacios de trabajo (Amazon Quick Desktop), defensa contra Prompt Injection y sesgo de confirmación.
12. **Anatomía, Tipos y Orquestación de Agentes de IA:** Capas del agente (LLM, memoria dual, protocolo MCP, planificación ReAct, guardrails), patrones de orquestación (Supervisor/Router, Pipeline) y flujos *Human-in-the-Loop* con aprobación en Microsoft Teams.
13. **Evaluación Práctica para Champions:** Cuestionario de 8 situaciones operativas con retroalimentación técnica expandible.

---

## 🚀 Ejecución Local

### Prerrequisitos
* Python 3.10 o superior
* Instalar dependencias:
  ```bash
  pip install -r requirements.txt
  ```

### Iniciar la aplicación
* **En Windows:** Ejecutar con doble clic el archivo `iniciar_presentacion.bat` o desde la terminal:
  ```bash
  python -m streamlit run app_presentacion_ia.py
  ```
* La aplicación se abrirá automáticamente en `http://localhost:8501`.

---

## 🌐 Despliegue en la Nube

### Opción A: Vercel (Vía Stlite / WebAssembly)
Este repositorio incluye configuración nativa para **Vercel** (`index.html` + `vercel.json`). La aplicación corre 100% en el navegador del usuario utilizando WebAssembly/Pyodide sin necesidad de servidores backend persistentes.

### Opción B: Streamlit Community Cloud
1. Ingresa a [share.streamlit.io](https://share.streamlit.io/).
2. Conecta con tu cuenta de GitHub y selecciona el repositorio `EdwarGomez/formacion-brujula`.
3. Archivo principal: `app_presentacion_ia.py`.
4. Haz clic en **Deploy**.

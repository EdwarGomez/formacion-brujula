import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def build_workbook():
    wb = openpyxl.Workbook()
    # Remove default sheet
    wb.remove(wb.active)

    # Styles definition
    font_family = "Segoe UI"
    
    font_title = Font(name=font_family, size=15, bold=True, color="FFFFFF")
    font_subtitle = Font(name=font_family, size=10, italic=True, color="E2E8F0")
    font_section = Font(name=font_family, size=11, bold=True, color="1E293B")
    
    font_th_orig = Font(name=font_family, size=9, bold=True, color="FFFFFF")
    font_th_diag = Font(name=font_family, size=9, bold=True, color="FFFFFF")
    font_th_prop = Font(name=font_family, size=9, bold=True, color="FFFFFF")
    
    font_data = Font(name=font_family, size=9, color="1E293B")
    font_data_bold = Font(name=font_family, size=9, bold=True, color="1E293B")
    font_data_small = Font(name=font_family, size=8.5, color="334155")
    
    fill_header_navy = PatternFill(start_color="1B365D", end_color="1B365D", fill_type="solid")
    fill_orig_header = PatternFill(start_color="2B4C7E", end_color="2B4C7E", fill_type="solid")
    fill_diag_header = PatternFill(start_color="C05621", end_color="C05621", fill_type="solid")
    fill_prop_header = PatternFill(start_color="1E6B47", end_color="1E6B47", fill_type="solid")
    
    fill_phase1_badge = PatternFill(start_color="EBF8FF", end_color="EBF8FF", fill_type="solid")
    fill_phase2_badge = PatternFill(start_color="F0FFF4", end_color="F0FFF4", fill_type="solid")
    fill_diag_cell = PatternFill(start_color="FFFDF5", end_color="FFFDF5", fill_type="solid")
    fill_zebra_orig = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")
    fill_zebra_prop = PatternFill(start_color="F4FDF7", end_color="F4FDF7", fill_type="solid")
    
    thin_gray = Side(border_style="thin", color="CBD5E1")
    medium_navy = Side(border_style="medium", color="1B365D")
    double_bottom = Side(border_style="double", color="1B365D")
    
    border_cell = Border(left=thin_gray, right=thin_gray, top=thin_gray, bottom=thin_gray)
    border_total = Border(top=thin_gray, bottom=double_bottom, left=thin_gray, right=thin_gray)

    align_center = Alignment(horizontal="center", vertical="center", wrap_text=True)
    align_left = Alignment(horizontal="left", vertical="top", wrap_text=True)
    align_center_top = Alignment(horizontal="center", vertical="top", wrap_text=True)

    # ==========================================
    # DATA DEFINITIONS
    # ==========================================
    original_sessions = [
        {
            "num": 1, "fase": "Fase 1", "ruta": "R2 – Adopción",
            "titulo": "Fundamentos de IA Generativa para Líderes",
            "audiencia": "Champions + Líderes de Área",
            "h_dict": 2, "h_prep": 2, "h_tot": 4,
            "temario": "• Qué es y qué no es IA Generativa: modelos de lenguaje, foundation models, agentes autónomos.\n• Limitaciones reales de los LLMs: alucinaciones, actualización de conocimiento, privacidad.\n• Casos de uso reales en manufactura, logística y hotelería — referenciando los demos de Proyecto Brújula.\n• Marco de IA Responsable: Ley 1581 de 2012, riesgos, consentimiento y gobernanza.\n• Cómo evaluar si un proceso es candidato a automatización con IA (viabilidad × impacto).",
            "entregable": "Presentación ejecutiva, material de referencia y cuestionario de evaluación de casos candidatos por área."
        },
        {
            "num": 2, "fase": "Fase 1", "ruta": "R2 – Adopción",
            "titulo": "Taller Práctico de Prompting y Asistentes",
            "audiencia": "Champions + Líderes de Área",
            "h_dict": 2, "h_prep": 2, "h_tot": 4,
            "temario": "• Técnicas de prompting efectivo: zero-shot, few-shot, chain-of-thought, system prompts.\n• Framework CERO: Contexto, Especificidad, Rol, Output — con ejercicios en vivo.\n• Uso práctico de los agentes del Proyecto Brújula: Challenger (costos), Sky (CEDI), Habitel (eventos).\n• Buenas prácticas de interacción con asistentes conversacionales empresariales.\n• Errores comunes y cómo evitarlos — alucinaciones, prompt injection, sesgo.",
            "entregable": "Guía de prompts recomendados por caso de uso (Challenger, Sky, Habitel) + grabación de la sesión."
        },
        {
            "num": 3, "fase": "Fase 1", "ruta": "R4 – Refuerzo",
            "titulo": "Refuerzo Challenger + Sky",
            "audiencia": "Champions de Challenger y Grupo Sky",
            "h_dict": 2, "h_prep": 2, "h_tot": 4,
            "temario": "• [Challenger] Uso del agente de análisis de costos y gastos contables: consultas, filtros y drill-down por Centro de Costo.\n• [Challenger] Interpretación de resultados y detección de anomalías — comparativo presupuesto vs. real vs. año anterior.\n• [Challenger] Cómo escalar a nuevos reportes o reglas de negocio sin modificar código.\n• [Sky] Tablero conversacional WMS: consulta de KPIs (OTIF, IRA, ocupación volumétrica, muelles).\n• [Sky] Vista 3D del CEDI: navegación, filtros por bodega y exportación de resultados.\n• [Sky] Consultas avanzadas en lenguaje natural — ejemplos con datos reales de operación.",
            "entregable": "Manual de usuario por negocio (Challenger y Sky): guía de consultas frecuentes, interpretación y flujo de escalamiento."
        },
        {
            "num": 4, "fase": "Fase 1", "ruta": "R4 – Refuerzo",
            "titulo": "Refuerzo Habitel + Métricas de Adopción",
            "audiencia": "Champions de Habitel + Líderes del Programa",
            "h_dict": 2, "h_prep": 2, "h_tot": 4,
            "temario": "• [Habitel] Flujo completo del chatbot de cotización de eventos vía WhatsApp y web: captura, propuesta y PDF.\n• [Habitel] Flujo de aprobación ejecutiva vía Teams: umbrales, notificaciones, respuesta y seguimiento automático.\n• [Habitel] Manejo de excepciones: solicitudes fuera de catálogo, disponibilidad limitada, descuentos especiales.\n• Métricas de adopción del programa: usuarios activos, preguntas frecuentes, calidad de respuestas, valor generado.\n• Cómo identificar y escalar oportunidades de mejora desde el área al equipo de IA.",
            "entregable": "Manual de usuario Habitel + Dashboard de métricas de adopción (plantilla) + grabación de la sesión."
        },
        {
            "num": 5, "fase": "Fase 1", "ruta": "R2 – Adopción",
            "titulo": "Amazon Quick: Adopción y Dashboards Conversacionales",
            "audiencia": "Champions + Equipo TI",
            "h_dict": 2, "h_prep": 2, "h_tot": 4,
            "temario": "• Qué es Amazon Quick y cómo se diferencia de los agentes custom de Amazon Bedrock.\n• Espacios, datasets, topics y configuración de fuentes de datos en Quick.\n• Creación de dashboards conversacionales y preguntas en lenguaje natural sobre datos empresariales.\n• Gobernanza de acceso: RBAC (control por rol), Row-Level Security, perfiles de usuario y auditoría.\n• Casos de uso inmediatos en Grupo LEMCO: reportes financieros, KPIs de operación, consultas de documentos.",
            "entregable": "Configuración guiada de un Topic de Amazon Quick sobre una fuente de datos del grupo + grabación."
        },
        {
            "num": 6, "fase": "Fase 2", "ruta": "R3 – Entrega",
            "titulo": "Plataforma AWS, Seguridad y Gobernanza",
            "audiencia": "Equipo TI + Equipo IA",
            "h_dict": 2, "h_prep": 2, "h_tot": 4,
            "temario": "• Recorrido completo de la arquitectura en producción: servicios AWS por agente (Bedrock, Lambda, Fargate, S3, DynamoDB).\n• VPC, subnets, security groups, IAM roles y políticas de mínimo privilegio.\n• Gestión de identidad: Amazon Cognito, integración con Azure Entra ID (SSO/MFA), RBAC granular.\n• Control de acceso por rol y por negocio: cómo se segmenta la información entre Challenger, Sky y Habitel.\n• Infraestructura como código (IaC con CDK): despliegue, actualización y rollback de los stacks de producción.",
            "entregable": "Documento de arquitectura as-built (as-deployed) de los tres MVPs + diagrama de seguridad y RBAC."
        },
        {
            "num": 7, "fase": "Fase 2", "ruta": "R3 – Entrega",
            "titulo": "Runbooks Operativos, Monitoreo y FinOps",
            "audiencia": "Equipo TI + Equipo IA",
            "h_dict": 2, "h_prep": 2, "h_tot": 4,
            "temario": "• Runbook de operación diaria: monitoreo con CloudWatch, alertas configuradas, umbrales y respuesta a incidentes.\n• Escalamiento N1→N2→N3: proceso, canales de contacto, tiempos de respuesta (SLA < 2h para P1).\n• Actualización de modelos de Amazon Bedrock: validación, aprobación y cambio de versión sin downtime.\n• Re-indexación de Knowledge Bases: cuándo hacerla, cómo validar la calidad post-actualización.\n• FinOps: presupuestos y alertas de costos AWS, análisis de consumo por agente, optimización progresiva.",
            "entregable": "Runbook operativo completo documentado en repositorio Git + Dashboard de monitoreo y costos configurado."
        },
        {
            "num": 8, "fase": "Fase 2", "ruta": "R1 – Técnica",
            "titulo": "Amazon Bedrock: Modelos, API y Optimización",
            "audiencia": "Equipo IA + TI",
            "h_dict": 2, "h_prep": 2, "h_tot": 4,
            "temario": "• Arquitectura de Amazon Bedrock: APIs (InvokeModel, Converse), playground, SDKs y configuración de acceso.\n• Catálogo de modelos disponibles: Claude (Anthropic), Amazon Nova, Meta Llama, Mistral — diferencias y casos de uso.\n• Parámetros de inferencia: temperatura, top-p, max tokens — cómo afectan calidad, costo y latencia.\n• Estrategias de optimización de costos: batch inference (−50%), prompt caching (−90%), model routing automático.\n• Laboratorio: invocar modelos desde consola y código Python — comparar costos y latencias en vivo.",
            "entregable": "Notebook de laboratorio con ejemplos de invocación, comparativa de modelos y estrategias de optimización."
        },
        {
            "num": 9, "fase": "Fase 2", "ruta": "R1 – Técnica",
            "titulo": "Agentes, AgentCore y Protocolo MCP",
            "audiencia": "Equipo IA + TI",
            "h_dict": 2, "h_prep": 2, "h_tot": 4,
            "temario": "• Amazon Bedrock Agents y AgentCore Runtime: orquestación, memoria, observabilidad e identidad.\n• Ciclo Sense-Plan-Act-Loop: cómo el agente razona, planifica y ejecuta herramientas.\n• Protocolo MCP (Model Context Protocol): transportes stdio y HTTP+SSE, servidores, clientes, capacidades y arnés.\n• Patrones de orquestación: multi-agente con supervisor/router, Human-in-the-Loop, Tool Calling y return of control.\n• Laboratorio: recorrido técnico del agente Challenger de producción — arquitectura, tools y flujo de ejecución.",
            "entregable": "Diagrama de arquitectura de agentes actualizado + guía de patrones MCP para el equipo de desarrollo."
        },
        {
            "num": 10, "fase": "Fase 2", "ruta": "R1 – Técnica",
            "titulo": "RAG, Knowledge Bases y Guardrails",
            "audiencia": "Equipo IA + TI",
            "h_dict": 2, "h_prep": 2, "h_tot": 4,
            "temario": "• Retrieval Augmented Generation (RAG): arquitectura, pipeline de indexación y consulta, evaluación de relevancia.\n• Amazon Bedrock Knowledge Bases: ingesta, chunking, embeddings (Titan, Cohere), almacenes vectoriales (S3 Vectors, Aurora pgvector).\n• Estrategias de reranking y evaluación de calidad de recuperación — métricas y umbrales prácticos.\n• Amazon Bedrock Guardrails: filtros de contenido, topic denial, PII detection, contextual grounding, anti-prompt injection.\n• Laboratorio: configurar una Knowledge Base con documentación interna del grupo — validación de calidad en vivo.",
            "entregable": "Knowledge Base de referencia configurada + política de Guardrails documentada por agente."
        },
        {
            "num": 11, "fase": "Fase 2", "ruta": "R1 – Técnica",
            "titulo": "Kiro: IDE de IA y Desarrollo de Agentes",
            "audiencia": "Equipo IA + TI",
            "h_dict": 2, "h_prep": 2, "h_tot": 4,
            "temario": "• Introducción a Kiro IDE: spec-driven development, hooks, steering y flujos de trabajo con IA integrada.\n• Cómo el equipo de CNID usó Kiro para construir los demos del Proyecto Brújula — caso de estudio real.\n• Configuración de Kiro con acceso a Amazon Bedrock: modelos, conexiones y personalización.\n• Construcción de un agente simple en Kiro: del spec al código funcional en tiempo real.\n• Integración de Kiro en el ciclo de desarrollo del CoE de IA de Grupo LEMCO: estándares, revisión y control de versiones.",
            "entregable": "Entorno Kiro configurado para el equipo de IA de Grupo LEMCO + guía de inicio y estándares de desarrollo."
        }
    ]

    diagnostics = [
        "Innecesaria para el perfil: Los Champions ya cursan la formación con la EAN. Además, la instalación no debe consumir horas de clase; se asume como prerrequisito institucional previo por parte de TI LEMCO.\n\nAjuste: Reemplazar por Manejo de Espacios (Spaces) y Formación del 'Cerebro' de Conocimiento en Amazon Quick.",
        "Genérica y desalineada del uso operativo directo: El prompting abstracto no enseña a cruzar fuentes ni a estructurar investigación profunda de documentos.\n\nAjuste: Reemplazar por Capacidades de Investigación y Síntesis Profunda de Información (exploración documental, contraste y citas).",
        "Refuerzo aislado sin explotación de BI: Presentar el demo de forma pasiva no transfiere la capacidad de hacer analítica aumentada sobre datos corporativos.\n\nAjuste: Reemplazar por Capacidades de BI (Business Intelligence) y Analítica Aumentada con IA para Challenger (costos) y Sky (CEDI/WMS).",
        "Revisión limitada de un chatbot externo: La sesión 4 original auditaba un bot en Teams sin transferir la habilidad de crear y parametrizar agentes propios.\n\nAjuste: Reemplazar por Creación y Parametrización de Agentes Personalizados y Especializados a la medida (Habitel y áreas de apoyo).",
        "Tratamiento tardío y sin integración de gobierno: En el PDF original, Quick se trataba solo al final con sesgo a dashboards web simples.\n\nAjuste: Consolidar la Gobernanza integral de Espacios, Agentes Personalizados, Políticas RBAC y actualización continua del 'Cerebro'.",
        "Base necesaria pero desconectada de la práctica de desarrollo: La sesión original era puramente expositiva sobre la consola AWS.\n\nAjuste: Mantener la sesión de arquitectura, seguridad y gobernanza como cimiento previo obligatorio para la Fase 2 técnica.",
        "Ops fragmentada del ciclo de desarrollo: Se enseñaba monitoreo en CloudWatch antes de ver cómo se desarrollan los agentes.\n\nAjuste: Mover Runbooks y FinOps al cierre (Sesión 11) como ciclo de vida completo, e introducir Kiro de inmediato en la Sesión 7.",
        "Enfoque de consola y SDK aislado: Se explicaba Bedrock de manera teórica sin un entorno de ingeniería agéntica estructurado.\n\nAjuste: Conectar Kiro IDE directamente a los modelos de Bedrock (Claude, Nova, Llama) para desarrollo y optimización de costos en vivo.",
        "Conceptos abstractos de MCP y agentes: La sesión original mostraba el protocolo MCP en diapositivas y un recorrido de solo lectura.\n\nAjuste: Construir y depurar en Kiro servidores MCP funcionales conectados a bases de datos y APIs de las empresas de Grupo LEMCO.",
        "RAG configurado solo desde consola AWS: Falta de integración entre la base de conocimiento y el flujo de desarrollo de código.\n\nAjuste: Desarrollar la indexación vectorial y las políticas de Guardrails probando la recuperación y evasión directamente desde Kiro.",
        "Kiro relegado a demo final: Presentar Kiro al final no permitía usarlo durante las sesiones de Bedrock, MCP ni RAG.\n\nAjuste: Convertir la última sesión en la integración operativa completa: del spec en Kiro al despliegue en AWS con CDK, monitoreo y soporte."
    ]

    proposed_sessions = [
        {
            "num": 1, "fase": "Fase 1", "ruta": "Ruta Quick – Espacios & Contexto",
            "titulo": "Manejo de Espacios (Spaces) y Formación del 'Cerebro' de Conocimiento en Amazon Quick",
            "audiencia": "Champions + Líderes de Área (+ Soporte TI)",
            "h_dict": 2, "h_prep": 2, "h_tot": 4,
            "temario": "• [Prerrequisito cumplido]: Cliente Amazon Quick Desktop previamente instalado y autenticado por TI de Grupo LEMCO.\n• Manejo de Espacios (Spaces): organización, estructuración y particionamiento de los entornos de trabajo por área operativa.\n• Formación del 'cerebro' de conocimiento: carga, jerarquización e indexación de fuentes documentales y repositorios locales.\n• Estructuración del contexto empresarial para alimentar las respuestas del asistente según perfiles de usuario.\n• Interrogación contextual inicial: validación de la base de conocimiento cargada frente a consultas de procesos de negocio.",
            "entregable": "Estructura de Espacios (Spaces) configurada por unidad de negocio + Primer repositorio de conocimiento ('cerebro') indexado y validado."
        },
        {
            "num": 2, "fase": "Fase 1", "ruta": "Ruta Quick – Investigación",
            "titulo": "Capacidades de Investigación y Síntesis Profunda de Información en Amazon Quick",
            "audiencia": "Champions + Líderes de Área",
            "h_dict": 2, "h_prep": 2, "h_tot": 4,
            "temario": "• Capacidades de investigación: funcionalidades enfocadas en exploración documental extensiva y búsqueda semántica profunda.\n• Síntesis profunda de información: contraste analítico entre múltiples documentos (contratos, políticas, fichas técnicas de producto).\n• Detección de inconsistencias, variaciones normativas y vacíos de información en expedientes complejos.\n• Trazabilidad y citas de evidencia: verificación del origen de cada conclusión emitida por la herramienta para respaldo operativo.\n• Generación de entregables estructurados: redacción de informes analíticos, minutas técnicas y resúmenes ejecutivos.",
            "entregable": "Dossier de investigación operativa ejecutado en Quick sobre documentación corporativa real, con citas y respaldo de evidencia."
        },
        {
            "num": 3, "fase": "Fase 1", "ruta": "Ruta Quick – Business Intelligence",
            "titulo": "Capacidades de BI (Business Intelligence) y Analítica Aumentada: Casos Challenger y Sky",
            "audiencia": "Champions de Challenger y Sky (+ TI)",
            "h_dict": 2, "h_prep": 2, "h_tot": 4,
            "temario": "• Capacidades de BI (Business Intelligence): uso de funciones analíticas y de reportería integradas con IA en Amazon Quick.\n• Consultas analíticas en lenguaje natural sobre datos estructurados (archivos Excel, reportes CSV y bases operativas).\n• [Challenger] BI para manufactura: análisis de variaciones de costos y gastos por Centro de Costo, tendencias y márgenes.\n• [Sky] BI logístico: interrogación interactiva de KPIs de CEDI (OTIF, IRA, tiempos de ciclo de muelles y ocupación volumétrica).\n• Visualización analítica y exportación de tablas dinámicas con filtros automáticos generados por la IA.",
            "entregable": "Catálogo de consultas de BI en lenguaje natural validadas sobre datos de Challenger y Sky + Tablero analítico funcional."
        },
        {
            "num": 4, "fase": "Fase 1", "ruta": "Ruta Quick – Agentes Personalizados",
            "titulo": "Creación y Parametrización de Agentes Personalizados y Especializados: Casos Habitel y Áreas",
            "audiencia": "Champions de Habitel + Líderes de Área",
            "h_dict": 2, "h_prep": 2, "h_tot": 4,
            "temario": "• Creación de agentes personalizados y especializados: configuración y parametrización de asistentes a la medida del negocio.\n• Definición de directrices de rol (system prompts), tono comunicativo, umbrales de decisión y restricciones de alcance.\n• [Habitel] Configuración del agente especializado en cotizaciones de eventos: cálculo de tarifas, disponibilidad y redacción de propuestas.\n• [Áreas de soporte] Creación de asistentes especializados para procesos internos (e.g. compras, gestión humana, auditoría).\n• Pruebas de validación operativa: ajuste de instrucciones ante solicitudes no estándar y excepciones comerciales.",
            "entregable": "Agente personalizado y especializado configurado en Amazon Quick para eventos de Habitel (y micro-agente de área) con ficha técnica."
        },
        {
            "num": 5, "fase": "Fase 1", "ruta": "Ruta Quick – Gobernanza",
            "titulo": "Gobierno de Espacios, Seguridad (RBAC) y Despliegue de Agentes Especializados",
            "audiencia": "Champions + Líderes de Área + TI",
            "h_dict": 2, "h_prep": 2, "h_tot": 4,
            "temario": "• Administración centralizada del ecosistema: gobernanza de Espacios (Spaces), Topics y Agentes especializados en Grupo LEMCO.\n• Control de acceso basado en roles (RBAC) y segmentación estricta de información sensible entre Challenger, Sky y Habitel.\n• Cumplimiento normativo y seguridad de la información: aplicación de la Ley 1581 de 2012 y directrices corporativas de datos.\n• Mantenimiento del 'cerebro' de conocimiento: métricas de uso, detección de vacíos de información y ciclo de actualización del contexto.\n• Procedimiento formal de escalamiento de nuevos requerimientos de conectores o agentes complejos hacia el CoE de IA / TI.",
            "entregable": "Matriz de gobierno de Espacios y Agentes especializados por negocio + Protocolo de actualización del 'cerebro' y escalamiento a TI."
        },
        {
            "num": 6, "fase": "Fase 2", "ruta": "Ruta Técnica – AWS",
            "titulo": "Arquitectura AWS Desplegada, Seguridad y Gobernanza de Identidad",
            "audiencia": "Equipo TI + Equipo IA",
            "h_dict": 2, "h_prep": 2, "h_tot": 4,
            "temario": "• Topología en producción de Proyecto Brújula: Bedrock, Lambda, Fargate, S3, DynamoDB y API Gateway.\n• Seguridad perimetral: arquitectura VPC, subredes privadas, Security Groups y endpoints privados (VPC Endpoints).\n• Gestión de identidad federada: Amazon Cognito integrado con Microsoft Entra ID (SSO / MFA) y RBAC granular.\n• Control de acceso y políticas IAM de mínimo privilegio para aislamiento estricto de datos entre empresas de LEMCO.\n• Infraestructura como Código (IaC con AWS CDK): estructura de stacks, ciclo de despliegue y procedimientos de rollback.",
            "entregable": "Diagrama de arquitectura as-built verificado + Matriz de roles IAM y políticas de segmentación multi-empresa."
        },
        {
            "num": 7, "fase": "Fase 2", "ruta": "Ruta Técnica – Kiro",
            "titulo": "Kiro: Ingeniería Agéntica y Desarrollo Basado en Especificaciones (Spec-Driven)",
            "audiencia": "Equipo IA + TI",
            "h_dict": 2, "h_prep": 2, "h_tot": 4,
            "temario": "• Arquitectura del ecosistema Kiro: Kiro IDE, Kiro CLI, Kiro Web y sincronización multi-entorno.\n• Metodología Spec-Driven Development: descomposición estructurada en requerimientos, diseño técnico y plan de tareas (.kiro/specs/).\n• Definición de Steering Rules corporativas (.kiro/steering/) para garantizar estándares de código, seguridad y arquitectura en Grupo LEMCO.\n• Automatización mediante Agent Hooks: triggers programados ante eventos de guardado de archivos, commits o pruebas unitarias.\n• Configuración del workspace de desarrollo y migración de proyectos existentes hacia Kiro.",
            "entregable": "Workspace de desarrollo Kiro configurado con steering rules corporativas + Spec formal completo para un micro-agente."
        },
        {
            "num": 8, "fase": "Fase 2", "ruta": "Ruta Técnica – Bedrock & Kiro",
            "titulo": "Amazon Bedrock Integrado con Kiro: Modelos, Invocación y Optimización",
            "audiencia": "Equipo IA + TI",
            "h_dict": 2, "h_prep": 2, "h_tot": 4,
            "temario": "• Conexión de Kiro con Amazon Bedrock mediante perfiles AWS y credenciales seguras de desarrollo.\n• Catálogo de foundation models de punta: Claude Sonnet 5.5, GPT-6.1 (Sol), Gemini 4 (Argon), Amazon Nova, Llama 4 — criterios de selección por costo, latencia y capacidad analítica.\n• Invocación programática en Python usando SDK de AWS (APIs InvokeModel y Converse) guiada desde Kiro.\n• Configuración y ajuste de hiperparámetros de inferencia (temperatura, top-p, stop sequences, max tokens).\n• Estrategias de FinOps técnico: prompt caching (−90% costo en llamadas recurrentes), batch inference (−50%) y ruteo automático de modelos.",
            "entregable": "Suite de benchmarking de modelos y costos en Bedrock desarrollada y validada directamente desde Kiro."
        },
        {
            "num": 9, "fase": "Fase 2", "ruta": "Ruta Técnica – MCP & Agentes",
            "titulo": "Desarrollo de Agentes y Servidores MCP (Model Context Protocol) en Kiro",
            "audiencia": "Equipo IA + TI",
            "h_dict": 2, "h_prep": 2, "h_tot": 4,
            "temario": "• Arquitectura y especificación del protocolo MCP (Model Context Protocol): servidores, clientes, tools, resources y prompts.\n• Transportes de comunicación MCP: stdio para integración local y HTTP+SSE para microservicios y despliegue distribuido.\n• Construcción paso a paso de un servidor MCP en Python/TypeScript para conectar agentes a bases de datos y APIs internas de LEMCO.\n• Patrones de diseño agéntico: bucle Sense-Plan-Act, orquestación supervisor-trabajador y control humano en el ciclo (Human-in-the-Loop).\n• Integración de herramientas MCP con Amazon Bedrock Agents y AgentCore Runtime.",
            "entregable": "Servidor MCP funcional construido en Kiro con tools corporativas + Agente de prueba con ejecución de herramientas validada."
        },
        {
            "num": 10, "fase": "Fase 2", "ruta": "Ruta Técnica – RAG & Seguridad",
            "titulo": "RAG Avanzado, Knowledge Bases en Bedrock y Guardrails de Seguridad",
            "audiencia": "Equipo IA + TI",
            "h_dict": 2, "h_prep": 2, "h_tot": 4,
            "temario": "• Arquitectura RAG empresarial: pipeline de ingesta documental, estrategias de chunking y embeddings (Titan / Cohere).\n• Implementación de Amazon Bedrock Knowledge Bases con almacenes vectoriales (OpenSearch Serverless / S3 / pgvector).\n• Reranking contextual y métricas cuantitativas para evaluar la relevancia y fidelidad de las respuestas generadas.\n• Amazon Bedrock Guardrails: filtros de contenido, bloqueo de temas restringidos, enmascaramiento de PII y mitigación de inyección de prompts.\n• Ejecución de pruebas de penetración, validación de sesgo y baterías de evaluación automatizadas desde Kiro CLI.",
            "entregable": "Knowledge Base indexada con documentación interna de Grupo LEMCO + Política de Guardrails testeada y activa."
        },
        {
            "num": 11, "fase": "Fase 2", "ruta": "Ruta Técnica – DevOps & Ops",
            "titulo": "Ciclo de Vida Operativo: Despliegue de Agentes, Runbooks, Monitoreo y FinOps",
            "audiencia": "Equipo TI + Equipo IA",
            "h_dict": 2, "h_prep": 2, "h_tot": 4,
            "temario": "• Flujo integral de ingeniería agéntica: del spec y código en Kiro al empaquetamiento y despliegue en AWS con CDK / CI-CD.\n• Observabilidad operativa con Amazon CloudWatch: paneles de telemetría, métricas de latencia, tasa de error y consumo de tokens.\n• Protocolo formal de soporte operativo N1→N2→N3: clasificación de severidad de incidentes y SLAs de respuesta (P1 < 2 horas).\n• Mantenimiento continuo: procedimiento de re-indexación de Knowledge Bases y actualización de modelos sin indisponibilidad.\n• Gestión presupuestal FinOps: configuración de AWS Budgets, alarmas de umbral de gasto y optimización continua de costos por agente.",
            "entregable": "Runbook operativo integral documentado en Git (ciclo Kiro → CDK → CloudWatch) + Dashboard de alertas de incidentes y FinOps."
        }
    ]

    # ==========================================
    # SHEET 1: COMPARATIVO SESIÓN A SESIÓN (AL FRENTE)
    # ==========================================
    ws1 = wb.create_sheet(title="Comparativo_Sesion_a_Sesion")
    ws1.views.sheetView[0].showGridLines = True

    # Title Block
    ws1.merge_cells("A1:O1")
    title_cell = ws1["A1"]
    title_cell.value = "MATRIZ COMPARATIVA DE TRANSFERENCIA DE CONOCIMIENTO — PROYECTO BRÚJULA IA"
    title_cell.font = font_title
    title_cell.fill = fill_header_navy
    title_cell.alignment = align_center
    ws1.row_dimensions[1].height = 36

    ws1.merge_cells("A2:O2")
    sub_cell = ws1["A2"]
    sub_cell.value = "Alineación Estratégica: Propuesta Original del Proveedor (PDF) vs. Propuesta Ajustada (Amazon Quick Desktop & Kiro IDE) · 11 Sesiones · 44 Horas Totales (22h Dictadas + 22h Preparación)"
    sub_cell.font = font_subtitle
    sub_cell.fill = fill_header_navy
    sub_cell.alignment = align_center
    ws1.row_dimensions[2].height = 22

    # Super-headers in Row 4
    ws1.merge_cells("A4:B4")
    ws1["A4"].value = "IDENTIFICADOR"
    ws1["A4"].fill = PatternFill(start_color="0F172A", end_color="0F172A", fill_type="solid")
    ws1["A4"].font = font_th_orig
    ws1["A4"].alignment = align_center

    ws1.merge_cells("C4:H4")
    ws1["C4"].value = "PROPUESTA ORIGINAL (PDF ACTUAL DEL PROVEEDOR CNID)"
    ws1["C4"].fill = fill_orig_header
    ws1["C4"].font = font_th_orig
    ws1["C4"].alignment = align_center

    ws1.merge_cells("I4:I4")
    ws1["I4"].value = "DIAGNÓSTICO Y BRECHA"
    ws1["I4"].fill = fill_diag_header
    ws1["I4"].font = font_th_diag
    ws1["I4"].alignment = align_center

    ws1.merge_cells("J4:O4")
    ws1["J4"].value = "PROPUESTA AJUSTADA (ENFOQUE AMAZON QUICK DESKTOP + KIRO IDE)"
    ws1["J4"].fill = fill_prop_header
    ws1["J4"].font = font_th_prop
    ws1["J4"].alignment = align_center
    ws1.row_dimensions[4].height = 24

    # Column Headers in Row 5
    headers_s1 = [
        ("N°", 5),
        ("Fase", 9),
        # Original
        ("Ruta Original", 14),
        ("Título de Sesión Original", 26),
        ("Audiencia Original", 18),
        ("Horas Orig. (Dict+Prep=Tot)", 14),
        ("Temario y Alcance Original (PDF)", 38),
        ("Entregable Original", 22),
        # Diagnóstico
        ("Motivo de Ajuste / Brecha Detectada", 28),
        # Propuesta
        ("Ruta Propuesta", 16),
        ("Título de Sesión Propuesto", 30),
        ("Audiencia Propuesta", 20),
        ("Horas Prop. (Dict+Prep=Tot)", 14),
        ("Temario y Alcance Práctico Propuesto", 44),
        ("Entregable Tangible Propuesto", 26)
    ]

    for col_idx, (h_name, width) in enumerate(headers_s1, start=1):
        cell = ws1.cell(row=5, column=col_idx, value=h_name)
        cell.alignment = align_center
        col_letter = get_column_letter(col_idx)
        ws1.column_dimensions[col_letter].width = width
        
        if col_idx in [1, 2]:
            cell.fill = PatternFill(start_color="1E293B", end_color="1E293B", fill_type="solid")
            cell.font = font_th_orig
        elif 3 <= col_idx <= 8:
            cell.fill = fill_orig_header
            cell.font = font_th_orig
        elif col_idx == 9:
            cell.fill = fill_diag_header
            cell.font = font_th_diag
        else:
            cell.fill = fill_prop_header
            cell.font = font_th_prop
    ws1.row_dimensions[5].height = 28

    # Populate Rows (Rows 6 to 16)
    for idx in range(11):
        row_num = 6 + idx
        orig = original_sessions[idx]
        diag = diagnostics[idx]
        prop = proposed_sessions[idx]
        
        ws1.cell(row=row_num, column=1, value=orig["num"]).alignment = align_center_top
        ws1.cell(row=row_num, column=1).font = font_data_bold
        
        fase_cell = ws1.cell(row=row_num, column=2, value=orig["fase"])
        fase_cell.alignment = align_center_top
        fase_cell.font = font_data_bold
        fase_cell.fill = fill_phase1_badge if "1" in orig["fase"] else fill_phase2_badge

        # Original Block
        ws1.cell(row=row_num, column=3, value=orig["ruta"]).alignment = align_center_top
        ws1.cell(row=row_num, column=4, value=orig["titulo"]).alignment = align_left
        ws1.cell(row=row_num, column=4).font = font_data_bold
        ws1.cell(row=row_num, column=5, value=orig["audiencia"]).alignment = align_left
        ws1.cell(row=row_num, column=6, value=f"{orig['h_dict']}h dict + {orig['h_prep']}h prep\n= {orig['h_tot']}h tot").alignment = align_center_top
        ws1.cell(row=row_num, column=7, value=orig["temario"]).alignment = align_left
        ws1.cell(row=row_num, column=8, value=orig["entregable"]).alignment = align_left
        
        # Diagnosis Block
        diag_cell = ws1.cell(row=row_num, column=9, value=diag)
        diag_cell.alignment = align_left
        diag_cell.fill = fill_diag_cell
        diag_cell.font = font_data_small

        # Proposed Block
        ws1.cell(row=row_num, column=10, value=prop["ruta"]).alignment = align_center_top
        ws1.cell(row=row_num, column=11, value=prop["titulo"]).alignment = align_left
        ws1.cell(row=row_num, column=11).font = font_data_bold
        ws1.cell(row=row_num, column=12, value=prop["audiencia"]).alignment = align_left
        ws1.cell(row=row_num, column=13, value=f"{prop['h_dict']}h dict + {prop['h_prep']}h prep\n= {prop['h_tot']}h tot").alignment = align_center_top
        ws1.cell(row=row_num, column=14, value=prop["temario"]).alignment = align_left
        ws1.cell(row=row_num, column=15, value=prop["entregable"]).alignment = align_left
        
        # Zebra striping and borders
        is_even = (idx % 2 == 0)
        for c_idx in range(1, 16):
            c_cell = ws1.cell(row=row_num, column=c_idx)
            c_cell.border = border_cell
            if 3 <= c_idx <= 8 and is_even:
                c_cell.fill = fill_zebra_orig
            elif 10 <= c_idx <= 15 and is_even:
                c_cell.fill = fill_zebra_prop
        
        ws1.row_dimensions[row_num].height = 120

    # Totals Row (Row 17)
    tot_row = 17
    ws1.cell(row=tot_row, column=1, value="TOTAL").alignment = align_center
    ws1.cell(row=tot_row, column=1).font = font_data_bold
    ws1.cell(row=tot_row, column=2, value="11 Sesiones").alignment = align_center
    ws1.cell(row=tot_row, column=2).font = font_data_bold
    
    ws1.cell(row=tot_row, column=3, value="4 Rutas Orig.").alignment = align_center
    ws1.cell(row=tot_row, column=3).font = font_data_bold
    ws1.cell(row=tot_row, column=4, value="Programa Original Base (PDF)").font = font_data_bold
    ws1.cell(row=tot_row, column=5, value="Champions + TI").font = font_data_bold
    ws1.cell(row=tot_row, column=6, value="22h dict + 22h prep\n= 44h total").alignment = align_center
    ws1.cell(row=tot_row, column=6).font = font_data_bold
    ws1.cell(row=tot_row, column=7, value="5 sesiones Fase 1 (Adopción) + 6 sesiones Fase 2 (Técnica)").font = font_data_bold
    ws1.cell(row=tot_row, column=8, value="11 Entregables base").font = font_data_bold
    
    ws1.cell(row=tot_row, column=9, value="Balance Contractual 100%").alignment = align_center
    ws1.cell(row=tot_row, column=9).font = font_data_bold
    ws1.cell(row=tot_row, column=9).fill = fill_diag_cell

    ws1.cell(row=tot_row, column=10, value="5 Rutas Ajust.").alignment = align_center
    ws1.cell(row=tot_row, column=10).font = font_data_bold
    ws1.cell(row=tot_row, column=11, value="Programa Ajustado (Quick Spaces/BI/Agentes + Kiro)").font = font_data_bold
    ws1.cell(row=tot_row, column=12, value="Champions + CoE IA + TI").font = font_data_bold
    ws1.cell(row=tot_row, column=13, value="22h dict + 22h prep\n= 44h total").alignment = align_center
    ws1.cell(row=tot_row, column=13).font = font_data_bold
    ws1.cell(row=tot_row, column=14, value="5 sesiones Quick (Spaces, Cerebro, Investigación, BI, Agentes) + 6 sesiones Kiro/Bedrock/MCP").font = font_data_bold
    ws1.cell(row=tot_row, column=15, value="11 Entregables operativos").font = font_data_bold

    for c_idx in range(1, 16):
        c_cell = ws1.cell(row=tot_row, column=c_idx)
        c_cell.border = border_total
        if c_idx in [1, 2, 6, 13]:
            c_cell.fill = PatternFill(start_color="E2E8F0", end_color="E2E8F0", fill_type="solid")
    ws1.row_dimensions[tot_row].height = 32

    # Freeze Panes below headers
    ws1.freeze_panes = "C6"

    # ==========================================
    # SHEET 2: RESUMEN EJECUTIVO Y PARÁMETROS
    # ==========================================
    ws2 = wb.create_sheet(title="Resumen_Ejecutivo")
    ws2.views.sheetView[0].showGridLines = True

    ws2.merge_cells("A1:G1")
    t2 = ws2["A1"]
    t2.value = "RESUMEN EJECUTIVO Y CONDICIONES DEL PLAN DE TRANSFERENCIA — PROYECTO BRÚJULA"
    t2.font = font_title
    t2.fill = fill_header_navy
    t2.alignment = align_center
    ws2.row_dimensions[1].height = 36

    ws2.merge_cells("A2:G2")
    s2 = ws2["A2"]
    s2.value = "Justificación de Negocio, Cumplimiento de Restricciones Horarias y Matriz de Transformación Curricular"
    s2.font = font_subtitle
    s2.fill = fill_header_navy
    s2.alignment = align_center
    ws2.row_dimensions[2].height = 20

    # Section 1: Parameters Card
    ws2.merge_cells("A4:G4")
    ws2["A4"].value = "1. PARÁMETROS Y RESTRICCIONES CONTRACTUALES VIGENTES"
    ws2["A4"].font = font_section
    ws2["A4"].fill = PatternFill(start_color="E2E8F0", end_color="E2E8F0", fill_type="solid")
    ws2.row_dimensions[4].height = 24

    params_data = [
        ("Proyecto y Referencia", "Proyecto Brújula — RFP-BRUJULA-IA-2026-001 (Anexo Plan de Transferencia de Conocimiento)"),
        ("Entidad Beneficiaria", "Grupo LEMCO (Challenger S.A.S, Grupo Sky, Hotel Habitel)"),
        ("Proveedor Responsable", "CNID (AWS Partner) — Perfil Cloud Architect"),
        ("Modelo Contractual", "Valor Agregado (Compromiso del RFP a costo COP $0 para Grupo LEMCO — Tarifa base $320,000/h)"),
        ("Presupuesto Máximo Autorizado", "44 Horas Totales (22 Horas Dictadas en 11 Sesiones de 2 horas + 22 Horas de Preparación)"),
        ("Estructura por Sesión", "2 Horas de dictado sincrónico + 2 Horas de preparación equivalente = 4 Horas totales por sesión"),
        ("Prerrequisito de Instalación", "La instalación y autenticación inicial de Amazon Quick Desktop es asumida previamente por TI de Grupo LEMCO, liberando tiempo pedagógico para explotación analítica directa."),
        ("Franja Horaria Establecida", "Lunes, Miércoles y Viernes de 3:00 PM a 6:00 PM (COT)"),
        ("Pausa de Diciembre 2026", "Mes de diciembre libre de formación formal para foco total en paso de MVPs a producción"),
        ("Vouchers de Certificación", "17 Vouchers para certificación AWS Certified AI Practitioner (AIF-C01) incluidos como Valor Agregado")
    ]

    for p_idx, (k, v) in enumerate(params_data, start=5):
        ws2.cell(row=p_idx, column=1, value=k).font = font_data_bold
        ws2.cell(row=p_idx, column=1).alignment = align_left
        ws2.merge_cells(start_row=p_idx, start_column=2, end_row=p_idx, end_column=7)
        ws2.cell(row=p_idx, column=2, value=v).font = font_data
        ws2.cell(row=p_idx, column=2).alignment = align_left
        ws2.row_dimensions[p_idx].height = 22
        for c in range(1, 8):
            ws2.cell(row=p_idx, column=c).border = border_cell

    # Section 2: Core Transformation Matrix
    r_start = 16
    ws2.merge_cells(f"A{r_start}:G{r_start}")
    ws2[f"A{r_start}"].value = "2. MATRIZ DE TRANSFORMACIÓN CURRICULAR: DIAGNÓSTICO VS. SOLUCIÓN"
    ws2[f"A{r_start}"].font = font_section
    ws2[f"A{r_start}"].fill = PatternFill(start_color="E2E8F0", end_color="E2E8F0", fill_type="solid")
    ws2.row_dimensions[r_start].height = 24

    r_h = r_start + 1
    ws2.merge_cells(f"B{r_h}:C{r_h}")
    ws2.merge_cells(f"E{r_h}:F{r_h}")

    ws2.cell(row=r_h, column=1, value="Dimensión / Eje").alignment = align_center
    ws2.cell(row=r_h, column=1).fill = fill_header_navy
    ws2.cell(row=r_h, column=1).font = font_th_orig

    ws2.cell(row=r_h, column=2, value="Propuesta Original (PDF CNID)").alignment = align_center
    ws2.cell(row=r_h, column=2).fill = fill_orig_header
    ws2.cell(row=r_h, column=2).font = font_th_orig

    ws2.cell(row=r_h, column=4, value="Brecha Operativa Identificada").alignment = align_center
    ws2.cell(row=r_h, column=4).fill = fill_diag_header
    ws2.cell(row=r_h, column=4).font = font_th_diag

    ws2.cell(row=r_h, column=5, value="Propuesta Ajustada (Grupo LEMCO)").alignment = align_center
    ws2.cell(row=r_h, column=5).fill = fill_prop_header
    ws2.cell(row=r_h, column=5).font = font_th_prop

    ws2.cell(row=r_h, column=7, value="Impacto y Beneficio Concreto").alignment = align_center
    ws2.cell(row=r_h, column=7).fill = fill_header_navy
    ws2.cell(row=r_h, column=7).font = font_th_orig
    ws2.row_dimensions[r_h].height = 26

    transformation_rows = [
        (
            "Manejo de Espacios y 'Cerebro' de Conocimiento",
            "La propuesta original iniciaba con conceptos abstractos de IA y prompting genérico (Sesiones 1 y 2), postergando Quick al final.",
            "Los Champions ya cursaron formación con la EAN. Dedicar tiempo a teoría o instalaciones básicas resta horas a la estructuración de la información corporativa.",
            "Sesión 1 dedicada por completo a la estructuración de Espacios (Spaces) y formación del 'cerebro' de conocimiento (contexto documental y reglas de negocio).",
            "Los equipos organizan sus espacios por unidad operativa y alimentan el asistente con información real de procesos desde el primer día."
        ),
        (
            "Capacidades de Investigación Profunda",
            "Taller de prompting genérico centrado en fórmulas lingüísticas (CERO) sin contraste de documentos reales.",
            "Los usuarios no aprenden a contrastar expedientes complejos ni a auditar la trazabilidad de las fuentes generadas por la herramienta.",
            "Sesión 2 enfocada en exploración semántica, síntesis profunda, detección de discrepancias y respaldo mediante citas de evidencia.",
            "Rigor analítico: redacción de informes técnicos y minutas operativas con sustento documental explícito para auditoría interna."
        ),
        (
            "Capacidades de BI (Business Intelligence)",
            "Sesión 3 de refuerzo con demostraciones guiadas pasivas de los tres MVPs, desconectadas de las capacidades analíticas de Quick.",
            "El usuario observa cómo funciona el modelo del proveedor pero no aprende a generar consultas de reportería ni dashboards analíticos.",
            "Sesión 3 enfocada en Business Intelligence aumentado con IA: análisis de costos (Challenger) e indicadores de CEDI/WMS (Sky) sobre archivos estructurados.",
            "Autonomía analítica: los Champions interrogan variaciones de centros de costo e indicadores logísticos (OTIF/IRA) en lenguaje natural."
        ),
        (
            "Creación de Agentes Personalizados",
            "Sesión 4 limitada a auditar las conversaciones del bot de cotización de eventos de Habitel en WhatsApp y Teams.",
            "No transfiere el conocimiento para parametrizar nuevos asistentes ni ajustar las instrucciones del sistema según las reglas de cada área.",
            "Sesión 4 dedicada a la creación, parametrización y puesta a punto de agentes especializados en Quick (cotizaciones Habitel y procesos departamentales).",
            "Capacidad interna instalada: las áreas configuran y afinan sus propios asistentes especializados con directrices y límites operativos precisos."
        ),
        (
            "Kiro y Desarrollo Agéntico (Fase 2)",
            "Kiro relegado a una sesión final (Sesión 11) como demo informativa, mientras Bedrock, MCP y RAG se enseñaban de forma abstracta en consola.",
            "El equipo de TI e IA no puede apropiar la ingeniería agéntica si el entorno de desarrollo se presenta como una charla final.",
            "Kiro se posiciona como el entorno metodológico central desde la Sesión 7 (Spec-Driven, Steering Rules, Hooks) para programar Bedrock, MCPs y RAG.",
            "Estandarización técnica: el CoE de IA produce código versionado, con especificaciones formales y conectores corporativos reutilizables."
        ),
        (
            "Transferencia Técnica y MCP",
            "Sesión 9 expositiva sobre conceptos de orquestación y recorrido de solo lectura del agente Challenger.",
            "Dependencia técnica: el personal de TI de Grupo LEMCO queda inhabilitado para construir nuevas herramientas o integrar nuevos orígenes de datos.",
            "Sesión 9 práctica de programación en Kiro de un servidor MCP propio en Python/TypeScript conectado a bases de datos y APIs internas.",
            "Soberanía operativa: el equipo interno desarrolla y prueba herramientas de datos personalizadas sin requerir horas adicionales de desarrollo."
        ),
        (
            "Gobernanza y Operación",
            "Runbooks y FinOps en la sesión 7, desconectados del código y las herramientas que el equipo de desarrollo usa a diario.",
            "Dificultad para auditar y monitorear los costos y la calidad de los modelos si la operación no se vincula al ciclo de despliegue continuo.",
            "Sesión 11 de cierre técnico que unifica el ciclo completo: del spec en Kiro al despliegue con AWS CDK, monitoreo en CloudWatch y presupuestos FinOps.",
            "Operación y gobierno sin fisuras: control de costos por agente, alarmas preventivas y runbooks claros de escalamiento para soporte P1 a P3."
        )
    ]

    for idx, (dim, orig_txt, brecha_txt, prop_txt, impacto_txt) in enumerate(transformation_rows):
        cur_r = r_h + 1 + idx
        ws2.merge_cells(f"B{cur_r}:C{cur_r}")
        ws2.merge_cells(f"E{cur_r}:F{cur_r}")
        
        ws2.cell(row=cur_r, column=1, value=dim).font = font_data_bold
        ws2.cell(row=cur_r, column=1).alignment = align_left
        
        ws2.cell(row=cur_r, column=2, value=orig_txt).font = font_data
        ws2.cell(row=cur_r, column=2).alignment = align_left
        
        c_br = ws2.cell(row=cur_r, column=4, value=brecha_txt)
        c_br.font = font_data_small
        c_br.alignment = align_left
        c_br.fill = fill_diag_cell
        
        c_pr = ws2.cell(row=cur_r, column=5, value=prop_txt)
        c_pr.font = font_data
        c_pr.alignment = align_left
        
        c_im = ws2.cell(row=cur_r, column=7, value=impacto_txt)
        c_im.font = font_data
        c_im.alignment = align_left
        
        for col_i in range(1, 8):
            ws2.cell(row=cur_r, column=col_i).border = border_cell
            
        ws2.row_dimensions[cur_r].height = 82

    # Section 3: Summary Table of Hours
    r_sum_title = cur_r + 2
    ws2.merge_cells(f"A{r_sum_title}:G{r_sum_title}")
    ws2[f"A{r_sum_title}"].value = "3. CONSOLIDADO DE HORAS Y SESIONES POR FASE — CUMPLIMIENTO DEL LÍMITE CONTRACTUAL"
    ws2[f"A{r_sum_title}"].font = font_section
    ws2[f"A{r_sum_title}"].fill = PatternFill(start_color="E2E8F0", end_color="E2E8F0", fill_type="solid")
    ws2.row_dimensions[r_sum_title].height = 24

    sum_h_r = r_sum_title + 1
    sum_headers = [
        "Fase del Programa", "Audiencia Principal", "Sesiones", "Horas Dictadas", 
        "Horas Preparación", "Horas Totales", "Cumplimiento Restricción"
    ]
    for c_idx, h_text in enumerate(sum_headers, start=1):
        c = ws2.cell(row=sum_h_r, column=c_idx, value=h_text)
        c.font = font_th_orig
        c.fill = fill_header_navy
        c.alignment = align_center
    ws2.row_dimensions[sum_h_r].height = 24

    summary_phase_data = [
        ("Fase 1: Adopción y Operación (Amazon Quick: Spaces, BI y Agentes)", "Champions de Negocio + Líderes + TI", 5, 10, 10, 20, "Exacto (5 sesiones x 2h = 10h dictadas)"),
        ("Fase 2: Técnica y Entrega (Kiro IDE + Bedrock + MCP + DevOps)", "Equipo TI + CoE de IA", 6, 12, 12, 24, "Exacto (6 sesiones x 2h = 12h dictadas)"),
        ("TOTAL CONSOLIDADO DEL PROGRAMA", "Grupo LEMCO (Negocio + TI)", 11, 22, 22, 44, "Límite Máximo Respetado (22h dictadas / 44h totales)")
    ]

    for p_i, (f_name, aud, sess, h_d, h_p, h_t, cump) in enumerate(summary_phase_data):
        row_pos = sum_h_r + 1 + p_i
        is_tot = (p_i == 2)
        
        ws2.cell(row=row_pos, column=1, value=f_name).font = font_data_bold if is_tot else font_data
        ws2.cell(row=row_pos, column=2, value=aud).font = font_data
        ws2.cell(row=row_pos, column=3, value=sess).alignment = align_center
        ws2.cell(row=row_pos, column=3).font = font_data_bold if is_tot else font_data
        ws2.cell(row=row_pos, column=4, value=h_d).alignment = align_center
        ws2.cell(row=row_pos, column=4).font = font_data_bold if is_tot else font_data
        ws2.cell(row=row_pos, column=5, value=h_p).alignment = align_center
        ws2.cell(row=row_pos, column=5).font = font_data_bold if is_tot else font_data
        ws2.cell(row=row_pos, column=6, value=h_t).alignment = align_center
        ws2.cell(row=row_pos, column=6).font = font_data_bold if is_tot else font_data
        ws2.cell(row=row_pos, column=7, value=cump).alignment = align_center
        ws2.cell(row=row_pos, column=7).font = font_data_bold if is_tot else font_data_small
        
        ws2.row_dimensions[row_pos].height = 24
        for col_c in range(1, 8):
            cell_c = ws2.cell(row=row_pos, column=col_c)
            cell_c.border = border_total if is_tot else border_cell
            if is_tot:
                cell_c.fill = PatternFill(start_color="E2E8F0", end_color="E2E8F0", fill_type="solid")

    ws2.column_dimensions["A"].width = 24
    ws2.column_dimensions["B"].width = 28
    ws2.column_dimensions["C"].width = 12
    ws2.column_dimensions["D"].width = 30
    ws2.column_dimensions["E"].width = 28
    ws2.column_dimensions["F"].width = 16
    ws2.column_dimensions["G"].width = 32

    # ==========================================
    # SHEET 3: DETALLE PROPUESTA AJUSTADA (READY FOR PROVIDER)
    # ==========================================
    ws3 = wb.create_sheet(title="Detalle_Propuesta_Ajustada")
    ws3.views.sheetView[0].showGridLines = True

    ws3.merge_cells("A1:H1")
    t3 = ws3["A1"]
    t3.value = "ANEXO TÉCNICO AJUSTADO: PROGRAMA DE TRANSFERENCIA DE CONOCIMIENTO — PROYECTO BRÚJULA"
    t3.font = font_title
    t3.fill = fill_prop_header
    t3.alignment = align_center
    ws3.row_dimensions[1].height = 36

    ws3.merge_cells("A2:H2")
    s3 = ws3["A2"]
    s3.value = "Especificación Detallada de Contenidos, Audiencias y Entregables por Sesión · Enfoque Amazon Quick Desktop y Kiro IDE"
    s3.font = font_subtitle
    s3.fill = fill_prop_header
    s3.alignment = align_center
    ws3.row_dimensions[2].height = 20

    headers_s3 = [
        ("N°", 6),
        ("Fase", 10),
        ("Ruta Formativa", 20),
        ("Título Oficial de la Sesión", 34),
        ("Audiencia Convocada", 24),
        ("Dedicación Horaria", 16),
        ("Contenido Temático Detallado", 52),
        ("Entregable Tangible Verificable", 30)
    ]

    for c_i, (h_t, w_v) in enumerate(headers_s3, start=1):
        cell_h = ws3.cell(row=4, column=c_i, value=h_t)
        cell_h.font = font_th_prop
        cell_h.fill = fill_prop_header
        cell_h.alignment = align_center
        col_l = get_column_letter(c_i)
        ws3.column_dimensions[col_l].width = w_v
    ws3.row_dimensions[4].height = 28

    for p_i, p_data in enumerate(proposed_sessions):
        r_num = 5 + p_i
        ws3.cell(row=r_num, column=1, value=p_data["num"]).alignment = align_center_top
        ws3.cell(row=r_num, column=1).font = font_data_bold
        
        f_c = ws3.cell(row=r_num, column=2, value=p_data["fase"])
        f_c.alignment = align_center_top
        f_c.font = font_data_bold
        f_c.fill = fill_phase1_badge if "1" in p_data["fase"] else fill_phase2_badge
        
        ws3.cell(row=r_num, column=3, value=p_data["ruta"]).alignment = align_center_top
        ws3.cell(row=r_num, column=4, value=p_data["titulo"]).alignment = align_left
        ws3.cell(row=r_num, column=4).font = font_data_bold
        ws3.cell(row=r_num, column=5, value=p_data["audiencia"]).alignment = align_left
        ws3.cell(row=r_num, column=6, value=f"{p_data['h_dict']}h dictado\n{p_data['h_prep']}h preparación\nTotal: {p_data['h_tot']} horas").alignment = align_center_top
        ws3.cell(row=r_num, column=7, value=p_data["temario"]).alignment = align_left
        ws3.cell(row=r_num, column=8, value=p_data["entregable"]).alignment = align_left
        
        ws3.row_dimensions[r_num].height = 115
        is_even = (p_i % 2 == 0)
        for c_col in range(1, 9):
            cell_item = ws3.cell(row=r_num, column=c_col)
            cell_item.border = border_cell
            if is_even and c_col not in [1, 2]:
                cell_item.fill = fill_zebra_prop

    # Totals Row
    tot_s3 = 16
    ws3.cell(row=tot_s3, column=1, value="TOTAL").alignment = align_center
    ws3.cell(row=tot_s3, column=1).font = font_data_bold
    ws3.cell(row=tot_s3, column=2, value="11").alignment = align_center
    ws3.cell(row=tot_s3, column=2).font = font_data_bold
    ws3.cell(row=tot_s3, column=3, value="5 Rutas").alignment = align_center
    ws3.cell(row=tot_s3, column=3).font = font_data_bold
    ws3.cell(row=tot_s3, column=4, value="Programa Ajustado Consolidado").font = font_data_bold
    ws3.cell(row=tot_s3, column=5, value="Champions + TI + CoE IA").font = font_data_bold
    ws3.cell(row=tot_s3, column=6, value="22h dictado\n22h preparación\nTotal: 44h").alignment = align_center
    ws3.cell(row=tot_s3, column=6).font = font_data_bold
    ws3.cell(row=tot_s3, column=7, value="Fase 1: 5 sesiones Amazon Quick (20h) · Fase 2: 6 sesiones Kiro & AWS (24h)").font = font_data_bold
    ws3.cell(row=tot_s3, column=8, value="11 Entregables formales").font = font_data_bold

    for col_c in range(1, 9):
        c_cell = ws3.cell(row=tot_s3, column=col_c)
        c_cell.border = border_total
        c_cell.fill = PatternFill(start_color="E2E8F0", end_color="E2E8F0", fill_type="solid")
    ws3.row_dimensions[tot_s3].height = 30

    ws3.freeze_panes = "C5"

    # ==========================================
    # SHEET 4: PROPUESTA ORIGINAL PDF (FIRM REFERENCE)
    # ==========================================
    ws4 = wb.create_sheet(title="Propuesta_Original_PDF")
    ws4.views.sheetView[0].showGridLines = True

    ws4.merge_cells("A1:H1")
    t4 = ws4["A1"]
    t4.value = "PROPUESTA ORIGINAL DEL PROVEEDOR CNID — PLAN DE TRANSFERENCIA DE CONOCIMIENTO (PDF)"
    t4.font = font_title
    t4.fill = fill_orig_header
    t4.alignment = align_center
    ws4.row_dimensions[1].height = 36

    ws4.merge_cells("A2:H2")
    s4 = ws4["A2"]
    s4.value = "Transcripción Fiel del Anexo RFP-BRUJULA-IA-2026-001 (Versión Ajustada 29 Oct 2026) · 11 Sesiones · 44 Horas"
    s4.font = font_subtitle
    s4.fill = fill_orig_header
    s4.alignment = align_center
    ws4.row_dimensions[2].height = 20

    for c_i, (h_t, w_v) in enumerate(headers_s3, start=1):
        cell_h = ws4.cell(row=4, column=c_i, value=h_t)
        cell_h.font = font_th_orig
        cell_h.fill = fill_orig_header
        cell_h.alignment = align_center
        col_l = get_column_letter(c_i)
        ws4.column_dimensions[col_l].width = w_v
    ws4.row_dimensions[4].height = 28

    for o_i, o_data in enumerate(original_sessions):
        r_num = 5 + o_i
        ws4.cell(row=r_num, column=1, value=o_data["num"]).alignment = align_center_top
        ws4.cell(row=r_num, column=1).font = font_data_bold
        
        f_c = ws4.cell(row=r_num, column=2, value=o_data["fase"])
        f_c.alignment = align_center_top
        f_c.font = font_data_bold
        f_c.fill = fill_phase1_badge if "1" in o_data["fase"] else fill_phase2_badge
        
        ws4.cell(row=r_num, column=3, value=o_data["ruta"]).alignment = align_center_top
        ws4.cell(row=r_num, column=4, value=o_data["titulo"]).alignment = align_left
        ws4.cell(row=r_num, column=4).font = font_data_bold
        ws4.cell(row=r_num, column=5, value=o_data["audiencia"]).alignment = align_left
        ws4.cell(row=r_num, column=6, value=f"{o_data['h_dict']}h dictado\n{o_data['h_prep']}h preparación\nTotal: {o_data['h_tot']} horas").alignment = align_center_top
        ws4.cell(row=r_num, column=7, value=o_data["temario"]).alignment = align_left
        ws4.cell(row=r_num, column=8, value=o_data["entregable"]).alignment = align_left
        
        ws4.row_dimensions[r_num].height = 110
        is_even = (o_i % 2 == 0)
        for c_col in range(1, 9):
            cell_item = ws4.cell(row=r_num, column=c_col)
            cell_item.border = border_cell
            if is_even and c_col not in [1, 2]:
                cell_item.fill = fill_zebra_orig

    # Totals Row
    ws4.cell(row=tot_s3, column=1, value="TOTAL").alignment = align_center
    ws4.cell(row=tot_s3, column=1).font = font_data_bold
    ws4.cell(row=tot_s3, column=2, value="11").alignment = align_center
    ws4.cell(row=tot_s3, column=2).font = font_data_bold
    ws4.cell(row=tot_s3, column=3, value="4 Rutas").alignment = align_center
    ws4.cell(row=tot_s3, column=3).font = font_data_bold
    ws4.cell(row=tot_s3, column=4, value="Programa Original Base (PDF)").font = font_data_bold
    ws4.cell(row=tot_s3, column=5, value="Champions + TI").font = font_data_bold
    ws4.cell(row=tot_s3, column=6, value="22h dictado\n22h preparación\nTotal: 44h").alignment = align_center
    ws4.cell(row=tot_s3, column=6).font = font_data_bold
    ws4.cell(row=tot_s3, column=7, value="Fase 1: 5 sesiones (20h) · Fase 2: 6 sesiones (24h)").font = font_data_bold
    ws4.cell(row=tot_s3, column=8, value="11 Entregables base").font = font_data_bold

    for col_c in range(1, 9):
        c_cell = ws4.cell(row=tot_s3, column=col_c)
        c_cell.border = border_total
        c_cell.fill = PatternFill(start_color="E2E8F0", end_color="E2E8F0", fill_type="solid")
    ws4.row_dimensions[tot_s3].height = 30

    ws4.freeze_panes = "C5"

    output_path = "Propuesta_Ajustada_Capacitacion_Brujula_IA.xlsx"
    wb.save(output_path)
    print(f"Successfully generated updated workbook at: {output_path}")

if __name__ == "__main__":
    build_workbook()

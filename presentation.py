import streamlit as st
import pandas as pd

# Configuración de página
st.set_page_config(
    page_title="Presentación NL2SQL",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS personalizado para mejorar la presentación
st.markdown("""
<style>
    .big-title {
        font-size: 3.5rem !important;
        font-weight: bold;
        text-align: center;
        color: #1E88E5;
        margin-bottom: 1rem;
    }
    .subtitle {
        font-size: 1.8rem !important;
        text-align: center;
        color: #424242;
        margin-bottom: 2rem;
    }
    .section-title {
        font-size: 2.5rem !important;
        font-weight: bold;
        color: #1565C0;
        margin-bottom: 1.5rem;
    }
    .highlight-box {
        background-color: #E3F2FD;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1E88E5;
        margin: 15px 0;
    }
    .code-box {
        background-color: #F5F5F5;
        padding: 15px;
        border-radius: 8px;
        font-family: monospace;
        margin: 10px 0;
    }
    .bullet-point {
        font-size: 1.3rem;
        margin: 10px 0;
        line-height: 1.8;
    }
    .slide-number {
        position: fixed;
        bottom: 20px;
        right: 20px;
        font-size: 1.2rem;
        color: #757575;
    }
</style>
""", unsafe_allow_html=True)

# Inicializar estado de la slide
if 'slide' not in st.session_state:
    st.session_state.slide = 0

# Definir slides
def slide_portada():
    st.markdown('<p class="big-title">🎓 Sistema NL2SQL</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Consultas a Bases de Datos en Lenguaje Natural</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="highlight-box">
            <h3 style="text-align: center;">Transformando palabras en consultas SQL</h3>
            <p style="text-align: center; font-size: 1.2rem; margin-top: 20px;">
                📊 Bases de Datos + 🤖 Inteligencia Artificial
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <p style="text-align: center; font-size: 1.3rem;">
            <strong>Estudiante:</strong> Bayaslian Santiago <br>
            <strong>Carrera:</strong> Ciencia de Datos e IA<br>
            <strong>Docente:</strong> Yanina Scudero
        </p>
        """, unsafe_allow_html=True)

def slide_problema():
    st.markdown('<p class="section-title">❓ El Problema</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="highlight-box">
            <h3>🚫 Situación Actual</h3>
            <div class="bullet-point">• Usuarios necesitan conocer SQL</div>
            <div class="bullet-point">• Curva de aprendizaje pronunciada</div>
            <div class="bullet-point">• Dependencia de personal técnico</div>
            <div class="bullet-point">• Consultas complejas intimidan</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="highlight-box" style="background-color: #E8F5E9; border-left-color: #43A047;">
            <h3>✅ Solución Propuesta</h3>
            <div class="bullet-point">• Consultas en lenguaje natural</div>
            <div class="bullet-point">• Interfaz intuitiva</div>
            <div class="bullet-point">• Acceso democratizado</div>
            <div class="bullet-point">• Traducción automática a SQL</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.info("💡 **Ejemplo:** 'listar todos los clientes' → `SELECT * FROM clientes;`")

def slide_arquitectura_bd():
    st.markdown('<p class="section-title">🗄️ Arquitectura de Base de Datos</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="highlight-box">
            <h3>📋 Tablas del Sistema</h3>
            <div class="bullet-point"><strong>👥 clientes</strong> - Información de clientes</div>
            <div class="bullet-point"><strong>🛍️ productos</strong> - Catálogo de productos</div>
            <div class="bullet-point"><strong>🏷️ rubros</strong> - Categorías de productos</div>
            <div class="bullet-point"><strong>🏢 sucursales</strong> - Puntos de venta</div>
            <div class="bullet-point"><strong>💰 ventas</strong> - Transacciones realizadas</div>
            <div class="bullet-point"><strong>📄 facturas</strong> - Documentación fiscal</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="highlight-box">
            <h3>🔗 Relaciones Clave</h3>
            <div class="bullet-point">productos ↔ rubros (N:1)</div>
            <div class="bullet-point">ventas ↔ clientes (N:1)</div>
            <div class="bullet-point">ventas ↔ sucursales (N:1)</div>
            <div class="bullet-point">facturas ↔ ventas (1:1)</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.success("✅ **Base de Datos Normalizada** con integridad referencial")
    
    st.markdown("---")
    st.markdown("""
    <div class="code-box">
    <strong>🔧 Tecnología:</strong> SQLite<br>
    <strong>✓ Ventajas:</strong> Ligera, portable, sin servidor, ideal para prototipado
    </div>
    """, unsafe_allow_html=True)

def slide_enfoque_tecnico():
    st.markdown('<p class="section-title">🧠 Enfoque Técnico: NL2SQL</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-box">
        <h3 style="text-align: center;">¿Cómo funciona la traducción?</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="background-color: #FFF3E0; padding: 20px; border-radius: 10px; height: 280px;">
            <h3 style="color: #F57C00;">1️⃣ Preprocesamiento</h3>
            <div class="bullet-point" style="font-size: 1.1rem;">
                • Normalización de texto<br>
                • Eliminación de stopwords<br>
                • Tokenización<br>
                • Limpieza de caracteres
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color: #E1F5FE; padding: 20px; border-radius: 10px; height: 280px;">
            <h3 style="color: #0277BD;">2️⃣ Embeddings</h3>
            <div class="bullet-point" style="font-size: 1.1rem;">
                • Modelo: MiniLM-L12<br>
                • Texto → Vectores numéricos<br>
                • Captura significado semántico<br>
                • 384 dimensiones
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background-color: #F3E5F5; padding: 20px; border-radius: 10px; height: 280px;">
            <h3 style="color: #7B1FA2;">3️⃣ Matching</h3>
            <div class="bullet-point" style="font-size: 1.1rem;">
                • Similitud coseno<br>
                • Encuentra patrón similar<br>
                • Score de confianza<br>
                • Retorna SQL correspondiente
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.info("🎯 **Clave:** No usa keywords exactas, sino comprensión semántica del contexto")

def slide_embeddings():
    st.markdown('<p class="section-title">🔢 ¿Qué son los Embeddings?</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("""
        <div class="highlight-box">
            <h3>Transformación de Texto a Vectores</h3>
            <p style="font-size: 1.2rem;">
                Los embeddings convierten palabras o frases en vectores numéricos que capturan 
                su <strong>significado semántico</strong>.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="code-box">
        <strong>Ejemplo:</strong><br><br>
        "listar clientes" → [0.23, -0.45, 0.78, ..., 0.12] (384 números)<br>
        "mostrar clientes" → [0.25, -0.43, 0.76, ..., 0.14] (384 números)<br>
        <br>
        ➜ Vectores similares = Significados similares
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="highlight-box" style="background-color: #FFF3E0; border-left-color: #F57C00;">
            <h3>Ventajas</h3>
            <div class="bullet-point">✓ Captura sinónimos</div>
            <div class="bullet-point">✓ Entiende contexto</div>
            <div class="bullet-point">✓ Multilingüe</div>
            <div class="bullet-point">✓ No requiere reglas</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.success("🤖 **Modelo usado:** `paraphrase-multilingual-MiniLM-L12-v2` (HuggingFace)")

def slide_similitud_coseno():
    st.markdown('<p class="section-title">📐 Similitud Coseno</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 3])
    
    with col1:
        st.markdown("""
        <div class="highlight-box">
            <h3>¿Cómo mide la cercanía?</h3>
            <p style="font-size: 1.2rem;">
                Calcula el <strong>ángulo</strong> entre dos vectores en espacio n-dimensional.
            </p>
            <br>
            <div class="code-box">
            <strong>Fórmula:</strong><br>
            cos(θ) = (A · B) / (||A|| × ||B||)<br>
            <br>
            <strong>Rango:</strong> -1 a 1<br>
            • 1 = Idénticos<br>
            • 0 = Ortogonales<br>
            • -1 = Opuestos
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="highlight-box">
            <h3>En nuestro sistema</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Ejemplo de scores
        ejemplos_df = pd.DataFrame({
            'Consulta Usuario': ['listar clientes', 'listar clientes', 'listar clientes'],
            'Patrón del Diccionario': ['mostrar clientes', 'ventas totales', 'productos por rubro'],
            'Score': [0.95, 0.32, 0.28],
            'Resultado': ['✅ MATCH', '❌ Descartado', '❌ Descartado']
        })
        
        st.dataframe(ejemplos_df, use_container_width=True, hide_index=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.warning("⚠️ **Umbral de confianza:** 0.6 (60%) - Por debajo se alerta al usuario")

def slide_componentes():
    st.markdown('<p class="section-title">⚙️ Componentes del Sistema</p>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["🔍 Consultar", "➕ Agregar Patrón", "📚 Diccionario"])
    
    with tab1:
        st.markdown("""
        <div class="highlight-box">
            <h3>Interfaz de Consulta</h3>
            <div class="bullet-point">• Usuario ingresa pregunta en lenguaje natural</div>
            <div class="bullet-point">• Sistema encuentra el patrón más similar</div>
            <div class="bullet-point">• Muestra SQL generado y score de confianza</div>
            <div class="bullet-point">• Ejecuta y presenta resultados en tabla</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.code("""
# Ejemplo de flujo
consulta_nl = "listar todos los productos"
sql, score, match = query_to_sql(consulta_nl)
# → SQL: "SELECT * FROM productos;"
# → Score: 0.89
        """, language="python")
    
    with tab2:
        st.markdown("""
        <div class="highlight-box">
            <h3>Expansión Dinámica</h3>
            <div class="bullet-point">• Agregar nuevos patrones sin código</div>
            <div class="bullet-point">• Ingresa frase NL + consulta SQL</div>
            <div class="bullet-point">• Sistema calcula embedding automáticamente</div>
            <div class="bullet-point">• Disponible inmediatamente para uso</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.success("✅ **Ventaja clave:** No requiere reentrenar modelo ni reiniciar app")
    
    with tab3:
        st.markdown("""
        <div class="highlight-box">
            <h3>Repositorio de Patrones</h3>
            <div class="bullet-point">• Vista de todos los pares NL-SQL</div>
            <div class="bullet-point">• Búsqueda y filtrado</div>
            <div class="bullet-point">• Referencia rápida para usuarios</div>
            <div class="bullet-point">• 15+ patrones predefinidos</div>
        </div>
        """, unsafe_allow_html=True)

def slide_demo():
    st.markdown('<p class="section-title">🚀 Demostración en Vivo</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-box" style="background-color: #FFEBEE; border-left-color: #C62828;">
        <h2 style="text-align: center; color: #C62828;">⚠️ CAMBIAR A LA APP PRINCIPAL ⚠️</h2>
        <p style="text-align: center; font-size: 1.5rem; margin-top: 20px;">
            Ahora mostraré el sistema funcionando en tiempo real
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="highlight-box">
            <h3>📋 Casos a Demostrar</h3>
            <div class="bullet-point">1. Consulta exitosa (alta confianza)</div>
            <div class="bullet-point">2. Consulta ambigua (baja confianza)</div>
            <div class="bullet-point">3. Agregar nuevo patrón</div>
            <div class="bullet-point">4. Usar el patrón recién agregado</div>
            <div class="bullet-point">5. Explorar diccionario completo</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="highlight-box" style="background-color: #E8F5E9; border-left-color: #43A047;">
            <h3>💡 Ejemplos Sugeridos</h3>
            <div class="code-box">
            • "listar clientes"<br>
            • "ventas totales"<br>
            • "productos más caros"<br>
            • "cuántas ventas hubo"<br>
            • "mostrar todas las facturas"
            </div>
        </div>
        """, unsafe_allow_html=True)

def slide_ciencia_datos():
    st.markdown('<p class="section-title">🎓 Perspectiva: Ciencia de Datos & IA</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="highlight-box">
            <h3>🌍 Aplicaciones Reales</h3>
            <div class="bullet-point">• Chatbots empresariales (Slack, Teams)</div>
            <div class="bullet-point">• Asistentes de Business Intelligence</div>
            <div class="bullet-point">• Democratización de datos</div>
            <div class="bullet-point">• Reducción de carga en equipos IT</div>
            <div class="bullet-point">• Análisis self-service</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.success("💼 **Caso real:** Microsoft Power BI Q&A, Google BigQuery natural language")
    
    with col2:
        st.markdown("""
        <div class="highlight-box" style="background-color: #FFF3E0; border-left-color: #F57C00;">
            <h3>⚠️ Limitaciones</h3>
            <div class="bullet-point">• Consultas complejas (JOINs múltiples)</div>
            <div class="bullet-point">• Ambigüedad del lenguaje natural</div>
            <div class="bullet-point">• Dependiente de diccionario inicial</div>
            <div class="bullet-point">• No valida lógica del SQL</div>
            <div class="bullet-point">• Requiere mantenimiento de patrones</div>
        </div>
        """, unsafe_allow_html=True)

def slide_evolucion():
    st.markdown('<p class="section-title">🔮 Evolución y Mejoras Futuras</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="highlight-box">
            <h3>🚀 Corto Plazo</h3>
            <div class="bullet-point">✓ Logging de consultas fallidas</div>
            <div class="bullet-point">✓ Validación de SQL antes de ejecutar</div>
            <div class="bullet-point">✓ Sugerencias automáticas de patrones</div>
            <div class="bullet-point">✓ Historial de consultas por usuario</div>
            <div class="bullet-point">✓ Exportación de resultados (CSV/Excel)</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="highlight-box" style="background-color: #E8F5FE; border-left-color: #0277BD;">
            <h3>🤖 Largo Plazo (LLMs)</h3>
            <div class="bullet-point">• Integración con GPT-4/Claude</div>
            <div class="bullet-point">• Generación de SQL sin diccionario</div>
            <div class="bullet-point">• Comprensión de contexto conversacional</div>
            <div class="bullet-point">• Fine-tuning en esquema específico</div>
            <div class="bullet-point">• Explicación del razonamiento SQL</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.info("💡 **Tendencia:** Modelos como Text-to-SQL (Google Bard, ChatGPT Code Interpreter)")

def slide_arquitectura_completa():
    st.markdown('<p class="section-title">🏗️ Arquitectura Completa del Sistema</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: #FAFAFA; padding: 30px; border-radius: 10px; border: 2px solid #E0E0E0;">
        <div style="text-align: center; font-family: monospace; font-size: 1.1rem; line-height: 2.5;">
            📱 <strong>Usuario (Interfaz Streamlit)</strong><br>
            ⬇️<br>
            🔤 <strong>Preprocesamiento de Texto</strong><br>
            (Normalización, Stopwords, Tokenización)<br>
            ⬇️<br>
            🧠 <strong>Modelo de Embeddings</strong><br>
            (MiniLM-L12: Texto → Vector 384D)<br>
            ⬇️<br>
            📐 <strong>Similitud Coseno</strong><br>
            (Comparación con Diccionario)<br>
            ⬇️<br>
            ✅ <strong>Selección de Mejor Match</strong><br>
            (Score + Patrón correspondiente)<br>
            ⬇️<br>
            💾 <strong>Ejecución SQL en SQLite</strong><br>
            (Query + Fetch Results)<br>
            ⬇️<br>
            📊 <strong>Presentación de Resultados</strong><br>
            (DataFrame + Métricas)
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Capas del Sistema", "7", "Modulares")
    with col2:
        st.metric("Tiempo Promedio", "< 1s", "Por consulta")
    with col3:
        st.metric("Librerías Principales", "5", "PyTorch, Transformers, SQLite, Streamlit, Scikit-learn")

def slide_metricas():
    st.markdown('<p class="section-title">📊 Métricas y Evaluación</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="highlight-box">
            <h3>📈 Métricas Implementadas</h3>
            <div class="bullet-point"><strong>Score de Confianza:</strong> Similitud coseno (0-1)</div>
            <div class="bullet-point"><strong>Umbral:</strong> 0.6 para alertas</div>
            <div class="bullet-point"><strong>Match exacto:</strong> > 0.8</div>
            <div class="bullet-point"><strong>Tiempo de respuesta:</strong> < 1 segundo</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Ejemplo de métricas
        metrics_data = {
            'Rango Score': ['0.8 - 1.0', '0.6 - 0.8', '< 0.6'],
            'Interpretación': ['✅ Excelente', '⚠️ Aceptable', '❌ Revisar'],
            'Acción': ['Ejecutar', 'Mostrar alerta', 'Sugerir reformular']
        }
        st.dataframe(pd.DataFrame(metrics_data), use_container_width=True, hide_index=True)
    
    with col2:
        st.markdown("""
        <div class="highlight-box" style="background-color: #E8F5E9; border-left-color: #43A047;">
            <h3>🎯 Evaluación Cualitativa</h3>
            <div class="bullet-point"><strong>Precisión:</strong> ¿SQL correcto para la consulta?</div>
            <div class="bullet-point"><strong>Recall:</strong> ¿Encuentra patrones relevantes?</div>
            <div class="bullet-point"><strong>Usabilidad:</strong> ¿Interfaz intuitiva?</div>
            <div class="bullet-point"><strong>Extensibilidad:</strong> ¿Fácil agregar patrones?</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.success("✅ **Testing:** Validación manual con casos de uso reales del dominio empresarial")

def slide_conclusiones():
    st.markdown('<p class="section-title">🎯 Conclusiones</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-box" style="background-color: #E3F2FD; border-left-color: #1976D2;">
        <h3 style="text-align: center;">Logros del Proyecto</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="bullet-point">✅ <strong>Integración exitosa</strong> de BD con IA</div>
        <div class="bullet-point">✅ <strong>Interfaz accesible</strong> para usuarios no técnicos</div>
        <div class="bullet-point">✅ <strong>Sistema extensible</strong> dinámicamente</div>
        <div class="bullet-point">✅ <strong>Arquitectura modular</strong> y escalable</div>
        <div class="bullet-point">✅ <strong>Respuestas en tiempo real</strong> (< 1s)</div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="bullet-point">🎓 <strong>Aprendizajes:</strong> NLP, embeddings, similitud</div>
        <div class="bullet-point">💾 <strong>Prácticas de BD:</strong> normalización, integridad</div>
        <div class="bullet-point">🤝 <strong>Puente BD-IA:</strong> complementariedad</div>
        <div class="bullet-point">🚀 <strong>Aplicabilidad:</strong> casos reales empresariales</div>
        <div class="bullet-point">🔮 <strong>Proyección:</strong> evolución con LLMs</div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    <div class="highlight-box" style="background-color: #FFF3E0; border-left-color: #F57C00;">
        <h3 style="text-align: center;">💡 Reflexión Final</h3>
        <p style="text-align: center; font-size: 1.3rem; margin-top: 15px;">
            La combinación de <strong>bases de datos estructuradas</strong> con 
            <strong>inteligencia artificial</strong> abre nuevas posibilidades para la 
            democratización del acceso a la información empresarial.
        </p>
    </div>
    """, unsafe_allow_html=True)

def slide_preguntas():
    st.markdown('<p class="big-title">❓ Preguntas</p>', unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 50px;">
            <h2 style="font-size: 3rem; color: #1976D2;">¿Consultas?</h2>
            <br><br>
            <p style="font-size: 1.5rem;">Gracias por su atención</p>
            <br>
            <p style="font-size: 1.2rem; color: #757575;">
                📧 [tu_email]@ejemplo.com<br>
                💼 GitHub: github.com/[tu_usuario]
            </p>
        </div>
        """, unsafe_allow_html=True)

# Lista de slides
slides = [
    ("Portada", slide_portada),
    ("El Problema", slide_problema),
    ("Arquitectura BD", slide_arquitectura_bd),
    ("Enfoque Técnico", slide_enfoque_tecnico),
    ("Embeddings", slide_embeddings),
    ("Similitud Coseno", slide_similitud_coseno),
    ("Componentes", slide_componentes),
    ("Arquitectura Completa", slide_arquitectura_completa),
    ("Métricas", slide_metricas),
    ("Demo", slide_demo),
    ("Ciencia de Datos", slide_ciencia_datos),
    ("Evolución Futura", slide_evolucion),
    ("Conclusiones", slide_conclusiones),
    ("Preguntas", slide_preguntas)
]

# Mostrar slide actual
current_slide_name, current_slide_func = slides[st.session_state.slide]
current_slide_func()

# Navegación
st.markdown("---")
col1, col2, col3, col4, col5 = st.columns([1, 1, 2, 1, 1])

with col1:
    if st.button("⏮️ Primera", use_container_width=True):
        st.session_state.slide = 0
        st.rerun()

with col2:
    if st.button("◀️ Anterior", use_container_width=True, disabled=(st.session_state.slide == 0)):
        st.session_state.slide -= 1
        st.rerun()

with col3:
    st.markdown(f"""
    <div style="text-align: center; padding: 8px; background-color: #E3F2FD; border-radius: 8px;">
        <strong style="font-size: 1.1rem;">{st.session_state.slide + 1} / {len(slides)}</strong>
        <span style="color: #757575; margin-left: 15px;">{current_slide_name}</span>
    </div>
    """, unsafe_allow_html=True)

with col4:
    if st.button("Siguiente ▶️", use_container_width=True, disabled=(st.session_state.slide == len(slides) - 1)):
        st.session_state.slide += 1
        st.rerun()

with col5:
    if st.button("Última ⏭️", use_container_width=True):
        st.session_state.slide = len(slides) - 1
        st.rerun()

# Atajos de teclado (info)
with st.sidebar:
    st.markdown("""
    ### ⌨️ Navegación
    
    **Botones disponibles:**
    - ⏮️ Primera slide
    - ◀️ Slide anterior
    - ▶️ Slide siguiente
    - ⏭️ Última slide
    
    ### 📋 Índice de Slides
    """)
    
    for idx, (name, _) in enumerate(slides):
        if idx == st.session_state.slide:
            st.markdown(f"**➡️ {idx + 1}. {name}**")
        else:
            if st.button(f"{idx + 1}. {name}", key=f"nav_{idx}"):
                st.session_state.slide = idx
                st.rerun()
    
    st.markdown("---")
    st.markdown("""
    ### 💡 Tips para Presentar
    - Usa pantalla completa (F11)
    - Mantén ritmo constante
    - Interactúa con la demo
    - Prepara respuestas a preguntas comunes
    """)

# Número de slide en esquina
st.markdown(f'<div class="slide-number">Slide {st.session_state.slide + 1}/{len(slides)}</div>', unsafe_allow_html=True)

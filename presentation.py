import streamlit as st
import pandas as pd

# Configuración de página
st.set_page_config(
    page_title="NL→SQL: Habla con tu BD",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS personalizado mejorado
st.markdown("""
<style>
    /* Estilos generales */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Contenedor de slides */
    .slide-container {
        background: white;
        border-radius: 20px;
        padding: 50px;
        margin: 20px auto;
        max-width: 1400px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        min-height: 70vh;
    }
    
    /* Títulos */
    .big-title {
        font-size: 4rem !important;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        animation: fadeInDown 0.8s ease;
    }
    
    .subtitle {
        font-size: 2rem !important;
        text-align: center;
        color: #424242;
        margin-bottom: 2rem;
        font-weight: 300;
    }
    
    .section-title {
        font-size: 3rem !important;
        font-weight: bold;
        color: #667eea;
        margin-bottom: 2rem;
        border-bottom: 4px solid #764ba2;
        padding-bottom: 10px;
        animation: fadeIn 0.6s ease;
    }
    
    /* Cajas destacadas */
    .highlight-box {
        background: linear-gradient(135deg, #E3F2FD 0%, #F3E5F5 100%);
        padding: 30px;
        border-radius: 15px;
        border-left: 6px solid #667eea;
        margin: 20px 0;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.2);
        transition: transform 0.3s ease;
    }
    
    .highlight-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
    }
    
    .warning-box {
        background: linear-gradient(135deg, #FFF3E0 0%, #FFE0B2 100%);
        padding: 30px;
        border-radius: 15px;
        border-left: 6px solid #F57C00;
        margin: 20px 0;
    }
    
    .success-box {
        background: linear-gradient(135deg, #E8F5E9 0%, #C8E6C9 100%);
        padding: 30px;
        border-radius: 15px;
        border-left: 6px solid #43A047;
        margin: 20px 0;
    }
    
    .danger-box {
        background: linear-gradient(135deg, #FFEBEE 0%, #FFCDD2 100%);
        padding: 30px;
        border-radius: 15px;
        border-left: 6px solid #E53935;
        margin: 20px 0;
    }
    
    /* Código */
    .code-box {
        background: #2D2D2D;
        color: #F8F8F2;
        padding: 25px;
        border-radius: 12px;
        font-family: 'Courier New', monospace;
        margin: 15px 0;
        font-size: 1.1rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    /* Bullet points */
    .bullet-point {
        font-size: 1.4rem;
        margin: 15px 0;
        line-height: 2;
        color: #333;
    }
    
    .big-bullet {
        font-size: 1.8rem;
        margin: 20px 0;
        line-height: 2;
        font-weight: 600;
    }
    
    /* Badges */
    .badge {
        display: inline-block;
        padding: 8px 20px;
        border-radius: 20px;
        font-weight: bold;
        margin: 5px;
        font-size: 1.1rem;
    }
    
    .badge-primary {
        background: #667eea;
        color: white;
    }
    
    .badge-success {
        background: #43A047;
        color: white;
    }
    
    .badge-warning {
        background: #F57C00;
        color: white;
    }
    
    /* Animaciones */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    /* Número de slide */
    .slide-number {
        position: fixed;
        bottom: 20px;
        right: 30px;
        font-size: 1.3rem;
        color: white;
        background: rgba(102, 126, 234, 0.9);
        padding: 10px 20px;
        border-radius: 25px;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    /* Ocultar elementos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Inicializar estado
if 'slide' not in st.session_state:
    st.session_state.slide = 0

# ==================== SLIDES ====================

def slide_portada():
    st.markdown('<p class="big-title">💬 Habla con tu Base de Datos</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Consultas en Lenguaje Natural usando Inteligencia Artificial</p>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="highlight-box">
            <h2 style="text-align: center; color: #667eea;">De esto...</h2>
            <div class="code-box">
SELECT clientes.nombre, SUM(ventas.total)<br>
FROM clientes<br>
JOIN ventas ON clientes.id = ventas.cliente_id<br>
GROUP BY clientes.nombre;
            </div>
            <h2 style="text-align: center; color: #764ba2; margin-top: 30px;">...a esto:</h2>
            <p style="text-align: center; font-size: 1.8rem; margin-top: 20px; font-weight: 600;">
                "ventas por cliente"
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style="text-align: center;">
            <p style="font-size: 1.5rem; margin: 10px 0;">
                <strong>Estudiante:</strong> <span class="badge badge-primary">Bayaslian Santiago</span>
            </p>
            <p style="font-size: 1.3rem; color: #666;">
                Tecnicatura en Ciencia de Datos e Inteligencia Artificial<br>
                Instituto Tecnológico Beltrán
            </p>
            <p style="font-size: 1.2rem; color: #888; margin-top: 20px;">
                Docente: Yanina Scudero
            </p>
        </div>
        """, unsafe_allow_html=True)

def slide_gancho():
    st.markdown('<p class="section-title">🎯 Pregunta para ustedes</p>', unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 40px;">
            <h1 style="font-size: 3rem; color: #667eea; margin-bottom: 40px;">
                ¿Cuánto tiempo les llevaría aprender SQL lo suficientemente bien para escribir consultas complejas?
            </h1>
            <p style="font-size: 1.8rem; color: #666; margin-top: 50px;">
                ⏰ ¿Semanas? ¿Meses?
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="warning-box">
            <h3 style="text-align: center;">🤔 La Realidad</h3>
            <div class="bullet-point">
                • JOINs, subconsultas, agregaciones...<br>
                • Sintaxis específica por motor de BD<br>
                • Años de práctica para dominar
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="success-box">
            <h3 style="text-align: center;">💡 La Solución</h3>
            <div class="bullet-point">
                • Hablar en lenguaje natural<br>
                • Sin memorizar sintaxis<br>
                • Acceso inmediato a los datos
            </div>
        </div>
        """, unsafe_allow_html=True)

def slide_problema():
    st.markdown('<p class="section-title">⚠️ El Problema Real</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="danger-box">
            <h2 style="color: #E53935; text-align: center;">😰 Sin NL→SQL</h2>
            <div class="big-bullet">❌ Barrera técnica alta</div>
            <div class="big-bullet">❌ Dependencia de IT</div>
            <div class="big-bullet">❌ Tiempos de respuesta lentos</div>
            <div class="big-bullet">❌ Datos subutilizados</div>
            <div class="big-bullet">❌ Usuarios frustrados</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="text-align: center; margin-top: 20px;">
            <p style="font-size: 1.3rem; color: #666;">
                <strong>Ejemplo típico:</strong><br>
                "Necesito un reporte" → Ticket a IT → Espera 3 días
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="success-box">
            <h2 style="color: #43A047; text-align: center;">🚀 Con NL→SQL</h2>
            <div class="big-bullet">✅ Acceso democratizado</div>
            <div class="big-bullet">✅ Autonomía de usuarios</div>
            <div class="big-bullet">✅ Respuestas en segundos</div>
            <div class="big-bullet">✅ Datos aprovechados</div>
            <div class="big-bullet">✅ Productividad aumentada</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="text-align: center; margin-top: 20px;">
            <p style="font-size: 1.3rem; color: #666;">
                <strong>Ahora:</strong><br>
                "ventas totales" → Resultado instantáneo
            </p>
        </div>
        """, unsafe_allow_html=True)

def slide_base_datos():
    st.markdown('<p class="section-title">🗄️ Nuestra Base de Datos</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-box">
        <h3 style="text-align: center; font-size: 1.8rem;">Base de datos empresarial normalizada</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="background: #E3F2FD; padding: 25px; border-radius: 15px; height: 100%;">
            <h3 style="color: #1976D2; text-align: center;">📋 Tablas Principales</h3>
            <div class="bullet-point">
                <strong>👥 clientes</strong><br>
                <strong>🛍️ productos</strong><br>
                <strong>🏷️ rubros</strong><br>
                <strong>🏢 sucursales</strong><br>
                <strong>💰 ventas</strong><br>
                <strong>📄 facturas</strong>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: #F3E5F5; padding: 25px; border-radius: 15px; height: 100%;">
            <h3 style="color: #7B1FA2; text-align: center;">🔗 Relaciones</h3>
            <div class="bullet-point">
                productos → rubros<br>
                ventas → clientes<br>
                ventas → sucursales<br>
                facturas → ventas
            </div>
            <p style="text-align: center; margin-top: 20px;">
                <span class="badge badge-success">Integridad Referencial</span>
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background: #FFF3E0; padding: 25px; border-radius: 15px; height: 100%;">
            <h3 style="color: #F57C00; text-align: center;">⚙️ Tecnología</h3>
            <div class="bullet-point">
                <strong>SQLite</strong><br><br>
                ✓ Ligera<br>
                ✓ Sin servidor<br>
                ✓ Portable<br>
                ✓ Perfecta para demos
            </div>
        </div>
        """, unsafe_allow_html=True)

def slide_demo_momento():
    st.markdown('<p class="big-title">🚀 ¡MOMENTO DEMO!</p>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="danger-box" style="text-align: center; padding: 50px;">
        <h1 style="font-size: 4rem; color: #E53935; margin: 0;">⚠️</h1>
        <h2 style="font-size: 2.5rem; margin-top: 20px;">CAMBIAR A LA APP PRINCIPAL</h2>
        <p style="font-size: 1.5rem; margin-top: 30px; color: #666;">
            Vamos a ver el sistema funcionando en vivo
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="highlight-box">
            <h3>📝 Secuencia de Demo</h3>
            <div class="bullet-point">
                <strong>1.</strong> Consulta simple que funciona<br>
                <strong>2.</strong> Mostrar el SQL generado<br>
                <strong>3.</strong> Ver score de confianza<br>
                <strong>4.</strong> Consulta que NO está en el diccionario<br>
                <strong>5.</strong> Agregar esa consulta (Tab 2)<br>
                <strong>6.</strong> Probar nuevamente → ¡Funciona!
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="success-box">
            <h3>💡 Consultas Sugeridas</h3>
            <div class="code-box">
✅ "listar clientes"<br>
✅ "ventas totales"<br>
✅ "mostrar productos"<br>
❌ "productos más caros" (falla inicial)<br>
➕ Agregar: SELECT * FROM productos<br>
&nbsp;&nbsp;&nbsp;&nbsp;ORDER BY precio DESC LIMIT 5;
            </div>
        </div>
        """, unsafe_allow_html=True)

def slide_como_funciona():
    st.markdown('<p class="section-title">🧠 ¿Cómo Funciona por Dentro?</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: #FAFAFA; padding: 40px; border-radius: 15px; border: 3px solid #667eea;">
        <div style="text-align: center; font-size: 1.4rem; line-height: 3;">
            <strong style="font-size: 1.8rem; color: #667eea;">📱 Usuario escribe:</strong> "listar clientes"<br>
            ⬇️<br>
            <strong style="font-size: 1.8rem; color: #7B1FA2;">🔤 Preprocesamiento:</strong> limpieza, normalización<br>
            ⬇️<br>
            <strong style="font-size: 1.8rem; color: #F57C00;">🧠 Embeddings:</strong> texto → vector de números<br>
            ⬇️<br>
            <strong style="font-size: 1.8rem; color: #43A047;">📐 Similitud:</strong> compara con diccionario<br>
            ⬇️<br>
            <strong style="font-size: 1.8rem; color: #1976D2;">✅ Match encontrado:</strong> "mostrar clientes" (95%)<br>
            ⬇️<br>
            <strong style="font-size: 1.8rem; color: #E53935;">💾 Ejecuta SQL:</strong> SELECT * FROM clientes;<br>
            ⬇️<br>
            <strong style="font-size: 1.8rem; color: #667eea;">📊 Muestra resultados</strong> en tabla
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("⏱️ Tiempo Total", "< 1 seg", "Ultra rápido")
    with col2:
        st.metric("🎯 Precisión", "95%+", "Alta confianza")
    with col3:
        st.metric("🔧 Capas", "7", "Modulares")

def slide_diccionario():
    st.markdown('<p class="section-title">📚 El Diccionario: Un Traductor</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-box">
        <h3 style="text-align: center; font-size: 2rem;">Piensen en un traductor Español → Inglés</h3>
        <p style="text-align: center; font-size: 1.5rem; margin-top: 20px;">
            Aquí traducimos: <strong>Español → SQL</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Tabla de ejemplos
    ejemplos_dict = pd.DataFrame({
        '🗣️ Lenguaje Natural': [
            'listar clientes',
            'ventas totales',
            'productos por rubro',
            'mostrar facturas'
        ],
        '⚙️ SQL Generado': [
            'SELECT * FROM clientes;',
            'SELECT SUM(total) FROM ventas;',
            'SELECT rubro_id, COUNT(*) FROM productos GROUP BY rubro_id;',
            'SELECT * FROM facturas;'
        ],
        '🎯 Uso': [
            'Consulta simple',
            'Agregación',
            'Agrupamiento',
            'Consulta simple'
        ]
    })
    
    st.dataframe(ejemplos_dict, use_container_width=True, height=250)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="success-box">
            <h3>✅ Ventajas</h3>
            <div class="bullet-point">
                • Simple de entender<br>
                • Fácil de expandir<br>
                • No requiere reentrenamiento<br>
                • Transparente para el usuario
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="warning-box">
            <h3>⚠️ Pero...</h3>
            <div class="bullet-point">
                • Limitado a patrones conocidos<br>
                • Requiere mantenimiento<br>
                • No genera SQL nuevo<br>
                • Depende del diccionario inicial
            </div>
        </div>
        """, unsafe_allow_html=True)

def slide_embeddings():
    st.markdown('<p class="section-title">🔢 Entendiendo Significados (Embeddings)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-box">
        <h3 style="text-align: center; font-size: 2rem;">¿Cómo sabe que "listar" y "mostrar" son parecidos?</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("""
        <div style="background: #E3F2FD; padding: 30px; border-radius: 15px;">
            <h3 style="color: #1976D2;">📖 Analogía Simple</h3>
            <p style="font-size: 1.4rem; line-height: 2;">
                Cuando ustedes leen <strong>"auto"</strong> y <strong>"carro"</strong>, 
                saben que significan lo mismo, ¿verdad?
            </p>
            <p style="font-size: 1.4rem; line-height: 2; margin-top: 20px;">
                El modelo hace algo similar: convierte palabras en <strong>números</strong> 
                que representan su <strong>significado</strong>.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class="code-box">
<strong>Ejemplo:</strong><br><br>
"listar clientes" → [0.23, -0.45, 0.78, ..., 0.12]<br>
"mostrar clientes" → [0.25, -0.43, 0.76, ..., 0.14]<br>
<br>
<span style="color: #43A047;">→ Vectores casi idénticos = Significados similares</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: #F3E5F5; padding: 30px; border-radius: 15px;">
            <h3 style="color: #7B1FA2; text-align: center;">🎯 Lo Importante</h3>
            <div class="bullet-point">
                ✓ No memoriza palabras exactas<br><br>
                ✓ Entiende el <strong>contexto</strong><br><br>
                ✓ Funciona con sinónimos<br><br>
                ✓ Multilingüe
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class="success-box">
            <p style="text-align: center; font-size: 1.2rem;">
                <strong>Modelo usado:</strong><br>
                MiniLM-L12<br>
                (384 dimensiones)
            </p>
        </div>
        """, unsafe_allow_html=True)

def slide_similitud():
    st.markdown('<p class="section-title">📐 Encontrando Coincidencias</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-box">
        <h3 style="text-align: center; font-size: 2rem;">
            Una vez que tenemos los vectores, ¿cómo encontramos el más parecido?
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 3])
    
    with col1:
        st.markdown("""
        <div style="background: #FFF3E0; padding: 30px; border-radius: 15px;">
            <h3 style="color: #F57C00;">📏 Similitud del Coseno</h3>
            <p style="font-size: 1.3rem; line-height: 2;">
                Mide qué tan "parecidos" son dos vectores calculando el ángulo entre ellos.
            </p>
            <div class="code-box" style="margin-top: 20px;">
<strong>Resultado:</strong> 0 a 1<br>
<br>
1.0 = Idénticos<br>
0.8-1.0 = Muy similares<br>
0.6-0.8 = Similares<br>
< 0.6 = Diferentes
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="highlight-box">
            <h3 style="text-align: center;">🔍 Ejemplo en Acción</h3>
        </div>
        """, unsafe_allow_html=True)
        
        ejemplos_sim = pd.DataFrame({
            'Tu Consulta': ['listar clientes', 'listar clientes', 'listar clientes'],
            'Patrón en Diccionario': ['mostrar clientes', 'ventas totales', 'productos por rubro'],
            'Score': ['0.95', '0.32', '0.28'],
            'Decisión': ['✅ ELEGIR ESTE', '❌ Descartar', '❌ Descartar']
        })
        
        st.dataframe(ejemplos_sim, use_container_width=True, hide_index=True)
        
        st.markdown("""
        <div class="warning-box" style="margin-top: 20px;">
            <p style="text-align: center; font-size: 1.2rem;">
                ⚠️ Si el score es menor a <strong>0.6</strong>, el sistema avisa que tal vez no entendió bien
            </p>
        </div>
        """, unsafe_allow_html=True)

def slide_aprendizaje():
    st.markdown('<p class="section-title">🎓 El Sistema Aprende de Ustedes</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-box">
        <h3 style="text-align: center; font-size: 2rem;">
            Esta es la parte más interesante: ¡Pueden enseñarle cosas nuevas!
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="background: #FFEBEE; padding: 30px; border-radius: 15px; text-align: center; height: 350px;">
            <h2 style="color: #E53935; font-size: 3rem;">1️⃣</h2>
            <h3 style="color: #E53935;">Pregunta Falla</h3>
            <p style="font-size: 1.3rem; margin-top: 20px;">
                "productos más caros"
            </p>
            <p style="font-size: 1.1rem; color: #666; margin-top: 20px;">
                ❌ Score bajo (0.4)<br>
                No está en el diccionario
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: #FFF3E0; padding: 30px; border-radius: 15px; text-align: center; height: 350px;">
            <h2 style="color: #F57C00; font-size: 3rem;">2️⃣</h2>
            <h3 style="color: #F57C00;">Agregar Patrón</h3>
            <p style="font-size: 1.3rem; margin-top: 20px;">
                Tab "Agregar Frase"
            </p>
            <div class="code-box" style="font-size: 0.9rem; margin-top: 20px;">
NL: "productos más caros"<br>
SQL: SELECT * FROM productos<br>
ORDER BY precio DESC LIMIT 5;
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background: #E8F5E9; padding: 30px; border-radius: 15px; text-align: center; height: 350px;">
            <h2 style="color: #43A047; font-size: 3rem;">3️⃣</h2>
            <h3 style="color: #43A047;">¡Funciona!</h3>
            <p style="font-size: 1.3rem; margin-top: 20px;">
                Intentar de nuevo
            </p>
            <p style="font-size: 1.1rem; color: #666; margin-top: 20px;">
                ✅ Score alto (0.98)<br>
                Aprendió en 10 segundos
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="success-box">
        <h3 style="text-align: center; font-size: 1.8rem;">
            💡 Esto significa que el sistema <strong>crece con el uso</strong>
        </h3>
        <p style="text-align: center; font-size: 1.4rem; margin-top: 20px;">
            Cuantas más consultas agreguen, más inteligente se vuelve
        </p>
    </div>
    """, unsafe_allow_html=True)

def slide_limitaciones():
    st.markdown('<p class="section-title">🤔 Siendo Honestos: Limitaciones</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="warning-box">
        <h3 style="text-align: center; font-size: 1.8rem;">
            No es mágico. Tiene limitaciones importantes.
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="danger-box">
            <h3>❌ No Puede Hacer</h3>
            <div class="big-bullet">
                • Generar SQL totalmente nuevo<br>
                • Entender consultas muy complejas<br>
                • Razonar sobre el contexto<br>
                • Combinar múltiples tablas sin ejemplo<br>
                • Corregir SQL incorrecto
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class="code-box">
<strong>Ejemplo que fallaría:</strong><br>
<br>
"Dame los clientes que compraron<br>
productos de electrónica en la<br>
sucursal centro durante el último<br>
trimestre con descuento mayor a 10%"<br>
<br>
<span style="color: #E53935;">❌ Demasiado complejo sin patrón previo</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="success-box">
            <h3>✅ Sí Puede Hacer</h3>
            <div class="big-bullet">
                • Consultas similares a las conocidas<br>
                • Usar sinónimos efectivamente<br>
                • Aprender rápido nuevos patrones<br>
                • Dar feedback de confianza<br>
                • Ejecutar queries instantáneamente
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class="highlight-box">
            <h3 style="text-align: center;">🎯 El Punto Clave</h3>
            <p style="font-size: 1.3rem; text-align: center; margin-top: 15px;">
                Es un <strong>traductor con diccionario</strong>, no un generador de SQL con IA avanzada.
            </p>
            <p style="font-size: 1.2rem; text-align: center; margin-top: 15px; color: #666;">
                Los sistemas reales (ChatGPT, etc.) usan millones de ejemplos,<br>nosotros usamos ~15.
            </p>
        </div>
        """, unsafe_allow_html=True)

def slide_casos_uso():
    st.markdown('<p class="section-title">🌍 Casos de Uso Reales</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-box">
        <h3 style="text-align: center; font-size: 1.8rem;">
            ¿Dónde se usa esto en el mundo real?
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background: #E3F2FD; padding: 30px; border-radius: 15px; margin-bottom: 20px;">
            <h3 style="color: #1976D2;">📊 Business Intelligence</h3>
            <div class="bullet-point">
                • <strong>Microsoft Power BI</strong>: Q&A natural language<br>
                • <strong>Tableau</strong>: Ask Data feature<br>
                • <strong>Google BigQuery</strong>: Natural language queries
            </div>
        </div>
        
        <div style="background: #F3E5F5; padding: 30px; border-radius: 15px;">
            <h3 style="color: #7B1FA2;">🏢 Empresas</h3>
            <div class="bullet-point">
                • Ejecutivos consultando KPIs<br>
                • Analistas sin conocimiento técnico<br>
                • Reportes automáticos por Slack/Teams
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: #E8F5E9; padding: 30px; border-radius: 15px; margin-bottom: 20px;">
            <h3 style="color: #43A047;">🤖 ChatGPT + Plugins</h3>
            <div class="bullet-point">
                • Literalmente lo que vieron hoy<br>
                • Pero con millones de patrones<br>
                • Y contexto conversacional
            </div>
        </div>
        
        <div style="background: #FFF3E0; padding: 30px; border-radius: 15px;">
            <h3 style="color: #F57C00;">🏥 Otros Sectores</h3>
            <div class="bullet-point">
                • <strong>Salud</strong>: Consultar historias clínicas<br>
                • <strong>Legal</strong>: Búsqueda en casos jurídicos<br>
                • <strong>Finanzas</strong>: Análisis de transacciones
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="success-box">
        <h3 style="text-align: center; font-size: 1.6rem;">
            💰 Mercado en crecimiento: <strong>$15.7B USD</strong> proyectado para 2028
        </h3>
    </div>
    """, unsafe_allow_html=True)

def slide_futuro():
    st.markdown('<p class="section-title">🔮 El Futuro: LLMs</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-box">
        <h3 style="text-align: center; font-size: 2rem;">
            Nuestro sistema → Diccionario de 15 patrones
        </h3>
        <h3 style="text-align: center; font-size: 2rem; margin-top: 20px; color: #667eea;">
            Sistemas avanzados → Millones de ejemplos + razonamiento
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background: #E3F2FD; padding: 30px; border-radius: 15px;">
            <h3 style="color: #1976D2; text-align: center;">🎯 Nuestro Enfoque</h3>
            <div class="bullet-point">
                ✓ Embedding-based matching<br>
                ✓ Diccionario predefinido<br>
                ✓ Sin generación de SQL<br>
                ✓ Rápido y ligero<br>
                ✓ Transparente<br>
                ✓ Controlable
            </div>
            <p style="text-align: center; margin-top: 20px;">
                <span class="badge badge-primary">Ideal para Aprender</span>
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: #F3E5F5; padding: 30px; border-radius: 15px;">
            <h3 style="color: #7B1FA2; text-align: center;">🚀 LLMs (GPT-4, Claude)</h3>
            <div class="bullet-point">
                ✓ Generan SQL desde cero<br>
                ✓ Entienden contexto complejo<br>
                ✓ Razonamiento multi-paso<br>
                ✓ Conversaciones naturales<br>
                ✓ Aprenden el schema automáticamente<br>
                ✓ Explican el razonamiento
            </div>
            <p style="text-align: center; margin-top: 20px;">
                <span class="badge badge-warning">Producción Real</span>
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="code-box">
<strong>Ejemplo con LLM:</strong><br>
<br>
Usuario: "¿Cuál fue la sucursal con mejor desempeño el mes pasado?"<br>
<br>
LLM: [Analiza el schema] → [Genera SQL] → [Ejecuta] → [Interpreta]<br>
<br>
Respuesta: "La Sucursal Centro tuvo las mejores ventas en octubre<br>
con $487,320 en total, 23% más que el mes anterior."
    </div>
    """, unsafe_allow_html=True)

def slide_conexion_materia():
    st.markdown('<p class="section-title">🎓 Conexión con lo que Ustedes Saben</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-box">
        <h3 style="text-align: center; font-size: 2rem;">
            Este proyecto combina conceptos que ya conocen
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="success-box">
            <h3>✅ De su materia de BD</h3>
            <div class="big-bullet">
                📋 <strong>SELECT, WHERE, GROUP BY</strong><br>
                → El sistema los genera automáticamente<br><br>
                
                🔗 <strong>Foreign Keys & JOINs</strong><br>
                → Están en nuestro schema<br><br>
                
                📊 <strong>Normalización</strong><br>
                → Separamos rubros, productos, ventas<br><br>
                
                🔒 <strong>Integridad Referencial</strong><br>
                → Garantizada en SQLite
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="highlight-box" style="background: linear-gradient(135deg, #FFF3E0 0%, #FFE0B2 100%); border-left-color: #F57C00;">
            <h3>➕ Lo Nuevo: IA</h3>
            <div class="big-bullet">
                🧠 <strong>Embeddings</strong><br>
                → Representaciones vectoriales<br><br>
                
                📐 <strong>Similitud del Coseno</strong><br>
                → Medida de proximidad<br><br>
                
                🤖 <strong>NLP (Procesamiento de Lenguaje)</strong><br>
                → Entender texto humano<br><br>
                
                🔄 <strong>Machine Learning</strong><br>
                → Modelos preentrenados
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="code-box">
<strong>Comparación Directa:</strong><br>
<br>
Lo que escriben normalmente:<br>
SELECT * FROM clientes WHERE email LIKE '%@gmail.com';<br>
<br>
Lo que hace el sistema:<br>
"clientes con email de gmail" → [Busca patrón] → [Ejecuta SQL]
    </div>
    """, unsafe_allow_html=True)

def slide_cierre():
    st.markdown('<p class="section-title">💭 Para Reflexionar</p>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 50px; border-radius: 20px; color: white;">
            <h2 style="text-align: center; font-size: 2.5rem; margin-bottom: 30px;">
                El futuro no es elegir entre SQL o IA
            </h2>
            <h2 style="text-align: center; font-size: 2.5rem;">
                Es <strong>combinarlos</strong>
            </h2>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="success-box">
            <h3 style="text-align: center;">✅ Lo que Logramos</h3>
            <div class="bullet-point">
                • Integración BD + IA<br>
                • Interfaz accesible<br>
                • Sistema extensible<br>
                • Respuestas en < 1 segundo<br>
                • Arquitectura modular
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="highlight-box" style="background: linear-gradient(135deg, #FFF3E0 0%, #FFE0B2 100%); border-left-color: #F57C00;">
            <h3 style="text-align: center;">🎓 Aprendizajes</h3>
            <div class="bullet-point">
                • NLP práctico<br>
                • Embeddings y similitud<br>
                • Arquitectura de sistemas<br>
                • Limitaciones de IA<br>
                • Diseño de interfaces
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: #E8F5E9; padding: 40px; border-radius: 15px; border: 3px solid #43A047;">
        <h3 style="text-align: center; font-size: 2rem; color: #2E7D32; margin-bottom: 20px;">
            💡 Mensaje Final
        </h3>
        <p style="text-align: center; font-size: 1.5rem; line-height: 2; color: #333;">
            Ustedes ya dominan las <strong>bases de datos</strong>.<br>
            Ahora imaginen qué podrían construir si aprenden un poco de <strong>IA</strong>.<br><br>
            La combinación de ambas es donde está el verdadero potencial.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def slide_preguntas():
    st.markdown('<div class="slide-container">', unsafe_allow_html=True)
    st.markdown('<p class="big-title">❓</p>', unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 60px;">
            <h1 style="font-size: 4rem; color: #667eea; margin-bottom: 30px;">
                ¿Preguntas?
            </h1>
            <p style="font-size: 2rem; color: #666; margin-top: 40px;">
                Gracias por su atención 🙏
            </p>
            
            <div style="margin-top: 60px; padding: 30px; background: linear-gradient(135deg, #E3F2FD 0%, #F3E5F5 100%); border-radius: 15px;">
                <p style="font-size: 1.5rem; margin: 10px 0;">
                    <strong>Bayaslian Santiago</strong>
                </p>
                <p style="font-size: 1.2rem; color: #666; margin: 10px 0;">
                    Tecnicatura en Ciencia de Datos e IA
                </p>
                <p style="font-size: 1.2rem; color: #666;">
                    Instituto Tecnológico Beltrán
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== LISTA DE SLIDES ====================

slides = [
    ("💬 Portada", slide_portada),
    ("🎯 El Gancho", slide_gancho),
    ("⚠️ El Problema", slide_problema),
    ("🗄️ Base de Datos", slide_base_datos),
    ("🚀 DEMO", slide_demo_momento),
    ("🧠 ¿Cómo Funciona?", slide_como_funciona),
    ("📚 El Diccionario", slide_diccionario),
    ("🔢 Embeddings", slide_embeddings),
    ("📐 Similitud", slide_similitud),
    ("🎓 Aprende de Ti", slide_aprendizaje),
    ("🤔 Limitaciones", slide_limitaciones),
    ("🌍 Casos de Uso", slide_casos_uso),
    ("🔮 El Futuro", slide_futuro),
    ("🎓 Conexión BD", slide_conexion_materia),
    ("💭 Reflexión", slide_cierre),
    ("❓ Preguntas", slide_preguntas)
]

# ==================== NAVEGACIÓN ====================

# Mostrar slide actual
current_slide_name, current_slide_func = slides[st.session_state.slide]
current_slide_func()

# Número de slide
st.markdown(f'<div class="slide-number">{st.session_state.slide + 1} / {len(slides)}</div>', unsafe_allow_html=True)

# Controles de navegación
st.markdown("---")
col1, col2, col3, col4, col5 = st.columns([1, 1, 2, 1, 1])

with col1:
    if st.button("⏮️ Primera", use_container_width=True, type="secondary"):
        st.session_state.slide = 0
        st.rerun()

with col2:
    if st.button("◀️ Anterior", use_container_width=True, disabled=(st.session_state.slide == 0), type="secondary"):
        st.session_state.slide -= 1
        st.rerun()

with col3:
    st.markdown(f"""
    <div style="text-align: center; padding: 12px; background: white; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
        <strong style="font-size: 1.3rem; color: #667eea;">{st.session_state.slide + 1} / {len(slides)}</strong>
        <span style="color: #888; margin-left: 20px; font-size: 1.1rem;">{current_slide_name}</span>
    </div>
    """, unsafe_allow_html=True)

with col4:
    if st.button("Siguiente ▶️", use_container_width=True, disabled=(st.session_state.slide == len(slides) - 1), type="primary"):
        st.session_state.slide += 1
        st.rerun()

with col5:
    if st.button("Última ⏭️", use_container_width=True, type="secondary"):
        st.session_state.slide = len(slides) - 1
        st.rerun()

# ==================== SIDEBAR ====================

with st.sidebar:
    st.markdown("""
    <div style="padding: 20px; background: white; border-radius: 10px; margin-bottom: 20px;">
        <h2 style="color: #667eea; text-align: center;">📋 Índice</h2>
    </div>
    """, unsafe_allow_html=True)
    
    for idx, (name, _) in enumerate(slides):
        if idx == st.session_state.slide:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                        padding: 12px; border-radius: 8px; margin: 5px 0; color: white;">
                <strong>➡️ {idx + 1}. {name}</strong>
            </div>
            """, unsafe_allow_html=True)
        else:
            if st.button(f"{idx + 1}. {name}", key=f"nav_{idx}", use_container_width=True):
                st.session_state.slide = idx
                st.rerun()
    
    st.markdown("---")
    st.markdown("""
    <div style="background: #E8F5E9; padding: 20px; border-radius: 10px;">
        <h3 style="color: #2E7D32;">💡 Tips</h3>
        <p style="font-size: 0.9rem;">
            • Usa F11 para pantalla completa<br>
            • Mantén ritmo constante<br>
            • Interactúa con la demo<br>
            • Prepara respuestas comunes<br>
            • ¡Disfruta la presentación!
        </p>
    </div>
    """, unsafe_allow_html=True)

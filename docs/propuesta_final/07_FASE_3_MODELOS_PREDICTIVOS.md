# 7. FASE 3 - MODELOS PREDICTIVOS (Descripción Conceptual)

## ⚠️ IMPORTANTE

**Esta fase NO incluye implementación**. Solo se entrega:
- Catálogo de casos de uso de Machine Learning
- Análisis exploratorio de datos (EDA)
- Propuesta de arquitectura ML
- Roadmap de desarrollo (sin estimación de esfuerzo)

**La implementación se cotizará en proyecto separado** (estimación preliminar: 8-12 semanas).

---

## 7.1. Objetivo de la Fase

**Diseñar la estrategia y arquitectura** para implementación futura de modelos de analítica predictiva y Machine Learning, aprovechando los datos centralizados en el Data Lake.

### Objetivos Específicos

1. ✅ Identificar casos de uso viables de ML/IA
2. ✅ Realizar análisis exploratorio de datos (EDA)
3. ✅ Proponer arquitectura técnica para MLOps
4. ✅ Crear roadmap de implementación (sin estimaciones)
5. ✅ Documentar recomendaciones para siguiente proyecto

---

## 7.2. Alcance de Fase 3 (Solo Descripción)

### ✅ Incluido

- Catálogo de 8-10 casos de uso de ML priorizados
- EDA (Exploratory Data Analysis) con visualizaciones
- Propuesta de arquitectura ML conceptual
- Roadmap cualitativo de implementación
- Recomendaciones técnicas y de negocio

### ❌ NO Incluido

- Desarrollo de modelos predictivos
- Entrenamiento de algoritmos ML
- Deployment de modelos en producción
- MLOps y monitoreo de modelos
- Integración de predicciones en dashboards

---

## 7.3. Casos de Uso de Machine Learning Identificados

Basado en el audio de Lucía (09-oct-2025):

> *"armar predicciones, decir por ejemplo tocando algunas variables de precios, variables de costos, variables de inflación estimada por país y que se yo poner a armar predicciones de venta de los próximos tres años"*

### 7.3.1. Caso de Uso 1: Forecasting de Ventas (Prioridad Alta)

**Descripción:**  
Predecir ventas de los próximos 3 años por producto, país y mes, considerando variables internas (histórico de ventas, estacionalidad, promociones) y externas (inflación, indicadores económicos, competencia).

**Datos Requeridos:**
- Histórico de ventas (VA05, KE24) - mínimo 36 meses
- Variables macroeconómicas (inflación, PIB, tipo de cambio) - fuente externa
- Calendario de promociones/campañas - input manual
- Precios históricos (ZVEL015)
- Stock histórico (ZLEL008)

**Algoritmos Candidatos:**
- **SARIMA** (Seasonal ARIMA) - Serie temporal clásica
- **Prophet** (Facebook) - Manejo de estacionalidad múltiple
- **LSTM** (Long Short-Term Memory) - Deep Learning para series temporales
- **XGBoost/LightGBM** - Gradient Boosting con variables exógenas

**Variables Predictoras:**
- Ventas históricas (lag 1, 3, 6, 12 meses)
- Tendencia y estacionalidad
- Inflación proyectada por país
- Índice de precios
- Eventos especiales (días festivos, campañas)
- Variables dummy por país/producto

**Métricas de Evaluación:**
- MAPE (Mean Absolute Percentage Error) <10%
- RMSE (Root Mean Square Error)
- MAE (Mean Absolute Error)

**Valor de Negocio:**
- Planeación de producción/inventario más precisa
- Optimización de compras de materias primas
- Mejora en asignación de presupuesto comercial
- Reducción de quiebres y obsolescencia

---

### 7.3.2. Caso de Uso 2: Predicción de Costos (Prioridad Alta)

**Descripción:**  
Proyectar costos de producción y logísticos considerando variaciones en precios de materias primas, tipo de cambio, inflación y volúmenes.

**Datos Requeridos:**
- Costos estándar históricos (MM60)
- Precios de compra (ME2L)
- Tipos de cambio históricos - fuente externa
- Inflación por país - fuente externa
- Volúmenes de producción/venta

**Algoritmos Candidatos:**
- **Regresión Lineal Multiple**
- **Random Forest Regressor**
- **Redes Neuronales** (feedforward)

**Variables Predictoras:**
- Precio materias primas (histórico + proyección)
- Tipo de cambio
- Inflación
- Volumen de producción
- Costos de transporte
- Costos de energía

**Valor de Negocio:**
- Mejora en accuracy de presupuestos
- Identificación temprana de desviaciones
- Optimización de pricing
- Negociaciones más informadas con proveedores

---

### 7.3.3. Caso de Uso 3: Predicción de Demanda (Prioridad Media)

**Descripción:**  
Anticipar demanda futura a nivel SKU-Centro-Semana para optimizar niveles de inventario.

**Datos Requeridos:**
- Movimientos de inventario (MB59)
- Órdenes de venta (VA05)
- Stock histórico (ZLEL008)
- Lead times de proveedores (ME2L)

**Algoritmos Candidatos:**
- **Prophet** con variables exógenas
- **LSTM** con atención
- **Temporal Fusion Transformer (TFT)**

**Valor de Negocio:**
- Reducción de costos de inventario (15-25%)
- Mejora en nivel de servicio
- Reducción de obsolescencia

---

### 7.3.4. Caso de Uso 4: Segmentación de Clientes (Prioridad Media)

**Descripción:**  
Agrupar clientes por comportamiento de compra, rentabilidad y potencial para estrategias comerciales diferenciadas.

**Datos Requeridos:**
- Ventas por cliente (KE24)
- Rentabilidad por cliente
- Frecuencia de compra
- Antigüedad del cliente
- Canales utilizados

**Algoritmos Candidatos:**
- **K-Means Clustering**
- **DBSCAN**
- **Hierarchical Clustering**
- **RFM Analysis** (Recency, Frequency, Monetary)

**Valor de Negocio:**
- Personalización de estrategias comerciales
- Identificación de clientes de alto valor
- Optimización de recursos de ventas

---

### 7.3.5. Caso de Uso 5: Detección de Anomalías Financieras (Prioridad Media)

**Descripción:**  
Identificar transacciones contables inusuales o potencialmente fraudulentas.

**Datos Requeridos:**
- Partidas de mayor general (FAGLL03)
- Documentos contables (FB03)
- Patrones históricos

**Algoritmos Candidatos:**
- **Isolation Forest**
- **Autoencoder** (Deep Learning)
- **One-Class SVM**

**Valor de Negocio:**
- Reducción de riesgo de fraude
- Mejora en controles internos
- Auditoría más eficiente

---

### 7.3.6. Caso de Uso 6: Optimización de Precios (Prioridad Baja)

**Descripción:**  
Recomendar precios óptimos por producto-mercado maximizando margen sin perder competitividad.

**Datos Requeridos:**
- Histórico de precios y ventas
- Elasticidad de demanda estimada
- Precios de competencia (si disponible)
- Costos

**Algoritmos Candidatos:**
- **Regresión con optimización**
- **Reinforcement Learning**

---

### 7.3.7. Caso de Uso 7: Predicción de Churn de Clientes (Prioridad Baja)

**Descripción:**  
Predecir qué clientes tienen alto riesgo de dejar de comprar.

**Datos Requeridos:**
- Transacciones históricas
- Patrones de compra
- Interacciones con servicio al cliente

**Algoritmos Candidatos:**
- **Logistic Regression**
- **Random Forest Classifier**
- **XGBoost Classifier**

---

### 7.3.8. Caso de Uso 8: Forecasting de OPEX (Prioridad Baja)

**Descripción:**  
Proyectar gastos operativos por centro de costo para mejor control presupuestario.

**Datos Requeridos:**
- OPEX histórico (KSB1)
- Presupuestos históricos
- Variables de contexto (headcount, volumen operación)

**Algoritmos Candidatos:**
- **SARIMA**
- **Prophet**

---

## 7.4. Análisis Exploratorio de Datos (EDA)

### 7.4.1. Objetivo del EDA

Evaluar la **calidad y viabilidad de los datos** para modelos de ML:
- Completitud de datos históricos
- Presencia de outliers y valores nulos
- Distribuciones estadísticas
- Correlaciones entre variables
- Estacionalidad y tendencias

### 7.4.2. EDA por Caso de Uso

#### EDA 1: Forecasting de Ventas

**Análisis de Series Temporales:**

```python
# Pseudocódigo ilustrativo
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Cargar datos de ventas
df_ventas = load_from_bigquery("SELECT * FROM casa_bi.fact_ventas")

# Análisis de completitud
print(f"Registros totales: {len(df_ventas)}")
print(f"Rango fechas: {df_ventas['fecha'].min()} a {df_ventas['fecha'].max()}")
print(f"Valores nulos: {df_ventas.isnull().sum()}")

# Agregación mensual
ventas_mensual = df_ventas.groupby('fecha')['valor_neto'].sum()

# Descomposición de serie temporal
decomposition = seasonal_decompose(ventas_mensual, model='additive', period=12)
decomposition.plot()

# Identificar estacionalidad
seasonal_pattern = decomposition.seasonal

# Análisis de outliers
Q1 = ventas_mensual.quantile(0.25)
Q3 = ventas_mensual.quantile(0.75)
IQR = Q3 - Q1
outliers = ventas_mensual[(ventas_mensual < Q1 - 1.5*IQR) | (ventas_mensual > Q3 + 1.5*IQR)]
print(f"Outliers detectados: {len(outliers)}")
```

**Resultados Esperados del EDA:**
- ✅ Completitud de datos: ≥95%
- ✅ Estacionalidad clara: Picos en Q4 (fin de año)
- ⚠️ Outliers: COVID-19 (2020-2021) requiere tratamiento
- ✅ Tendencia: Crecimiento promedio 8% anual

#### EDA 2: Predicción de Costos

**Análisis de Correlaciones:**

```python
# Análisis de correlación
import seaborn as sns

# Variables de costo
variables_costo = ['costo_materia_prima', 'tipo_cambio', 'inflacion', 
                   'volumen', 'costo_logistica']

# Matriz de correlación
corr_matrix = df_costos[variables_costo].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')

# Variables más correlacionadas con costo total
print(corr_matrix['costo_total'].sort_values(ascending=False))
```

**Resultados Esperados:**
- Alta correlación: Costo materia prima ↔ Costo total (r=0.85)
- Media correlación: Tipo cambio ↔ Costo total (r=0.60)
- Baja correlación: Inflación ↔ Costo total (r=0.35)

---

## 7.5. Propuesta de Arquitectura ML

### 7.5.1. Stack Tecnológico Recomendado

**Opción 1: Google Cloud Platform (Recomendada - continuidad con BigQuery)**

```
┌─────────────────────────────────────────────────────────┐
│                   GCP ML ARCHITECTURE                   │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  DATA LAYER                                            │
│  ┌──────────────────────────────────────────┐         │
│  │  BigQuery (Data Lake)                    │         │
│  │  - Datos históricos centralizados        │         │
│  │  - Feature store                          │         │
│  └──────────────────────────────────────────┘         │
│                     │                                  │
│                     ▼                                  │
│  DEVELOPMENT LAYER                                     │
│  ┌──────────────────────────────────────────┐         │
│  │  Vertex AI Workbench (Jupyter)           │         │
│  │  - Análisis exploratorio (EDA)           │         │
│  │  - Desarrollo de modelos                 │         │
│  │  - Experimentación                        │         │
│  └──────────────────────────────────────────┘         │
│                     │                                  │
│                     ▼                                  │
│  TRAINING LAYER                                        │
│  ┌──────────────────────────────────────────┐         │
│  │  Vertex AI Training                      │         │
│  │  - Entrenamiento distribuido             │         │
│  │  - Hyperparameter tuning (AutoML)        │         │
│  │  - Model versioning                      │         │
│  └──────────────────────────────────────────┘         │
│                     │                                  │
│                     ▼                                  │
│  DEPLOYMENT LAYER                                      │
│  ┌──────────────────────────────────────────┐         │
│  │  Vertex AI Prediction                    │         │
│  │  - Model serving (REST API)              │         │
│  │  - Batch predictions                      │         │
│  │  - A/B testing                            │         │
│  └──────────────────────────────────────────┘         │
│                     │                                  │
│                     ▼                                  │
│  MONITORING LAYER                                      │
│  ┌──────────────────────────────────────────┐         │
│  │  Vertex AI Model Monitoring              │         │
│  │  - Drift detection                        │         │
│  │  - Performance metrics                    │         │
│  │  - Alerting                               │         │
│  └──────────────────────────────────────────┘         │
│                     │                                  │
│                     ▼                                  │
│  CONSUMPTION LAYER                                     │
│  ┌──────────────────────────────────────────┐         │
│  │  Power BI / Custom Apps                  │         │
│  │  - Visualización de predicciones         │         │
│  │  - Dashboards de ML                       │         │
│  └──────────────────────────────────────────┘         │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**Componentes Clave:**
- **BigQuery ML:** Para modelos simples (regresión, clasificación) directamente en SQL
- **Vertex AI:** Plataforma completa MLOps
- **Cloud Functions:** Orquestación de pipelines
- **Cloud Scheduler:** Reentrenamiento periódico
- **Cloud Storage:** Almacenamiento de artifacts

**Costo Estimado Mensual:** USD $800-1,500 (en producción)

---

**Opción 2: Azure Machine Learning (Si Elanco estandariza en Azure)**

Similar a GCP pero usando:
- Azure ML Studio
- Azure Databricks
- Azure Synapse Analytics

---

### 7.5.2. MLOps Pipeline

**Ciclo de Vida Completo:**

```
1. FEATURE ENGINEERING
   ├─ Extracción de features desde BigQuery
   ├─ Transformaciones (scaling, encoding)
   └─ Feature store (reutilizable)

2. MODEL TRAINING
   ├─ Train/validation/test split
   ├─ Hyperparameter tuning
   ├─ Model selection (comparar algoritmos)
   └─ Model registry (versionado)

3. MODEL EVALUATION
   ├─ Métricas de performance
   ├─ Validación con datos de negocio
   └─ Aprobación stakeholders

4. MODEL DEPLOYMENT
   ├─ Containerización (Docker)
   ├─ Deployment en endpoint REST
   └─ A/B testing (modelo nuevo vs. actual)

5. MONITORING & RETRAINING
   ├─ Monitoreo de drift
   ├─ Tracking de performance
   └─ Reentrenamiento automático (cuando performance < umbral)
```

---

### 7.5.3. Integración con Power BI

**Visualización de Predicciones:**

1. **Predicciones en tiempo real:**
   - Llamada a API de Vertex AI desde Power BI (Python script)
   - Mostrar predicción junto a valores reales
   
2. **Predicciones batch:**
   - Almacenar predicciones en tabla BigQuery
   - Power BI consume tabla de predicciones
   - Dashboard de "Forecast vs. Real"

3. **Dashboard de ML Monitoring:**
   - Métricas de performance de modelos
   - Alertas de drift
   - Comparativo modelos

---

## 7.6. Roadmap de Implementación (Cualitativo)

### Fase Futura 1: MVP de Forecasting de Ventas (8-10 semanas)

**Objetivo:** Implementar primer modelo productivo

**Actividades:**
- Setup de infraestructura Vertex AI
- Feature engineering para ventas
- Desarrollo y entrenamiento de 3 modelos candidatos (SARIMA, Prophet, LSTM)
- Evaluación y selección del mejor modelo
- Deployment en producción
- Integración con Power BI
- Capacitación usuarios

**Entregable:** Modelo de forecasting de ventas operativo con predicciones mensuales para próximos 12 meses.

---

### Fase Futura 2: Predicción de Costos (6-8 semanas)

**Objetivo:** Segundo modelo productivo

**Actividades:**
- Feature engineering para costos
- Desarrollo de modelo de regresión
- Validación con controladores
- Deployment
- Dashboard de análisis de varianza predicho vs. real

---

### Fase Futura 3: Modelos Adicionales (12-16 semanas)

**Objetivo:** Escalar a casos de uso complementarios

**Actividades:**
- Predicción de demanda
- Segmentación de clientes
- Detección de anomalías financieras

---

### Fase Futura 4: MLOps Maduro (4-6 semanas)

**Objetivo:** Automatización completa

**Actividades:**
- CI/CD para modelos ML
- Reentrenamiento automático
- A/B testing framework
- Monitoreo avanzado

---

## 7.7. Consideraciones y Recomendaciones

### 7.7.1. Requisitos de Datos

✅ **Requerimientos Mínimos:**
- Mínimo **36 meses de datos históricos** (3 años)
- Completitud >95% en variables clave
- Calidad de datos validada (sin errores sistemáticos)

⚠️ **Riesgos:**
- Eventos extraordinarios (COVID-19) requieren tratamiento especial
- Cambios estructurales del negocio (fusiones, nuevas líneas) afectan modelos

### 7.7.2. Equipo Requerido

**Para implementación futura:**
- 1 Data Scientist (ML Engineer)
- 1 MLOps Engineer
- 1 Analista de Negocio (Subject Matter Expert)
- Soporte de equipo actual (Lucía, JMB)

### 7.7.3. Inversión Estimada

**Proyecto completo de ML (3 modelos):**
- Desarrollo: USD $20,000-$30,000
- Infraestructura GCP (1 año): USD $10,000-$15,000
- **Total:** USD $30,000-$45,000

**Duración:** 6-8 meses para MVP + 2 modelos

### 7.7.4. ROI Esperado

**Beneficios cuantificables:**
- Reducción inventario: 15-20% (USD $150K-$200K/año)
- Mejora accuracy presupuesto: 25-30% ($100K/año)
- Reducción obsolescencia: 10-15% ($50K/año)

**ROI:** 200-300% en primer año

---

## 7.8. Entregables de Fase 3

✅ **Catálogo de Casos de Uso ML** (8 casos priorizados)  
✅ **Análisis Exploratorio de Datos (EDA)** con visualizaciones  
✅ **Propuesta de Arquitectura ML** (diagramas GCP/Azure)  
✅ **Roadmap de Implementación** (4 fases cualitativas)  
✅ **Recomendaciones Técnicas y de Negocio**  
✅ **Estimación Preliminar de Inversión** (siguiente proyecto)

---

## 7.9. Próximos Pasos (Post Fase 3)

1. **Evaluación de propuesta ML** por Management
2. **Decisión de inversión** en proyecto ML (Go/No-Go)
3. **Priorización de casos de uso** (consenso con negocio)
4. **Solicitud de cotización detallada** para implementación
5. **Kick-off de proyecto ML** (si aprobado)

---

*Siguiente sección: [08_ESTIMACION_DE_ESFUERZOS_Y_COSTOS.md](08_ESTIMACION_DE_ESFUERZOS_Y_COSTOS.md)*

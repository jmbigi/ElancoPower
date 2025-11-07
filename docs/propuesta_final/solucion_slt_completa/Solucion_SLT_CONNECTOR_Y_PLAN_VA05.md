# BigQuery Connector for SAP (Basado en SLT)
## SOLUCIÓN COMPLETA IMPLEMENTABLE PARA ELANCO POWER

> **📖 DOCUMENTACIÓN COMPLETA EN 4 ARCHIVOS:**
> 1. **INDICE_GENERAL.md** - Empieza aquí para navegar toda la documentación
> 2. **RESUMEN_EJECUTIVO_SLT.md** - Para ejecutivos y sponsors (15 min)
> 3. **README_SOLUCION_COMPLETA_SLT.md** - Para project managers (30 min)
> 4. **Este documento (PARTE 1)** - Guía técnica de implementación (FASES 1-3)
> 5. **Solucion_SLT_CONNECTOR_Y_PLAN_VA05_PARTE2.md** - Monitoreo, troubleshooting, cronograma y costos
>
> **Total:** 50+ scripts funcionales, 10 semanas implementación, 70 días-persona

---

## 📑 CONTENIDO DE ESTE DOCUMENTO (PARTE 1)

### Secciones Incluidas:
- ✅ Arquitectura y componentes clave
- ✅ Recursos humanos requeridos (7 roles)
- ✅ FASE 1: Prerrequisitos e Infraestructura (Semanas 1-2)
  - Instalación SAP SLT Server
  - Instalación BigQuery Connector
  - Configuración GCP
  - SAP Cloud Connector
  - Permisos SAP
- ✅ FASE 2: Configuración SLT y Replicación (Semanas 3-5)
  - Configuración RFC
  - Configuración LTRC
  - Carga inicial (6 tablas)
  - Verificación de datos
  - Activación CDC
- ✅ FASE 3: Data Products y Vistas (Semana 6)
  - Vista VA05_SALES_ORDERS
  - Vistas de KPIs
  - Vistas materializadas
  - Diccionario de datos
- ✅ FASE 4: Monitoreo (inicio) (Semana 7)
  - Scripts de monitoreo SLT
  - Cloud Monitoring setup

### ⏭️ Continúa en PARTE 2:
- FASE 4: Monitoreo completo (dashboards, alertas)
- Problemas comunes y soluciones (5 problemas detallados)
- Cronograma detallado (10 semanas, 70 días-persona)
- Entregables finales del proyecto
- Costos estimados (Infraestructura: $55,200 año 1)
- Plan de soporte post-implementación
- Criterios de aceptación

---

## 🔄 Arquitectura BigQuery Connector for SAP (Basado en SLT)

La Opción 1B es la arquitectura estándar recomendada por SAP y Google cuando la **semántica de negocio** y la **integridad de los datos a nivel de aplicación SAP** son críticas. Esta solución utiliza el servidor **SAP Landscape Transformation (SLT)** como *middleware* primario.

### 📝 Componentes Clave y Flujo de Trabajo

| Componente | Rol Principal | Justificación |
| :--- | :--- | :--- |
| **SAP Source System (S/4HANA)** | Fuente de datos transaccionales. | El sistema principal donde residen las tablas de aplicación y se generan los logs de cambio (CDC). |
| **SAP Landscape Transformation Server (SLT)** | **Motor de Replicación ABAP.** Lee los logs de cambio del sistema fuente, traduce las estructuras de las tablas de SAP, y gestiona el *Delta Queue*. | Componente SAP que asegura la integridad lógica y la continuidad de la replicación incremental. |
| **BigQuery Connector for SAP** | **Software ABAP Add-on** instalado en el servidor SLT. | Utiliza **RFCs** (Remote Function Calls) para la comunicación con el sistema SAP fuente y establece el protocolo de transferencia con la API de BigQuery. |
| **SAP Cloud Connector** | **Túnel de Red.** (Necesario si SLT es *on-premise*). Asegura la comunicación saliente segura desde el SLT hacia la API de BigQuery en Google Cloud Platform (GCP). | Proporciona un canal seguro **sin abrir puertos de firewall entrantes** al centro de datos. |
| **Google Cloud BigQuery** | **Destino Final (Data Warehouse).** | Recibe los datos replicados del Conector SLT, cargándolos directamente en tablas para análisis. |

---

## 👥 RECURSOS HUMANOS REQUERIDOS

### Equipo de Implementación

| Rol | Cantidad | Experiencia Requerida | Responsabilidades | Esfuerzo (días) |
|-----|----------|----------------------|-------------------|-----------------|
| **SAP Basis Senior** | 1 | 5+ años en SAP Basis, SLT, administración de servidores SAP | Instalación y configuración SLT, permisos, RFC, monitoring | 15 días |
| **SAP ABAP Developer** | 1 | 3+ años en ABAP, conocimiento de tablas SAP SD/MM | Configuración de transformaciones, validación de datos, debugging | 10 días |
| **Google Cloud Architect** | 1 | 3+ años en GCP, BigQuery, IAM, networking | Configuración BigQuery, Service Accounts, IAM, Cloud Connector | 8 días |
| **SAP SD/MM Functional** | 1 | 5+ años en módulos SD/MM, conocimiento de VA05, ME2N, etc. | Validación funcional, mapeo de transacciones a tablas, testing | 7 días |
| **Data Engineer** | 1 | 3+ años en SQL, BigQuery, modelado dimensional | Creación de vistas, materialización, optimización queries | 10 días |
| **DevOps Engineer** | 1 | 3+ años en automation, scripts bash/python, monitoring | Scripts de deployment, monitoring, alertas, documentación técnica | 8 días |
| **Project Manager** | 1 | PMP o similar, experiencia en proyectos SAP-Cloud | Coordinación, seguimiento, gestión de riesgos | 12 días |

**Total Esfuerzo Estimado:** 70 días-persona (10 semanas calendario con equipo paralelo)

**Total Esfuerzo Estimado:** 70 días-persona (10 semanas calendario con equipo paralelo)

---

## 🛠️ PLAN DE IMPLEMENTACIÓN COMPLETO VA05 (Órdenes de Venta)

La transacción **VA05** muestra las Órdenes de Venta Abiertas, requiriendo principalmente las tablas **VBAK** (Cabecera) y **VBAP** (Posiciones). El siguiente plan detalla la implementación completa.

---

## 📦 FASE 1: PRERREQUISITOS E INFRAESTRUCTURA (Semanas 1-2)

### 1.1 Instalación y Configuración SAP SLT Server

**Responsable:** SAP Basis Senior

#### Checklist de Instalación
```bash
# Verificación de prerrequisitos del servidor
# Sistema operativo: SUSE Linux Enterprise Server 15 o RHEL 8
# RAM mínima: 32 GB (recomendado 64 GB para producción)
# CPU: 8 cores mínimo
# Disco: 500 GB SSD para datos temporales y logs
```

#### Script de Verificación de Sistema
```bash
#!/bin/bash
# verify_slt_prereqs.sh
# Verificación de prerrequisitos para SAP SLT Server

echo "=== Verificación de Prerrequisitos SAP SLT ==="
echo ""

# Verificar OS
echo "1. Sistema Operativo:"
cat /etc/os-release | grep -E "^(NAME|VERSION)="
echo ""

# Verificar RAM
echo "2. Memoria RAM:"
total_ram=$(free -g | awk '/^Mem:/{print $2}')
echo "RAM Total: ${total_ram} GB"
if [ "$total_ram" -lt 32 ]; then
    echo "⚠️  ADVERTENCIA: Se requieren al menos 32 GB de RAM"
else
    echo "✓ RAM suficiente"
fi
echo ""

# Verificar CPU
echo "3. CPU Cores:"
cpu_cores=$(nproc)
echo "Cores disponibles: ${cpu_cores}"
if [ "$cpu_cores" -lt 8 ]; then
    echo "⚠️  ADVERTENCIA: Se recomiendan al menos 8 cores"
else
    echo "✓ CPU suficiente"
fi
echo ""

# Verificar espacio en disco
echo "4. Espacio en Disco:"
df -h / | tail -1
disk_space=$(df -BG / | tail -1 | awk '{print $4}' | sed 's/G//')
if [ "$disk_space" -lt 500 ]; then
    echo "⚠️  ADVERTENCIA: Se recomiendan al menos 500 GB libres"
else
    echo "✓ Espacio suficiente"
fi
echo ""

# Verificar conectividad a SAP source system
echo "5. Conectividad SAP Source System:"
read -p "Ingrese hostname del SAP Source: " sap_host
read -p "Ingrese puerto (ej. 3300): " sap_port
nc -zv "$sap_host" "$sap_port" 2>&1
echo ""

# Verificar conectividad a Google Cloud
echo "6. Conectividad Google Cloud:"
ping -c 3 bigquery.googleapis.com
echo ""

echo "=== Verificación Completa ==="
```

#### Instalación SLT (Pasos Detallados)

**Paso 1: Obtener el software**
- Descargar SAP Landscape Transformation Server desde SAP Service Marketplace
- Versión recomendada: SLT 2.0 SP14 o superior (compatible con S/4HANA)
- Download ID: 73554900100900002785

**Paso 2: Instalación usando SWPM**
```bash
# Ejecutar SAP Software Provisioning Manager
cd /path/to/swpm
./sapinst SAPINST_USE_HOSTNAME=slt-server.elanco.local
```

**Parámetros de instalación:**
- SID: SLT
- Instance Number: 00
- Schema user: SAPSR3
- Database: HANA 2.0 SPS06 (mínimo, requerido para S/4HANA)

**Paso 3: Post-instalación**
```bash
# Verificar instalación
su - sltadm
sapcontrol -nr 00 -function GetProcessList

# Aplicar notas SAP críticas
# SAP Note 2750281 - BigQuery Connector for SAP prerequisites
# SAP Note 2890171 - SLT Performance optimization
# SAP Note 2935091 - SLT 2.0 SP14 corrections
```

### 1.2 Instalación BigQuery Connector for SAP

**Responsable:** SAP ABAP Developer + SAP Basis Senior

#### Instalación del Add-on ABAP

```abap
* Descargar el BigQuery Connector Add-on desde Google Cloud Marketplace
* Package: /GOOG/BIGQUERY_CONNECTOR
* Version: 2.3 o superior

* Instalación usando transacción SAINT:
* 1. Ejecutar transacción SAINT
* 2. Seleccionar "Load Support Package from front-end"
* 3. Cargar archivo K900001.SAR
* 4. Importar componente /GOOG/BIGQUERY_CONNECTOR
* 5. Activar componente
```

#### Configuración del Connector

**Transacción: /GOOG/BQCONFIG**

```abap
* ============================================
* Script ABAP de configuración inicial
* Ejecutar en SE38 o SE80
* ============================================

REPORT z_configure_bq_connector.

DATA: lv_project_id TYPE string,
      lv_dataset_id TYPE string,
      lv_service_account TYPE string,
      lv_key_file TYPE string.

* Parámetros de configuración
lv_project_id = 'elanco-power-analytics'.
lv_dataset_id = 'SAP_SD_REPLICAS'.
lv_service_account = 'slt-replication@elanco-power-analytics.iam.gserviceaccount.com'.
lv_key_file = '/usr/sap/SLT/keys/elanco-bq-key.json'.

* Llamar función de configuración
CALL FUNCTION '/GOOG/BQ_SET_CONNECTION'
  EXPORTING
    iv_project_id       = lv_project_id
    iv_dataset_id       = lv_dataset_id
    iv_service_account  = lv_service_account
    iv_key_file_path    = lv_key_file
  EXCEPTIONS
    configuration_error = 1
    OTHERS             = 2.

IF sy-subrc = 0.
  WRITE: / 'Configuración exitosa de BigQuery Connector'.
ELSE.
  WRITE: / 'Error en configuración:', sy-subrc.
ENDIF.
```

### 1.3 Configuración Google Cloud Platform

**Responsable:** Google Cloud Architect

#### 1.3.1 Crear Proyecto GCP

```bash
#!/bin/bash
# setup_gcp_project.sh
# Configuración inicial de proyecto GCP para SLT

PROJECT_ID="elanco-power-analytics"
REGION="us-central1"
DATASET_ID="SAP_SD_REPLICAS"

# Crear proyecto
gcloud projects create $PROJECT_ID \
  --name="Elanco Power Analytics" \
  --labels=environment=production,application=sap-replication

# Configurar proyecto activo
gcloud config set project $PROJECT_ID

# Habilitar APIs necesarias
echo "Habilitando APIs de GCP..."
gcloud services enable bigquery.googleapis.com
gcloud services enable bigquerystorage.googleapis.com
gcloud services enable cloudresourcemanager.googleapis.com
gcloud services enable iam.googleapis.com
gcloud services enable logging.googleapis.com
gcloud services enable monitoring.googleapis.com

echo "✓ APIs habilitadas correctamente"
```

#### 1.3.2 Crear Service Account

```bash
#!/bin/bash
# create_service_account.sh

PROJECT_ID="elanco-power-analytics"
SA_NAME="slt-replication"
SA_DISPLAY_NAME="SAP SLT Replication Service Account"
SA_EMAIL="${SA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com"
KEY_FILE="./elanco-bq-key.json"

# Crear Service Account
gcloud iam service-accounts create $SA_NAME \
  --display-name="$SA_DISPLAY_NAME" \
  --description="Service account para replicación SAP SLT a BigQuery"

# Asignar roles necesarios
echo "Asignando roles IAM..."
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:${SA_EMAIL}" \
  --role="roles/bigquery.dataEditor"

gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:${SA_EMAIL}" \
  --role="roles/bigquery.jobUser"

gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:${SA_EMAIL}" \
  --role="roles/logging.logWriter"

# Crear y descargar clave
echo "Generando clave JSON..."
gcloud iam service-accounts keys create $KEY_FILE \
  --iam-account=$SA_EMAIL

echo "✓ Service Account creado y configurado"
echo "✓ Clave guardada en: $KEY_FILE"
echo ""
echo "⚠️  IMPORTANTE: Transfiera este archivo de forma segura al servidor SLT"
echo "   Ubicación destino: /usr/sap/SLT/keys/elanco-bq-key.json"
echo "   Permisos: chmod 400 y chown sltadm:sapsys"
```

#### 1.3.3 Crear Dataset BigQuery

```bash
#!/bin/bash
# create_bigquery_dataset.sh

PROJECT_ID="elanco-power-analytics"
DATASET_ID="SAP_SD_REPLICAS"
LOCATION="us-central1"

# Crear dataset
bq mk \
  --dataset \
  --location=$LOCATION \
  --description="Dataset para réplicas de tablas SAP SD (Sales & Distribution)" \
  --default_table_expiration=0 \
  --default_partition_expiration=0 \
  --label=source:sap \
  --label=module:sd \
  --label=environment:production \
  ${PROJECT_ID}:${DATASET_ID}

echo "✓ Dataset ${DATASET_ID} creado en ${LOCATION}"

# Crear dataset adicional para staging
bq mk \
  --dataset \
  --location=$LOCATION \
  --description="Dataset staging para procesamiento temporal" \
  --default_table_expiration=604800 \
  --label=source:sap \
  --label=type:staging \
  ${PROJECT_ID}:SAP_STAGING

echo "✓ Dataset SAP_STAGING creado"

# Crear dataset para vistas analíticas
bq mk \
  --dataset \
  --location=$LOCATION \
  --description="Vistas analíticas y data products para usuarios finales" \
  --label=source:sap \
  --label=type:analytics \
  ${PROJECT_ID}:SAP_ANALYTICS

echo "✓ Dataset SAP_ANALYTICS creado"
```

### 1.4 Configuración SAP Cloud Connector

**Responsable:** Google Cloud Architect + SAP Basis Senior

#### 1.4.1 Instalación Cloud Connector

```bash
#!/bin/bash
# install_cloud_connector.sh
# Instalación de SAP Cloud Connector para túnel seguro

# Descargar SAP Cloud Connector
# URL: https://tools.hana.ondemand.com/#cloud
wget https://tools.hana.ondemand.com/additional/sapcc-2.16.0-linux-x64.zip

# Extraer y preparar
unzip sapcc-2.16.0-linux-x64.zip
cd sapcc-2.16.0

# Instalar
sudo ./install.sh

# Iniciar servicio
sudo systemctl start scc_daemon
sudo systemctl enable scc_daemon

# Verificar status
sudo systemctl status scc_daemon

echo "✓ SAP Cloud Connector instalado"
echo "  Acceder a: https://localhost:8443"
echo "  Usuario inicial: Administrator"
echo "  Password inicial: manage"
```

#### 1.4.2 Configuración del Túnel

```javascript
// Configuración Cloud Connector (via UI en https://localhost:8443)
// O mediante API REST

{
  "subaccount": {
    "region": "us-central1",
    "subaccountName": "Elanco Power Analytics",
    "displayName": "Elanco SAP to BigQuery Tunnel",
    "locationId": "cf-us10"
  },
  "cloudResources": [
    {
      "virtualHost": "bigquery.googleapis.com",
      "virtualPort": 443,
      "internalHost": "bigquery.googleapis.com",
      "internalPort": 443,
      "protocol": "HTTPS",
      "description": "BigQuery API endpoint",
      "accessPolicy": "PATH",
      "paths": [
        "/bigquery/v2/**",
        "/upload/bigquery/v2/**"
      ]
    }
  ],
  "onPremiseResources": [
    {
      "virtualHost": "sap-source.elanco.local",
      "virtualPort": 3300,
      "internalHost": "sap-prod.elanco.local",
      "internalPort": 3300,
      "protocol": "RFC",
      "description": "SAP ECC Production System"
    }
  ]
}
```

### 1.5 Configuración de Permisos SAP

**Responsable:** SAP Basis Senior

#### Script de Creación de Usuario de Replicación

```abap
*----------------------------------------------------------------------*
* Program: Z_CREATE_SLT_REPLICATION_USER
* Purpose: Crear usuario técnico para replicación SLT con permisos mínimos necesarios
*----------------------------------------------------------------------*
REPORT z_create_slt_replication_user.

DATA: lt_bapilogond TYPE TABLE OF bapilogond,
      lt_bapiusert  TYPE TABLE OF bapiusert,
      lt_bapiprof   TYPE TABLE OF bapiprof,
      lt_return     TYPE TABLE OF bapiret2,
      ls_bapilogond TYPE bapilogond,
      ls_bapiusert  TYPE bapiusert,
      ls_bapiprof   TYPE bapiprof,
      lv_username   TYPE xuusername VALUE 'SLT_REPL'.

* Datos de login
ls_bapilogond-ustyp = 'B'.  " Tipo: Usuario técnico/sistema
ls_bapilogond-gltgv = '20251231'.  " Válido hasta
ls_bapilogond-gltgb = '20250101'.  " Válido desde
ls_bapilogond-usclass = 'REF'.     " Clase de usuario: Referencia
APPEND ls_bapilogond TO lt_bapilogond.

* Descripción
ls_bapiusert-langu = 'E'.
ls_bapiusert-useralias = 'SLT Replication User'.
APPEND ls_bapiusert TO lt_bapiusert.

* Perfiles de autorización necesarios
ls_bapiprof-bapiprof = 'S_A.SYSTEM'.  " Perfil sistema para RFC
APPEND ls_bapiprof TO lt_bapiprof.

ls_bapiprof-bapiprof = 'Z_SLT_REPLICATION'.  " Perfil custom (crear previamente)
APPEND ls_bapiprof TO lt_bapiprof.

* Crear usuario
CALL FUNCTION 'BAPI_USER_CREATE1'
  EXPORTING
    username    = lv_username
  TABLES
    logondata   = lt_bapilogond
    description = lt_bapiusert
    profiles    = lt_bapiprof
    return      = lt_return.

* Verificar resultado
IF line_exists( lt_return[ type = 'E' ] ).
  WRITE: / 'Error al crear usuario:'.
  LOOP AT lt_return INTO DATA(ls_return) WHERE type = 'E'.
    WRITE: / ls_return-message.
  ENDLOOP.
ELSE.
  WRITE: / 'Usuario SLT_REPL creado exitosamente'.
  
  * Commit
  CALL FUNCTION 'BAPI_TRANSACTION_COMMIT'
    EXPORTING
      wait = 'X'.
ENDIF.
```

#### Perfil de Autorización Z_SLT_REPLICATION

```abap
*----------------------------------------------------------------------*
* Objetos de autorización necesarios para usuario SLT_REPL
* Crear mediante transacción PFCG
*----------------------------------------------------------------------*

* Nombre del rol: Z_SLT_REPLICATION
* Descripción: Rol para replicación SLT a BigQuery

* Autorizaciones necesarias:
* 
* 1. S_RFC - Autorización para llamadas RFC
*    RFC_TYPE: FUGR (Function Group)
*    RFC_NAME: * (todos los grupos de funciones necesarios)
*    ACTVT: 16 (Execute)
*
* 2. S_TABU_DIS - Autorización para lectura de tablas
*    DICBERCLS: SD_VBAK (Cabecera órdenes venta)
*    DICBERCLS: SD_VBAP (Posiciones órdenes venta)  
*    DICBERCLS: &NC& (Tablas sin clase)
*    ACTVT: 03 (Display)
*
* 3. S_TABU_NAM - Autorización por nombre de tabla
*    TABLE: VBAK
*    TABLE: VBAP
*    TABLE: VBUK (Status documento)
*    TABLE: VBUP (Status posición)
*    TABLE: KNA1 (Maestro clientes)
*    TABLE: MARA (Maestro materiales)
*    ACTVT: 03 (Display)
*
* 4. S_TABU_CLI - Autorización mandante
*    CLIIDMAINT: X (Cross-client maintenance)
*
* 5. S_BTCH_JOB - Autorización para jobs background
*    JOBACTION: RELE (Release)
*    JOBGROUP: * (Todos los grupos)
*
* 6. S_DATASET - Autorización para archivos (logs)
*    ACTVT: 34 (Create/Write)
*    PROGRAM: /GOOG/*
*    FILENAME: /usr/sap/SLT/logs/*
```

---

## 📦 FASE 2: CONFIGURACIÓN SLT Y REPLICACIÓN (Semanas 3-5)

---

## 📦 FASE 2: CONFIGURACIÓN SLT Y REPLICACIÓN (Semanas 3-5)

### 2.1 Configuración Conexión RFC al Sistema Fuente

**Responsable:** SAP Basis Senior

#### Crear RFC Destination (Transacción SM59)

```abap
*----------------------------------------------------------------------*
* Configuración RFC Connection desde SLT a SAP Source
* Transacción: SM59
*----------------------------------------------------------------------*

* Datos de la conexión RFC:
* RFC Destination: SAP_SOURCE_PRD
* Connection Type: 3 (ABAP Connection)
* Description: Conexión a SAP S/4HANA Producción para SLT

* Technical Settings:
* Target Host: sap-prod.elanco.local
* System Number: 00
* Load Balancing: Yes
* Message Server: sap-msg.elanco.local
* Logon Group: SPACE (default)

* Logon & Security:
* Client: 100
* User: SLT_REPL (usuario técnico creado previamente)
* Language: EN
* Current User: No (usar credenciales explícitas)

* Special Options:
* Trusted System: No
* SSO: No
```

#### Script de Prueba de Conexión RFC

```abap
*----------------------------------------------------------------------*
* Program: Z_TEST_RFC_CONNECTION
* Purpose: Verificar conectividad RFC a sistema fuente
*----------------------------------------------------------------------*
REPORT z_test_rfc_connection.

DATA: lv_dest TYPE rfcdest VALUE 'SAP_SOURCE_PRD',
      lt_tables TYPE TABLE OF dd02l,
      lv_count TYPE i.

* Test 1: Verificar conexión básica
WRITE: / 'Test 1: Verificación de conexión RFC'.
CALL FUNCTION 'RFC_PING'
  DESTINATION lv_dest
  EXCEPTIONS
    communication_failure = 1 MESSAGE TEXT-001
    system_failure        = 2 MESSAGE TEXT-002.

IF sy-subrc = 0.
  WRITE: / '✓ Conexión RFC exitosa'.
ELSE.
  WRITE: / '✗ Error en conexión RFC:', TEXT-001.
  EXIT.
ENDIF.

* Test 2: Verificar lectura de metadata de tablas
WRITE: / 'Test 2: Lectura de metadata tablas SD'.
CALL FUNCTION 'DD_TABL_EXPAND'
  DESTINATION lv_dest
  EXPORTING
    dd02l_n_tab = 'VBAK'
  TABLES
    dd02l_tab   = lt_tables
  EXCEPTIONS
    OTHERS      = 1.

IF sy-subrc = 0.
  WRITE: / '✓ Metadata de tabla VBAK leída correctamente'.
ELSE.
  WRITE: / '✗ Error al leer metadata de VBAK'.
ENDIF.

* Test 3: Verificar lectura de datos
WRITE: / 'Test 3: Lectura de datos de VBAK'.
SELECT COUNT(*) FROM vbak CONNECTION (lv_dest) INTO lv_count UP TO 1 ROWS.
IF sy-subrc = 0.
  WRITE: / '✓ Lectura de datos VBAK exitosa'.
ELSE.
  WRITE: / '✗ Error al leer datos de VBAK'.
ENDIF.

WRITE: / ''.
WRITE: / '=== Resumen de pruebas ==='.
WRITE: / 'Destination RFC:', lv_dest.
WRITE: / 'Todas las pruebas completadas'.
```

### 2.2 Configuración SLT Replication (Transacción LTRC)

**Responsable:** SAP ABAP Developer + SAP Basis Senior

#### Paso 1: Crear Configuración de Replicación

```abap
*----------------------------------------------------------------------*
* Configuración en LTRC (Landscape Transformation Configuration)
*----------------------------------------------------------------------*

* 1. Ejecutar transacción LTRC
* 2. Click en "New Configuration"

* Configuration Name: BQ_SD_REPLICATION
* Description: Replicación módulo SD a BigQuery
* Source System: SAP_SOURCE_PRD (RFC destination)
* Target System: /GOOG/BIGQUERY (BigQuery Connector)
* Schema Name: SAP_SD_REPLICAS (dataset en BigQuery)

* Advanced Settings:
* - Data Transfer Jobs: 8 (paralelismo)
* - Batch Size: 50000 registros
* - Commit Interval: 10000 registros
* - Error Handling: Stop on Error = No, Log and Continue = Yes
* - Logging Level: Info (cambiar a Debug para troubleshooting)
```

#### Paso 2: Configurar Tablas para Replicación

**Tabla VBAK - Cabecera de Órdenes de Venta**

```sql
-- Configuración en LTRC para tabla VBAK
-- Tabla: VBAK
-- Descripción: Sales Document: Header Data

-- Modo de Replicación: Replication
-- Carga Inicial: Yes
-- Replicación Delta: Yes (CDC via database logs)

-- Filtros de datos (WHERE clause):
-- VBAK~AUART IN ('OR', 'ZOR', 'ZSER')  -- Solo tipos de documento relevantes
-- VBAK~VKORG = '1000'                   -- Solo organización de ventas 1000

-- Campos a replicar: ALL (*)
-- Campos sensibles a excluir: ninguno

-- Transformaciones:
-- NETWR: Convertir a USD si es necesario
-- ERDAT: Mantener formato SAP (YYYYMMDD)

-- Configuración de performance:
-- Package Size: 10000 (VBAK es tabla mediana)
-- Initial Load Method: Table Splitting (por rangos de VBELN)
-- Number of Jobs: 4
```

**Tabla VBAP - Posiciones de Órdenes de Venta**

```sql
-- Configuración en LTRC para tabla VBAP
-- Tabla: VBAP  
-- Descripción: Sales Document: Item Data

-- Modo de Replicación: Replication
-- Carga Inicial: Yes
-- Replicación Delta: Yes (CDC via database logs)

-- Filtros de datos (WHERE clause):
-- VBAP~ABGRU = ''  -- Excluir posiciones rechazadas

-- Campos a replicar: ALL (*)

-- Configuración de performance:
-- Package Size: 50000 (VBAP es tabla grande)
-- Initial Load Method: Table Splitting (por rangos de VBELN + POSNR)
-- Number of Jobs: 8
-- Read Frequency (Delta): 30 segundos
```

#### Script de Configuración Automatizada

```abap
*----------------------------------------------------------------------*
* Program: Z_SETUP_SLT_REPLICATION
* Purpose: Configurar automáticamente replicación de tablas SD
*----------------------------------------------------------------------*
REPORT z_setup_slt_replication.

DATA: lv_config_name TYPE ltrc_config_name VALUE 'BQ_SD_REPLICATION',
      lt_tables      TYPE TABLE OF ltrc_table_config,
      ls_table       TYPE ltrc_table_config.

* Configuración tabla VBAK
CLEAR ls_table.
ls_table-tabname = 'VBAK'.
ls_table-repl_mode = 'R'.  " Replication mode
ls_table-load_mode = 'I'.  " Initial load
ls_table-delta_mode = 'Y'. " Delta active
ls_table-package_size = 10000.
ls_table-num_jobs = 4.
ls_table-where_clause = `AUART IN ('OR','ZOR','ZSER') AND VKORG = '1000'`.
APPEND ls_table TO lt_tables.

* Configuración tabla VBAP
CLEAR ls_table.
ls_table-tabname = 'VBAP'.
ls_table-repl_mode = 'R'.
ls_table-load_mode = 'I'.
ls_table-delta_mode = 'Y'.
ls_table-package_size = 50000.
ls_table-num_jobs = 8.
ls_table-where_clause = `ABGRU = ''`.
APPEND ls_table TO lt_tables.

* Configuración tabla VBUK (Status documento)
CLEAR ls_table.
ls_table-tabname = 'VBUK'.
ls_table-repl_mode = 'R'.
ls_table-load_mode = 'I'.
ls_table-delta_mode = 'Y'.
ls_table-package_size = 10000.
ls_table-num_jobs = 4.
APPEND ls_table TO lt_tables.

* Configuración tabla VBUP (Status posición)
CLEAR ls_table.
ls_table-tabname = 'VBUP'.
ls_table-repl_mode = 'R'.
ls_table-load_mode = 'I'.
ls_table-delta_mode = 'Y'.
ls_table-package_size = 50000.
ls_table-num_jobs = 8.
APPEND ls_table TO lt_tables.

* Tablas maestras relacionadas
* KNA1 - Maestro de clientes
CLEAR ls_table.
ls_table-tabname = 'KNA1'.
ls_table-repl_mode = 'R'.
ls_table-load_mode = 'I'.
ls_table-delta_mode = 'Y'.
ls_table-package_size = 5000.
ls_table-num_jobs = 2.
APPEND ls_table TO lt_tables.

* MARA - Maestro de materiales
CLEAR ls_table.
ls_table-tabname = 'MARA'.
ls_table-repl_mode = 'R'.
ls_table-load_mode = 'I'.
ls_table-delta_mode = 'Y'.
ls_table-package_size = 10000.
ls_table-num_jobs = 4.
APPEND ls_table TO lt_tables.

* Llamar API de configuración SLT
LOOP AT lt_tables INTO ls_table.
  CALL FUNCTION 'LTRC_ADD_TABLE_TO_CONFIG'
    EXPORTING
      iv_config_name  = lv_config_name
      is_table_config = ls_table
    EXCEPTIONS
      config_not_found = 1
      table_exists     = 2
      OTHERS          = 3.
  
  IF sy-subrc = 0.
    WRITE: / '✓ Tabla', ls_table-tabname, 'configurada correctamente'.
  ELSE.
    WRITE: / '✗ Error configurando tabla', ls_table-tabname, ':', sy-subrc.
  ENDIF.
ENDLOOP.

WRITE: / ''.
WRITE: / 'Configuración completada para', lines( lt_tables ), 'tablas'.
```

### 2.3 Ejecución de Carga Inicial

**Responsable:** SAP ABAP Developer

#### Script de Monitoreo de Carga Inicial

```abap
*----------------------------------------------------------------------*
* Program: Z_MONITOR_SLT_INITIAL_LOAD
* Purpose: Monitorear progreso de carga inicial
*----------------------------------------------------------------------*
REPORT z_monitor_slt_initial_load.

DATA: lv_config TYPE ltrc_config_name VALUE 'BQ_SD_REPLICATION',
      lt_status TYPE TABLE OF ltrc_repl_status,
      ls_status TYPE ltrc_repl_status,
      lv_total_rows TYPE i,
      lv_replicated_rows TYPE i,
      lv_progress TYPE p DECIMALS 2.

* Obtener status de todas las tablas
CALL FUNCTION 'LTRC_GET_REPLICATION_STATUS'
  EXPORTING
    iv_config_name = lv_config
  TABLES
    et_status      = lt_status.

WRITE: / '=== Status de Replicación Inicial ==='.
WRITE: / 'Configuración:', lv_config.
WRITE: / 'Timestamp:', sy-datum, sy-uzeit.
WRITE: / ''.

* Mostrar status por tabla
WRITE: / 'Tabla', 15 'Status', 30 'Rows Total', 50 'Rows Replicados', 70 'Progreso'.
WRITE: / sy-uline.

LOOP AT lt_status INTO ls_status.
  IF ls_status-total_rows > 0.
    lv_progress = ( ls_status-replicated_rows / ls_status-total_rows ) * 100.
  ELSE.
    lv_progress = 0.
  ENDIF.
  
  WRITE: / ls_status-tabname, 
         15 ls_status-status,
         30 ls_status-total_rows,
         50 ls_status-replicated_rows,
         70 lv_progress, '%'.
ENDLOOP.

* Calcular totales
CLEAR: lv_total_rows, lv_replicated_rows.
LOOP AT lt_status INTO ls_status.
  ADD ls_status-total_rows TO lv_total_rows.
  ADD ls_status-replicated_rows TO lv_replicated_rows.
ENDLOOP.

IF lv_total_rows > 0.
  lv_progress = ( lv_replicated_rows / lv_total_rows ) * 100.
ENDIF.

WRITE: / sy-uline.
WRITE: / 'TOTAL', 30 lv_total_rows, 50 lv_replicated_rows, 70 lv_progress, '%'.
WRITE: / ''.

* Verificar si hay errores
IF line_exists( lt_status[ status = 'ERROR' ] ).
  WRITE: / '⚠️  ADVERTENCIA: Hay tablas con errores'.
  WRITE: / 'Revisar transacción LTRC o logs en SLR5'.
ENDIF.
```

#### Comando para Iniciar Replicación

```abap
* Iniciar replicación mediante transacción LTRC:
* 
* 1. Ejecutar LTRC
* 2. Seleccionar configuración: BQ_SD_REPLICATION
* 3. Para cada tabla:
*    - Click en tabla (ej. VBAK)
*    - Botón "Start Replication"
*    - Confirmar parámetros
*    - Click "Execute"
*
* O mediante programa background:

REPORT z_start_replication.

DATA: lv_config TYPE ltrc_config_name VALUE 'BQ_SD_REPLICATION',
      lt_tables TYPE TABLE OF tabname.

APPEND 'VBAK' TO lt_tables.
APPEND 'VBAP' TO lt_tables.
APPEND 'VBUK' TO lt_tables.
APPEND 'VBUP' TO lt_tables.
APPEND 'KNA1' TO lt_tables.
APPEND 'MARA' TO lt_tables.

LOOP AT lt_tables INTO DATA(lv_table).
  CALL FUNCTION 'LTRC_START_REPLICATION'
    EXPORTING
      iv_config_name = lv_config
      iv_table_name  = lv_table
      iv_mode        = 'I'  " Initial load
    EXCEPTIONS
      OTHERS         = 1.
  
  IF sy-subrc = 0.
    WRITE: / '✓ Replicación iniciada para tabla', lv_table.
    COMMIT WORK.
    WAIT UP TO 2 SECONDS.  " Espaciar inicio de jobs
  ELSE.
    WRITE: / '✗ Error iniciando replicación para', lv_table.
  ENDIF.
ENDLOOP.
```

### 2.4 Verificación de Datos en BigQuery

**Responsable:** Data Engineer

#### Script de Verificación de Conteo de Registros

```sql
-- verify_initial_load.sql
-- Verificar que los conteos de registros coincidan entre SAP y BigQuery

-- Crear vista para comparación de conteos
CREATE OR REPLACE VIEW SAP_ANALYTICS.replication_verification AS
WITH sap_counts AS (
  -- Estos valores deben obtenerse del sistema SAP
  -- Ejecutar: SELECT COUNT(*) FROM VBAK WHERE AUART IN ('OR','ZOR','ZSER') AND VKORG = '1000'
  SELECT 'VBAK' as table_name, 45230 as sap_count UNION ALL
  SELECT 'VBAP', 234567 UNION ALL
  SELECT 'VBUK', 45230 UNION ALL
  SELECT 'VBUP', 234567 UNION ALL
  SELECT 'KNA1', 12450 UNION ALL
  SELECT 'MARA', 67890
),
bq_counts AS (
  SELECT 'VBAK' as table_name, COUNT(*) as bq_count FROM `elanco-power-analytics.SAP_SD_REPLICAS.VBAK` UNION ALL
  SELECT 'VBAP', COUNT(*) FROM `elanco-power-analytics.SAP_SD_REPLICAS.VBAP` UNION ALL
  SELECT 'VBUK', COUNT(*) FROM `elanco-power-analytics.SAP_SD_REPLICAS.VBUK` UNION ALL
  SELECT 'VBUP', COUNT(*) FROM `elanco-power-analytics.SAP_SD_REPLICAS.VBUP` UNION ALL
  SELECT 'KNA1', COUNT(*) FROM `elanco-power-analytics.SAP_SD_REPLICAS.KNA1` UNION ALL
  SELECT 'MARA', COUNT(*) FROM `elanco-power-analytics.SAP_SD_REPLICAS.MARA`
)
SELECT 
  s.table_name,
  s.sap_count,
  b.bq_count,
  b.bq_count - s.sap_count as difference,
  ROUND(SAFE_DIVIDE(b.bq_count, s.sap_count) * 100, 2) as completeness_pct,
  CASE 
    WHEN ABS(b.bq_count - s.sap_count) = 0 THEN '✓ Perfect Match'
    WHEN ABS(b.bq_count - s.sap_count) <= s.sap_count * 0.01 THEN '⚠️ Minor Difference (<1%)'
    ELSE '✗ Significant Difference'
  END as status
FROM sap_counts s
JOIN bq_counts b ON s.table_name = b.table_name
ORDER BY s.table_name;

-- Ejecutar verificación
SELECT * FROM SAP_ANALYTICS.replication_verification;
```

#### Script de Validación de Estructura de Datos

```sql
-- validate_data_structure.sql
-- Validar que las estructuras de las tablas sean correctas

-- Verificar tabla VBAK
SELECT 
  column_name,
  data_type,
  is_nullable,
  description
FROM `elanco-power-analytics.SAP_SD_REPLICAS.INFORMATION_SCHEMA.COLUMNS`
WHERE table_name = 'VBAK'
ORDER BY ordinal_position;

-- Verificar campos clave existen
SELECT 
  'VBAK' as table_name,
  COUNT(DISTINCT VBELN) as unique_sales_orders,
  COUNT(*) as total_rows,
  MIN(ERDAT) as earliest_date,
  MAX(ERDAT) as latest_date
FROM `elanco-power-analytics.SAP_SD_REPLICAS.VBAK`;

-- Verificar tabla VBAP
SELECT 
  'VBAP' as table_name,
  COUNT(DISTINCT VBELN) as unique_sales_orders,
  COUNT(*) as total_positions,
  ROUND(COUNT(*) / COUNT(DISTINCT VBELN), 2) as avg_positions_per_order
FROM `elanco-power-analytics.SAP_SD_REPLICAS.VBAP`;

-- Verificar integridad referencial VBAK -> VBAP
SELECT
  'Referential Integrity Check' as check_type,
  COUNT(DISTINCT v.VBELN) as sales_orders_in_vbap,
  (SELECT COUNT(DISTINCT VBELN) FROM `elanco-power-analytics.SAP_SD_REPLICAS.VBAK`) as sales_orders_in_vbak,
  COUNT(DISTINCT v.VBELN) - (SELECT COUNT(DISTINCT VBELN) FROM `elanco-power-analytics.SAP_SD_REPLICAS.VBAK`) as orphaned_records
FROM `elanco-power-analytics.SAP_SD_REPLICAS.VBAP` v
LEFT JOIN `elanco-power-analytics.SAP_SD_REPLICAS.VBAK` k ON v.VBELN = k.VBELN
WHERE k.VBELN IS NULL;
```

### 2.5 Activación de Replicación Delta (CDC)

**Responsable:** SAP ABAP Developer

#### Configuración de CDC

```abap
*----------------------------------------------------------------------*
* Program: Z_ACTIVATE_CDC_REPLICATION
* Purpose: Activar replicación delta (Change Data Capture)
*----------------------------------------------------------------------*
REPORT z_activate_cdc_replication.

DATA: lv_config TYPE ltrc_config_name VALUE 'BQ_SD_REPLICATION',
      lt_tables TYPE TABLE OF tabname.

* Tablas para activar CDC
APPEND 'VBAK' TO lt_tables.
APPEND 'VBAP' TO lt_tables.
APPEND 'VBUK' TO lt_tables.
APPEND 'VBUP' TO lt_tables.

WRITE: / '=== Activación de Replicación Delta (CDC) ==='.
WRITE: / ''.

LOOP AT lt_tables INTO DATA(lv_table).
  * Activar logging de base de datos para CDC
  CALL FUNCTION 'LTRC_ACTIVATE_TABLE_LOGGING'
    EXPORTING
      iv_config_name = lv_config
      iv_table_name  = lv_table
    EXCEPTIONS
      OTHERS         = 1.
  
  IF sy-subrc = 0.
    WRITE: / '✓ Logging activado para tabla', lv_table.
    
    * Iniciar replicación delta
    CALL FUNCTION 'LTRC_START_REPLICATION'
      EXPORTING
        iv_config_name = lv_config
        iv_table_name  = lv_table
        iv_mode        = 'D'  " Delta mode
      EXCEPTIONS
        OTHERS         = 1.
    
    IF sy-subrc = 0.
      WRITE: / '✓ Replicación delta iniciada para', lv_table.
    ELSE.
      WRITE: / '✗ Error iniciando replicación delta para', lv_table.
    ENDIF.
  ELSE.
    WRITE: / '✗ Error activando logging para', lv_table.
  ENDIF.
  
  WRITE: / ''.
ENDLOOP.

WRITE: / 'Proceso de activación CDC completado'.
```

#### Script de Prueba de CDC

```abap
*----------------------------------------------------------------------*
* Program: Z_TEST_CDC_REPLICATION
* Purpose: Probar que la replicación delta funciona correctamente
*----------------------------------------------------------------------*
REPORT z_test_cdc_replication.

DATA: lv_vbeln TYPE vbak-vbeln,
      lv_timestamp_start TYPE timestamp,
      lv_timestamp_end TYPE timestamp,
      lv_wait_seconds TYPE i VALUE 120.

* Obtener timestamp inicial
GET TIME STAMP FIELD lv_timestamp_start.

WRITE: / '=== Prueba de Replicación Delta (CDC) ==='.
WRITE: / 'Timestamp inicio:', lv_timestamp_start.
WRITE: / ''.

* Crear una orden de venta de prueba
* NOTA: Esto debe ejecutarse en el sistema SAP fuente
WRITE: / 'Paso 1: Crear orden de venta de prueba en SAP'.
WRITE: / '  Ejecutar transacción VA01 manualmente y anotar número de orden'.
READ LINE 1.
WRITE: / 'Ingrese número de orden creada (VBELN):'.
READ LINE 2 LINE VALUE lv_vbeln.

IF lv_vbeln IS INITIAL.
  WRITE: / '✗ No se ingresó número de orden. Prueba cancelada.'.
  EXIT.
ENDIF.

WRITE: / '✓ Orden de venta:', lv_vbeln.
WRITE: / ''.

* Esperar tiempo de replicación
WRITE: / 'Paso 2: Esperando', lv_wait_seconds, 'segundos para replicación...'.
WAIT UP TO lv_wait_seconds SECONDS.

GET TIME STAMP FIELD lv_timestamp_end.

* Verificar en BigQuery (debe ejecutarse via script SQL)
WRITE: / ''.
WRITE: / 'Paso 3: Verificar en BigQuery'.
WRITE: / '  Ejecutar el siguiente query en BigQuery:'.
WRITE: / ''.
WRITE: / '  SELECT VBELN, ERDAT, ERZET, ERNAM, NETWR'.
WRITE: / '  FROM `elanco-power-analytics.SAP_SD_REPLICAS.VBAK`'.
WRITE: / '  WHERE VBELN = ''', lv_vbeln, ''''.
WRITE: / ''.
WRITE: / 'Timestamp fin:', lv_timestamp_end.
WRITE: / 'Tiempo transcurrido:', lv_wait_seconds, 'segundos'.
WRITE: / ''.
WRITE: / 'Si el registro aparece en BigQuery, la replicación CDC está funcionando ✓'.
```

---

## 📦 FASE 3: CREACIÓN DE DATA PRODUCTS Y VISTAS ANALÍTICAS (Semana 6)

---

## 📦 FASE 3: CREACIÓN DE DATA PRODUCTS Y VISTAS ANALÍTICAS (Semana 6)

### 3.1 Vista Unificada VA05 - Órdenes de Venta

**Responsable:** Data Engineer + SAP SD/MM Functional

#### Vista Base: Órdenes de Venta Completas

```sql
-- view_va05_sales_orders.sql
-- Vista que replica la funcionalidad de transacción VA05

CREATE OR REPLACE VIEW `elanco-power-analytics.SAP_ANALYTICS.VA05_SALES_ORDERS` AS
WITH sales_header AS (
  SELECT
    VBELN as sales_order,
    ERDAT as creation_date,
    ERZET as creation_time,
    ERNAM as created_by,
    AUDAT as document_date,
    VBTYP as document_category,
    AUART as order_type,
    VKORG as sales_org,
    VTWEG as distribution_channel,
    SPART as division,
    KUNNR as sold_to_party,
    WAERK as currency,
    NETWR as net_value,
    VKBUR as sales_office,
    VKGRP as sales_group,
    VDATU as requested_delivery_date
  FROM `elanco-power-analytics.SAP_SD_REPLICAS.VBAK`
),
sales_items AS (
  SELECT
    VBELN as sales_order,
    POSNR as item_number,
    MATNR as material,
    ARKTX as item_description,
    KWMENG as order_quantity,
    VRKME as sales_unit,
    NETWR as net_value,
    WAERK as currency,
    WERKS as plant,
    LGORT as storage_location,
    VSTEL as shipping_point,
    ROUTE as route,
    PSTYV as item_category,
    PRODH as product_hierarchy
  FROM `elanco-power-analytics.SAP_SD_REPLICAS.VBAP`
),
document_status AS (
  SELECT
    VBELN as sales_order,
    GBSTK as overall_status,
    ABSTK as rejection_status,
    LFSTK as delivery_status,
    FSSTK as billing_status,
    CMGST as credit_management_status
  FROM `elanco-power-analytics.SAP_SD_REPLICAS.VBUK`
),
item_status AS (
  SELECT
    VBELN as sales_order,
    POSNR as item_number,
    GBSTA as overall_item_status,
    ABSTA as rejection_status,
    LFSTA as delivery_status,
    FKSTA as billing_status,
    WBSTA as goods_movement_status
  FROM `elanco-power-analytics.SAP_SD_REPLICAS.VBUP`
),
customer_master AS (
  SELECT
    KUNNR as customer_number,
    NAME1 as customer_name,
    LAND1 as country,
    REGIO as region,
    ORT01 as city,
    PSTLZ as postal_code,
    STRAS as street,
    KTOKD as account_group
  FROM `elanco-power-analytics.SAP_SD_REPLICAS.KNA1`
),
material_master AS (
  SELECT
    MATNR as material,
    MAKTX as material_description,
    MTART as material_type,
    MATKL as material_group,
    MEINS as base_unit,
    BRGEW as gross_weight,
    NTGEW as net_weight,
    GEWEI as weight_unit
  FROM `elanco-power-analytics.SAP_SD_REPLICAS.MARA` m
  LEFT JOIN `elanco-power-analytics.SAP_SD_REPLICAS.MAKT` t 
    ON m.MATNR = t.MATNR AND t.SPRAS = 'E'
)
SELECT
  -- Identificadores
  h.sales_order,
  i.item_number,
  
  -- Información de cabecera
  h.creation_date,
  PARSE_DATE('%Y%m%d', h.creation_date) as creation_date_parsed,
  h.creation_time,
  h.created_by,
  h.document_date,
  PARSE_DATE('%Y%m%d', h.document_date) as document_date_parsed,
  h.document_category,
  h.order_type,
  
  -- Organización de ventas
  h.sales_org,
  h.distribution_channel,
  h.division,
  h.sales_office,
  h.sales_group,
  
  -- Cliente
  h.sold_to_party,
  c.customer_name,
  c.country,
  c.region,
  c.city,
  
  -- Material
  i.material,
  LTRIM(i.material, '0') as material_no_leading_zeros,
  i.item_description,
  m.material_description as master_material_description,
  m.material_type,
  m.material_group,
  
  -- Cantidades y valores
  i.order_quantity,
  i.sales_unit,
  i.net_value as item_net_value,
  h.net_value as header_net_value,
  h.currency,
  
  -- Logística
  i.plant,
  i.storage_location,
  i.shipping_point,
  i.route,
  h.requested_delivery_date,
  PARSE_DATE('%Y%m%d', h.requested_delivery_date) as requested_delivery_date_parsed,
  
  -- Status
  ds.overall_status,
  ds.rejection_status as header_rejection_status,
  ds.delivery_status as header_delivery_status,
  ds.billing_status as header_billing_status,
  ds.credit_management_status,
  
  ist.overall_item_status,
  ist.rejection_status as item_rejection_status,
  ist.delivery_status as item_delivery_status,
  ist.billing_status as item_billing_status,
  ist.goods_movement_status,
  
  -- Campos calculados
  CASE 
    WHEN ds.overall_status = 'A' THEN 'Completamente procesado'
    WHEN ds.overall_status = 'B' THEN 'Parcialmente procesado'
    WHEN ds.overall_status = 'C' THEN 'No procesado'
    ELSE 'Desconocido'
  END as overall_status_text,
  
  CASE
    WHEN ist.delivery_status = 'A' THEN 'No relevante para entrega'
    WHEN ist.delivery_status = 'B' THEN 'Parcialmente entregado'
    WHEN ist.delivery_status = 'C' THEN 'Completamente entregado'
    ELSE 'Pendiente de entrega'
  END as delivery_status_text,
  
  -- Timestamp de última actualización
  CURRENT_TIMESTAMP() as last_updated

FROM sales_header h
LEFT JOIN sales_items i ON h.sales_order = i.sales_order
LEFT JOIN document_status ds ON h.sales_order = ds.sales_order
LEFT JOIN item_status ist ON i.sales_order = ist.sales_order AND i.item_number = ist.item_number
LEFT JOIN customer_master c ON h.sold_to_party = c.customer_number
LEFT JOIN material_master m ON i.material = m.material

WHERE 1=1
  -- Filtros equivalentes a selección estándar VA05
  AND h.document_category = 'C'  -- Orden de venta
  AND ds.overall_status IN ('B', 'C')  -- Órdenes no completamente procesadas (abiertas)
  AND ist.rejection_status = ''  -- Excluir posiciones rechazadas
;

-- Otorgar permisos de lectura a usuarios finales
GRANT `roles/bigquery.dataViewer` 
ON TABLE `elanco-power-analytics.SAP_ANALYTICS.VA05_SALES_ORDERS`
TO "group:sales-analysts@elanco.com";
```

### 3.2 Vistas Agregadas y KPIs

**Responsable:** Data Engineer

#### Dashboard de Órdenes de Venta - Métricas Clave

```sql
-- view_sales_orders_kpis.sql
-- Vista con KPIs agregados para dashboards ejecutivos

CREATE OR REPLACE VIEW `elanco-power-analytics.SAP_ANALYTICS.SALES_ORDERS_KPIS` AS
WITH daily_metrics AS (
  SELECT
    creation_date_parsed as order_date,
    sales_org,
    division,
    order_type,
    COUNT(DISTINCT sales_order) as total_orders,
    COUNT(item_number) as total_items,
    SUM(item_net_value) as total_net_value,
    AVG(item_net_value) as avg_item_value,
    SUM(order_quantity) as total_quantity
  FROM `elanco-power-analytics.SAP_ANALYTICS.VA05_SALES_ORDERS`
  WHERE creation_date_parsed IS NOT NULL
  GROUP BY 1, 2, 3, 4
),
delivery_metrics AS (
  SELECT
    creation_date_parsed as order_date,
    delivery_status_text,
    COUNT(DISTINCT sales_order) as orders_count,
    SUM(item_net_value) as net_value
  FROM `elanco-power-analytics.SAP_ANALYTICS.VA05_SALES_ORDERS`
  WHERE creation_date_parsed IS NOT NULL
  GROUP BY 1, 2
)
SELECT
  d.order_date,
  d.sales_org,
  d.division,
  d.order_type,
  
  -- Volumetría
  d.total_orders,
  d.total_items,
  ROUND(d.total_items / d.total_orders, 2) as avg_items_per_order,
  
  -- Valores
  ROUND(d.total_net_value, 2) as total_net_value,
  ROUND(d.avg_item_value, 2) as avg_item_value,
  ROUND(d.total_net_value / d.total_orders, 2) as avg_order_value,
  
  -- Cantidades
  ROUND(d.total_quantity, 2) as total_quantity,
  
  -- Status de entregas (join con delivery_metrics)
  ROUND(SUM(CASE WHEN dm.delivery_status_text = 'Completamente entregado' 
            THEN dm.orders_count ELSE 0 END) / d.total_orders * 100, 2) 
    as pct_fully_delivered,
  
  ROUND(SUM(CASE WHEN dm.delivery_status_text = 'Pendiente de entrega' 
            THEN dm.orders_count ELSE 0 END) / d.total_orders * 100, 2) 
    as pct_pending_delivery,
  
  -- Timestamp
  CURRENT_TIMESTAMP() as calculated_at
  
FROM daily_metrics d
LEFT JOIN delivery_metrics dm 
  ON d.order_date = dm.order_date
GROUP BY 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
ORDER BY d.order_date DESC;
```

#### Vista de Backlog de Órdenes Abiertas

```sql
-- view_sales_backlog.sql
-- Vista de backlog: órdenes abiertas pendientes de procesar

CREATE OR REPLACE VIEW `elanco-power-analytics.SAP_ANALYTICS.SALES_BACKLOG` AS
SELECT
  sales_order,
  item_number,
  creation_date_parsed,
  requested_delivery_date_parsed,
  
  -- Días de antigüedad
  DATE_DIFF(CURRENT_DATE(), creation_date_parsed, DAY) as days_since_creation,
  DATE_DIFF(requested_delivery_date_parsed, CURRENT_DATE(), DAY) as days_until_delivery,
  
  -- Criticidad
  CASE
    WHEN DATE_DIFF(requested_delivery_date_parsed, CURRENT_DATE(), DAY) < 0 THEN 'VENCIDO'
    WHEN DATE_DIFF(requested_delivery_date_parsed, CURRENT_DATE(), DAY) <= 7 THEN 'URGENTE'
    WHEN DATE_DIFF(requested_delivery_date_parsed, CURRENT_DATE(), DAY) <= 30 THEN 'PRÓXIMO'
    ELSE 'NORMAL'
  END as priority,
  
  -- Información clave
  sold_to_party,
  customer_name,
  material,
  material_no_leading_zeros,
  item_description,
  order_quantity,
  sales_unit,
  item_net_value,
  currency,
  
  -- Status
  overall_status_text,
  delivery_status_text,
  billing_status as item_billing_status,
  
  -- Organización
  sales_org,
  division,
  plant,
  sales_office,
  sales_group

FROM `elanco-power-analytics.SAP_ANALYTICS.VA05_SALES_ORDERS`
WHERE 
  -- Solo órdenes abiertas
  overall_status != 'A'  -- No completamente procesadas
  AND item_rejection_status = ''  -- No rechazadas
  AND item_delivery_status != 'C'  -- No completamente entregadas
ORDER BY 
  -- Ordenar por criticidad
  CASE priority
    WHEN 'VENCIDO' THEN 1
    WHEN 'URGENTE' THEN 2
    WHEN 'PRÓXIMO' THEN 3
    ELSE 4
  END,
  requested_delivery_date_parsed;
```

### 3.3 Vista Materializada para Performance

**Responsable:** Data Engineer

```sql
-- materialized_view_sales_orders_daily.sql
-- Vista materializada para optimizar consultas frecuentes

CREATE MATERIALIZED VIEW `elanco-power-analytics.SAP_ANALYTICS.MV_SALES_ORDERS_DAILY`
PARTITION BY order_date
CLUSTER BY sales_org, division
OPTIONS(
  enable_refresh = true,
  refresh_interval_minutes = 60,
  description = "Vista materializada de órdenes de venta, actualizada cada hora"
)
AS
SELECT
  creation_date_parsed as order_date,
  sales_org,
  division,
  order_type,
  sold_to_party,
  customer_name,
  country,
  
  -- Agregaciones
  COUNT(DISTINCT sales_order) as total_orders,
  COUNT(item_number) as total_items,
  SUM(item_net_value) as total_net_value,
  SUM(order_quantity) as total_quantity,
  
  -- Promedios
  AVG(item_net_value) as avg_item_value,
  AVG(order_quantity) as avg_quantity,
  
  -- Status agregado
  COUNTIF(overall_status_text = 'Completamente procesado') as orders_completed,
  COUNTIF(overall_status_text != 'Completamente procesado') as orders_open,
  COUNTIF(delivery_status_text = 'Completamente entregado') as items_delivered,
  COUNTIF(delivery_status_text != 'Completamente entregado') as items_pending,
  
  -- Timestamp
  MAX(last_updated) as last_data_update

FROM `elanco-power-analytics.SAP_ANALYTICS.VA05_SALES_ORDERS`
WHERE creation_date_parsed IS NOT NULL
GROUP BY 1, 2, 3, 4, 5, 6, 7;

-- Refrescar manualmente la primera vez
CALL BQ.REFRESH_MATERIALIZED_VIEW('elanco-power-analytics.SAP_ANALYTICS.MV_SALES_ORDERS_DAILY');
```

### 3.4 Diccionario de Datos y Documentación

**Responsable:** Data Engineer + SAP SD/MM Functional

```sql
-- data_dictionary_va05.sql
-- Documentación de campos y mapeo SAP -> BigQuery

CREATE OR REPLACE TABLE `elanco-power-analytics.SAP_ANALYTICS.DATA_DICTIONARY` AS
SELECT
  'VA05_SALES_ORDERS' as view_name,
  'sales_order' as field_name,
  'VBAK-VBELN' as sap_field,
  'STRING' as data_type,
  'Número de orden de venta' as description,
  'Identificador único de la orden' as business_meaning,
  'No' as is_calculated,
  'VA05, VA02, VA03' as related_transactions
UNION ALL SELECT 'VA05_SALES_ORDERS', 'creation_date', 'VBAK-ERDAT', 'STRING', 'Fecha de creación (formato YYYYMMDD)', 'Fecha en que se creó el documento', 'No', 'VA05'
UNION ALL SELECT 'VA05_SALES_ORDERS', 'creation_date_parsed', 'VBAK-ERDAT', 'DATE', 'Fecha de creación (formato DATE)', 'Versión parseada de ERDAT', 'Sí', 'VA05'
UNION ALL SELECT 'VA05_SALES_ORDERS', 'created_by', 'VBAK-ERNAM', 'STRING', 'Usuario que creó la orden', 'Login del usuario SAP', 'No', 'VA05, SU01'
UNION ALL SELECT 'VA05_SALES_ORDERS', 'order_type', 'VBAK-AUART', 'STRING', 'Tipo de orden (ej. OR, ZOR)', 'Clasifica el tipo de documento', 'No', 'VA05, VOV8'
UNION ALL SELECT 'VA05_SALES_ORDERS', 'sales_org', 'VBAK-VKORG', 'STRING', 'Organización de ventas', 'Unidad organizativa de ventas', 'No', 'VA05, OVX1'
UNION ALL SELECT 'VA05_SALES_ORDERS', 'sold_to_party', 'VBAK-KUNNR', 'STRING', 'Código de cliente solicitante', 'Cliente que ordena', 'No', 'VA05, XD03'
UNION ALL SELECT 'VA05_SALES_ORDERS', 'customer_name', 'KNA1-NAME1', 'STRING', 'Nombre del cliente', 'Razón social', 'No', 'XD03'
UNION ALL SELECT 'VA05_SALES_ORDERS', 'net_value', 'VBAK-NETWR', 'NUMERIC', 'Valor neto de la orden', 'Suma de posiciones sin impuestos', 'No', 'VA05'
UNION ALL SELECT 'VA05_SALES_ORDERS', 'item_number', 'VBAP-POSNR', 'STRING', 'Número de posición', 'Línea dentro de la orden', 'No', 'VA05'
UNION ALL SELECT 'VA05_SALES_ORDERS', 'material', 'VBAP-MATNR', 'STRING', 'Código de material', 'SKU con ceros iniciales', 'No', 'VA05, MM03'
UNION ALL SELECT 'VA05_SALES_ORDERS', 'material_no_leading_zeros', 'VBAP-MATNR', 'STRING', 'Código de material sin ceros', 'SKU limpio', 'Sí', 'VA05, MM03'
UNION ALL SELECT 'VA05_SALES_ORDERS', 'order_quantity', 'VBAP-KWMENG', 'NUMERIC', 'Cantidad ordenada', 'Cantidad en unidad de venta', 'No', 'VA05'
UNION ALL SELECT 'VA05_SALES_ORDERS', 'overall_status', 'VBUK-GBSTK', 'STRING', 'Status general del documento', 'A=Completo, B=Parcial, C=No procesado', 'No', 'VA05'
UNION ALL SELECT 'VA05_SALES_ORDERS', 'delivery_status', 'VBUP-LFSTA', 'STRING', 'Status de entrega', 'A=No relevante, B=Parcial, C=Completo', 'No', 'VA05, VL03N'
UNION ALL SELECT 'VA05_SALES_ORDERS', 'delivery_status_text', NULL, 'STRING', 'Status de entrega (texto)', 'Descripción legible del status', 'Sí', 'VA05'
UNION ALL SELECT 'VA05_SALES_ORDERS', 'priority', NULL, 'STRING', 'Prioridad calculada', 'VENCIDO/URGENTE/PRÓXIMO/NORMAL', 'Sí', 'N/A'
;

-- Crear vista de documentación legible
CREATE OR REPLACE VIEW `elanco-power-analytics.SAP_ANALYTICS.VW_DATA_DICTIONARY` AS
SELECT
  view_name,
  field_name,
  sap_field,
  data_type,
  description,
  business_meaning,
  is_calculated,
  related_transactions
FROM `elanco-power-analytics.SAP_ANALYTICS.DATA_DICTIONARY`
ORDER BY view_name, field_name;
```

---

## 📦 FASE 4: MONITOREO, ALERTAS Y MANTENIMIENTO (Semana 7)

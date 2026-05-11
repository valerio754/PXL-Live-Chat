# PXL-Live | Sistema de Chat Colaborativo en Tiempo Real

##  Descripción General

**PXL-Live** es una aplicación web SPA (*Single Page Application*) desarrollada para permitir la comunicación colaborativa en tiempo real entre múltiples usuarios mediante el protocolo **WebSocket**.

El sistema fue creado como parte de una actividad académica enfocada en comprender e implementar comunicación bidireccional persistente entre cliente y servidor, evitando técnicas tradicionales como polling o long-polling.

La aplicación permite:

- ✅ Conexión simultánea de múltiples usuarios
- ✅ Mensajería instantánea en tiempo real
- ✅ Persistencia de historial de mensajes
- ✅ Autenticación mediante Google Login
- ✅ Notificaciones de conexión y desconexión
- ✅ Interfaz moderna, responsiva y simple

---

#  Objetivo del Proyecto

Desarrollar una funcionalidad básica de chat colaborativo en tiempo real entre múltiples usuarios utilizando exclusivamente **WebSocket** como mecanismo de comunicación persistente entre cliente y servidor.

---

#  Visión del Sistema

Construir un sistema colaborativo que permita a los empleados de una empresa comunicarse en tiempo real mediante una aplicación web SPA utilizando WebSockets para mensajería instantánea, administrado por una API interna y respaldado por una base de datos local.

El sistema utiliza autenticación mediante **Google Identity Services** para identificar usuarios.

---

#  Tecnologías Utilizadas

| Componente | Tecnología |
|---|---|
| **Backend** | Python 3, FastAPI, Uvicorn |
| **Frontend** | HTML5, CSS3, JavaScript Vanilla |
| **Base de Datos** | SQLite |
| **Comunicación** | WebSocket |
| **Autenticación** | Google Identity Services |
| **Control de Versiones** | Git & GitHub |
| **Gestión Colaborativa** | Trello |
| **Exposición Pública** | Ngrok |

---

#  Arquitectura del Sistema

El sistema utiliza una arquitectura **Cliente - Servidor**.

##  Cliente (Frontend)

La interfaz web SPA desarrollada en HTML, CSS y JavaScript permite:

- Enviar mensajes
- Recibir mensajes en tiempo real
- Mostrar historial
- Gestionar autenticación
- Diferenciar visualmente usuarios

---

##  Servidor (Backend)

El backend desarrollado con FastAPI:

- Gestiona conexiones WebSocket
- Administra múltiples usuarios simultáneamente
- Realiza broadcast de mensajes
- Gestiona persistencia de datos
- Controla conexiones y desconexiones

---

##  Base de Datos

SQLite almacena:

- Usuario
- Mensaje
- Fecha
- Hora

---

#  Requerimientos Funcionales

| Código | Requerimiento |
|---|---|
| RF01 | El sistema debe permitir múltiples conexiones simultáneas mediante WebSocket |
| RF02 | El sistema debe permitir enviar mensajes en tiempo real |
| RF03 | El sistema debe mostrar mensajes recibidos instantáneamente |
| RF04 | El sistema debe almacenar el historial de mensajes |
| RF05 | El sistema debe recuperar el historial al conectarse |
| RF06 | El sistema debe notificar entradas de usuarios |
| RF07 | El sistema debe notificar desconexiones |
| RF08 | El sistema debe permitir autenticación mediante Google |
| RF09 | El sistema debe generar usuarios temporales automáticamente |
| RF10 | El sistema debe diferenciar mensajes propios y ajenos |

---

#  Requerimientos No Funcionales

| Código | Requerimiento |
|---|---|
| RNF01 | La interfaz debe ser simple y responsive |
| RNF02 | El sistema debe utilizar exclusivamente WebSocket |
| RNF03 | El código debe estar organizado y comentado |
| RNF04 | El sistema debe ejecutarse localmente sin configuraciones complejas |
| RNF05 | La aplicación debe mantener persistencia básica mediante SQLite |
| RNF06 | El sistema debe ser fácil de comprender y explicar |

---

#  Historias de Usuario Implementadas

---

## HU01 — Configuración del Entorno

###  Descripción

Como desarrollador, quiero configurar el entorno de trabajo y Git para asegurar la colaboración.

### ✅ Implementación

- Repositorio GitHub creado
- Organización frontend/backend
- Archivo `.gitignore`
- Archivo `requirements.txt`

---

## HU02 — Servidor WebSocket Base

###  Descripción

Como desarrollador, quiero un servidor que gestione múltiples conexiones bidireccionales.

### ✅ Implementación

- Endpoint `/ws/{user}`
- Clase `ConnectionManager`
- Gestión de conexiones activas
- Broadcast de mensajes
- Manejo de desconexiones

---

## HU03 — Interfaz de Usuario (SPA)

###  Descripción

Como usuario, quiero una interfaz web limpia para enviar y recibir mensajes.

### ✅ Implementación

- Diseño oscuro moderno
- SPA responsiva
- Auto-scroll
- Input de mensajes
- Burbujas de chat
- Diferenciación visual de usuarios

---

## HU04 — Identificación de Usuario

###  Descripción

Como usuario, quiero identificarme mediante Google o un nombre temporal.

### ✅ Implementación

- Integración Google Login
- Login manual
- Generación automática de `Invitado_XXX`
- Persistencia de sesión con localStorage

---

## HU05 — Notificaciones de Sesión

###  Descripción

Como usuario, quiero saber quién entra o sale del chat.

### ✅ Implementación

- Mensajes del sistema
- Notificaciones de conexión
- Notificaciones de desconexión

---

## HU06 — Persistencia e Historial

###  Descripción

Como usuario, quiero ver mensajes antiguos al conectarme.

### ✅ Implementación

- Base de datos SQLite
- Tabla `messages`
- Recuperación automática del historial

---

## HU07 — Documentación y Cierre

###  Descripción

Como docente, quiero ejecutar el proyecto fácilmente.

### ✅ Implementación

- README detallado
- Código estructurado
- Evidencias del sistema
- Documentación de instalación

---

#  Guía de Instalación y Ejecución

## 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/valerio754/PXL-Live-Chat.git
cd PXL-Live-Chat
```

---

## 2️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Ejecutar el servidor

```bash
python -m uvicorn backend.main:app --reload
```

---

## 4️⃣ Abrir la aplicación

Abre tu navegador en:

```bash
http://127.0.0.1:8000/frontend/index.html
```

---

#  Acceso Externo con Ngrok

Si deseas permitir acceso desde Internet:

```bash
ngrok http 8000
```

Luego actualiza la URL en la configuración de Google Cloud Console.

---

#  Estructura del Proyecto

```bash
PXL-LIVE-CHAT/
│
├── backend/
│   └── main.py              # Servidor FastAPI y WebSocket
│
├── frontend/
│   └── index.html           # Interfaz SPA
│
├── pxl_chat.db              # Base de datos SQLite
├── requirements.txt         # Dependencias del proyecto
├── README.md                # Documentación principal
└── .gitignore               # Archivos ignorados por Git
```

---

#  Características Principales

- Comunicación en tiempo real con WebSocket
- Arquitectura SPA
- Persistencia local con SQLite
- Sistema multiusuario
- Historial automático
- Login con Google
- Diseño moderno responsive
- Gestión de conexiones activas

---

#  Aprendizajes del Proyecto

Durante el desarrollo del sistema se aplicaron conocimientos sobre:

- WebSockets
- FastAPI
- Manejo de conexiones concurrentes
- Arquitectura cliente-servidor
- Persistencia de datos
- SPA con JavaScript Vanilla
- Gestión de sesiones
- Integración con servicios externos

---

#  Grupo de Desarrollo — PIXEL

Proyecto desarrollado por el grupo **PIXEL** para la materia de **Sistemas Colaborativos**.

##  Integrantes

- Valerio Yucra Coria
- Lorena Camacho Berrios
- Elias Fabian Tenorio Claros
- Bruce Carlos Alvarez Coronado
- Aracely Alcon Fuentes

---

**Universidad Mayor de San Simón (UMSS)**||||||||||||||||||||||||||||||
Carrera de Ingeniería de Sistemas
Materia: Sistemas Colaborativos

---

#  Gestión del Proyecto

- GitHub para control de versiones
- Trello para gestión de tareas
- Metodología incremental basada en Historias de Usuario

---

#  Licencia

Proyecto desarrollado con fines académicos y educativos.

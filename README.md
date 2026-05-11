# PXL-Live | Sistema de Chat Colaborativo en Tiempo Real

##  Descripción General

PXL-Live es una aplicación web SPA (Single Page Application) desarrollada para permitir la comunicación colaborativa en tiempo real entre múltiples usuarios mediante el protocolo WebSocket.

El sistema fue desarrollado como parte de la actividad académica “Chat colaborativo en tiempo real con WebSocket”, cuyo objetivo principal es comprender e implementar comunicación bidireccional persistente entre cliente y servidor evitando técnicas tradicionales como polling o long-polling.

La aplicación permite:
- Conexión simultánea de múltiples usuarios
- Mensajería instantánea
- Persistencia de historial
- Autenticación mediante Google
- Notificaciones de conexión y desconexión
- Interfaz web moderna y simple

---

#  Objetivo del Proyecto

Desarrollar una funcionalidad básica de chat colaborativo en tiempo real entre múltiples usuarios utilizando exclusivamente WebSocket como mecanismo de comunicación persistente entre cliente y servidor.

---

#  Visión del Sistema

Construir un sistema colaborativo que permita a los empleados de una empresa comunicarse en tiempo real mediante una aplicación web SPA utilizando WebSockets para mensajería instantánea, administrado por una API interna y respaldado por una base de datos local.

El sistema utiliza un servicio de identidad externo mediante Google Login para autenticación de usuarios.

---

#  Tecnologías Utilizadas

## Backend
- Python 3
- FastAPI
- Uvicorn
- WebSocket
- SQLite

## Frontend
- HTML5
- CSS3
- JavaScript Vanilla

## Autenticación
- Google Identity Services
- invitado(usuairo_123)
## Gestión Colaborativa
- GitHub
- Trello
-zoom-met
---

#  Arquitectura del Sistema

El sistema utiliza una arquitectura Cliente-Servidor.

## Cliente
La interfaz web SPA desarrollada en HTML, CSS y JavaScript permite:
- Enviar mensajes
- Recibir mensajes en tiempo real
- Mostrar historial
- Gestionar autenticación

## Servidor
El backend desarrollado con FastAPI:
- Gestiona conexiones WebSocket
- Administra múltiples usuarios simultáneamente
- Realiza broadcast de mensajes
- Gestiona persistencia de datos

## Base de Datos
SQLite almacena:
- Usuario
- Mensaje
- Hora
- Fecha

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

### Descripción
Como desarrollador, quiero configurar el entorno de trabajo y Git para asegurar la colaboración.

### Implementación
- Repositorio GitHub creado
- Organización frontend/backend
- Archivo `.gitignore`
- Archivo `requirements.txt`

---

## HU02 — Servidor WebSocket Base

### Descripción
Como desarrollador, quiero un servidor que gestione múltiples conexiones bidireccionales.

### Implementación
- Endpoint `/ws/{user}`
- Clase `ConnectionManager`
- Gestión de conexiones activas
- Broadcast de mensajes
- Manejo de desconexiones

---

## HU03 — Interfaz de Usuario (SPA)

### Descripción
Como usuario, quiero una interfaz web limpia para enviar y recibir mensajes.

### Implementación
- Diseño oscuro moderno
- SPA responsiva
- Auto-scroll
- Input de mensajes
- Burbujas de chat
- Diferenciación visual de usuarios

---

## HU04 — Identificación de Usuario

### Descripción
Como usuario, quiero identificarme mediante Google o un nombre temporal.

### Implementación
- Integración Google Login
- Login manual
- Generación automática de `Invitado_XXX`
- Persistencia de sesión con localStorage

---

## HU05 — Notificaciones de Sesión

### Descripción
Como usuario, quiero saber quién entra o sale del chat.

### Implementación
- Mensajes de sistema
- Notificaciones de conexión
- Notificaciones de desconexión

---

## HU06 — Persistencia e Historial

### Descripción
Como usuario, quiero ver mensajes antiguos al conectarme.

### Implementación
- Base de datos SQLite
- Tabla `messages`
- Recuperación automática del historial

---

## HU07 — Documentación y Cierre

### Descripción
Como docente, quiero ejecutar el proyecto fácilmente.

### Implementación
- README detallado
- Código estructurado
- Evidencias del sistema
- Documentación de instalación

---

#  Estructura del Proyecto

```bash
PXL-LIVE-CHAT/
│
├── backend/
│   └── main.py
│
├── frontend/
│   └── index.html
│
├── pxl_chat.db
├── requirements.txt
├── README.md
└── .gitignore
1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/valerio754/PXL-Live-Chat.git](https://github.com/valerio754/PXL-Live-Chat.git)

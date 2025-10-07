<div align="center">

# 🏥 Backend GHL - Nivel 2

### Sistema de Gestión de Citas y Contactos con GoHighLevel

![CI Status](https://github.com/Hernandz09/Backend_GHL-Nivel-2/workflows/CI%20-%20Django%20Backend/badge.svg)
![Python](https://img.shields.io/badge/Python-3.10%20|%203.11%20|%203.12-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.2.6-green?logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-3.16.1-red?logo=django&logoColor=white)
![License](https://img.shields.io/badge/License-GHL%20Nivel%202-orange)

**API REST robusta para la gestión integral de citas y contactos con integración bidireccional a GoHighLevel**

[Características](#-características-principales) •
[Instalación](#-instalación-rápida) •
[API Docs](#-documentación-de-la-api) •
[CI/CD](#-integración-continua)

</div>

---

## 🚀 Características Principales

✨ **Gestión de Contactos**
- Creación de contactos ficticios en GoHighLevel
- Sincronización bidireccional con GHL
- Manejo automático de duplicados
- Almacenamiento local en SQLite

📅 **Sistema de Citas**
- CRUD completo de citas
- Vinculación automática con contactos
- Estados personalizables (confirmed, cancelled, etc.)
- Integración con calendarios de GHL

🔗 **Webhooks**
- Recepción de eventos de GoHighLevel
- Sincronización automática de datos
- Manejo robusto de errores

🔒 **Calidad y Seguridad**
- Tests automatizados con pytest
- Análisis de código con flake8, black, isort
- Análisis de seguridad con bandit
- CI/CD con GitHub Actions

## 📋 Requisitos

- Python 3.10, 3.11 o 3.12
- pip (gestor de paquetes de Python)
- Git

## 🛠️ Stack Tecnológico

<table>
<tr>
<td align="center" width="33%">

### Backend
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-ff1709?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

</td>
<td align="center" width="33%">

### Base de Datos
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

</td>
<td align="center" width="33%">

### DevOps & CI/CD
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

</td>
</tr>
</table>

### 📦 Dependencias Principales

| Categoría | Tecnología | Versión | Propósito |
|-----------|-----------|---------|-----------|
| **Framework** | Django | 5.2.6 | Framework web principal |
| **API REST** | Django REST Framework | 3.16.1 | Construcción de API RESTful |
| **CORS** | django-cors-headers | 4.7.0 | Manejo de CORS |
| **Env Management** | django-environ | 0.12.0 | Gestión de variables de entorno |
| **HTTP Client** | requests | 2.32.4 | Peticiones HTTP a GHL API |
| **WSGI Server** | gunicorn | 23.0.0 | Servidor de producción |
| **Static Files** | whitenoise | 6.8.2 | Servir archivos estáticos |

### 🧪 Herramientas de Desarrollo

| Herramienta | Propósito |
|-------------|-----------|
| **pytest** | Framework de testing |
| **pytest-django** | Plugin de pytest para Django |
| **coverage** | Cobertura de código |
| **flake8** | Linting de código |
| **black** | Formateo automático |
| **isort** | Ordenamiento de imports |
| **bandit** | Análisis de seguridad |

---

## 🔧 Instalación Rápida

### 1️⃣ Clonar el Repositorio
```bash
git clone https://github.com/Hernandz09/Backend_GHL-Nivel-2.git
cd Backend_GHL-Nivel-2
```

### 2️⃣ Crear Entorno Virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instalar Dependencias
```bash
cd backend
pip install -r requirements.txt

# Para desarrollo (incluye herramientas de testing)
pip install -r requirements-dev.txt
```

### 4️⃣ Configurar Variables de Entorno
```bash
cp env.example .env
```

Edita el archivo `.env` con tus credenciales:
```env
# Django Settings
SECRET_KEY=tu-clave-secreta-super-segura
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# GoHighLevel API
GHL_API_KEY=tu-api-key-de-ghl
GHL_LOCATION_ID=tu-location-id
GHL_ASSIGNED_USER_ID=tu-user-id
GHL_API_VERSION=2021-04-15
```

### 5️⃣ Ejecutar Migraciones
```bash
python manage.py migrate
```

### 6️⃣ Crear Superusuario (Opcional)
```bash
python manage.py createsuperuser
```

### 7️⃣ Iniciar Servidor
```bash
python manage.py runserver
```

🎉 **¡Listo!** El servidor estará disponible en `http://localhost:8000`

## 🧪 Testing

### Ejecutar tests de Django
```bash
cd backend
python manage.py test
```

### Ejecutar tests con pytest (recomendado para desarrollo)
```bash
cd backend
pip install -r requirements-dev.txt
pytest
```

### Ejecutar tests con cobertura
```bash
cd backend
pytest --cov=. --cov-report=html
```

---

## 📡 Documentación de la API

### Base URL
```
http://localhost:8000
```

### 🔗 Endpoints Disponibles

#### **Contactos**

<details>
<summary><b>📝 POST /contacts/create/</b> - Crear contacto ficticio en GHL</summary>

**Request Body:**
```json
{
    "firstName": "Juan",
    "lastName": "Pérez",
    "email": "juan.perez@email.com",
    "phone": "+1234567890",
    "source": "API",
    "locationId": "tu-location-id"  // opcional
}
```

**Response (201 Created):**
```json
{
    "id": 1,
    "ghl_id": "contacto-ghl-id",
    "location_id": "tu-location-id",
    "first_name": "Juan",
    "last_name": "Pérez",
    "email": "juan.perez@email.com",
    "phone": "+1234567890",
    "source": "API",
    "date_added": "2024-01-15T10:30:00Z",
    "date_updated": "2024-01-15T10:30:00Z"
}
```

**Características:**
- ✅ Crea contacto en GoHighLevel
- ✅ Almacena localmente en BD
- ✅ Maneja duplicados automáticamente
- ✅ Agrega tag "paciente-ficticio"

</details>

<details>
<summary><b>📋 GET /contacts/</b> - Listar todos los contactos</summary>

**Response (200 OK):**
```json
[
    {
        "id": 1,
        "ghl_id": "contacto-ghl-id",
        "first_name": "Juan",
        "last_name": "Pérez",
        "email": "juan.perez@email.com",
        "phone": "+1234567890",
        "date_added": "2024-01-15T10:30:00Z"
    }
]
```

</details>

#### **Citas**

<details>
<summary><b>📝 POST /appointments/create/</b> - Crear cita ligada a contacto</summary>

**Request Body:**
```json
{
    "calendarId": "tu-calendar-id",
    "contactId": "contacto-ghl-id",
    "startTime": "2024-01-20T10:00:00Z",
    "endTime": "2024-01-20T11:00:00Z",
    "title": "Consulta médica",
    "appointmentStatus": "confirmed",
    "assignedUserId": "tu-user-id",
    "locationId": "tu-location-id"
}
```

**Response (201 Created):**
```json
{
    "id": 1,
    "ghl_id": "cita-ghl-id",
    "location_id": "tu-location-id",
    "calendar_id": "tu-calendar-id",
    "contact_id": "contacto-ghl-id",
    "title": "Consulta médica",
    "appointment_status": "confirmed",
    "start_time": "2024-01-20T10:00:00Z",
    "end_time": "2024-01-20T11:00:00Z",
    "date_added": "2024-01-15T10:30:00Z"
}
```

</details>

<details>
<summary><b>📋 GET /appointments/</b> - Listar todas las citas</summary>

**Response (200 OK):**
```json
[
    {
        "id": 1,
        "ghl_id": "cita-ghl-id",
        "title": "Consulta médica",
        "appointment_status": "confirmed",
        "start_time": "2024-01-20T10:00:00Z",
        "end_time": "2024-01-20T11:00:00Z"
    }
]
```

</details>

<details>
<summary><b>🔄 PUT /appointments/&lt;appointment_id&gt;/update/</b> - Actualizar cita</summary>

**Request Body:**
```json
{
    "title": "Consulta médica actualizada",
    "appointmentStatus": "cancelled",
    "startTime": "2024-01-20T14:00:00Z",
    "endTime": "2024-01-20T15:00:00Z"
}
```

**Response (200 OK):**
```json
{
    "message": "Cita actualizada exitosamente",
    "appointment": { /* datos actualizados */ }
}
```

</details>

<details>
<summary><b>🗑️ DELETE /appointments/&lt;appointment_id&gt;/delete/</b> - Eliminar cita</summary>

**Response (200 OK):**
```json
{
    "message": "Cita eliminada exitosamente",
    "deleted_id": "cita-ghl-id"
}
```

</details>

#### **Webhooks**

<details>
<summary><b>🔔 POST /webhook/ghl/</b> - Recibir eventos de GoHighLevel</summary>

**Eventos soportados:**
- `ContactCreate` - Nuevo contacto creado
- `ContactUpdate` - Contacto actualizado
- `ContactDelete` - Contacto eliminado
- `AppointmentCreate` - Nueva cita creada
- `AppointmentUpdate` - Cita actualizada
- `AppointmentDelete` - Cita eliminada

**Request Body (ejemplo):**
```json
{
    "type": "ContactCreate",
    "locationId": "tu-location-id",
    "contact": {
        "id": "contacto-ghl-id",
        "firstName": "María",
        "lastName": "González",
        "email": "maria@email.com"
    }
}
```

**Response (200 OK):**
```json
{
    "status": "success",
    "message": "Webhook procesado correctamente"
}
```

</details>

### 🔄 Flujo de Trabajo Completo

```mermaid
graph LR
    A[Cliente] -->|1. POST /contacts/create/| B[Backend]
    B -->|2. Crear contacto| C[GoHighLevel API]
    C -->|3. Retorna contacto_id| B
    B -->|4. Guarda en BD| D[(SQLite)]
    B -->|5. Retorna contacto| A
    A -->|6. POST /appointments/create/| B
    B -->|7. Crear cita| C
    C -->|8. Retorna cita_id| B
    B -->|9. Guarda en BD| D
    B -->|10. Retorna cita| A
```

### 📝 Ejemplo de Uso Completo

```bash
# 1. Crear un contacto
curl -X POST http://localhost:8000/contacts/create/ \
  -H "Content-Type: application/json" \
  -d '{
    "firstName": "María",
    "lastName": "González",
    "email": "maria.gonzalez@email.com",
    "phone": "+1234567891",
    "source": "API"
  }'

# Respuesta: { "ghl_id": "abc123", ... }

# 2. Crear una cita para ese contacto
curl -X POST http://localhost:8000/appointments/create/ \
  -H "Content-Type: application/json" \
  -d '{
    "calendarId": "tu-calendar-id",
    "contactId": "abc123",
    "startTime": "2024-01-20T14:00:00Z",
    "endTime": "2024-01-20T15:00:00Z",
    "title": "Consulta médica",
    "appointmentStatus": "confirmed"
  }'

# 3. Listar todas las citas
curl -X GET http://localhost:8000/appointments/

# 4. Actualizar una cita
curl -X PUT http://localhost:8000/appointments/abc123/update/ \
  -H "Content-Type: application/json" \
  -d '{
    "appointmentStatus": "cancelled"
  }'

# 5. Eliminar una cita
curl -X DELETE http://localhost:8000/appointments/abc123/delete/
```

---

## 🔍 Calidad de Código

### Linting con flake8
```bash
cd backend
flake8 .
```

### Formateo con Black
```bash
cd backend
black .
```

### Ordenar imports con isort
```bash
cd backend
isort .
```

### Análisis de seguridad con Bandit
```bash
cd backend
bandit -r . -ll
```

## 🔄 Integración Continua

El proyecto utiliza GitHub Actions para CI/CD. Los workflows se ejecutan automáticamente en:

- **Push** a las ramas: `main`, `pruebas`, `develop`
- **Pull Requests** hacia: `main`, `develop`

### Workflows incluidos:

1. **Test**: Ejecuta tests en múltiples versiones de Python (3.10, 3.11, 3.12)
2. **Code Quality**: Verifica formateo, imports y seguridad
3. **Build**: Valida que el proyecto esté listo para producción

### Ver estado de CI
Puedes ver el estado de los workflows en:
- Badge en este README
- Pestaña "Actions" en GitHub

## 📁 Estructura del Proyecto

```
Backend_GHL-Nivel-2/
├── 📂 .github/
│   └── workflows/
│       └── ci.yml                    # ⚙️ Configuración de CI/CD
│
├── 📂 backend/                       # 🎯 Código principal
│   ├── 📂 appointments/              # 📅 App de citas y contactos
│   │   ├── models.py                 # 🗄️ Modelos: Contact, Appointment
│   │   ├── views.py                  # 🔧 Lógica de negocio y API
│   │   ├── serializers.py            # 🔄 Serializadores DRF
│   │   ├── urls.py                   # 🛣️ Rutas de la API
│   │   ├── admin.py                  # 👨‍💼 Configuración del admin
│   │   └── tests.py                  # 🧪 Tests unitarios
│   │
│   ├── 📂 mi_proyecto/               # ⚙️ Configuración Django
│   │   ├── settings.py               # 🔧 Settings principal
│   │   ├── urls.py                   # 🛣️ URLs raíz
│   │   ├── wsgi.py                   # 🚀 WSGI para producción
│   │   └── asgi.py                   # 🚀 ASGI para async
│   │
│   ├── manage.py                     # 🎮 CLI de Django
│   ├── db.sqlite3                    # 💾 Base de datos SQLite
│   ├── requirements.txt              # 📦 Dependencias producción
│   ├── requirements-dev.txt          # 🛠️ Dependencias desarrollo
│   ├── pytest.ini                    # 🧪 Config de pytest
│   ├── .flake8                       # 📏 Config de flake8
│   ├── pyproject.toml                # 🎨 Config de Black/isort
│   ├── .env                          # 🔐 Variables de entorno (no versionado)
│   └── env.example                   # 📋 Ejemplo de .env
│
├── 📂 docs/                          # 📚 Documentación
│   ├── CONTACTOS_INTEGRACION.md      # 📖 Guía de integración
│   └── CI_CD.md                      # 📖 Guía de CI/CD
│
├── 📂 postman/                       # 📮 Colección de Postman
│   └── Backend_GHL.postman_collection.json
│
├── 📂 venv/                          # 🐍 Entorno virtual (no versionado)
├── .gitignore                        # 🚫 Archivos ignorados
└── README.md                         # 📖 Este archivo
```

### 🗄️ Modelos de Datos

#### **Contact** (Contacto)
```python
- ghl_id: ID único de GoHighLevel
- location_id: ID de la ubicación en GHL
- first_name: Nombre
- last_name: Apellido
- email: Correo electrónico
- phone: Teléfono
- source: Origen del contacto
- date_added: Fecha de creación
- date_updated: Fecha de actualización
```

#### **Appointment** (Cita)
```python
- ghl_id: ID único de GoHighLevel
- location_id: ID de la ubicación en GHL
- calendar_id: ID del calendario
- contact_id: ID del contacto asociado
- title: Título de la cita
- appointment_status: Estado (confirmed, cancelled, etc.)
- assigned_user_id: ID del usuario asignado
- notes: Notas adicionales
- start_time: Fecha/hora de inicio
- end_time: Fecha/hora de fin
- source: Origen de la cita
- date_added: Fecha de creación
- date_updated: Fecha de actualización
```

## 🌿 Ramas

- **main**: Rama principal (producción)
- **pruebas**: Rama para pruebas y experimentos
- **develop**: Rama de desarrollo (si se usa)

## 📚 Documentación Adicional

| Documento | Descripción |
|-----------|-------------|
| 📖 [Integración de Contactos](docs/CONTACTOS_INTEGRACION.md) | Guía completa de integración con GHL |
| 📖 [CI/CD](docs/CI_CD.md) | Documentación de integración continua |
| 📮 [Colección Postman](postman/) | Colección para probar la API |

---

## 🔐 Variables de Entorno

### Configuración Completa

Crea un archivo `.env` en el directorio `backend/` basado en `env.example`:

```env
# ============================================
# DJANGO SETTINGS
# ============================================
SECRET_KEY=tu-clave-secreta-super-segura-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# ============================================
# GOHIGHLEVEL API CONFIGURATION
# ============================================
GHL_API_KEY=tu-api-key-de-gohighlevel
GHL_LOCATION_ID=tu-location-id-de-ghl
GHL_ASSIGNED_USER_ID=tu-user-id-de-ghl
GHL_API_VERSION=2021-04-15

# ============================================
# CORS SETTINGS (opcional)
# ============================================
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8080

# ============================================
# DATABASE (opcional - por defecto usa SQLite)
# ============================================
# DATABASE_URL=sqlite:///db.sqlite3
```

### 📝 Descripción de Variables

| Variable | Requerida | Descripción |
|----------|-----------|-------------|
| `SECRET_KEY` | ✅ Sí | Clave secreta de Django para seguridad |
| `DEBUG` | ✅ Sí | Modo debug (True/False) |
| `ALLOWED_HOSTS` | ✅ Sí | Hosts permitidos separados por coma |
| `GHL_API_KEY` | ✅ Sí | API Key de GoHighLevel |
| `GHL_LOCATION_ID` | ✅ Sí | ID de ubicación en GHL |
| `GHL_ASSIGNED_USER_ID` | ⚠️ Recomendado | ID de usuario para asignar citas |
| `GHL_API_VERSION` | ⚠️ Recomendado | Versión de la API de GHL |
| `CORS_ALLOWED_ORIGINS` | ❌ Opcional | Orígenes permitidos para CORS |

### 🔑 Obtener Credenciales de GoHighLevel

1. Inicia sesión en tu cuenta de [GoHighLevel](https://app.gohighlevel.com/)
2. Ve a **Settings** → **API Keys**
3. Crea una nueva API Key o usa una existente
4. Copia el **Location ID** desde la configuración de tu ubicación
5. Copia tu **User ID** desde tu perfil

---

## 🤝 Contribuir

¿Quieres contribuir al proyecto? ¡Genial! Sigue estos pasos:

### 📝 Proceso de Contribución

1. **Fork** el proyecto
2. **Crea una rama** para tu feature
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit** tus cambios
   ```bash
   git commit -m '✨ Add: Nueva funcionalidad increíble'
   ```
4. **Push** a la rama
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Abre un Pull Request**

### ✅ Checklist antes de PR

- [ ] Los tests pasan localmente (`pytest`)
- [ ] El código está formateado (`black .` y `isort .`)
- [ ] No hay errores de linting (`flake8 .`)
- [ ] Se agregaron tests para nuevas funcionalidades
- [ ] La documentación está actualizada

> 💡 **Nota:** Los Pull Requests activarán automáticamente los workflows de CI que validarán tu código.

### 🎨 Convenciones de Commits

Usamos commits semánticos:

- `✨ Add:` Nueva funcionalidad
- `🐛 Fix:` Corrección de bugs
- `📚 Docs:` Cambios en documentación
- `🎨 Style:` Formateo, sin cambios de código
- `♻️ Refactor:` Refactorización de código
- `🧪 Test:` Agregar o modificar tests
- `⚡ Perf:` Mejoras de rendimiento

---

## 🚀 Despliegue

### Despliegue en Producción

Para desplegar en producción, asegúrate de:

1. **Configurar variables de entorno de producción**
   ```env
   DEBUG=False
   SECRET_KEY=clave-super-segura-aleatoria
   ALLOWED_HOSTS=tu-dominio.com
   ```

2. **Usar una base de datos robusta** (PostgreSQL recomendado)
   ```env
   DATABASE_URL=postgresql://user:password@localhost/dbname
   ```

3. **Recolectar archivos estáticos**
   ```bash
   python manage.py collectstatic --noinput
   ```

4. **Ejecutar con Gunicorn**
   ```bash
   gunicorn mi_proyecto.wsgi:application --bind 0.0.0.0:8000
   ```

### 🐳 Docker (Próximamente)

Estamos trabajando en agregar soporte para Docker para facilitar el despliegue.

---

## 🐛 Solución de Problemas

### Problemas Comunes

<details>
<summary><b>Error: "No module named 'django'"</b></summary>

**Solución:** Asegúrate de tener el entorno virtual activado e instala las dependencias:
```bash
venv\Scripts\activate  # Windows
pip install -r backend/requirements.txt
```
</details>

<details>
<summary><b>Error: "DJANGO_SETTINGS_MODULE is not set"</b></summary>

**Solución:** Asegúrate de estar en el directorio `backend/` al ejecutar comandos de Django:
```bash
cd backend
python manage.py runserver
```
</details>

<details>
<summary><b>Error de conexión con GoHighLevel API</b></summary>

**Solución:** Verifica que:
1. Tu `GHL_API_KEY` sea válida
2. El `GHL_LOCATION_ID` sea correcto
3. Tengas permisos en la cuenta de GHL
4. La API Key no haya expirado
</details>

<details>
<summary><b>Tests fallan en CI pero pasan localmente</b></summary>

**Solución:** 
1. Verifica que el archivo `.env` no esté siendo usado en CI
2. Revisa los logs en GitHub Actions
3. Asegúrate de que no haya dependencias de datos locales
</details>

---

## 📊 Estado del Proyecto

| Aspecto | Estado |
|---------|--------|
| **Tests** | ![CI Status](https://github.com/Hernandz09/Backend_GHL-Nivel-2/workflows/CI%20-%20Django%20Backend/badge.svg) |
| **Cobertura** | En progreso |
| **Documentación** | ✅ Completa |
| **API** | ✅ Funcional |
| **Integración GHL** | ✅ Activa |

---

## 🎯 Roadmap

### ✅ Completado
- [x] API REST completa para contactos y citas
- [x] Integración bidireccional con GoHighLevel
- [x] Sistema de webhooks
- [x] Tests automatizados
- [x] CI/CD con GitHub Actions
- [x] Documentación completa

### 🚧 En Progreso
- [ ] Aumentar cobertura de tests a 90%+
- [ ] Agregar autenticación JWT
- [ ] Implementar rate limiting

### 📋 Planeado
- [ ] Soporte para Docker
- [ ] Dashboard web con React
- [ ] Notificaciones por email
- [ ] Exportación de reportes
- [ ] API de estadísticas
- [ ] Integración con más calendarios

---

## 📞 Soporte

¿Necesitas ayuda? Aquí hay algunas opciones:

- 📖 **Documentación**: Revisa la carpeta [docs/](docs/)
- 🐛 **Issues**: Reporta bugs en [GitHub Issues](https://github.com/Hernandz09/Backend_GHL-Nivel-2/issues)
- 💬 **Discusiones**: Únete a las [GitHub Discussions](https://github.com/Hernandz09/Backend_GHL-Nivel-2/discussions)
- 📮 **Postman**: Usa la colección en [postman/](postman/) para probar la API

---

## 📄 Licencia

Este proyecto es parte del programa **GHL Nivel 2**.

---

## 👥 Autor

<div align="center">

**Desarrollado con ❤️ por**

[![GitHub](https://img.shields.io/badge/GitHub-Hernandz09-181717?style=for-the-badge&logo=github)](https://github.com/Hernandz09)

</div>

---

<div align="center">

### ⭐ Si este proyecto te fue útil, considera darle una estrella

**[⬆ Volver arriba](#-backend-ghl---nivel-2)**

</div>

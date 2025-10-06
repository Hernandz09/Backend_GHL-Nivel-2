# Integración de Contactos + Citas (GHL)

## Descripción
Esta funcionalidad permite crear contactos ficticios en GHL y luego crear citas ligadas a esos contactos, cumpliendo con el objetivo de la Sala 2/3.

## Endpoints Disponibles

### 1. Crear Contacto Ficticio
**POST** `/contacts/create/`

**Payload:**
```json
{
    "firstName": "Juan",
    "lastName": "Pérez",
    "email": "juan.perez@email.com",
    "phone": "+1234567890",
    "source": "API",
    "locationId": "tu-location-id" // opcional, usa GHL_LOCATION_ID del .env
}
```

**Respuesta:**
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

### 2. Listar Contactos
**GET** `/contacts/`

### 3. Crear Cita con Contacto
**POST** `/appointments/create/`

**Payload:**
```json
{
    "calendarId": "tu-calendar-id",
    "contactId": "contacto-ghl-id-del-paso-1",
    "startTime": "2024-01-20T10:00:00Z",
    "endTime": "2024-01-20T11:00:00Z",
    "title": "Consulta médica",
    "appointmentStatus": "confirmed",
    "assignedUserId": "tu-user-id",
    "locationId": "tu-location-id"
}
```

## Flujo de Trabajo Completo - Integración Doble

### Paso 1: Crear Contacto Ficticio
```bash
curl -X POST http://localhost:8000/contacts/create/ \
  -H "Content-Type: application/json" \
  -d '{
    "firstName": "María",
    "lastName": "González",
    "email": "maria.gonzalez.nueva@email.com",
    "phone": "+1234567891",
    "source": "API",
    "locationId": "CRlTCqv7ASS9xOpPQ59O"
  }'
```

**Respuesta esperada:**
```json
{
    "id": 1,
    "ghl_id": "nuevo-contacto-ghl-id",
    "location_id": "CRlTCqv7ASS9xOpPQ59O",
    "first_name": "María",
    "last_name": "González",
    "email": "maria.gonzalez.nueva@email.com",
    "phone": "+1234567891",
    "source": "API",
    "date_added": "2024-01-15T10:30:00Z",
    "date_updated": "2024-01-15T10:30:00Z"
}
```

### Paso 2: Crear Cita Ligada al Contacto
```bash
curl -X POST http://localhost:8000/appointments/create/ \
  -H "Content-Type: application/json" \
  -d '{
    "calendarId": "tu-calendar-id",
    "contactId": "nuevo-contacto-ghl-id-del-paso-1",
    "startTime": "2024-01-20T14:00:00Z",
    "endTime": "2024-01-20T15:00:00Z",
    "title": "Consulta médica - María González",
    "appointmentStatus": "confirmed",
    "assignedUserId": "tu-user-id",
    "locationId": "CRlTCqv7ASS9xOpPQ59O"
  }'
```

### Paso 3: Verificar Integración
```bash
# Ver contactos creados
curl -X GET http://localhost:8000/contacts/

# Ver citas creadas
curl -X GET http://localhost:8000/appointments/
```

## Variables de Entorno Requeridas

Asegúrate de tener configuradas estas variables en tu archivo `.env`:

```env
GHL_API_KEY=tu-api-key
GHL_LOCATION_ID=tu-location-id
GHL_ASSIGNED_USER_ID=tu-user-id
GHL_API_VERSION=2021-04-15
```

## Características

- ✅ Creación de contactos ficticios en GHL
- ✅ Almacenamiento local de contactos en BD
- ✅ Creación de citas ligadas a contactos existentes
- ✅ Sincronización bidireccional con GHL
- ✅ Manejo de errores y validaciones
- ✅ Webhooks para actualizaciones automáticas
- ✅ **Manejo automático de contactos duplicados**
- ✅ **Integración doble: Contactos + Citas**

## Notas Importantes

1. Los contactos se crean tanto en GHL como en la base de datos local
2. Las citas requieren un `contactId` válido de GHL
3. Se incluye automáticamente el tag "paciente-ficticio" en los contactos creados
4. El sistema maneja automáticamente la sincronización de datos
5. **Si intentas crear un contacto duplicado, el sistema devuelve el contacto existente automáticamente**
6. **El flujo completo garantiza que las citas estén ligadas a contactos reales de GHL**

## Manejo de Contactos Duplicados

Si intentas crear un contacto con un teléfono o email que ya existe en GHL, el sistema:

1. Detecta el error de duplicado
2. Extrae el ID del contacto existente
3. Obtiene los datos del contacto existente desde GHL
4. Guarda/actualiza el contacto en la base de datos local
5. Devuelve una respuesta exitosa con los datos del contacto existente

**Ejemplo de respuesta para contacto duplicado:**
```json
{
    "message": "Contacto duplicado encontrado. Se devuelve el contacto existente.",
    "duplicate_field": "phone",
    "existing_contact_id": "xiVM6fAR0x0mBwNHQFrH",
    "contact": {
        "id": 1,
        "ghl_id": "xiVM6fAR0x0mBwNHQFrH",
        "location_id": "CRlTCqv7ASS9xOpPQ59O",
        "first_name": "María",
        "last_name": "González",
        "email": "maria.gonzalez@email.com",
        "phone": "+1234567890",
        "source": "API",
        "date_added": "2024-01-15T10:30:00Z",
        "date_updated": "2024-01-15T10:30:00Z"
    }
}
```

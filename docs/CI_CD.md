# Integración Continua (CI/CD)

## 📋 Descripción General

Este proyecto utiliza **GitHub Actions** para automatizar pruebas, verificaciones de calidad de código y validaciones de despliegue.

## 🔄 Workflows Configurados

### 1. Test Job
Ejecuta las pruebas del proyecto en múltiples versiones de Python.

**Características:**
- Matriz de pruebas: Python 3.10, 3.11, 3.12
- Ejecuta migraciones de base de datos
- Corre todos los tests de Django
- Verifica linting con flake8
- Comprueba que no haya migraciones pendientes

**Se ejecuta en:**
- Push a `main`, `pruebas`, `develop`
- Pull requests hacia `main`, `develop`

### 2. Code Quality Job
Verifica la calidad y seguridad del código.

**Características:**
- Formateo con **Black**
- Ordenamiento de imports con **isort**
- Análisis de seguridad con **Bandit**

**Nota:** Estos checks son informativos (continue-on-error) para no bloquear el workflow inicialmente.

### 3. Build Job
Valida que el proyecto esté listo para producción.

**Características:**
- Recolecta archivos estáticos
- Ejecuta `check --deploy` para validar configuración de producción
- Solo se ejecuta si los jobs anteriores pasan exitosamente

## 🚀 Cómo Funciona

### Flujo de Trabajo

```
┌─────────────────┐
│  Push/PR        │
└────────┬────────┘
         │
         ├──────────────────┬──────────────────┐
         ▼                  ▼                  ▼
    ┌─────────┐       ┌──────────┐      ┌──────────┐
    │  Test   │       │  Code    │      │  Build   │
    │  Job    │       │  Quality │      │  Check   │
    └─────────┘       └──────────┘      └──────────┘
         │                  │                  │
         └──────────────────┴──────────────────┘
                            │
                            ▼
                    ┌──────────────┐
                    │   Success    │
                    │   or Fail    │
                    └──────────────┘
```

### Triggers (Disparadores)

El workflow se activa automáticamente cuando:

1. **Push a ramas específicas:**
   - `main`
   - `pruebas`
   - `develop`

2. **Pull Request hacia:**
   - `main`
   - `develop`

## 📊 Verificar Estado de CI

### En GitHub
1. Ve a la pestaña **Actions** del repositorio
2. Verás la lista de workflows ejecutados
3. Click en cualquier workflow para ver detalles

### Badge de Estado
El README incluye un badge que muestra el estado actual:

```markdown
![CI Status](https://github.com/Hernandz09/Backend_GHL-Nivel-2/workflows/CI%20-%20Django%20Backend/badge.svg)
```

Estados posibles:
- ✅ **Passing**: Todas las pruebas pasaron
- ❌ **Failing**: Algunas pruebas fallaron
- 🟡 **Running**: Workflow en ejecución

## 🛠️ Ejecutar Checks Localmente

Antes de hacer push, puedes ejecutar los mismos checks localmente:

### 1. Instalar dependencias de desarrollo
```bash
cd backend
pip install -r requirements-dev.txt
```

### 2. Ejecutar tests
```bash
python manage.py test
# o con pytest
pytest
```

### 3. Verificar linting
```bash
flake8 .
```

### 4. Formatear código
```bash
black .
isort .
```

### 5. Análisis de seguridad
```bash
bandit -r . -ll
```

### 6. Verificar migraciones
```bash
python manage.py makemigrations --check --dry-run
```

### 7. Check de despliegue
```bash
python manage.py check --deploy
```

## 🔧 Configuración de Herramientas

### Flake8 (`.flake8`)
- Longitud máxima de línea: 127
- Excluye: migraciones, venv, archivos de configuración
- Complejidad máxima: 10

### Black (`pyproject.toml`)
- Longitud de línea: 127
- Versiones objetivo: Python 3.10, 3.11, 3.12
- Excluye: migraciones, entornos virtuales

### isort (`pyproject.toml`)
- Perfil: black (compatible con Black)
- Secciones personalizadas para Django
- Ordena imports de forma consistente

### pytest (`pytest.ini`)
- Genera reportes de cobertura
- Formatos: terminal, HTML, XML
- Busca tests en la app `appointments`

## 📈 Cobertura de Código

El workflow genera reportes de cobertura que puedes ver localmente:

```bash
cd backend
pytest --cov=. --cov-report=html
# Abre htmlcov/index.html en tu navegador
```

## 🚨 Solución de Problemas

### El workflow falla en tests
1. Revisa los logs en GitHub Actions
2. Ejecuta los tests localmente: `python manage.py test`
3. Verifica que todas las migraciones estén aplicadas

### Fallos de linting
1. Ejecuta `flake8 .` localmente
2. Corrige los errores reportados
3. Considera usar `black .` para auto-formatear

### Fallos de seguridad (Bandit)
1. Revisa el reporte de Bandit
2. Evalúa si son falsos positivos
3. Corrige problemas de seguridad reales
4. Usa `# nosec` solo si estás seguro que es seguro

### Fallos en check de despliegue
1. Revisa `settings.py`
2. Asegúrate de tener configuraciones apropiadas para producción
3. Verifica SECRET_KEY, ALLOWED_HOSTS, etc.

## 🔐 Secrets y Variables de Entorno

El workflow crea un `.env` temporal para CI:

```yaml
- name: Create .env file
  run: |
    cd backend
    cp env.example .env
    echo "SECRET_KEY=test-secret-key-for-ci-only" >> .env
    echo "DEBUG=True" >> .env
```

**Para producción**, configura GitHub Secrets:
1. Ve a Settings → Secrets and variables → Actions
2. Agrega secrets necesarios (API keys, credenciales, etc.)
3. Úsalos en el workflow con `${{ secrets.SECRET_NAME }}`

## 📝 Mejoras Futuras

Posibles mejoras al workflow de CI:

- [ ] Agregar cobertura de código con Codecov
- [ ] Implementar deployment automático
- [ ] Agregar tests de integración
- [ ] Configurar notificaciones (Slack, Discord, etc.)
- [ ] Agregar análisis de dependencias (Dependabot)
- [ ] Implementar semantic versioning automático
- [ ] Agregar Docker builds
- [ ] Tests de performance

## 📚 Referencias

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Django Testing](https://docs.djangoproject.com/en/stable/topics/testing/)
- [pytest-django](https://pytest-django.readthedocs.io/)
- [Black Documentation](https://black.readthedocs.io/)
- [Flake8 Documentation](https://flake8.pycqa.org/)

## 💡 Tips

1. **Commits frecuentes**: Haz commits pequeños para detectar problemas rápido
2. **Tests locales**: Siempre ejecuta tests antes de push
3. **Pre-commit hooks**: Considera usar pre-commit para automatizar checks locales
4. **Revisa logs**: Si falla CI, revisa los logs completos en GitHub Actions
5. **Mantén actualizado**: Actualiza regularmente las versiones de las actions

## 🤝 Contribuir

Al contribuir al proyecto:

1. Asegúrate de que todos los tests pasen
2. Mantén la cobertura de código alta
3. Sigue las guías de estilo (Black, isort, flake8)
4. Escribe tests para nuevas funcionalidades
5. Actualiza la documentación si es necesario

El workflow de CI te ayudará a mantener la calidad del código automáticamente.

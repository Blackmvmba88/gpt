# Mi Sistema GPT

**Tu asistente personal de inteligencia artificial**

Este es un sistema personal de GPT que proporciona una interfaz simple e intuitiva para interactuar con modelos de IA. Diseñado para ser tu propio sistema ("mi sistema") personalizable y fácil de usar.

## 🚀 Características

- Interfaz de consola colorida e intuitiva
- Historial de conversación con límite configurable
- Comandos del sistema integrados
- Configuración personalizable
- Soporte para múltiples idiomas (principalmente español)
- Respuestas simuladas inteligentes

## 📋 Requisitos

- Python 3.7+
- Las dependencias listadas en `requirements.txt`

## 🛠️ Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/Blackmvmba88/gpt.git
cd gpt
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. (Opcional) Copia y personaliza la configuración:
```bash
cp config.example.json config.json
```

## 🎯 Uso

Ejecuta el sistema:
```bash
python mi_sistema.py
```

### Comandos disponibles:
- `/help` - Mostrar ayuda
- `/clear` - Limpiar historial de conversación
- `/history` - Mostrar historial de conversación
- `/config` - Mostrar configuración actual
- `/quit` - Salir del sistema

## ⚙️ Configuración

Puedes personalizar el sistema editando `config.json`:

```json
{
    "system_name": "Mi Sistema GPT",
    "version": "1.0.0",
    "max_history": 10,
    "default_model": "gpt-3.5-turbo",
    "language": "es",
    "welcome_message": "¡Bienvenido a tu sistema personal de IA!"
}
```

## 🔮 Futuras mejoras

- Integración con API de OpenAI
- Soporte para múltiples modelos de IA
- Persistencia de conversaciones
- Interfaz web
- Plugins y extensiones
- Procesamiento de archivos

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir los cambios que te gustaría hacer.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

**Mi Sistema GPT** - *Tu asistente personal de IA*

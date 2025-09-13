#!/bin/bash

# Mi Sistema GPT - Startup Script
# This script makes it easy to start your personal GPT system

echo "🚀 Iniciando Mi Sistema GPT..."

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 no está instalado."
    exit 1
fi

# Check if requirements are installed
echo "📦 Verificando dependencias..."
python3 -c "import colorama, requests, dotenv" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "📥 Instalando dependencias..."
    pip3 install -r requirements.txt
fi

# Start the system
echo "✨ Iniciando tu asistente personal..."
echo
python3 mi_sistema.py
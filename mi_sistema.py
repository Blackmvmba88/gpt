#!/usr/bin/env python3
"""
Mi Sistema GPT - Personal GPT System
A simple interface for interacting with AI models
"""

import os
import sys
import json
from typing import Dict, List, Optional
import colorama
from colorama import Fore, Style
from dotenv import load_dotenv

# Initialize colorama for colored output
colorama.init()

class MiSistema:
    """
    Mi Sistema - A personal GPT interface
    """
    
    def __init__(self):
        """Initialize the system"""
        load_dotenv()
        self.config = self.load_config()
        self.conversation_history: List[Dict[str, str]] = []
        
    def load_config(self) -> Dict:
        """Load configuration from file or environment"""
        config = {
            "system_name": "Mi Sistema GPT",
            "version": "1.0.0",
            "max_history": 10,
            "default_model": "gpt-3.5-turbo"
        }
        
        # Try to load from config file
        config_file = "config.json"
        if os.path.exists(config_file):
            try:
                with open(config_file, 'r', encoding='utf-8') as f:
                    file_config = json.load(f)
                    config.update(file_config)
            except (json.JSONDecodeError, IOError):
                print(f"{Fore.YELLOW}Warning: Could not load config file{Style.RESET_ALL}")
        
        return config
    
    def display_banner(self):
        """Display the system banner"""
        print(f"{Fore.CYAN}╔══════════════════════════════════════╗{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║          {Fore.WHITE}MI SISTEMA GPT{Fore.CYAN}             ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║      {Fore.YELLOW}Tu Asistente Personal de IA{Fore.CYAN}     ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║            {Fore.GREEN}Versión {self.config['version']}{Fore.CYAN}            ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}╚══════════════════════════════════════╝{Style.RESET_ALL}")
        print()
    
    def display_help(self):
        """Display help information"""
        print(f"{Fore.GREEN}Comandos disponibles:{Style.RESET_ALL}")
        print(f"  {Fore.YELLOW}/help{Style.RESET_ALL}     - Mostrar esta ayuda")
        print(f"  {Fore.YELLOW}/clear{Style.RESET_ALL}    - Limpiar historial de conversación")
        print(f"  {Fore.YELLOW}/history{Style.RESET_ALL}  - Mostrar historial de conversación")
        print(f"  {Fore.YELLOW}/config{Style.RESET_ALL}   - Mostrar configuración actual")
        print(f"  {Fore.YELLOW}/quit{Style.RESET_ALL}     - Salir del sistema")
        print()
        print(f"{Fore.CYAN}Simplemente escribe tu mensaje para chatear con el sistema.{Style.RESET_ALL}")
        print()
    
    def display_config(self):
        """Display current configuration"""
        print(f"{Fore.GREEN}Configuración actual:{Style.RESET_ALL}")
        for key, value in self.config.items():
            print(f"  {Fore.YELLOW}{key}:{Style.RESET_ALL} {value}")
        print()
    
    def display_history(self):
        """Display conversation history"""
        if not self.conversation_history:
            print(f"{Fore.YELLOW}No hay historial de conversación.{Style.RESET_ALL}")
            return
        
        print(f"{Fore.GREEN}Historial de conversación:{Style.RESET_ALL}")
        for i, entry in enumerate(self.conversation_history, 1):
            role_color = Fore.BLUE if entry['role'] == 'user' else Fore.MAGENTA
            print(f"{role_color}{i}. {entry['role'].capitalize()}:{Style.RESET_ALL} {entry['content']}")
        print()
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history.clear()
        print(f"{Fore.GREEN}Historial de conversación limpiado.{Style.RESET_ALL}")
        print()
    
    def add_to_history(self, role: str, content: str):
        """Add message to conversation history"""
        self.conversation_history.append({"role": role, "content": content})
        
        # Keep only the last max_history messages
        if len(self.conversation_history) > self.config['max_history']:
            self.conversation_history = self.conversation_history[-self.config['max_history']:]
    
    def simulate_gpt_response(self, user_input: str) -> str:
        """
        Simulate a GPT response (placeholder for actual API integration)
        In a real implementation, this would call OpenAI's API or another AI service
        """
        # Simple responses based on keywords
        user_lower = user_input.lower()
        
        if any(word in user_lower for word in ['hola', 'hello', 'hi', 'buenos días', 'buenas tardes']):
            return "¡Hola! Soy tu asistente personal de IA. ¿En qué puedo ayudarte hoy?"
        
        elif any(word in user_lower for word in ['cómo estás', 'how are you', '¿cómo te sientes?']):
            return "¡Estoy funcionando perfectamente! Gracias por preguntar. ¿Cómo puedo asistirte?"
        
        elif any(word in user_lower for word in ['nombre', 'name', 'quién eres', 'who are you']):
            return f"Soy {self.config['system_name']}, tu sistema personal de inteligencia artificial."
        
        elif any(word in user_lower for word in ['ayuda', 'help', 'qué puedes hacer']):
            return "Puedo ayudarte con conversaciones, responder preguntas, y asistirte en diversas tareas. Usa '/help' para ver los comandos disponibles."
        
        elif any(word in user_lower for word in ['gracias', 'thank you', 'thanks']):
            return "¡De nada! Estoy aquí para ayudarte cuando lo necesites."
        
        elif any(word in user_lower for word in ['adiós', 'goodbye', 'bye', 'hasta luego']):
            return "¡Hasta luego! Ha sido un placer ayudarte. Vuelve cuando quieras."
        
        else:
            return f"He recibido tu mensaje: '{user_input}'. En una implementación completa, esto se procesaría con un modelo de IA real. ¿Hay algo específico en lo que pueda ayudarte?"
    
    def process_command(self, user_input: str) -> bool:
        """Process system commands. Returns True if command was processed, False otherwise"""
        if user_input.startswith('/'):
            command = user_input[1:].lower().strip()
            
            if command == 'help':
                self.display_help()
            elif command == 'clear':
                self.clear_history()
            elif command == 'history':
                self.display_history()
            elif command == 'config':
                self.display_config()
            elif command in ['quit', 'exit', 'salir']:
                print(f"{Fore.GREEN}¡Hasta luego! Gracias por usar Mi Sistema GPT.{Style.RESET_ALL}")
                return True
            else:
                print(f"{Fore.RED}Comando no reconocido: {command}{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}Usa '/help' para ver los comandos disponibles.{Style.RESET_ALL}")
            
            return False  # Continue running
        
        return False  # Not a command
    
    def run(self):
        """Main system loop"""
        self.display_banner()
        print(f"{Fore.CYAN}¡Bienvenido a tu sistema personal de IA!{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Escribe '/help' para ver los comandos disponibles.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Escribe '/quit' para salir.{Style.RESET_ALL}")
        print()
        
        try:
            while True:
                # Get user input
                user_input = input(f"{Fore.BLUE}Tú: {Style.RESET_ALL}").strip()
                
                if not user_input:
                    continue
                
                # Check if it's a system command
                if user_input.startswith('/'):
                    if self.process_command(user_input):
                        break  # Quit command was issued
                    continue
                
                # Add user message to history
                self.add_to_history("user", user_input)
                
                # Generate response
                response = self.simulate_gpt_response(user_input)
                
                # Add AI response to history
                self.add_to_history("assistant", response)
                
                # Display response
                print(f"{Fore.MAGENTA}Sistema: {Style.RESET_ALL}{response}")
                print()
                
        except KeyboardInterrupt:
            print(f"\n{Fore.GREEN}¡Hasta luego! Gracias por usar Mi Sistema GPT.{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            sys.exit(1)

def main():
    """Main entry point"""
    sistema = MiSistema()
    sistema.run()

if __name__ == "__main__":
    main()
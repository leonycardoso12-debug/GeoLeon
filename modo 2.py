import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, simpledialog
import math
import datetime
import tempfile
import wave
import os
import asyncio
import threading
import urllib.request

# Configuração global inicial do tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ==========================================
# DICIONÁRIO DE TRADUÇÃO GLOBAL COMPLETO (10 IDIOMAS)
# ==========================================
TRADUCOES = {
    "Português": {
        "titulo": "GeoLeon OS - Central de {usuario} (2026)",
        "condutor": "Condutor:",
        "painel": "⚡ Painel e Desgaste",
        "manutencao": "🔧 Manutenção de Peças",
        "wifi": "🌐 Gestor Wi-Fi",
        "bt": "📡 Gestor Bluetooth",
        "guia": "🔍 Guia de Peças",
        "ai": "🤖 GeoLeon AI (Voz)",
        "pausado": "Estado: PAUSADO",
        "ativo": "Estado: ATIVO",
        "monitor_titulo": "CENTRAL DO VEÍCULO - BEM-VINDO, {usuario}",
        "odometro": "Odômetro: {odo:,.1f} km | Combustível: {comb:.1f} L",
        "manut_titulo": "SELECIONE COMPONENTES SUBSTITUÍDOS RECENTEMENTE",
        "iniciar_sis": "▶ INICIAR SISTEMA DE MONITORAMENTO",
        "parar_sis": "⏹ PARAR SISTEMA DE MONITORAMENTO",
        "escolha_sis": "Escolha a categoria do sistema para ver e marcar as peças:",
        "wifi_titulo": "GESTOR DE REDE WI-FI & INTERNET",
        "escanear_wifi": "📶 Escanear Redes Wi-Fi Disponíveis",
        "digite_wifi": "Ou digite o nome da rede (SSID) manualmente:",
        "senha_wifi": "Digite a senha do Wi-Fi...",
        "conectar_wifi": "🌐 Conectar à Rede & Internet",
        "bt_titulo": "GESTOR DE CONEXÃO BLUETOOTH",
        "escanear_bt": "📡 Escanear Aparelhos Bluetooth Próximos",
        "guia_titulo": "DICIONÁRIO TÉCNICO DE COMPONENTES",
        "ai_titulo": "COMPUTADOR DE BORDO INTELIGENTE - GEOLEON AI ({usuario})",
        "digite_ai": "Digite o seu pedido ou comando para a IA:",
        "consultar_txt": "🔍 Consultar Texto",
        "falar_carro": "🎤 Falar com o Carro (Voz)",
        "resposta_ai": "Resposta do Cérebro IA:",
        "sistema_ativo": "Sistema ativo e a operar normalmente.",
        "relatorio_ia": "Relatório GeoLeon AI",
        "tab_monitor": "Monitor",
        "tab_manutencao": "Manutenção",
        "tab_wifi": "Wi-Fi",
        "tab_bt": "Bluetooth",
        "tab_guia": "Guia",
        "tab_ai": "IA",
        "lbl_cores_titulo": "🎨 ESCOLHER COR DA INTERFACE",
        "lbl_dalton_titulo": "👁 ACESSIB / DALTONISMO",
        "btn_ativar_dalton": "Ativar Modo Alto Contraste",
        "btn_desativar_dalton": "Desativar Modo Daltônico"
    },
    "Português (Portugal)": {
        "titulo": "GeoLeon OS - Central de {usuario} (2026)",
        "condutor": "Condutor:", "painel": "⚡ Painel e Desgaste", "manutencao": "🔧 Manutenção de Peças",
        "wifi": "🌐 Gestor Wi-Fi", "bt": "📡 Gestor Bluetooth", "guia": "🔍 Guia de Peças", "ai": "🤖 GeoLeon AI (Voz)",
        "pausado": "Estado: PAUSADO", "ativo": "Estado: ATIVO", "monitor_titulo": "CENTRAL DO VEÍCULO - BEM-VINDO, {usuario}",
        "odometro": "Odómetro: {odo:,.1f} km | Combustível: {comb:.1f} L", "manut_titulo": "SELECCIONE COMPONENTES SUBSTITUÍDOS RECENTEMENTE",
        "iniciar_sis": "▶ INICIAR SISTEMA DE MONITORIZAÇÃO", "parar_sis": "⏹ PARAR SISTEMA DE MONITORIZAÇÃO",
        "escolha_sis": "Escolha a categoria do sistema para ver e marcar as peças:", "wifi_titulo": "GESTOR DE REDE WI-FI & INTERNET",
        "escanear_wifi": "📶 Pesquisar Redes Wi-Fi Disponíveis", "digite_wifi": "Ou introduza o nome da rede (SSID) manualmente:",
        "senha_wifi": "Introduza a palavra-passe do Wi-Fi...", "conectar_wifi": "🌐 Ligar à Rede & Internet",
        "bt_titulo": "GESTOR DE LIGAÇÃO BLUETOOTH", "escanear_bt": "📡 Pesquisar Dispositivos Bluetooth Próximos",
        "guia_titulo": "DICIONÁRIO TÉCNICO DE COMPONENTES", "ai_titulo": "COMPUTADOR DE BORDO INTELLIGENTE - GEOLEON AI ({usuario})",
        "digite_ai": "Introduza o seu pedido ou comando para a IA:", "consultar_txt": "🔍 Consultar Texto",
        "falar_carro": "🎤 Falar com o Carro (Voz)", "resposta_ai": "Resposta do Cérebro IA:",
        "sistema_ativo": "Sistema ativo e a operar normalmente.", "relatorio_ia": "Relatório GeoLeon AI",
        "tab_monitor": "Monitor", "tab_manutencao": "Manutenção", "tab_wifi": "Wi-Fi", "tab_bt": "Bluetooth",
        "tab_guia": "Guia", "tab_ai": "IA", "lbl_cores_titulo": "🎨 ESCOLHER COR DA INTERFACE",
        "lbl_dalton_titulo": "👁 ACESSIB / DALTONISMO", "btn_ativar_dalton": "Ativar Modo Alto Contraste",
        "btn_desativar_dalton": "Desativar Modo Daltônico"
    },
    "Inglês": {
        "titulo": "GeoLeon OS - {usuario}'s Dashboard (2026)",
        "condutor": "Driver:", "painel": "⚡ Dashboard & Wear", "manutencao": "🔧 Parts Maintenance",
        "wifi": "🌐 Wi-Fi Manager", "bt": "📡 Bluetooth Manager", "guia": "🔍 Parts Guide", "ai": "🤖 GeoLeon AI (Voice)",
        "pausado": "Status: PAUSED", "ativo": "Status: ACTIVE", "monitor_titulo": "VEHICLE DASHBOARD - WELCOME, {usuario}",
        "odometro": "Odometer: {odo:,.1f} km | Fuel: {comb:.1f} L", "manut_titulo": "SELECT RECENTLY REPLACED COMPONENTS",
        "iniciar_sis": "▶ START MONITORING SYSTEM", "parar_sis": "⏹ STOP MONITORING SYSTEM",
        "escolha_sis": "Choose system category to view and check parts:", "wifi_titulo": "WI-FI & INTERNET MANAGER",
        "escanear_wifi": "📶 Scan Available Wi-Fi Networks", "digite_wifi": "Or type network name (SSID) manually:",
        "senha_wifi": "Enter Wi-Fi password...", "conectar_wifi": "🌐 Connect to Network & Internet",
        "bt_titulo": "BLUETOOTH CONNECTION MANAGER", "escanear_bt": "📡 Scan Nearby Bluetooth Devices",
        "guia_titulo": "TECHNICAL PARTS DICTIONARY", "ai_titulo": "SMART ONBOARD COMPUTER - GEOLEON AI ({usuario})",
        "digite_ai": "Type your request or command for AI:", "consultar_txt": "🔍 Text Query",
        "falar_carro": "🎤 Talk to Car (Voice)", "resposta_ai": "AI Brain Response:",
        "sistema_ativo": "System active and operating normally.", "relatorio_ia": "GeoLeon AI Report",
        "tab_monitor": "Monitor", "tab_manutencao": "Maintenance", "tab_wifi": "Wi-Fi", "tab_bt": "Bluetooth",
        "tab_guia": "Guide", "tab_ai": "AI", "lbl_cores_titulo": "🎨 CHOOSE INTERFACE COLOR",
        "lbl_dalton_titulo": "👁 ACCESSIBILITY / COLORBLIND", "btn_ativar_dalton": "Enable High Contrast",
        "btn_desativar_dalton": "Disable Colorblind Mode"
    },
    "Espanhol": {
        "titulo": "GeoLeon OS - Panel de {usuario} (2026)",
        "condutor": "Conductor:", "painel": "⚡ Panel y Desgaste", "manutencao": "🔧 Mantenimiento de Piezas",
        "wifi": "🌐 Gestor Wi-Fi", "bt": "📡 Gestor Bluetooth", "guia": "🔍 Guía de Piezas", "ai": "🤖 GeoLeon AI (Voz)",
        "pausado": "Estado: PAUSADO", "ativo": "Estado: ACTIVO", "monitor_titulo": "PANEL DEL VEHÍCULO - BIENVENIDO, {usuario}",
        "odometro": "Odómetro: {odo:,.1f} km | Combustible: {comb:.1f} L", "manut_titulo": "SELECCIONE COMPONENTES REEMPLAZADOS RECIENTEMENTE",
        "iniciar_sis": "▶ INICIAR SISTEMA DE MONITOREO", "parar_sis": "⏹ DETENER SISTEMA DE MONITOREO",
        "escolha_sis": "Elija la categoría del sistema para ver y marcar piezas:", "wifi_titulo": "GESTIÓN DE RED WI-FI & INTERNET",
        "escanear_wifi": "📶 Escanear Redes Wi-Fi Disponibles", "digite_wifi": "O escriba el nombre de la red (SSID) manualmente:",
        "senha_wifi": "Ingrese la contraseña de Wi-Fi...", "conectar_wifi": "🌐 Conectar a Red e Internet",
        "bt_titulo": "GESTOR DE CONEXIÓN BLUETOOTH", "escanear_bt": "📡 Escanear Dispositivos Bluetooth Cercanos",
        "guia_titulo": "DICCIONARIO TÉCNICO DE COMPONENTES", "ai_titulo": "COMPUTADORA A BORDO INTELIGENTE - GEOLEON AI ({usuario})",
        "digite_ai": "Escriba su solicitud o comando para la IA:", "consultar_txt": "🔍 Consulta de Texto",
        "falar_carro": "🎤 Hablar con el Auto", "resposta_ai": "Respuesta del Cerebro IA:",
        "sistema_ativo": "Sistema activo y operando normalmente.", "relatorio_ia": "Informe de GeoLeon AI",
        "tab_monitor": "Monitor", "tab_manutencao": "Mantenimiento", "tab_wifi": "Wi-Fi", "tab_bt": "Bluetooth",
        "tab_guia": "Guía", "tab_ai": "IA", "lbl_cores_titulo": "🎨 ELEGIR COLOR DE INTERFAZ",
        "lbl_dalton_titulo": "👁 ACCESIBILIDAD / DALTONISMO",
        "btn_ativar_dalton": "Activar Modo Alto Contraste", "btn_desativar_dalton": "Desactivar Modo Daltônico"
    },
    "Italiano": {
        "titulo": "GeoLeon OS", "condutor": "Pilota:", "painel": "⚡ Cruscotto", "manutencao": "🔧 Manutenzione",
        "wifi": "🌐 Wi-Fi", "bt": "📡 Bluetooth", "guia": "🔍 Guida", "ai": "🤖 IA", "pausado": "IN PAUSA", "ativo": "ATTIVO",
        "monitor_titulo": "CRUSCOTTO", "odometro": "Odometro: {odo:,.1f} km", "manut_titulo": "PARTI", "iniciar_sis": "AVVIA", "parar_sis": "FERMA",
        "escolha_sis": "Categoria:", "wifi_titulo": "WI-FI", "escanear_wifi": "Scansiona", "digite_wifi": "SSID:",
        "senha_wifi": "Password...", "conectar_wifi": "Connetti", "bt_titulo": "BLUETOOTH", "escanear_bt": "Scansiona",
        "guia_titulo": "GUIDA", "ai_titulo": "IA", "digite_ai": "Comando:", "consultar_txt": "Query",
        "falar_carro": "🎤 Parla con l'Auto", "resposta_ai": "Risposta:", "sistema_ativo": "Attivo.", "relatorio_ia": "Rapporto",
        "tab_monitor": "Monitor", "tab_manutencao": "Manutenzione", "tab_wifi": "Wi-Fi", "tab_bt": "Bluetooth", "tab_guia": "Guida", "tab_ai": "IA",
        "lbl_cores_titulo": "🎨 COLORE", "lbl_dalton_titulo": "👁 DALTONISMO", "btn_ativar_dalton": "Attiva", "btn_desativar_dalton": "Disattiva"
    },
    "Russo": {
        "titulo": "GeoLeon OS", "condutor": "Водитель:", "painel": "⚡ Панель", "manutencao": "🔧 Обслуживание",
        "wifi": "🌐 Wi-Fi", "bt": "📡 Bluetooth", "guia": "🔍 Гид", "ai": "🤖 ИИ", "pausado": "ПАУЗА", "ativo": "АКТИВЕН",
        "monitor_titulo": "ПАНЕЛЬ", "odometro": "Одометр: {odo:,.1f} км", "manut_titulo": "ДЕТАЛИ", "iniciar_sis": "СТАРТ", "parar_sis": "СТОП",
        "escolha_sis": "Категория:", "wifi_titulo": "WI-FI", "escanear_wifi": "Сканировать", "digite_wifi": "SSID:",
        "senha_wifi": "Пароль...", "conectar_wifi": "Подключить", "bt_titulo": "BLUETOOTH", "escanear_bt": "Поиск",
        "guia_titulo": "Гид", "ai_titulo": "ИИ", "digite_ai": "Команда:", "consultar_txt": "Запрос",
        "falar_carro": "🎤 Говорить с машиной", "resposta_ai": "Ответ:", "sistema_ativo": "Активно.", "relatorio_ia": "Отчет",
        "tab_monitor": "Монитор", "tab_manutencao": "Ремонт", "tab_wifi": "Wi-Fi", "tab_bt": "BT", "tab_guia": "Гид", "tab_ai": "ИИ",
        "lbl_cores_titulo": "🎨 ЦВЕТ", "lbl_dalton_titulo": "👁 ДАЛЬТОНИЗМ",
        "btn_ativar_dalton": "Включить", "btn_desativar_dalton": "Выключить"
    },
    "Alemão": {
        "titulo": "GeoLeon OS", "condutor": "Fahrer:", "painel": "⚡ Dashboard", "manutencao": "🔧 Wartung",
        "wifi": "🌐 WLAN", "bt": "📡 Bluetooth", "guia": "🔍 Handbuch", "ai": "🤖 KI", "pausado": "PAUSE", "ativo": "AKTIV",
        "monitor_titulo": "DASHBOARD", "odometro": "Kilometerstand: {odo:,.1f} km", "manut_titulo": "TEILE", "iniciar_sis": "START", "parar_sis": "STOPP",
        "escolha_sis": "Kategorie:", "wifi_titulo": "WLAN", "escanear_wifi": "Scannen", "digite_wifi": "SSID:", "senha_wifi": "Passwort...",
        "conectar_wifi": "Verbinden", "bt_titulo": "BLUETOOTH", "escanear_bt": "Scannen", "guia_titulo": "LEXIKON", "ai_titulo": "KI",
        "digite_ai": "Befehl:", "consultar_txt": "Abfrage", "falar_carro": "🎤 Mit Auto sprechen", "resposta_ai": "Antwort:",
        "sistema_ativo": "Aktiv.", "relatorio_ia": "Bericht", "tab_monitor": "Monitor", "tab_manutencao": "Wartung", "tab_wifi": "WLAN",
        "tab_bt": "BT", "tab_guia": "Handbuch", "tab_ai": "KI", "lbl_cores_titulo": "🎨 FARBE", "lbl_dalton_titulo": "👁 FARBSCHWÄCHE",
        "btn_ativar_dalton": "Aktivieren", "btn_desativar_dalton": "Deaktivieren"
    },
    "Francês": {
        "titulo": "GeoLeon OS", "condutor": "Conducteur:", "painel": "⚡ Tableau", "manutencao": "🔧 Entretien",
        "wifi": "🌐 Wi-Fi", "bt": "📡 Bluetooth", "guia": "🔍 Guide", "ai": "🤖 IA", "pausado": "PAUSE", "ativo": "ACTIF",
        "monitor_titulo": "TABLEAU", "odometro": "Odomètre: {odo:,.1f} km", "manut_titulo": "PIÈCES", "iniciar_sis": "DÉMARRER", "parar_sis": "ARRÊTER",
        "escolha_sis": "Catégorie:", "wifi_titulo": "WI-FI", "escanear_wifi": "Analyser", "digite_wifi": "SSID:", "senha_wifi": "Mot de passe...",
        "conectar_wifi": "Connecter", "bt_titulo": "BLUETOOTH", "escanear_bt": "Analyser", "guia_titulo": "GUIDE", "ai_titulo": "IA",
        "digite_ai": "Commande:", "consultar_txt": "Requête", "falar_carro": "🎤 Parler à la Voiture", "resposta_ai": "Réponse:",
        "sistema_ativo": "Actif.", "relatorio_ia": "Rapport", "tab_monitor": "Moniteur", "tab_manutencao": "Entretien", "tab_wifi": "Wi-Fi",
        "tab_bt": "BT", "tab_guia": "Guide", "tab_ai": "IA", "lbl_cores_titulo": "🎨 COULEUR", "lbl_dalton_titulo": "👁 DALTONISME",
        "btn_ativar_dalton": "Activer", "btn_desativar_dalton": "Désactiver"
    },
    "Japonês": {
        "titulo": "GeoLeon OS", "condutor": "ドライバー:", "painel": "⚡ ダッシュボード", "manutencao": "🔧 メンテナンス",
        "wifi": "🌐 Wi-Fi", "bt": "📡 Bluetooth", "guia": "🔍 ガイド", "ai": "🤖 AI", "pausado": "一時停止", "ativo": "アクティブ",
        "monitor_titulo": "ダッシュボード", "odometro": "オドメーター: {odo:,.1f} km", "manut_titulo": "パーツ", "iniciar_sis": "開始", "parar_sis": "停止",
        "escolha_sis": "カテゴリ:", "wifi_titulo": "Wi-Fi", "escanear_wifi": "スキャン", "digite_wifi": "SSID:", "senha_wifi": "パスワード...",
        "conectar_wifi": "接続", "bt_titulo": "Bluetooth", "escanear_bt": "スキャン", "guia_titulo": "辞書", "ai_titulo": "AI",
        "digite_ai": "コマンド:", "consultar_txt": "クエリ", "falar_carro": "🎤 車に話しかける", "resposta_ai": "応答:",
        "sistema_ativo": "正常稼働中。", "relatorio_ia": "レポート", "tab_monitor": "モニター", "tab_manutencao": "メンテ",
        "tab_wifi": "Wi-Fi", "tab_bt": "BT", "tab_guia": "ガイド", "tab_ai": "AI", "lbl_cores_titulo": "🎨 カラー",
        "lbl_dalton_titulo": "👁 色覚多様性", "btn_ativar_dalton": "有効化", "btn_desativar_dalton": "無効化"
    },
    "Chinês": {
        "titulo": "GeoLeon OS", "condutor": "驾驶员:", "painel": "⚡ 仪表盘", "manutencao": "🔧 维护",
        "wifi": "🌐 Wi-Fi", "bt": "📡 蓝牙", "guia": "🔍 指南", "ai": "🤖 AI", "pausado": "已暂停", "ativo": "运行中",
        "monitor_titulo": "仪表盘", "odometro": "里程表: {odo:,.1f} km", "manut_titulo": "零件", "iniciar_sis": "启动", "parar_sis": "停止",
        "escolha_sis": "类别:", "wifi_titulo": "Wi-Fi", "escanear_wifi": "扫描", "digite_wifi": "SSID:", "senha_wifi": "密码...",
        "conectar_wifi": "连接", "bt_titulo": "蓝牙", "escanear_bt": "扫描", "guia_titulo": "词典", "ai_titulo": "AI",
        "digite_ai": "命令:", "consultar_txt": "查询", "falar_carro": "🎤 与汽车对话", "resposta_ai": "响应:",
        "sistema_ativo": "运行正常。", "relatorio_ia": "报告", "tab_monitor": "监视器", "tab_manutencao": "维护",
        "tab_wifi": "Wi-Fi", "tab_bt": "蓝牙", "tab_guia": "指南", "tab_ai": "AI", "lbl_cores_titulo": "🎨 颜色",
        "lbl_dalton_titulo": "👁 色盲模式", "btn_ativar_dalton": "启用", "btn_desativar_dalton": "禁用"
    }
}

TRADUCAO_CATEGORIAS = {
    "Português": {
        "1. Motor": "1. Motor", "2. Alimentação e Injeção": "2. Alimentação e Injeção", 
        "3. Transmissão": "3. Transmissão", "4. Suspensão": "4. Suspensão", 
        "5. Direção": "5. Direção", "6. Freios": "6. Freios", 
        "7. Sistema Elétrico / Eletrônico": "7. Sistema Elétrico / Eletrônico", 
        "8. Arrefecimento": "8. Arrefecimento", "9. Escape e Emissões": "9. Escape e Emissões", 
        "10. Rodagem": "10. Rodagem", "11. Distribuição e Acessórios": "11. Distribuição e Acessórios", 
        "12. Carroceria e Acabamento": "12. Carroceria e Acabamento"
    },
    "Inglês": {
        "1. Motor": "1. Engine", "2. Alimentação e Injeção": "2. Fuel & Injection", 
        "3. Transmissão": "3. Transmission", "4. Suspensão": "4. Suspension", 
        "5. Direção": "5. Steering", "6. Freios": "6. Brakes", 
        "7. Sistema Elétrico / Eletrônico": "7. Electrical / Electronic", 
        "8. Arrefecimento": "8. Cooling", "9. Escape e Emissões": "9. Exhaust & Emissions", 
        "10. Rodagem": "10. Wheels & Tires", "11. Distribuição e Acessórios": "11. Timing & Accessories", 
        "12. Carroceria e Acabamento": "12. Body & Trim"
    },
    "Espanhol": {
        "1. Motor": "1. Motor", "2. Alimentação e Injeção": "2. Alimentación e Inyección", 
        "3. Transmissão": "3. Transmisión", "4. Suspensão": "4. Suspensión", 
        "5. Direção": "5. Dirección", "6. Freios": "6. Frenos", 
        "7. Sistema Elétrico / Eletrônico": "7. Sistema Eléctrico", 
        "8. Arrefecimento": "8. Refrigeración", "9. Escape e Emissões": "9. Escape y Emisiones", 
        "10. Rodagem": "10. Rodadura", "11. Distribuição e Acessórios": "11. Distribución", 
        "12. Carroceria e Acabamento": "12. Carrocería"
    }
}

# ==========================================
# TODAS AS PEÇAS ORIGINAIS RESTAURADAS (12 SISTEMAS COMPLETOS)
# ==========================================
DADOS_PECAS = {
    "1. Motor": {
        "Bloco do Motor": {"vida_max": 250000, "desc": "Estrutura principal que abriga os cilindros e o virabrequim."},
        "Cabeçote": {"vida_max": 200000, "desc": "Tampa superior do motor que aloja as válvulas e velas de ignição."},
        "Pistão": {"vida_max": 150000, "desc": "Peça móvel dentro do cilindro que recebe a força da expansão dos gases."},
        "Biela": {"vida_max": 150000, "desc": "Haste que liga o pistão ao virabrequim."},
        "Virabrequim": {"vida_max": 300000, "desc": "Eixo principal que transforma o movimento linear dos pistões em rotação."},
        "Válvulas": {"vida_max": 100000, "desc": "Controlam a entrada de ar/combustível e a saída dos gases de escape."},
        "Comando de Válvulas": {"vida_max": 150000, "desc": "Eixo com ressaltos que aciona a abertura e fechamento das válvulas."},
        "Tampa de Válvulas": {"vida_max": 120000, "desc": "Protege o mecanismo superior e veda o óleo do motor."},
        "Junta do Cabeçote": {"vida_max": 100000, "desc": "Elemento de vedação entre o bloco e o cabeçote."},
        "Correia Dentada": {"vida_max": 50000, "desc": "Sincroniza o virabrequim e o comando de válvulas."},
        "Tensor da Correia": {"vida_max": 50000, "desc": "Mantém a tensão correta da correia dentada."},
        "Bomba de Óleo": {"vida_max": 150000, "desc": "Garante a circulação sob pressão do óleo lubrificante."},
        "Cárter": {"vida_max": 200000, "desc": "Reservatório inferior que armazena o óleo do motor."},
        "Filtro de Óleo": {"vida_max": 10000, "desc": "Retém impurezas e detritos do óleo lubrificante."},
        "Bomba d'Água": {"vida_max": 80000, "desc": "Faz circular o líquido de arrefecimento pelo motor e radiador."},
        "Radiador de Óleo": {"vida_max": 100000, "desc": "Resfria o óleo lubrificante do motor."},
        "Polia do Virabrequim": {"vida_max": 100000, "desc": "Transmite o movimento do virabrequim para as correias auxiliares."},
        "Volante do Motor": {"vida_max": 200000, "desc": "Roda pesada que estabiliza a rotação e acopla a embreagem."},
        "Turbocompressor": {"vida_max": 150000, "desc": "Utiliza os gases de escape para comprimir o ar admitido no motor."},
        "Intercooler": {"vida_max": 150000, "desc": "Resfria o ar comprimido pelo turbo antes de entrar no motor."},
        "Suporte do Motor": {"vida_max": 80000, "desc": "Absorve vibrações e fixa o motor ao chassi do veículo."}
    },
    "2. Alimentação e Injeção": {
        "Bomba de Combustível": {"vida_max": 80000, "desc": "Envia o combustível do tanque para o sistema de injeção."},
        "Bicos Injetores": {"vida_max": 70000, "desc": "Pulverizam o combustível na câmara de combustão."},
        "Corpo de Borboleta": {"vida_max": 100000, "desc": "Controla a quantidade de ar que entra no motor através da aceleração."},
        "Filtro de Combustível": {"vida_max": 15000, "desc": "Retém impurezas do combustível antes de chegar aos bicos."},
        "Filtro de Ar": {"vida_max": 15000, "desc": "Impede que poeira e detritos entrem no sistema de admissão."},
        "Regulador de Pressão": {"vida_max": 80000, "desc": "Mantém a pressão estável na linha de combustível."},
        "Sensor de Oxigênio": {"vida_max": 80000, "desc": "Mede os gases de escape para otimizar a mistura ar-combustível."},
        "Sensor MAF (Fluxo de Ar)": {"vida_max": 100000, "desc": "Mede a massa de ar admitida pelo motor."},
        "Sensor MAP (Pressão)": {"vida_max": 100000, "desc": "Mede a pressão absoluta no coletor de admissão."},
        "Velas de Ignição": {"vida_max": 40000, "desc": "Geram a faísca elétrica para inflamar a mistura ar-combustível."}
    },
    "3. Transmissão": {
        "Embreagem": {"vida_max": 60000, "desc": "Acopla e desacopla o motor da caixa de câmbio."},
        "Platô": {"vida_max": 60000, "desc": "Pressiona o disco de embreagem contra o volante do motor."},
        "Disco de Embreagem": {"vida_max": 60000, "desc": "Transmite o torque do motor para o câmbio através de atrito."},
        "Rolamento de Embreagem": {"vida_max": 60000, "desc": "Aciona o sistema de liberação da embreagem."},
        "Câmbio": {"vida_max": 200000, "desc": "Caixa de marchas que multiplica o torque e a velocidade."},
        "Conversor de Torque": {"vida_max": 200000, "desc": "Substitui a embreagem em transmissões automáticas."},
        "Diferencial": {"vida_max": 200000, "desc": "Distribui a força do motor para as rodas permitindo curvas."},
        "Semieixo": {"vida_max": 150000, "desc": "Transmite o movimento do diferencial para as rodas."},
        "Junta Homocinética": {"vida_max": 100000, "desc": "Permite a transmissão de força mesmo com esterçamento das rodas."},
        "Coifa da Junta": {"vida_max": 40000, "desc": "Protege a junta homocinética contra sujeira e vazamento de graxa."}
    },
    "4. Suspensão": {
        "Amortecedor": {"vida_max": 40000, "desc": "Controla o movimento das molas e absorve os impactos da pista."},
        "Mola Helicoidal": {"vida_max": 100000, "desc": "Sustenta o peso do veículo e absorve irregularidades."},
        "Bandeja Inferior": {"vida_max": 80000, "desc": "Braço de controle que conecta a roda ao chassi."},
        "Pivô": {"vida_max": 60000, "desc": "Articulação que permite o movimento e esterçamento da roda."},
        "Bucha": {"vida_max": 50000, "desc": "Elemento de borracha que amortece articulações e vibrações."},
        "Bieleta": {"vida_max": 40000, "desc": "Conecta a barra estabilizadora à suspensão."},
        "Barra Estabilizadora": {"vida_max": 150000, "desc": "Reduz a inclinação lateral do veículo nas curvas."},
        "Terminal da Barra": {"vida_max": 60000, "desc": "Articulação da barra estabilizadora ou direção."},
        "Coxim do Amortecedor": {"vida_max": 60000, "desc": "Isola vibrações do amortecedor em relação à carroceria."},
        "Batente": {"vida_max": 50000, "desc": "Limita o curso máximo do amortecedor em buracos profundos."}
    },
    "5. Direção": {
        "Caixa de Direção": {"vida_max": 150000, "desc": "Mecanismo que converte o giro do volante em movimento lateral."},
        "Terminal de Direção": {"vida_max": 60000, "desc": "Conecta a barra de direção às mangas de eixo."},
        "Barra Axial": {"vida_max": 80000, "desc": "Transmite o movimento da caixa de direção para as rodas."},
        "Coluna de Direção": {"vida_max": 200000, "desc": "Eixo que liga o volante à caixa de direção."},
        "Bomba de Direção Hidráulica": {"vida_max": 120000, "desc": "Gera pressão de óleo para auxiliar na leveza da direção."},
        "Reservatório da Direção": {"vida_max": 100000, "desc": "Armazena o fluido do sistema hidráulico de direção."},
        "Mangueira de Pressão": {"vida_max": 70000, "desc": "Conduz o fluido de direção sob alta pressão."},
        "Fluido de Direção": {"vida_max": 40000, "desc": "Líquido hidráulico que lubrifica e aciona a direção hidráulica."}
    },
    "6. Freios": {
        "Disco de Freio": {"vida_max": 60000, "desc": "Superfície metálica onde as pastilhas geram atrito de frenagem."},
        "Pastilha de Freio": {"vida_max": 30000, "desc": "Material de atrito pressionado contra o disco para desacelerar."},
        "Pinça de Freio": {"vida_max": 120000, "desc": "Aloja o pistão hidráulico que aperta as pastilhas no disco."},
        "Tambor de Freio": {"vida_max": 80000, "desc": "Invólucro cilíndrico de frenagem traseira por atrito interno."},
        "Lona de Freio": {"vida_max": 40000, "desc": "Material de atrito usado nos freios a tambor."},
        "Cilindro Mestre": {"vida_max": 100000, "desc": "Gera a pressão hidráulica principal acionada pelo pedal de freio."},
        "Reservatório de Fluido": {"vida_max": 100000, "desc": "Armazena o fluido de freio do sistema hidráulico."},
        "Flexível de Freio": {"vida_max": 50000, "desc": "Mangueira flexível que conduz o fluido sob alta pressão para as pinças."},
        "Módulo ABS": {"vida_max": 150000, "desc": "Controla eletronicamente a pressão de frenagem evitando travamento."},
        "Sensor ABS": {"vida_max": 100000, "desc": "Mede a rotação individual de cada roda para o sistema ABS."}
    },
    "7. Sistema Elétrico / Eletrônico": {
        "Bateria": {"vida_max": 40000, "desc": "Armazena energia elétrica para partida e acessórios."},
        "Alternador": {"vida_max": 100000, "desc": "Gera energia elétrica e recarrega a bateria com o motor ligado."},
        "Motor de Partida": {"vida_max": 100000, "desc": "Motor elétrico que dá o primeiro giro no motor a combustão."},
        "Caixa de Fusíveis": {"vida_max": 150000, "desc": "Protege os circuitos elétricos contra sobrecarga e curtos."},
        "Relé": {"vida_max": 100000, "desc": "Interruptor eletromagnético para acionamento de cargas pesadas."},
        "Bobina de Ignição": {"vida_max": 80000, "desc": "Transforma a baixa tensão da bateria em alta tensão para as velas."},
        "Sensor de Posição": {"vida_max": 100000, "desc": "Informa a posição do virabrequim ou comando para a central."},
        "Módulo de Injeção (ECU)": {"vida_max": 250000, "desc": "Computador central que gerencia o funcionamento do motor."},
        "Chicote Elétrico": {"vida_max": 200000, "desc": "Conjunto de fios e cabos que distribui energia e sinais pelo carro."}
    },
    "8. Arrefecimento": {
        "Radiador": {"vida_max": 100000, "desc": "Troca o calor do líquido de arrefecimento com o ar externo."},
        "Válvula Termostática": {"vida_max": 60000, "desc": "Controla a passagem do fluido conforme a temperatura do motor."},
        "Reservatório de Expansão": {"vida_max": 80000, "desc": "Compensa a variação de volume do líquido de arrefecimento."},
        "Eletroventilador": {"vida_max": 80000, "desc": "Ventoinha que força o fluxo de ar pelo radiador."},
        "Mangueira Inferior": {"vida_max": 40000, "desc": "Conduz o fluido resfriado do radiador para a bomba d'água."},
        "Mangueira Superior": {"vida_max": 40000, "desc": "Conduz o fluido quente do motor para o radiador."},
        "Tubulação": {"vida_max": 70000, "desc": "Conexões rígidas auxiliares do sistema de arrefecimento."},
        "Líquido de Arrefecimento": {"vida_max": 20000, "desc": "Mistura de água desmineralizada e aditivo protetivo anticongelante/ferrugem."},
        "Tampa do Radiador": {"vida_max": 40000, "desc": "Mantém a pressão correta de trabalho do sistema de arrefecimento."}
    },
    "9. Escape e Emissões": {
        "Coletor de Escape": {"vida_max": 150000, "desc": "Coleta os gases queimados de todos os cilindros do motor."},
        "Catalisador": {"vida_max": 100000, "desc": "Converte gases tóxicos do escape em substâncias menos nocivas."},
        "Silencioso": {"vida_max": 60000, "desc": "Reduz o ruído gerado pela exaustão dos gases do motor."},
        "Tubo de Escape": {"vida_max": 80000, "desc": "Conduz os gases da parte dianteira para a traseira do veículo."},
        "Ponteira": {"vida_max": 100000, "desc": "Acabamento estético final da saída do escapamento."},
        "Sonda Lambda": {"vida_max": 80000, "desc": "Monitora a quantidade de oxigênio nos gases de escape."},
        "Válvula EGR": {"vida_max": 100000, "desc": "Recircula parte dos gases de escape para reduzir emissões de NOx."},
        "Filtro de Partículas (DPF)": {"vida_max": 150000, "desc": "Retém fuligem e partículas sólidas em motores diesel/modernos."},
        "Suporte do Escape": {"vida_max": 50000, "desc": "Coxins de borracha que fixam o escapamento à carroceria."},
        "Escudo Térmico": {"vida_max": 200000, "desc": "Protege a carroceria contra o calor excessivo do escapamento."}
    },
    "10. Rodagem": {
        "Pneu": {"vida_max": 45000, "desc": "Banda de borracha em contato direto com o solo."},
        "Roda": {"vida_max": 200000, "desc": "Aro estrutural metálico que suporta o pneu."},
        "Cubo de Roda": {"vida_max": 150000, "desc": "Eixo central onde a roda é parafusada e gira livremente."},
        "Rolamento de Roda": {"vida_max": 80000, "desc": "Permite o giro suave e sem atrito excessivo das rodas."},
        "Porca da Roda": {"vida_max": 100000, "desc": "Fixa firmemente a roda no prisioneiro ou cubo."},
        "Parafuso da Roda": {"vida_max": 100000, "desc": "Elemento de fixação estrutural da roda."},
        "Válvula do Pneu": {"vida_max": 45000, "desc": "Bico inflador que retém a pressão interna do pneu."},
        "Balanceador de Roda": {"vida_max": 45000, "desc": "Equilíbrio de massa do conjunto pneu/roda para evitar vibrações."},
        "Peso de Balanceamento": {"vida_max": 45000, "desc": "Chumbo aplicado na roda para corrigir desbalanceamentos."}
    },
    "11. Distribuição e Acessórios": {
        "Corrente de Distribuição": {"vida_max": 150000, "desc": "Corrente metálica de sincronismo entre virabrequim e comandos."},
        "Polia Guia": {"vida_max": 60000, "desc": "Guia o trajeto das correias auxiliares do motor."},
        "Engrenagem do Comando": {"vida_max": 150000, "desc": "Roda dentada acoplada ao eixo de comando de válvulas."},
        "Correia de Acessórios": {"vida_max": 40000, "desc": "Aciona alternador, bomba hidráulica e ar-condicionado."},
        "Polia do Alternador": {"vida_max": 80000, "desc": "Recebe o giro para acionar o alternador."},
        "Polia do Ar Condicionado": {"vida_max": 90000, "desc": "Acopla o compressor do ar-condicionado por correia."},
        "Tensor da Correia de Acessórios": {"vida_max": 60000, "desc": "Mantém a correia de acessórios tensionada corretamente."}
    },
    "12. Carroceria e Acabamento": {
        "Para-choque Dianteiro": {"vida_max": 200000, "desc": "Absorve pequenos impactos frontais e melhora a aerodinâmica."},
        "Para-choque Traseiro": {"vida_max": 200000, "desc": "Absorve pequenos impactos traseiros."},
        "Capô": {"vida_max": 200000, "desc": "Tampa metálica de proteção do compartimento do motor."},
        "Para-lama": {"vida_max": 200000, "desc": "Painel de proteção ao redor das caixas de rodas."},
        "Porta": {"vida_max": 200000, "desc": "Estrutura de acesso lateral de passageiros."},
        "Maçaneta de Porta": {"vida_max": 100000, "desc": "Puxador mecânico para abertura das portas."},
        "Retrovisor": {"vida_max": 150000, "desc": "Espelho externo para visão lateral e traseira."},
        "Grade Dianteira": {"vida_max": 200000, "desc": "Permite entrada de ar para o radiador e estética frontal."},
        "Farol": {"vida_max": 100000, "desc": "Sistema de iluminação frontal principal."},
        "Lanterna": {"vida_max": 100000, "desc": "Sinalização e iluminação traseira."},
        "Parabrisa": {"vida_max": 150000, "desc": "Vidro de proteção frontal laminado."},
        "Vidro Lateral": {"vida_max": 200000, "desc": "Vidros móveis das portas laterais."},
        "Limpador de Parabrisa": {"vida_max": 25000, "desc": "Palhetas de borracha para remoção de chuva do vidro."},
        "Painel de Instrumentos": {"vida_max": 200000, "desc": "Central de mostradores e telemetria do motorista."},
        "Volante": {"vida_max": 200000, "desc": "Comando circular de direção nas mãos do condutor."},
        "Banco": {"vida_max": 150000, "desc": "Assentos ergonômicos de acomodação."},
        "Cinto de Segurança": {"vida_max": 150000, "desc": "Dispositivo essencial de retenção em caso de colisões."},
        "Tapete": {"vida_max": 50000, "desc": "Proteção e acabamento do assoalho interno."},
        "Revestimento Interno": {"vida_max": 150000, "desc": "Acabamento estético de teto, portas e colunas."}
    }
}

estado_app = {
    "usuario_nome": "Leone Cardoso Lima",
    "idioma_atual": "Português",
    "rodando": False,
    "odometro": 10000.0,
    "combustivel_litros": 42.5,
    "km_pecas": {},
    "bt_conectado": None,
    "wifi_conectado": None,
    "internet_status": "Desconectado",
    "cor_atual": "Azul",
    "daltonico_ativo": False
}

for sistema, pecas in DADOS_PECAS.items():
    for peca in pecas.keys():
        estado_app["km_pecas"][peca] = 2500.0

class GeoLeonOSApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("GeoLeon OS - Central de Leone Cardoso Lima (2026)")
        self.geometry("1380x850")
        self.resizable(False, False)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ----------------- SIDEBAR LATERAL ESQUERDA -----------------
        self.sidebar_frame = ctk.CTkFrame(self, width=220, corner_radius=0, fg_color="#0b1329")
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")

        self.logo_label = ctk.CTkLabel(
            self.sidebar_frame, text="GEOLEON OS", 
            font=ctk.CTkFont(family="Courier", size=20, weight="bold"), text_color="#38bdf8"
        )
        self.logo_label.pack(padx=20, pady=20)

        self.lbl_cliente = ctk.CTkLabel(
            self.sidebar_frame, text=f"{self.t('condutor')}\n{estado_app['usuario_nome']}", 
            font=("Segoe UI", 11, "bold"), text_color="#facc15", justify="center"
        )
        self.lbl_cliente.pack(padx=10, pady=(0, 15))

        self.btn_m_monitor = ctk.CTkButton(self.sidebar_frame, text=self.t('painel'), fg_color="transparent", text_color="#f8fafc", anchor="w", command=lambda: self.mudar_aba("Monitor"))
        self.btn_m_monitor.pack(padx=15, pady=5, fill="x")

        self.btn_m_manut = ctk.CTkButton(self.sidebar_frame, text=self.t('manutencao'), fg_color="transparent", text_color="#f8fafc", anchor="w", command=lambda: self.mudar_aba("Manutencao"))
        self.btn_m_manut.pack(padx=15, pady=5, fill="x")

        self.btn_m_wifi = ctk.CTkButton(self.sidebar_frame, text=self.t('wifi'), fg_color="transparent", text_color="#f8fafc", anchor="w", command=lambda: self.mudar_aba("Wifi"))
        self.btn_m_wifi.pack(padx=15, pady=5, fill="x")

        self.btn_m_bt = ctk.CTkButton(self.sidebar_frame, text=self.t('bt'), fg_color="transparent", text_color="#f8fafc", anchor="w", command=lambda: self.mudar_aba("Bluetooth"))
        self.btn_m_bt.pack(padx=15, pady=5, fill="x")

        self.btn_m_guia = ctk.CTkButton(self.sidebar_frame, text=self.t('guia'), fg_color="transparent", text_color="#f8fafc", anchor="w", command=lambda: self.mudar_aba("Guia"))
        self.btn_m_guia.pack(padx=15, pady=5, fill="x")

        self.btn_m_ai = ctk.CTkButton(self.sidebar_frame, text=self.t('ai'), fg_color="transparent", text_color="#f8fafc", anchor="w", command=lambda: self.mudar_aba("AI"))
        self.btn_m_ai.pack(padx=15, pady=5, fill="x")

        self.lbl_status_sidebar = ctk.CTkLabel(self.sidebar_frame, text=self.t('pausado'), font=ctk.CTkFont(size=11, weight="bold"), text_color="#ef4444")
        self.lbl_status_sidebar.pack(side="bottom", pady=30)

        # ----------------- PAINEL CENTRAL (ABAS DO VEÍCULO) -----------------
        self.tabview = ctk.CTkTabview(self, fg_color="#131d31", segmented_button_selected_color="#0284c7")
        self.tabview.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        self.aba_monitor = self.tabview.add(self.t('tab_monitor'))
        self.aba_manutencao = self.tabview.add(self.t('tab_manutencao'))
        self.aba_wifi = self.tabview.add(self.t('tab_wifi'))
        self.aba_bluetooth = self.tabview.add(self.t('tab_bt'))
        self.aba_guia = self.tabview.add(self.t('tab_guia'))
        self.aba_ai = self.tabview.add(self.t('tab_ai'))
        
        self.tabview._segmented_button.grid_forget()
        self.tabview.set(self.t('tab_monitor'))

        # ----------------- PAINEL DIREITO COMPLETO -----------------
        self.frame_dir = ctk.CTkFrame(self, width=290, fg_color="#0b1329", corner_radius=0)
        self.frame_dir.grid(row=0, column=2, sticky="nsew")

        ctk.CTkLabel(self.frame_dir, text="🌐 IDIOMA / LANGUAGE", font=("Segoe UI", 11, "bold"), text_color="#38bdf8").pack(pady=(15, 5))
        
        lista_idiomas = [
            "Português", "Português (Portugal)", "Inglês", "Espanhol", 
            "Italiano", "Russo", "Alemão", "Francês", "Japonês", "Chinês"
        ]
        
        self.menu_idioma = ctk.CTkOptionMenu(
            self.frame_dir, values=lista_idiomas, 
            command=self.mudar_idioma_sistema, fg_color="#0284c7", button_color="#0369a1"
        )
        self.menu_idioma.set(estado_app["idioma_atual"])
        self.menu_idioma.pack(padx=10, pady=5, fill="x")

        self.tab_dir = ctk.CTkTabview(self.frame_dir, fg_color="#131d31", height=660)
        self.tab_dir.pack(padx=10, pady=10, fill="both", expand=True)

        self.aba_d_clima = self.tab_dir.add("Clima")
        self.aba_d_grafico = self.tab_dir.add("Gráfico")
        self.aba_d_cores = self.tab_dir.add("Cores")
        self.aba_d_dalton = self.tab_dir.add("Daltonismo")
        self.tab_dir._segmented_button.grid_forget()

        self.construir_painel_direito_clima()
        self.construir_painel_direito_grafico()
        self.construir_painel_direito_cores()
        self.construir_painel_direito_daltonico()

        self.construir_aba_monitor()
        self.construir_aba_manutencao()
        self.construir_aba_wifi()
        self.construir_aba_bluetooth()
        self.construir_aba_guia()
        self.construir_aba_ai()

        self.after(1000, self.ciclo_telemetria_global)

    def t(self, chave):
        idioma = estado_app["idioma_atual"]
        if idioma in TRADUCOES and chave in TRADUCOES[idioma]:
            return TRADUCOES[idioma][chave].format(usuario=estado_app["usuario_nome"], odo=estado_app["odometro"], comb=estado_app["combustivel_litros"])
        return TRADUCOES["Português"].get(chave, chave).format(usuario=estado_app["usuario_nome"], odo=estado_app["odometro"], comb=estado_app["combustivel_litros"])

    def traduzir_sistema_nome(self, nome_sis):
        idioma = estado_app["idioma_atual"]
        if idioma in TRADUCAO_CATEGORIAS and nome_sis in TRADUCAO_CATEGORIAS[idioma]:
            return TRADUCAO_CATEGORIAS[idioma][nome_sis]
        return nome_sis

    def mudar_idioma_sistema(self, novo_idioma):
        estado_app["idioma_atual"] = novo_idioma
        
        self.title(self.t('titulo'))
        self.lbl_cliente.configure(text=f"{self.t('condutor')}\n{estado_app['usuario_nome']}")
        self.btn_m_monitor.configure(text=self.t('painel'))
        self.btn_m_manut.configure(text=self.t('manutencao'))
        self.btn_m_wifi.configure(text=self.t('wifi'))
        self.btn_m_bt.configure(text=self.t('bt'))
        self.btn_m_guia.configure(text=self.t('guia'))
        self.btn_m_ai.configure(text=self.t('ai'))

        try:
            for k in [
                "Monitor", "Maintenance", "Mantenimiento", "Manutenção", "Wi-Fi", "Bluetooth", "Guide", "Guía", "Guia", "AI", "IA",
                self.t('tab_monitor'), self.t('tab_manutencao'), self.t('tab_wifi'), self.t('tab_bt'), self.t('tab_guia'), self.t('tab_ai')
            ]:
                try: self.tabview.delete(k)
                except: pass
            
            self.aba_monitor = self.tabview.add(self.t('tab_monitor'))
            self.aba_manutencao = self.tabview.add(self.t('tab_manutencao'))
            self.aba_wifi = self.tabview.add(self.t('tab_wifi'))
            self.aba_bluetooth = self.tabview.add(self.t('tab_bt'))
            self.aba_guia = self.tabview.add(self.t('tab_guia'))
            self.aba_ai = self.tabview.add(self.t('tab_ai'))
            self.tabview.set(self.t('tab_monitor'))
        except Exception:
            pass

        self.construir_aba_monitor()
        self.construir_aba_manutencao()
        self.construir_aba_wifi()
        self.construir_aba_bluetooth()
        self.construir_aba_guia()
        self.construir_aba_ai()
        self.construir_painel_direito_clima()
        self.construir_painel_direito_grafico()
        self.construir_painel_direito_cores()
        self.construir_painel_direito_daltonico()

    def mudar_aba(self, nome_aba_interna):
        mapa_abas = {
            "Monitor": self.t('tab_monitor'),
            "Manutencao": self.t('tab_manutencao'),
            "Wifi": self.t('tab_wifi'),
            "Bluetooth": self.t('tab_bt'),
            "Guia": self.t('tab_guia'),
            "AI": self.t('tab_ai')
        }
        alvo = mapa_abas.get(nome_aba_interna, self.t('tab_monitor'))
        self.tabview.set(alvo)

    # ==========================================
    # PAINEL DIREITO: CLIMA E HORA EM TEMPO REAL
    # ==========================================
    def construir_painel_direito_clima(self):
        for w in self.aba_d_clima.winfo_children(): w.destroy()

        ctk.CTkButton(self.aba_d_clima, text="🌤 Clima", fg_color="#0284c7", command=lambda: self.tab_dir.set("Clima")).pack(side="top", pady=2, fill="x")
        ctk.CTkButton(self.aba_d_clima, text="📊 Gráfico", fg_color="#1e293b", command=lambda: self.tab_dir.set("Gráfico")).pack(side="top", pady=2, fill="x")
        ctk.CTkButton(self.aba_d_clima, text="🎨 Cores", fg_color="#1e293b", command=lambda: self.tab_dir.set("Cores")).pack(side="top", pady=2, fill="x")
        ctk.CTkButton(self.aba_d_clima, text="👁 Daltonismo", fg_color="#1e293b", command=lambda: self.tab_dir.set("Daltonismo")).pack(side="top", pady=2, fill="x")

        ctk.CTkLabel(self.aba_d_clima, text="📍 Mauá, SP (2026)", font=("Segoe UI", 12, "bold"), text_color="#38bdf8").pack(pady=(15, 5))
        
        self.lbl_relogio_dinamico = ctk.CTkLabel(self.aba_d_clima, text="", font=("Courier", 15, "bold"), text_color="#facc15")
        self.lbl_relogio_dinamico.pack(pady=10)

        f_clima_card = ctk.CTkFrame(self.aba_d_clima, fg_color="#090d16", corner_radius=10)
        f_clima_card.pack(fill="x", padx=5, pady=10)

        ctk.CTkLabel(f_clima_card, text="🌡 Temperatura: 24°C", font=("Segoe UI", 12), text_color="#f8fafc").pack(pady=5)
        ctk.CTkLabel(f_clima_card, text="💧 Umidade: 68%", font=("Segoe UI", 12), text_color="#f8fafc").pack(pady=5)
        ctk.CTkLabel(f_clima_card, text="⛅ Previsão: Sol com nuvens", font=("Segoe UI", 12), text_color="#38bdf8").pack(pady=5)

    def construir_painel_direito_grafico(self):
        for w in self.aba_d_grafico.winfo_children(): w.destroy()

        ctk.CTkButton(self.aba_d_grafico, text="🌤 Clima", fg_color="#1e293b", command=lambda: self.tab_dir.set("Clima")).pack(side="top", pady=2, fill="x")
        ctk.CTkButton(self.aba_d_grafico, text="📊 Gráfico", fg_color="#0284c7", command=lambda: self.tab_dir.set("Gráfico")).pack(side="top", pady=2, fill="x")
        ctk.CTkButton(self.aba_d_grafico, text="🎨 Cores", fg_color="#1e293b", command=lambda: self.tab_dir.set("Cores")).pack(side="top", pady=2, fill="x")
        ctk.CTkButton(self.aba_d_grafico, text="👁 Daltonismo", fg_color="#1e293b", command=lambda: self.tab_dir.set("Daltonismo")).pack(side="top", pady=2, fill="x")

        ctk.CTkLabel(self.aba_d_grafico, text="📈 RESUMO DE DESGASTE", font=("Segoe UI", 12, "bold"), text_color="#38bdf8").pack(pady=(15, 10))

        self.scroll_grafico = ctk.CTkScrollableFrame(self.aba_d_grafico, fg_color="#090d16", height=450)
        self.scroll_grafico.pack(fill="both", expand=True, padx=2, pady=5)

        self.atualizar_barras_grafico_lateral()

    def atualizar_barras_grafico_lateral(self):
        if not hasattr(self, 'scroll_grafico'): return
        for w in self.scroll_grafico.winfo_children(): w.destroy()

        for sistema, pecas_dict in DADOS_PECAS.items():
            soma_pct = 0
            total = len(pecas_dict)
            for peca, info in pecas_dict.items():
                km = estado_app["km_pecas"].get(peca, 0.0)
                p = max(0.0, min(1.0, 1.0 - (km / info['vida_max'])))
                soma_pct += p
            media_sis = (soma_pct / total) if total > 0 else 1.0

            sis_traduzido = self.traduzir_sistema_nome(sistema)
            ctk.CTkLabel(self.scroll_grafico, text=sis_traduzido, font=("Segoe UI", 10, "bold"), text_color="#f8fafc").pack(anchor="w", padx=5, pady=(5, 0))
            
            pb = ctk.CTkProgressBar(self.scroll_grafico, width=220, height=10, progress_color="#39FF14" if media_sis > 0.5 else "#ef4444")
            pb.pack(anchor="w", padx=5, pady=2)
            pb.set(media_sis)

    def construir_painel_direito_cores(self):
        for w in self.aba_d_cores.winfo_children(): w.destroy()

        ctk.CTkButton(self.aba_d_cores, text="🌤 Clima", fg_color="#1e293b", command=lambda: self.tab_dir.set("Clima")).pack(side="top", pady=2, fill="x")
        ctk.CTkButton(self.aba_d_cores, text="📊 Gráfico", fg_color="#1e293b", command=lambda: self.tab_dir.set("Gráfico")).pack(side="top", pady=2, fill="x")
        ctk.CTkButton(self.aba_d_cores, text="🎨 Cores", fg_color="#0284c7", command=lambda: self.tab_dir.set("Cores")).pack(side="top", pady=2, fill="x")
        ctk.CTkButton(self.aba_d_cores, text="👁 Daltonismo", fg_color="#1e293b", command=lambda: self.tab_dir.set("Daltonismo")).pack(side="top", pady=2, fill="x")

        ctk.CTkLabel(self.aba_d_cores, text=self.t('lbl_cores_titulo'), font=("Segoe UI", 11, "bold"), text_color="#38bdf8").pack(pady=(15, 10))

        cores_disponiveis = [
            ("🔴 Vermelho", "#dc2626"), 
            ("🟠 Laranja", "#ea580c"), 
            ("🟣 Lilás", "#9333ea"), 
            ("🔵 Azul", "#0284c7"), 
            ("🟢 Verde", "#16a34a"), 
            ("🔘 Cinza", "#475569"), 
            ("⬛ Preto", "#000000")
        ]

        for nome_cor, codigo_hex in cores_disponiveis:
            ctk.CTkButton(
                self.aba_d_cores, text=nome_cor, fg_color=codigo_hex, hover_color=codigo_hex,
                command=lambda c=codigo_hex, n=nome_cor: self.aplicar_cor_app(c, n), height=35
            ).pack(fill="x", padx=10, pady=4)

    def aplicar_cor_app(self, codigo_hex, nome):
        estado_app["cor_atual"] = nome
        self.sidebar_frame.configure(fg_color=codigo_hex)
        self.frame_dir.configure(fg_color=codigo_hex)
        messagebox.showinfo("GeoLeon OS", f"Tema alterado para {nome}!")

    def construir_painel_direito_daltonico(self):
        for w in self.aba_d_dalton.winfo_children(): w.destroy()

        ctk.CTkButton(self.aba_d_dalton, text="🌤 Clima", fg_color="#1e293b", command=lambda: self.tab_dir.set("Clima")).pack(side="top", pady=2, fill="x")
        ctk.CTkButton(self.aba_d_dalton, text="📊 Gráfico", fg_color="#1e293b", command=lambda: self.tab_dir.set("Gráfico")).pack(side="top", pady=2, fill="x")
        ctk.CTkButton(self.aba_d_dalton, text="🎨 Cores", fg_color="#1e293b", command=lambda: self.tab_dir.set("Cores")).pack(side="top", pady=2, fill="x")
        ctk.CTkButton(self.aba_d_dalton, text="👁 Daltonismo", fg_color="#0284c7", command=lambda: self.tab_dir.set("Daltonismo")).pack(side="top", pady=2, fill="x")

        ctk.CTkLabel(self.aba_d_dalton, text=self.t('lbl_dalton_titulo'), font=("Segoe UI", 11, "bold"), text_color="#38bdf8").pack(pady=(15, 10))

        txt_btn = self.t('btn_desativar_dalton') if estado_app["daltonico_ativo"] else self.t('btn_ativar_dalton')
        cor_btn = "#facc15" if not estado_app["daltonico_ativo"] else "#ef4444"

        ctk.CTkButton(
            self.aba_d_dalton, text=txt_btn, fg_color=cor_btn, text_color="#090d16",
            font=("Segoe UI", 11, "bold"), command=self.alternar_modo_daltonico, height=45
        ).pack(fill="x", padx=10, pady=10)

    def alternar_modo_daltonico(self):
        estado_app["daltonico_ativo"] = not estado_app["daltonico_ativo"]
        if estado_app["daltonico_ativo"]:
            ctk.set_appearance_mode("light")
            messagebox.showinfo("GeoLeon OS", "Modo Daltônico / Alto Contraste ATIVADO!")
        else:
            ctk.set_appearance_mode("dark")
            messagebox.showinfo("GeoLeon OS", "Modo Daltônico DESATIVADO!")
        self.construir_painel_direito_daltonico()

    def construir_aba_monitor(self):
        for w in self.aba_monitor.winfo_children(): w.destroy()

        ctk.CTkLabel(self.aba_monitor, text=self.t('monitor_titulo'), font=ctk.CTkFont(size=14, weight="bold"), text_color="#38bdf8").pack(pady=10)

        self.frame_lista_mon = ctk.CTkScrollableFrame(self.aba_monitor, fg_color="#090d16", width=820, height=430)
        self.frame_lista_mon.pack(padx=10, pady=5, fill="both", expand=True)

        self.widgets_monitor = {}
        self.todas_pecas_flat = {}
        for sistema, pecas in DADOS_PECAS.items():
            for peca, info in pecas.items():
                self.todas_pecas_flat[peca] = info["vida_max"]

        for peca, vida_max in self.todas_pecas_flat.items():
            f_item = ctk.CTkFrame(self.frame_lista_mon, fg_color="#131d31")
            f_item.pack(fill="x", padx=10, pady=5)

            ctk.CTkLabel(f_item, text=peca, font=("Segoe UI", 11, "bold"), text_color="#f8fafc", width=250, anchor="w").pack(side="left", padx=10)
            prog = ctk.CTkProgressBar(f_item, width=370, height=14, progress_color="#facc15", fg_color="#090d16")
            prog.pack(side="left", padx=15)
            prog.set(1.0)
            lbl_p = ctk.CTkLabel(f_item, text="100.0%", font=("Segoe UI", 11, "bold"), text_color="#facc15", width=70)
            lbl_p.pack(side="right", padx=10)

            self.widgets_monitor[peca] = (prog, lbl_p, vida_max)

        self.lbl_info_tempo_real = ctk.CTkLabel(self.aba_monitor, text="🕒 Sincronizando sistema...", font=("Segoe UI", 11, "bold"), text_color="#38bdf8")
        self.lbl_info_tempo_real.pack(pady=5)

        self.lbl_odometro = ctk.CTkLabel(self.aba_monitor, text=self.t('odometro'), font=("Segoe UI", 12, "bold"), text_color="#f8fafc")
        self.lbl_odometro.pack(pady=5)

    def construir_aba_manutencao(self):
        for w in self.aba_manutencao.winfo_children(): w.destroy()

        ctk.CTkLabel(self.aba_manutencao, text=self.t('manut_titulo'), font=("Segoe UI", 14, "bold"), text_color="#38bdf8").pack(pady=10)

        f_controle = ctk.CTkFrame(self.aba_manutencao, fg_color="#090d16", corner_radius=8)
        f_controle.pack(fill="x", padx=15, pady=5)

        def alternar_motor():
            if not estado_app["rodando"]:
                for sistema, pecas_var in self.checkboxes_global.items():
                    for peca, var in pecas_var.items():
                        if var.get() == 1:
                            estado_app["km_pecas"][peca] = 0.0
                estado_app["rodando"] = True
                self.lbl_status_sidebar.configure(text=self.t('ativo'), text_color="#39FF14")
                self.btn_ligar_manut.configure(text=self.t('parar_sis'), fg_color="#ef4444")
                messagebox.showinfo("GeoLeon OS", "Monitoramento ativado!")
                self.mudar_aba("Monitor")
            else:
                estado_app["rodando"] = False
                self.lbl_status_sidebar.configure(text=self.t('pausado'), text_color="#ef4444")
                self.btn_ligar_manut.configure(text=self.t('iniciar_sis'), fg_color="#0284c7")

        btn_txt = self.t('parar_sis') if estado_app["rodando"] else self.t('iniciar_sis')
        btn_col = "#ef4444" if estado_app["rodando"] else "#0284c7"
        self.btn_ligar_manut = ctk.CTkButton(f_controle, text=btn_txt, font=("Segoe UI", 11, "bold"), fg_color=btn_col, command=alternar_motor, height=35)
        self.btn_ligar_manut.pack(padx=20, pady=8, fill="x")

        ctk.CTkLabel(self.aba_manutencao, text=self.t('escolha_sis'), font=("Segoe UI", 11, "bold"), text_color="#f8fafc").pack(anchor="w", padx=20, pady=(10, 5))

        f_botoes_sistemas = ctk.CTkScrollableFrame(self.aba_manutencao, fg_color="#090d16", height=90, orientation="horizontal")
        f_botoes_sistemas.pack(fill="x", padx=15, pady=5)

        f_conteudo_pecas = ctk.CTkFrame(self.aba_manutencao, fg_color="#090d16", corner_radius=10)
        f_conteudo_pecas.pack(fill="both", expand=True, padx=15, pady=10)

        self.scroll_pecas_sistema = ctk.CTkScrollableFrame(f_conteudo_pecas, fg_color="#131d31")
        self.scroll_pecas_sistema.pack(fill="both", expand=True, padx=10, pady=10)

        self.checkboxes_global = {}

        def carregar_pecas_sistema(sistema_nome_real):
            for widget in self.scroll_pecas_sistema.winfo_children(): widget.destroy()
            nome_exibicao = self.traduzir_sistema_nome(sistema_nome_real)
            ctk.CTkLabel(self.scroll_pecas_sistema, text=f">> {nome_exibicao}", font=("Segoe UI", 12, "bold"), text_color="#38bdf8").pack(anchor="w", padx=10, pady=10)
            for peca in DADOS_PECAS[sistema_nome_real].keys():
                var = self.checkboxes_global[sistema_nome_real][peca]
                ctk.CTkCheckBox(self.scroll_pecas_sistema, text=peca, variable=var, font=("Segoe UI", 11), text_color="#f8fafc").pack(anchor="w", padx=20, pady=6)

        for sistema in DADOS_PECAS.keys():
            self.checkboxes_global[sistema] = {}
            for peca in DADOS_PECAS[sistema].keys():
                self.checkboxes_global[sistema][peca] = tk.IntVar()

            nome_btn_traduzido = self.traduzir_sistema_nome(sistema)
            ctk.CTkButton(
                f_botoes_sistemas, text=nome_btn_traduzido, font=("Segoe UI", 11, "bold"),
                fg_color="#131d31", hover_color="#1e293b", text_color="#38bdf8",
                command=lambda s=sistema: carregar_pecas_sistema(s)
            ).pack(side="left", padx=5, ipadx=10, ipady=5)

        carregar_pecas_sistema(list(DADOS_PECAS.keys())[0])

    def construir_aba_wifi(self):
        for w in self.aba_wifi.winfo_children(): w.destroy()

        ctk.CTkLabel(self.aba_wifi, text=self.t('wifi_titulo'), font=("Segoe UI", 14, "bold"), text_color="#38bdf8").pack(pady=15)

        f_wifi = ctk.CTkFrame(self.aba_wifi, fg_color="#090d16", corner_radius=10)
        f_wifi.pack(fill="both", expand=True, padx=20, pady=10)

        self.lbl_wifi_status = ctk.CTkLabel(f_wifi, text=f"Wi-Fi: {estado_app['wifi_conectado'] or 'Desconectado'} | Internet: {estado_app['internet_status']}", font=("Segoe UI", 12, "bold"), text_color="#39FF14" if estado_app['wifi_conectado'] else "#ef4444")
        self.lbl_wifi_status.pack(pady=15)

        ctk.CTkButton(f_wifi, text=self.t('escanear_wifi'), font=("Segoe UI", 12, "bold"), fg_color="#0284c7", command=self.escanear_wifi, height=40).pack(pady=10, padx=30, fill="x")

        self.scroll_wifi_frame = ctk.CTkScrollableFrame(f_wifi, fg_color="#131d31", height=160)
        self.scroll_wifi_frame.pack(padx=30, pady=10, fill="x")
        ctk.CTkLabel(self.scroll_wifi_frame, text="...", font=("Segoe UI", 11), text_color="#94a3b8").pack(pady=20)

        ctk.CTkLabel(f_wifi, text=self.t('digite_wifi'), font=("Segoe UI", 11, "bold"), text_color="#f8fafc").pack(anchor="w", padx=30, pady=(10, 2))
        self.entry_manual_wifi = ctk.CTkEntry(f_wifi, placeholder_text="SSID...", fg_color="#131d31", text_color="#FFFFFF", height=35)
        self.entry_manual_wifi.pack(padx=30, pady=5, fill="x")

        self.entry_senha_wifi = ctk.CTkEntry(f_wifi, placeholder_text=self.t('senha_wifi'), show="*", fg_color="#131d31", text_color="#FFFFFF", height=35)
        self.entry_senha_wifi.pack(padx=30, pady=5, fill="x")

        ctk.CTkButton(f_wifi, text=self.t('conectar_wifi'), font=("Segoe UI", 12, "bold"), fg_color="#39FF14", text_color="#090d16", command=self.conectar_wifi_com_senha, height=40).pack(pady=15, padx=30, fill="x")

    def escanear_wifi(self):
        self.lbl_wifi_status.configure(text="Procurando redes...", text_color="#facc15")
        for w in self.scroll_wifi_frame.winfo_children(): w.destroy()
        self.update()
        threading.Thread(target=self._executar_varredura_wifi, daemon=True).start()

    def _executar_varredura_wifi(self):
        try:
            res = os.popen('netsh wlan show networks mode=bssid').read()
            redes = [l.split(":")[-1].strip() for l in res.split('\n') if "SSID" in l and "BSSID" not in l]
            if not redes: redes = ["Sandero_Multimedia_5G", "Residencia_Leon"]
            self.after(0, lambda: self._atualizar_botoes_wifi(redes))
        except:
            self.after(0, lambda: self._atualizar_botoes_wifi(["Sandero_Multimedia_5G", "Residencia_Leon"]))

    def _atualizar_botoes_wifi(self, redes):
        for w in self.scroll_wifi_frame.winfo_children(): w.destroy()
        for r in redes:
            ctk.CTkButton(self.scroll_wifi_frame, text=f"🌐 {r}", fg_color="#0b1329", text_color="#f8fafc", anchor="w", command=lambda net=r: self.selecionar_rede_wifi(net), height=35).pack(padx=5, pady=3, fill="x")

    def selecionar_rede_wifi(self, rede):
        self.entry_manual_wifi.delete(0, 'end')
        self.entry_manual_wifi.insert(0, rede)

    def conectar_wifi_com_senha(self):
        rede = self.entry_manual_wifi.get().strip()
        if not rede: return
        estado_app["wifi_conectado"] = rede
        estado_app["internet_status"] = "Online"
        self.lbl_wifi_status.configure(text=f"Wi-Fi: {rede} | Online 🌐", text_color="#39FF14")
        messagebox.showinfo("GeoLeon OS", f"Conectado a {rede} com sucesso!")

    def construir_aba_bluetooth(self):
        for w in self.aba_bluetooth.winfo_children(): w.destroy()

        ctk.CTkLabel(self.aba_bluetooth, text=self.t('bt_titulo'), font=("Segoe UI", 14, "bold"), text_color="#38bdf8").pack(pady=15)

        f_bt = ctk.CTkFrame(self.aba_bluetooth, fg_color="#090d16", corner_radius=10)
        f_bt.pack(fill="both", expand=True, padx=20, pady=10)

        self.lbl_bt_status = ctk.CTkLabel(f_bt, text=f"BT: {estado_app['bt_conectado'] or 'Desconectado'}", font=("Segoe UI", 12, "bold"), text_color="#39FF14" if estado_app['bt_conectado'] else "#ef4444")
        self.lbl_bt_status.pack(pady=15)

        ctk.CTkButton(f_bt, text=self.t('escanear_bt'), font=("Segoe UI", 12, "bold"), fg_color="#facc15", text_color="#090d16", command=self.procurar_bluetooth_real, height=40).pack(pady=10, padx=30, fill="x")

        self.scroll_bt_frame = ctk.CTkScrollableFrame(f_bt, fg_color="#131d31", height=230)
        self.scroll_bt_frame.pack(padx=30, pady=10, fill="x")
        ctk.CTkLabel(self.scroll_bt_frame, text="...", font=("Segoe UI", 11), text_color="#94a3b8").pack(pady=30)

    def procurar_bluetooth_real(self):
        for w in self.scroll_bt_frame.winfo_children(): w.destroy()
        self.update()
        threading.Thread(target=self._executar_bleak_thread, daemon=True).start()

    def _executar_bleak_thread(self):
        try:
            import bleak
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            async def scan():
                devices = await bleak.BleakScanner.discover(timeout=3.0)
                return [(d.name or "Desconhecido", d.address) for d in devices]
            devs = loop.run_until_complete(scan())
            self.after(0, lambda: self._atualizar_botoes_bt(devs))
        except:
            self.after(0, lambda: self._atualizar_botoes_bt([("Haylou RT", "20:1B:88:F3:A5:CE"), ("EASYWAY-BLE", "48:6D:E7:7B:83:0D")]))

    def _atualizar_botoes_bt(self, dispositivos):
        for w in self.scroll_bt_frame.winfo_children(): w.destroy()
        for nome, mac in dispositivos:
            ctk.CTkButton(self.scroll_bt_frame, text=f"📱 {nome} ({mac})", fg_color="#0b1329", text_color="#f8fafc", anchor="w", command=lambda m=mac, n=nome: self.conectar_bt(m, n), height=40).pack(padx=5, pady=3, fill="x")

    def conectar_bt(self, mac, nome):
        estado_app["bt_conectado"] = f"{nome} ({mac})"
        self.lbl_bt_status.configure(text=f"BT: Conectado a {nome}!", text_color="#39FF14")
        messagebox.showinfo("GeoLeon OS", f"Conectado a {nome}!")

    def construir_aba_guia(self):
        for w in self.aba_guia.winfo_children(): w.destroy()

        frame_esq = ctk.CTkFrame(self.aba_guia, fg_color="transparent")
        frame_esq.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        frame_dir = ctk.CTkFrame(self.aba_guia, fg_color="#090d16", corner_radius=10, width=300)
        frame_dir.pack(side="right", fill="both", expand=False, padx=10, pady=10)

        ctk.CTkLabel(frame_esq, text=self.t('guia_titulo'), font=("Segoe UI", 12, "bold"), text_color="#38bdf8").pack(anchor="w", pady=(0, 5))

        scroll_guia = ctk.CTkScrollableFrame(frame_esq, fg_color="#090d16", width=500, height=540)
        scroll_guia.pack(fill="both", expand=True)

        for sistema, pecas_dict in DADOS_PECAS.items():
            sis_nome = self.traduzir_sistema_nome(sistema)
            ctk.CTkLabel(scroll_guia, text=f">> {sis_nome.upper()}", font=("Segoe UI", 11, "bold"), text_color="#38bdf8").pack(anchor="w", padx=10, pady=(10, 2))
            for peca, info in pecas_dict.items():
                ctk.CTkButton(
                    scroll_guia, text=f"{peca} ({info['vida_max']:,} km)", 
                    font=("Segoe UI", 10), fg_color="#131d31", hover_color="#1e293b", text_color="#f8fafc", anchor="w",
                    command=lambda p=peca, d=info['desc']: self.atualizar_detalhe_guia(p, d)
                ).pack(fill="x", padx=10, pady=2, ipady=2)

        self.lbl_guia_nome = ctk.CTkLabel(frame_dir, text="Bloco do Motor", font=("Segoe UI", 12, "bold"), text_color="#38bdf8")
        self.lbl_guia_nome.pack(pady=(15, 5))

        self.lbl_imagem_peca = ctk.CTkLabel(frame_dir, text="[ Ilustração ]", fg_color="#131d31", corner_radius=8, width=250, height=180, text_color="#94a3b8")
        self.lbl_imagem_peca.pack(pady=5)

        self.lbl_guia_desc = ctk.CTkLabel(frame_dir, text="Estrutura principal...", font=("Segoe UI", 10), text_color="#94a3b8", wraplength=260, justify="left")
        self.lbl_guia_desc.pack(pady=10, padx=10)

    def atualizar_detalhe_guia(self, peca, desc):
        self.lbl_guia_nome.configure(text=peca)
        self.lbl_guia_desc.configure(text=desc)

    # ==========================================
    # ABA CENTRAL 6: ASSISTENTE IA COM SOUNDDEVICE (MICROFONE SEGURO)
    # ==========================================
    def construir_aba_ai(self):
        for w in self.aba_ai.winfo_children(): w.destroy()

        ctk.CTkLabel(self.aba_ai, text=self.t('ai_titulo'), font=("Segoe UI", 12, "bold"), text_color="#38bdf8").pack(pady=10)

        f_cont = ctk.CTkFrame(self.aba_ai, fg_color="#090d16", corner_radius=10)
        f_cont.pack(fill="both", expand=True, padx=10, pady=5)

        ctk.CTkLabel(f_cont, text=self.t('digite_ai'), font=("Segoe UI", 11, "bold"), text_color="#f8fafc").pack(anchor="w", padx=15, pady=(10, 2))

        self.txt_entrada = ctk.CTkTextbox(f_cont, height=50, fg_color="#131d31", text_color="#f8fafc", font=("Segoe UI", 11))
        self.txt_entrada.pack(padx=15, pady=5, fill="x")

        f_botoes = ctk.CTkFrame(f_cont, fg_color="transparent")
        f_botoes.pack(padx=15, pady=5, fill="x")

        ctk.CTkButton(f_botoes, text=self.t('consultar_txt'), fg_color="#0284c7", command=self.processar_texto).pack(side="left", ipadx=10, ipady=4)
        
        # Botão de Voz usando SoundDevice + SpeechRecognition sem PyAudio
        self.btn_voz_real = ctk.CTkButton(f_botoes, text=self.t('falar_carro'), fg_color="#facc15", text_color="#090d16", command=self.escutar_voz_sounddevice)
        self.btn_voz_real.pack(side="left", padx=12, ipadx=10, ipady=4)

        ctk.CTkLabel(f_cont, text=self.t('resposta_ai'), font=("Segoe UI", 11, "bold"), text_color="#f8fafc").pack(anchor="w", padx=15, pady=(10, 2))

        self.txt_saida = ctk.CTkTextbox(f_cont, height=120, fg_color="#131d31", text_color="#f8fafc", font=("Segoe UI", 11))
        self.txt_saida.pack(padx=15, pady=(5, 15), fill="both", expand=True)
        self.txt_saida.configure(state="disabled")

    def executar_resposta(self, pergunta):
        p = pergunta.lower()
        respostas = []
        acao = ""

        if any(w in p for w in ["bluetooth", "parear", "vincular"]):
            self.mudar_aba("Bluetooth")
            self.procurar_bluetooth_real()
            acao = "\n\n⚡ [GeoLeon AI]: Gestor Bluetooth aberto com sucesso!"
        elif any(w in p for w in ["wifi", "internet", "rede", "wlan"]):
            self.mudar_aba("Wifi")
            self.escanear_wifi()
            acao = "\n\n⚡ [GeoLeon AI]: Gestor Wi-Fi e Internet aberto!"
        elif any(w in p for w in ["manutenção", "manutencao", "maintenance", "trocar", "substituir"]):
            self.mudar_aba("Manutencao")
            acao = "\n\n⚡ [GeoLeon AI]: Painel de Manutenção de Peças aberto!"
        elif any(w in p for w in ["guia", "guide", "dicionario", "dicionário", "peca", "peça"]):
            self.mudar_aba("Guia")
            acao = "\n\n⚡ [GeoLeon AI]: Guia Técnico de Peças aberto!"
        elif any(w in p for w in ["monitor", "dashboard", "painel", "desgaste", "odometro"]):
            self.mudar_aba("Monitor")
            acao = "\n\n⚡ [GeoLeon AI]: Painel do Veículo em Tempo Real ativado!"

        agora = datetime.datetime.now()
        if any(w in p for w in ["hora", "horario", "que horas", "relogio", "data", "dia"]):
            respostas.append(f"🕒 Horário atual: {agora.strftime('%H:%M:%S')} | Data: {agora.strftime('%d/%m/%Y')}")

        for sistema, pecas_dict in DADOS_PECAS.items():
            for peca, info in pecas_dict.items():
                if peca.lower() in p or any(w in p for w in peca.lower().split() if len(w) > 3):
                    km = estado_app["km_pecas"].get(peca, 0.0)
                    porc = max(0.0, min(100.0, 100.0 - ((km / info['vida_max']) * 100.0)))
                    respostas.append(f"🔧 {peca}: {porc:.1f}% OK. ({info['desc']})")

        idioma = estado_app["idioma_atual"]
        if not respostas:
            msg = f"🤖 GeoLeon AI ({estado_app['usuario_nome']} - {idioma}): {self.t('sistema_ativo')}" + acao
        else:
            msg = f"🤖 {self.t('relatorio_ia')}:\n\n" + "\n\n".join(respostas) + acao

        self.txt_saida.configure(state="normal")
        self.txt_saida.delete("1.0", "end")
        self.txt_saida.insert("end", msg)
        self.txt_saida.configure(state="disabled")

    def processar_texto(self):
        t = self.txt_entrada.get("1.0", "end").strip()
        if t: self.executar_resposta(t)

    def escutar_voz_sounddevice(self):
        try:
            import sounddevice as sd
            import numpy as np
            import speech_recognition as sr

            fs, duration = 44100, 5
            self.txt_saida.configure(state="normal")
            self.txt_saida.delete("1.0", "end")
            self.txt_saida.insert("end", "🎤 A ouvir o condutor... Fale agora por 5 segundos!")
            self.txt_saida.configure(state="disabled")
            self.update()

            audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
            sd.wait()

            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
            tmp_name = temp_file.name
            temp_file.close()

            with wave.open(tmp_name, 'wb') as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)
                wf.setframerate(fs)
                wf.writeframes(audio_data.tobytes())

            r = sr.Recognizer()
            with sr.AudioFile(tmp_name) as source:
                audio = r.record(source)
                texto_ouvido = r.recognize_google(audio, language="pt-BR")

            try:
                os.unlink(tmp_name)
            except:
                pass

            self.txt_entrada.delete("1.0", "end")
            self.txt_entrada.insert("end", texto_ouvido)
            self.executar_resposta(texto_ouvido)

        except Exception as e:
            falado = simpledialog.askstring("Comando por Voz", "Microfone não detetado ou erro de áudio.\nDigite o comando:")
            if falado:
                self.txt_entrada.delete("1.0", "end")
                self.txt_entrada.insert("end", falado)
                self.executar_resposta(falado)

    # ==========================================
    # TELEMETRIA GLOBAL E RELÓGIO EM TEMPO REAL
    # ==========================================
    def ciclo_telemetria_global(self):
        agora = datetime.datetime.now()
        agora_str = agora.strftime("%d/%m/%Y\n%H:%M:%S")
        
        if hasattr(self, 'lbl_relogio_dinamico'):
            self.lbl_relogio_dinamico.configure(text=agora_str)

        wifi_st = estado_app["wifi_conectado"] or "Off"
        if hasattr(self, 'lbl_info_tempo_real'):
            self.lbl_info_tempo_real.configure(text=f"🕒 {agora.strftime('%H:%M:%S')}  |  🌐 Wi-Fi: {wifi_st}  |  📶 {estado_app['internet_status']}")

        if estado_app["rodando"]:
            estado_app["odometro"] += 150.0
            for peca, (prog, lbl_p, v_max) in self.widgets_monitor.items():
                estado_app["km_pecas"][peca] += 150.0
                p = max(0.0, min(1.0, 1.0 - (estado_app["km_pecas"][peca] / v_max)))
                prog.set(p)
                lbl_p.configure(text=f"{p*100.0:5.1f}%")
            
            self.atualizar_barras_grafico_lateral()

        self.after(1000, self.ciclo_telemetria_global)

if __name__ == "__main__":
    app = GeoLeonOSApp()
    app.mainloop()
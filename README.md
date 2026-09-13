# 🏢 Podnikový informační systém — Backend (REST API)

Tento repozitář obsahuje backendovou část aplikace napsanou v frameworku **Django** a **Django REST Framework**. Jako databáze je použito **PostgreSQL**.

### 🔗 Propojení
* **Frontend repozitář najdete zde:** [https://github.com/cestmirstrmiska/evidence-projektu-frontend]

### 🛠️ Prerekvizity a setup databáze
Před spuštěním aplikace je nutné mít nainstalovaný **PostgreSQL server** a vytvořenou prázdnou databázi. Přihlašovací údaje k databázi (název, uživatel, heslo) si upravte lokálně ve vašem souboru `config/settings.py` v sekci `DATABASES`.

### 🚀 Jak spustit backend lokálně:
1. **Aktivujte virtuální prostředí:**
   `venv\Scripts\activate` (Windows) nebo `source venv/bin/activate` (Mac/Linux)
2. **Nainstalujte veškeré závislé knihovny:**
   `pip install -r requirements.txt`
3. **Spusťte databázové migrace:**
   `python manage.py migrate`
4. **Spusťte vývojový server:**
   `python manage.py runserver`

Backend bude po spuštění naslouchat a poskytovat REST API na adrese `http://127.0.0.1:8000/api`.

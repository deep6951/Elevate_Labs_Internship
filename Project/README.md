# 🛡️ Cyber Threat Intelligence Dashboard

A web-based Cyber Threat Intelligence (CTI) Dashboard built with Flask that allows users to analyze IP addresses, domains, and URLs using threat intelligence APIs such as VirusTotal and AbuseIPDB. The dashboard displays threat information, Indicators of Compromise (IOCs), reputation scores, and visual analytics.

---

## 📌 Features

- 🔍 IP Address Reputation Lookup
- 🌐 Domain Reputation Lookup
- 🦠 URL Threat Analysis
- 📊 Interactive Dashboard
- 📈 Threat Statistics and Charts
- 📋 IOC Detection
- 📁 Search History
- 📤 Export Results
- 🎨 Responsive User Interface

---

## 🛠️ Technologies Used

- Python 3.x
- Flask
- HTML5
- CSS3
- JavaScript
- Bootstrap 5
- VirusTotal API
- AbuseIPDB API
- MongoDB / SQLite
- Chart.js

---

## 📂 Project Structure

```
cyber-threat-intelligence-dashboard/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│
├── static/
│   ├── css/
│   ├── js/
│
├── utils/
│   ├── virustotal.py
│   ├── abuseipdb.py
│   └── charts.py
│
└── database/
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/cyber-threat-intelligence-dashboard.git
```

### Open Project

```bash
cd cyber-threat-intelligence-dashboard
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 API Keys

Create a `.env` file in the project root.

Example:

```
VIRUSTOTAL_API_KEY=YOUR_API_KEY
ABUSEIPDB_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 📷 Screenshots

Add screenshots here after completing the project.

```
screenshots/
```

---

## 📈 Future Improvements

- Threat Feed Integration
- Malware Hash Lookup
- Email Reputation Lookup
- IOC Timeline
- PDF Report Generation
- Dark Mode
- User Authentication

---

## 👨‍💻 Author

Deep Patel

Cybersecurity Intern

---

## 📄 License

This project is licensed under the MIT License.

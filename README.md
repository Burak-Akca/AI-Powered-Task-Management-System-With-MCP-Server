# 🤖 Personal Assistant - AI-Powered Task Management System With MCP Server

**A comprehensive personal assistant built with Django, FastMCP, and Docker that provides intelligent task management, note-taking, email automation, weather updates, news aggregation, and reminder functionality.**

---

## ✨ Features

### 🎯 **Core Functionality**
- **Smart Note Management** ✅: Create, list, and manage notes with automatic database handling
- **Email Automation** ✅: Send emails via SMTP with Gmail integration

### **Service API**
 
- **News Aggregation** 🔄: Fetch latest news headlines by category and country *(Coming Soon)*
- **Reminder System** 🔄: Set time-based reminders with background processing *(Coming Soon)*
- **Weather Intelligence** 🔄: Get detailed weather forecasts and alerts using National Weather *(Coming Soon)* 
### 🛠️ **Technical Features**
- **FastMCP Integration**: Model Context Protocol for seamless AI tool interaction
- **PostgreSQL Database**: Robust data persistence with automatic connection retry
- **Docker Compose**: Multi-service orchestration with health checks
- **Async Operations**: Non-blocking operations for better performance
- **Error Handling**: Comprehensive error handling with graceful fallbacks

---

## 🏗️ Architecture

### **System Components**
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   FastMCP       │    │   Django Web    │    │   PostgreSQL    │
│   Assistant     │◄──►│   Application   │◄──►│   Database      │
│   (Tools)       │    │   (Notes UI)    │    │   (Docker)      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   External      │    │   Docker        │    │     Docker      │
│   APIs          │    │   Compose       │    │     Compose     │
│   (Gmail SMTP)  │    │  (Orchestration)│    │ (Orchestration) │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### **Tool Ecosystem**
| Tool | Function | Status | Description |
|------|----------|--------|-------------|
| `notes_tool.py` | Note Management | ✅ **Active** | Create, list, and manage notes with web UI |
| `email_tool.py` | Email Sending | ✅ **Active** | Send emails via SMTP with async support |
| `weather_tool.py` | Weather Data | 🔄 **Coming Soon** | Get forecasts and alerts from NWS API |
| `news_tool.py` | News Headlines | 🔄 **Coming Soon** | Fetch news by category and country |
| `reminder_tool.py` | Reminders | 🔄 **Coming Soon** | Set time-based reminders |

---

## 🚀 Quick Start

### **Prerequisites**
- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/)
- Python 3.11+ (for local development)
- PostgreSQL (handled by Docker)

### **1. Clone and Setup**
```bash
git clone https://github.com/Burak-Akca/AI-Powered-Task-Management-System-With-MCP-Server
cd AI-Powered-Task-Management-System-With-MCP-Server
```

### **2. Environment Configuration**
Create a `.env` file in the project root:
```env
# Database Configuration
POSTGRES_DB=notedb
POSTGRES_USER=noter
POSTGRES_PASSWORD=noterpass
DB_NAME=notedb
DB_USER=noter
DB_PASSWORD=noterpass
DB_HOST=db
DB_PORT=5432

# Application Settings
DEBUG=True


```




### **3. Development Setup**
```bash

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install MCP server (required for Claude integration)
uv run mcp install assistant.py

# Run Django migrations
docker compose exec web python manage.py migrate


# Access database (optinal)
docker compose exec db psql -U noter -d notedb




# Start all services
docker compose up --build -d


```

### **4. MCP Server Installation & Configuration**
After installing dependencies in your virtual environment, run the MCP server installation command:

```bash
uv run mcp install assistant.py
```

This command performs the following operations to run `assistant.py` in an MCP-compatible manner:

- **Isolated Python Environment**: Uses `uv` to run the MCP command in an isolated Python environment
- **MCP Server Registration**: Applies the `mcp install assistant.py` command to load or register the MCP server within `assistant.py`
- **Automatic Configuration**: Automatically registers the MCP server to your Claude configuration file

#### **Manual Configuration (if needed)**
If you encounter errors with the default configuration, manually update your Claude Desktop config file with the following:

```json
{
  "mcpServers": {
    "personal_assistant": {
      "command": "uv",
      "args": [
        "--directory",
        "give project root directory path here",
        "run",
        "assistant.py"
      ]
    }
  }
}
```

**Note**: Replace `"give project root directory path here"` with your actual project root directory path.

### **5. Access the Application**
- **Web Interface**: http://localhost:8001
- **Assistant API**: Running on default FastMCP port

---

## 🛠️ Tool Usage

### **📝 Notes Management** ✅ **Available Now**

#### **🛠️ Tool: add_note**
📌 **Description**: Adds a new note with a title and optional content.

💬 **Example prompt**:
```
Create a new note with the title "Meeting Summary" and the content "Discussed project deadlines and assigned tasks to the team."
```

```python
# Add a new note
add_note(title="Meeting Notes", content="Important discussion points...")
```

#### **🛠️ Tool: list_notes**
📌 **Description**: Retrieves the most recent notes from the database.

💬 **Example prompt**:
```
Show me the notes.
```

```python
# List recent notes
list_notes(limit=10)
```

#### **🛠️ Tool: start_notes_app**
📌 **Description**: Starts the Django notes app via Docker and opens it in the browser.

💬 **Example prompt**:
```
Start the notes application and open it in the browser.
```

```python
# Start the notes web application
start_notes_app()
```

### **📧 Email Automation** ✅ **Available Now**

#### **🛠️ Tool: send_email**
📌 **Description**: Sends an email using Gmail's SMTP service.

🔐 **Required fields**:
- `to_email`: Recipient's email address
- `subject`: Subject of the email
- `body`: The body content of the message
- `from_email`: Sender's Gmail address
- `password`: Gmail App Password (not your regular account password)

🛡️ **Important**: If you are using Gmail, you must generate an App Password and use that instead of your normal account password. This is required when two-factor authentication is enabled.

💬 **Example prompt**:
```
Send an email to example@gmail.com with the subject "Weekly Sync" and the message "Meeting starts at 10 AM sharp." Use my Gmail address example@customdomain.com and the app password I provided.
```

```python
# Send an email
send_email(
    to_email="recipient@example.com",
    subject="Important Update",
    body="This is the email content...",
    from_email="your-email@gmail.com",
    password="your-app-password"
)
```

### **🌤️ Weather Information** 🔄 **Coming Soon**
```python
# Get weather forecast
get_forecast(latitude=40.7128, longitude=-74.0060)

# Get weather alerts
get_alerts(state="NY")
```

### **📰 News Headlines** 🔄 **Coming Soon**
```python
# Get general news
get_news_headlines(category="general", country="us")

# Get technology news
get_news_headlines(category="technology", country="us")
```

### **⏰ Reminder System** 🔄 **Coming Soon**
```python
# Set a reminder
set_reminder(
    date="2024-01-15 14:30",
    message="Team meeting at 2:30 PM"
)
```

---


### **Service Management**
```bash
# View logs
docker compose logs -f

# Restart services
docker compose restart

# Stop all services
docker compose down

# Rebuild and start
docker compose up --build -d
```

---

## 📁 Project Structure

```
personal_assistant/
├── 📄 assistant.py              # Main FastMCP assistant
├── 📄 notes_tool.py             # Note management tools
├── 📄 email_tool.py             # Email automation
├── 📄 compose.yaml              # Docker Compose configuration
├── 📄 requirements.txt          # Python dependencies
├── 📄 Dockerfile                # Container configuration
├── 📁 src/                      # Django application
│   ├── 📁 NoteApp/             # Django project settings
│   ├── 📁 notes/               # Notes app
│   └── 📄 manage.py            # Django management
├── 📁 utils/                    # Utility modules
│   └── 📄 get_connection.py    # Database connection with retry
└── 📄 README.md                 # This file
```

---

## 🔌 API Integration

### **FastMCP Protocol**
The assistant uses the Model Context Protocol (MCP) for seamless AI integration with Claude and other MCP-compatible clients:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("personal_assistant")

# Register active tools
mcp.tool()(send_email)
mcp.tool()(add_note)
mcp.tool()(list_notes)
mcp.tool()(start_notes_app)

# Future tools (commented out for now)
# mcp.tool()(set_reminder)
# mcp.tool()(get_forecast)
# mcp.tool()(get_alerts)
# mcp.tool()(get_news_headlines)
```

### **External APIs**
- **Gmail SMTP** ✅: Email sending capabilities *(Currently Active)*
- **National Weather Service** 🔄: Free weather data and alerts *(Coming Soon)*
- **NewsAPI** 🔄: News headlines and articles *(Coming Soon)*

---

## 🐳 Docker Configuration

### **Services**
- **web**: Django application (port 8001)
- **db**: PostgreSQL database (port 5432)

### **Health Checks**
```yaml
healthcheck:
  test: ["CMD-SHELL", "pg_isready -U noter -d notedb"]
  interval: 5s
  timeout: 5s
  retries: 10
```

### **Networks**
- **notenet**: Internal network for service communication

---

## 🔒 Security & Configuration

### **Environment Variables**
- Database credentials
- API keys for external services
- Debug settings





---

## 🚨 Troubleshooting

### **Common Issues**

1. **Database Connection Failed**
   ```bash
   # Check if database is running
   docker compose ps
   
   # View database logs
   docker compose logs db
   ```

2. **Port Already in Use**
   ```bash
   # Check what's using the port (Windows)
   netstat -ano | findstr :8001
   
   # Check what's using the port (Linux/macOS)
   sudo netstat -tuln | grep 8001
   
   # Stop conflicting services
   docker compose down
   ```


---


## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **FastMCP**: For the Model Context Protocol implementation
- **Django**: For the web framework
- **PostgreSQL**: For the database system
- **Docker**: For containerization

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/Burak-Akca/AI-Powered-Task-Management-System-With-MCP-Server/issues)
- **Documentation**: This README and inline code comments
- **Community**: Check our [Code of Conduct](CODE_OF_CONDUCT.md)

---

**Made with ❤️ for intelligent task management and productivity enhancement.**

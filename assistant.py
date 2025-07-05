from mcp.server.fastmcp import FastMCP
from email_tool import send_email
from reminder_tool import set_reminder
from weather_tool import get_forecast, get_alerts
from news_tool import get_news_headlines
from notes_tool import add_note,list_notes,start_notes_app

mcp = FastMCP("personal_assistant")

# Register all tools
mcp.tool()(send_email)
mcp.tool()(add_note)
mcp.tool()(list_notes)
mcp.tool()(start_notes_app)

# mcp.tool()(set_reminder)
# mcp.tool()(get_forecast)
# mcp.tool()(get_alerts)
# mcp.tool()(get_news_headlines)
if __name__ == "__main__":
    mcp.run()

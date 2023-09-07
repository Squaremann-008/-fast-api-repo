from fastapi import FastAPI, HTTPException, Query
from datetime import datetime
import os

app = FastAPI()

@app.get("/api/")
async def api_endpoint(
    slack_name: str = Query('Oiseh', description="Slack name"),
    track: str = Query('backend', description="Track")
):
    try:
        # Get current day of the week and UTC time
        current_day = datetime.utcnow().strftime("%A")
        current_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

        # Get the GitHub URL of the file being run
        file_url = "https://github.com/Squaremann-008/-fast-api-repo/blob/main/stage1/app.py"
        # Get the GitHub URL of the full source code
        full_source_code_url = "https://github.com/Squaremann-008/-fast-api-repo/"

        # Prepare the response JSON
        response_data = {
            "slack_name": slack_name,
            "current_day": current_day,
            "utc_time": current_time,
            "track": track,
            "github_file_url": file_url,
            "github_repo_url": full_source_code_url,
            "status_code": 200
        }

        return response_data
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

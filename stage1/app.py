from fastapi import FastAPI, HTTPException, Query
from datetime import datetime
import os

app = FastAPI()

@app.get("/info/")
async def get_info(
    slack_name: str = Query(Oiseh, description="Slack name"),
    track: str = Query(Backend, description="Track")
):
    try:
        # Get current day of the week and UTC time
        current_day = datetime.utcnow().strftime("%A")
        current_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

        # Get the GitHub URL of the file being run
        file_url = f"https://github.com/your-username/your-repo/blob/main/{os.path.basename(__file__)}"

        # Get the GitHub URL of the full source code
        full_source_code_url = "https://github.com/your-username/your-repo"

        # Prepare the response JSON
        response_data = {
            "slack_name": slack_name,
            "current_day": current_day,
            "current_utc_time": current_time,
            "track": track,
            "file_github_url": file_url,
            "full_source_code_github_url": full_source_code_url,
            "status_code": "success"
        }

        return response_data
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

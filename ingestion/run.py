from app.ingest import app

if __name__ == "__main__":
    app.run(app.config["HOST"])

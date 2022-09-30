# FastAPI Server APP

This is a simple example FastAPI application that pretends to be a bookstore.

Clone the FastAPI server app.
```bash
cd /home/(username)
git clone https://github.com/alanmgg/FastAPI-BD.git
```

Start FastAPI.
```bash
cd /opt
mkdir app
cd /home/(username)/FastAPI-BD/apiServer
pip3 install -r requirements.txt
cd ..
uvicorn apiServer:app --reload
```

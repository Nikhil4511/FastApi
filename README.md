# ⚡ FastAPI Learning Projects

A hands-on collection of FastAPI projects: building REST APIs, validating data with Pydantic, managing a patient records API (GET / POST / PUT / DELETE), and serving a machine learning model for insurance prediction.

## 📁 Project Structure

```
.
├── main.py              # Basic FastAPI app: first endpoints
├── patients.json        # Sample patient data (acts as a simple data store)
├── patiens.py           # Patient endpoints: read/view/sort records
├── post-request.py      # POST: create new patient records
├── put-delete.py        # PUT / DELETE: update and remove patient records
├── Pydantic/            # Pydantic models and data validation examples
├── insuranceprediction/ # Insurance prediction ML project
├── Serving-model/       # Serving the trained model through a FastAPI endpoint
└── myenv/               # Virtual environment (not committed)
```

## ✨ Features

- REST API built with **FastAPI**
- Full **CRUD** on patient data: `GET`, `POST`, `PUT`, `DELETE`
- Request/response validation with **Pydantic**
- JSON file used as a lightweight database
- ML model served as a prediction API
- Automatic interactive docs (Swagger UI and ReDoc)

## ⚙️ Setup

**Prerequisites:** Python 3.9+

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

# 2. Create and activate a virtual environment
python -m venv myenv
myenv\Scripts\activate           # Windows
source myenv/bin/activate        # macOS/Linux

# 3. Install dependencies
pip install fastapi "uvicorn[standard]" pydantic
pip install scikit-learn pandas joblib   # for the ML model-serving projects
```

## ▶️ Running the Apps

Start any file with Uvicorn (use the file name without `.py`; `post-request.py` and `put-delete.py` contain hyphens, so rename them, e.g. `post_request.py`, before using them as modules):

```bash
uvicorn main:app --reload
uvicorn patiens:app --reload
```

The server runs at **http://127.0.0.1:8000**.

| URL | Description |
|---|---|
| `/docs` | Swagger UI (interactive API docs) |
| `/redoc` | ReDoc documentation |
| `/openapi.json` | OpenAPI schema |

## 🔌 Example Endpoints (Patient API)

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome / health check |
| GET | `/view` | View all patients |
| GET | `/patient/{patient_id}` | Get a single patient |
| GET | `/sort?sort_by=bmi&order=asc` | Sort patients by a field |
| POST | `/create` | Add a new patient |
| PUT | `/edit/{patient_id}` | Update a patient |
| DELETE | `/delete/{patient_id}` | Delete a patient |

> Adjust the routes above to match the ones defined in your code.

### Sample request

```bash
curl -X POST http://127.0.0.1:8000/create \
  -H "Content-Type: application/json" \
  -d '{"id": "P001", "name": "Nikhil", "age": 22, "weight": 70, "height": 1.75}'
```

## 🧠 Topics Covered

- Path and query parameters
- Request bodies and Pydantic models
- Field validation, computed fields and custom validators
- HTTP status codes and `HTTPException` error handling
- Reading and writing JSON data
- Serving a trained ML model via an API endpoint

## 🛠️ Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Pydantic](https://docs.pydantic.dev/)
- scikit-learn / pandas (model serving)

## 🔒 Notes

Don't commit `myenv/`, `__pycache__/`, `.vscode/` or any secrets. Suggested `.gitignore`:

```
myenv/
__pycache__/
.vscode/
.env
```

## 🤝 Contributing

Suggestions and pull requests are welcome.

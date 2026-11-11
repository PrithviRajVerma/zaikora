# 🍽️ Zaikora – Backend API (FastAPI)

FastAPI-powered backend for Zaikora restaurant and food ordering platform.

## 🚀 Features

- **FastAPI**: High performance, async, type-safe API with automatic OpenAPI (Swagger) documentation.
- **Motor / MongoDB**: Async MongoDB integration.
- **Pydantic v2**: Robust data validation and settings management.
- **Structured Logging**: Clean, formatted console and JSON logs with Loguru.
- **CORS & HTTP Logging**: Preconfigured CORS and request-response timing middleware.
- **Health Check & Error Handlers**: Standardized JSON responses for status, 404, and exceptions.

## 📁 Architecture

```text
backend/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints/
│   │       │   └── health.py     # Health check endpoint
│   │       └── router.py         # v1 route registry
│   ├── core/
│   │   ├── config.py             # Settings & env validation
│   │   ├── database.py           # Async MongoDB connection
│   │   └── logger.py             # Loguru logger setup
│   ├── middlewares/
│   │   └── http_logger.py        # HTTP request logging middleware
│   ├── models/                   # Database documents
│   ├── schemas/                  # Pydantic schemas
│   ├── services/                 # Business logic
│   ├── utils/                    # Shared helpers
│   └── main.py                   # FastAPI app entry point
├── tests/                        # Test suite
├── requirements.txt              # Pip dependencies
├── pyproject.toml                # UV / Python project configuration
└── package.json                  # PNPM workspace integration
```

## ⚙️ Getting Started

### 1. Prerequisites

- Python 3.11+
- `uv` (recommended) or standard `python -m venv`

### 2. Environment Setup

Create `.env` inside `backend/`:

```env
PORT=5000
NODE_ENV=development
CLIENT_URL=http://localhost:5173

MONGO_URI=mongodb://localhost:27017/zaikora
JWT_SECRET=your_jwt_secret_key

RAZORPAY_KEY_ID=your_razorpay_key_id
RAZORPAY_KEY_SECRET=your_razorpay_key_secret

CLOUDINARY_CLOUD_NAME=your_cloudinary_cloud_name
CLOUDINARY_API_KEY=your_cloudinary_api_key
CLOUDINARY_API_SECRET=your_cloudinary_api_secret
```

### 3. Install Dependencies

Using `uv`:
```bash
uv venv
uv pip install -r requirements.txt
```

### 4. Run Development Server

Using `uv`:
```bash
uv run uvicorn app.main:app --reload --port 5000
```

Or using `pnpm` from anywhere in the monorepo:
```bash
pnpm dev:backend
# or from root to run both frontend and backend:
pnpm dev
```

### 5. Interactive API Documentation

- Swagger UI: `http://localhost:5000/docs`
- ReDoc: `http://localhost:5000/redoc`
- Health check: `http://localhost:5000/api/health`

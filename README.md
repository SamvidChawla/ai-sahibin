# ♻️ AI-SahiBin

**Smart Waste Classification & Disposal Routing**

AI-SahiBin is an intelligent, edge-optimized web application designed to take the guesswork out of recycling. Snap a photo of your trash, and our AI will classify it, give you specific disposal instructions, and route you to the nearest verified drop-off center using Google Maps.

---

## 🌍 The Problem & Our Solution

### The Issue

Improper waste sorting leads to contaminated recycling streams, environmental hazards (especially with e-waste and batteries), and overflowing landfills. People often *want* to recycle, but they don't know *how* to classify complex items or *where* to take them.

### How We Solve It

1. **Identify** — Users upload an image of their waste. Our custom ML model runs a lightweight CPU inference to identify the specific item (e.g., "PCB", "PET Bottle").
2. **Normalize** — The backend maps specific items to broad categories (e-waste, plastic, organic) and provides actionable, eco-friendly disposal steps.
3. **Locate** — Using the user's geolocation, the app queries Google Maps for the closest specialized recycling center tailored to that specific waste category.

---

## 🛠️ Tech Stack

This project is structured as a **Monorepo**, housing both the frontend and backend in a unified format.

### Frontend (`/frontend`)

| Tool | Purpose |
|---|---|
| React.js (via Vite) | UI Framework |
| Tailwind CSS & Custom CSS Variables | Styling |
| Framer Motion | Animations & micro-interactions |
| `@react-google-maps/api` | Mapping (using modern `useJsApiLoader`) |

### Backend (`/backend`)

| Tool | Purpose |
|---|---|
| Python / FastAPI | Server Framework |
| YOLO (exported to `.onnx`) | ML inference — CPU-optimized, low-RAM edge |
| Google Places API | Nearby recycling center lookup |
| `slowapi` | IP-based rate limiting (DDoS/spam protection) |

---

## 🚀 How to Run Locally

**Prerequisites:** Node.js and Python 3.9+ must be installed. Run the backend and frontend in **two separate terminal windows**.

### 1. Backend Setup

```bash
cd backend
pip install -r requirements.txt
```

Create a `.env` file inside `/backend`:

```env
GOOGLE_PLACES_API_KEY=your_google_maps_api_key_here
```

Start the server:

```bash
uvicorn main:app --reload
```

> Backend runs on **http://localhost:8000**

---

### 2. Frontend Setup

```bash
cd frontend
npm install
```

Create a `.env` file inside `/frontend`:

```env
VITE_GOOGLE_MAPS_API_KEY=your_google_maps_api_key_here
VITE_API_URL=http://localhost:8000
```

Start the client:

```bash
npm run dev
```

> Frontend runs on **http://localhost:5173**

---

## 🛑 Disclaimer

> This is a demonstration prototype built for a hackathon and is not intended for production use.

- **Stateless by design:** The app is Stateless by design. That said, we still recommend not uploading sensitive or personal images.
- **Google Maps / Places API:** Location features are powered by Google Maps. Their own [Terms & Conditions](https://cloud.google.com/maps-platform/terms) and [Privacy Policy](https://policies.google.com/privacy) apply.
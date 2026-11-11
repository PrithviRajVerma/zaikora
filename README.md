# 🍽️ Zaikora – Restaurant & Food Ordering Platform

**A Taste Worth Remembering.**

Zaikora is a modern, full-stack restaurant and food ordering platform built using the MERN stack, TypeScript, and pnpm. It aims to provide customers with a seamless food ordering experience while offering restaurant administrators an intuitive dashboard to manage menus, customers, and orders.

> 🚧 **Project Status:** Under Development

---

## ✨ Features

### 👤 Customer Features
- Browse restaurant food menu.
- Explore food categories.
- Search and filter food items.
- User registration and secure login.
- Add and remove items from the shopping cart.
- Manage item quantities.
- Place food orders.
- Secure online payments using Razorpay.
- View order history and order status.

### 🛠️ Admin Features
- Admin authentication and authorization.
- Interactive admin dashboard.
- Add, update, and delete food items.
- Manage food categories.
- Upload and manage food images.
- View and manage customer orders.
- Update order statuses.
- Monitor restaurant performance and revenue.

### 🔐 Security & Backend
- RESTful API architecture.
- JWT-based authentication.
- Password hashing using bcrypt.
- Role-based access control.
- Protected API routes.
- Secure payment verification.
- MongoDB database integration.

---

## 🧰 Tech Stack

### Frontend
- React.js
- TypeScript
- Vite
- Tailwind CSS
- React Router DOM
- Axios
- Lucide React

### Backend
- Python 3.11+
- FastAPI
- Uvicorn
- Motor (Async MongoDB)
- Pydantic v2 & Pydantic Settings
- Loguru (Structured logging)
- JSON Web Tokens (JWT) / Passlib / Bcrypt

### Tools & Services
- pnpm – Monorepo workspace management
- uv – Fast Python package & environment manager
- Razorpay – Payment gateway
- Cloudinary – Image storage
- Git & GitHub – Version control
- Postman / Swagger UI – API testing

---

## 📁 Project Structure

```text
zaikora/
│
├── frontend/
│   ├── public/
│   └── src/
│       ├── assets/
│       ├── components/
│       ├── context/
│       ├── hooks/
│       ├── pages/
│       ├── services/
│       ├── types/
│       ├── App.tsx
│       ├── main.tsx
│       └── index.css
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── endpoints/
│   │   │       │   └── health.py
│   │   │       └── router.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── database.py
│   │   │   └── logger.py
│   │   ├── middlewares/
│   │   │   └── http_logger.py
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── utils/
│   │   └── main.py
│   ├── tests/
│   ├── pyproject.toml
│   ├── requirements.txt
│   ├── package.json
│   └── README.md
│
├── pnpm-workspace.yaml
├── package.json
├── pnpm-lock.yaml
└── README.md
```

---

## ⚙️ Getting Started

Follow these instructions to set up the project locally.

### Prerequisites

Make sure you have the following installed:

- Node.js (20.19+ or 22.12+)
- pnpm
- Python 3.11+ (and `uv` recommended)
- MongoDB Atlas account or local MongoDB installation
- Git

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/zaikora.git

cd zaikora
```

### 2. Install dependencies

Install all workspace dependencies:

```bash
pnpm install
```

### 3. Configure environment variables

Create `.env` files in the frontend and backend directories.

**Backend – `backend/.env`**

```env
PORT=5000
NODE_ENV=development

CLIENT_URL=http://localhost:5173

MONGO_URI=your_mongodb_connection_string

JWT_SECRET=your_jwt_secret

RAZORPAY_KEY_ID=your_razorpay_key_id
RAZORPAY_KEY_SECRET=your_razorpay_key_secret

CLOUDINARY_CLOUD_NAME=your_cloudinary_cloud_name
CLOUDINARY_API_KEY=your_cloudinary_api_key
CLOUDINARY_API_SECRET=your_cloudinary_api_secret
```

**Frontend – `frontend/.env`**

```env
VITE_API_URL=http://localhost:5000
```

> Never commit actual environment variables or API credentials to GitHub.

### 4. Run the development servers

Start both frontend and backend from the project root:

```bash
pnpm dev
```

Alternatively, run them individually:

**Frontend**

```bash
pnpm dev:frontend
```

**Backend**

```bash
pnpm dev:backend
```

### 5. Access the application

| Service | URL |
|---|---|
| Frontend | http://localhost:5173 |
| Backend API | http://localhost:5000 |

---

## 💳 Payment Integration

Zaikora uses Razorpay for online payment processing.

The planned payment workflow includes:

1. Customer places an order.
2. Backend creates a Razorpay order.
3. Frontend opens the Razorpay checkout.
4. Customer completes payment.
5. Backend verifies the payment signature.
6. Payment status and order details are updated.

Payment verification must happen on the backend. Webhooks will also be used to handle reliable payment status updates.

---

## 🎨 Design Philosophy

Zaikora follows a modern and premium restaurant branding approach.

| Element | Value |
|---|---|
| Primary Color | `#173B35` |
| Background | `#FAF9F6` |
| Accent Color | `#D5B98B` |
| Typography | Playfair Display & Poppins |
| Design Style | Modern, Elegant & Minimal |

---

## 🗺️ Development Roadmap

- [x] Initial project setup
- [x] pnpm workspace configuration
- [x] React + TypeScript setup
- [x] FastAPI + Python setup
- [ ] Responsive homepage
- [ ] Navbar and footer
- [ ] Food menu and category management
- [ ] MongoDB database integration
- [ ] User authentication
- [ ] Food cart functionality
- [ ] Checkout and order placement
- [ ] Razorpay payment integration
- [ ] Admin dashboard
- [ ] Image uploads using Cloudinary
- [ ] Testing and optimization
- [ ] Production deployment

---

## 🔮 Future Enhancements

- Real-time order tracking.
- Customer reviews and ratings.
- Wishlist functionality.
- Email notifications.
- Discount coupons.
- Restaurant analytics.
- Responsive mobile experience.

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome!

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

---

## 👨‍💻 Author

**YOUR NAME**

GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)

---

## 📄 License

This project is currently developed for educational and portfolio purposes.

---

**Zaikora – A Taste Worth Remembering.** 🍽️
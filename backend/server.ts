import express, { type Request, type Response } from "express";
import cors from "cors";
import cookieParser from "cookie-parser";
import dotenv from "dotenv";

import connectDB from "./configs/db.ts";
import logger from "./utils/logger.ts";
import httpLogger from "./middlewares/httpLogger.ts";

dotenv.config();

const app = express();

if (process.env.NODE_ENV === "production") {
  app.set("trust proxy", 1);
}

// CORS configuration
app.use(
  cors({
    origin: process.env.CLIENT_URL || "http://localhost:5173",
    credentials: true,
  }),
);


app.use(express.json({ limit: "10mb" }));
app.use(express.urlencoded({ extended: true, limit: "10mb" }));
app.use(cookieParser());
app.use(httpLogger);

app.get("/api/health", (_req: Request, res: Response) => {
  res.status(200).json({
    success: true,
    message: "Zaikora API is running successfully.",
    environment: process.env.NODE_ENV || "development",
    timestamp: new Date().toISOString(),
  });
});

app.use((_req: Request, res: Response) => {
  res.status(404).json({
    success: false,
    message: "Route not found.",
  });
});

// Global error handler
app.use(
  (
    error: Error & { statusCode?: number },
    _req: Request,
    res: Response,
    _next: express.NextFunction,
  ) => {
    logger.error(
      {
        message: error.message,
        stack:
          process.env.NODE_ENV === "development"
            ? error.stack
            : undefined,
      },
      "Unhandled application error",
    );

    res.status(error.statusCode || 500).json({
      success: false,
      message:
        process.env.NODE_ENV === "production"
          ? "Internal server error."
          : error.message,
    });
  },
);

// Start server after connecting to MongoDB
const startServer = async (): Promise<void> => {
  try {
    await connectDB();

    const PORT = Number(process.env.PORT) || 5000;

    const server = app.listen(PORT, () => {
      logger.info(
        {
          port: PORT,
          environment: process.env.NODE_ENV || "development",
        },
        `Zaikora API server running on port ${PORT}`,
      );
    });



    const shutdown = (signal: string): void => {
      logger.info(`${signal} received. Shutting down server...`);

      server.close(() => {
        logger.info("HTTP server closed.");
        process.exit(0);
      });

      setTimeout(() => {
        logger.error("Graceful shutdown timed out.");
        process.exit(1);
      }, 10_000).unref();
    };

    process.on("SIGTERM", () => shutdown("SIGTERM"));
    process.on("SIGINT", () => shutdown("SIGINT"));
  } catch (error) {
    logger.fatal({ error }, "Failed to start Zaikora server.");
    process.exit(1);
  }
};

void startServer();
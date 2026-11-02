import dotenv from "dotenv";

dotenv.config();

const requiredEnvVariables = [ 
    "MONGO_URI",
    "JWT_SECRET"
]

for(const key of requiredEnvVariables){
    if(!process.env[key]){
        throw new Error( `Missing required envirnoment variable : ${key}`);
    }
}

export const env = {
  PORT: Number(process.env.PORT) || 5000,
  MONGO_URI: process.env.MONGO_URI!,
  JWT_SECRET: process.env.JWT_SECRET!,
  CLIENT_URL: process.env.CLIENT_URL || "http://localhost:5173",
};


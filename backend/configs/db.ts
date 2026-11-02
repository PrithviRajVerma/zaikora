import mongoose, { connection } from "mongoose";
import {env} from "./env.ts";
 
const connectDB = async () : Promise<void> => {

    try {
        const connection = await mongoose.connect(
            env.MONGO_URI
        );

        console.log(
            `MongoDB connect: ${connection.connection.host}`
        )
    } catch (error){
        console.error("MongoDB connection failed:", error);
        throw error;
        
    }

}

export default connectDB;

import morgan from "morgan";
import logger from "../utils/logger.ts";

const httpLogger = morgan("combined", {
  stream: {
    write: (message: string) => {
      logger.info(
        { context: "HTTP" },
        message.trim()
      );
    },
  },
});

export default httpLogger;

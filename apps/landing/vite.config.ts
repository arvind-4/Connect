import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  build: {
    cssCodeSplit: false,
    rollupOptions: {
      output: {
        dir: "dist",
        entryFileNames: "index.min.js",
        chunkFileNames: "[name].min.js",
        manualChunks: (id) => {
          if (id.includes("node_modules")) {
            return "vendor";
          }
        },
        assetFileNames: (assetInfo) => {
          if (assetInfo.name?.endsWith(".css")) {
            return "index.min.css";
          }
          return "[name][extname]";
        },
      },
    },
  },
});

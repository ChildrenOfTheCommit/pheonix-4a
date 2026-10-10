import vue from '@vitejs/plugin-vue'
import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'
import VueDevtools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({ //
  plugins: [
    vue(),
    tailwindcss(),
    VueDevtools(),
  ],
})

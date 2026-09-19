import { createApp } from 'vue'
import '@/index.css'


// @ts-expect-error Vue files are resolved by the Vite plugin at build time.
import App from './App.vue'

const app = createApp(App)

app.mount('#app')

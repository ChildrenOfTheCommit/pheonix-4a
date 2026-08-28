import '@/index.css'
import 'boxicons/css/boxicons.min.css'

import {createApp} from 'vue'
import {createPinia} from 'pinia'

import App from '@/App.vue'

const app = createApp(App)
app.use(createPinia())

app.mount('#app')

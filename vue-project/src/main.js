import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import axios from 'axios'

const instance =axios.create({
    baseURL:"http://192.168.25.27",
    timeout:1000,
});
const app = createApp(App)

app.use(router)
app.config.globalProperties.$axios = axios; 
app.mount('#app')

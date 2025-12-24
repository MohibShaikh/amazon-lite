import { createApp } from 'vue'
import App from './App.vue'
import Face from './components/Face.vue'


const app = createApp(App)
app.component('Face', Face)

app.mount('#app')

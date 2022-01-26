// import 'vite/modulepreload-polyfill'

import { createApp } from 'vue'
import Aos from 'aos'
import 'aos/dist/aos.css';
import Home from '../views/Home.vue'

import { Quasar } from 'quasar'
import quasarUserOptions from './quasar-user-options'

Aos.init()


createApp(Home).use(Quasar, quasarUserOptions).mount('#app')
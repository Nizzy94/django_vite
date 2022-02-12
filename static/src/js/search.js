// import 'vite/modulepreload-polyfill'

import { createApp } from 'vue'
import Aos from 'aos'
import 'aos/dist/aos.css';
import Search from '../views/Search.vue'

import { Quasar } from 'quasar'
import quasarUserOptions from './quasar-user-options'

Aos.init()


createApp(Search).use(Quasar, quasarUserOptions).mount('#app')
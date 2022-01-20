// import 'vite/modulepreload-polyfill'

import { createApp } from 'vue'
import Home from '../views/Home.vue'

import { Quasar } from 'quasar'
import quasarUserOptions from './quasar-user-options'

// Import Quasar css
// import 'quasar/src/css/index.sass'


createApp(Home).use(Quasar, quasarUserOptions).mount('#app')
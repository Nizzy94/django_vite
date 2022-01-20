import { createApp } from 'vue'
import About from '../views/About.vue'

import { Quasar } from 'quasar'
import quasarUserOptions from './quasar-user-options'


createApp(About).use(Quasar, quasarUserOptions).mount('#app')
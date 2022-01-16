import { createApp } from 'vue'
import Home from '../views/About.vue'

import { Quasar } from 'quasar'
import quasarUserOptions from './quasar-user-options'


createApp(Home).use(Quasar, quasarUserOptions).mount('#app')
import { createApp } from 'vue'
import Contact from '../views/Contact.vue'

import { Quasar } from 'quasar'
import quasarUserOptions from './quasar-user-options'


createApp(Contact).use(Quasar, quasarUserOptions).mount('#app')
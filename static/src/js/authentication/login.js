import { createApp } from 'vue'
import Auth from '../../views/authentication/Auth.vue'

import { Quasar } from 'quasar'
import quasarUserOptions from '../quasar-user-options'


createApp(Auth).use(Quasar, quasarUserOptions).mount('#app')
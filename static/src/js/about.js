import { createApp } from 'vue'
import Aos from 'aos'
import 'aos/dist/aos.css';
import About from '../views/About.vue'

import { Quasar } from 'quasar'
import quasarUserOptions from './quasar-user-options'


Aos.init()


createApp(About).use(Quasar, quasarUserOptions).mount('#app')
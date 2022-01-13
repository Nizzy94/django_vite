import { createApp } from 'vue'
import About from '../views/About.vue'


import { Quasar } from 'quasar'
import quasarUserOptions from '../../../src/quasar-user-options'

// Import Quasar css
// import 'quasar/src/css/index.sass'

createApp(About).use(Quasar, quasarUserOptions).mount('#app')
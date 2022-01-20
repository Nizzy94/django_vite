import { createApp } from 'vue'
import BlogDetail from '../../views/blog/BlogDetail.vue'

import { Quasar } from 'quasar'
import quasarUserOptions from '../quasar-user-options'


createApp(BlogDetail).use(Quasar, quasarUserOptions).mount('#app')
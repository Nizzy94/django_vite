import { createApp } from 'vue'
import Blog from '../../views/blog/Blog.vue'

import { Quasar } from 'quasar'
import quasarUserOptions from '../quasar-user-options'


createApp(Blog).use(Quasar, quasarUserOptions).mount('#app')
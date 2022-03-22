import { createApp, ref } from 'vue'
import Blog from '../../views/blog/Blog.vue'

import { Quasar, Notify } from 'quasar'
import quasarUserOptions from '../quasar-user-options'


const app = document.getElementById('app')


const userIsAuthenticated = ref(false)

if (app.dataset.userIsAuthenticated == 'True') {
    userIsAuthenticated.value = true
}

createApp(Blog).provide('user_is_authenticated', userIsAuthenticated.value)
    .use(Quasar, {
            plugins: {
                Notify
            },
        },
        quasarUserOptions).mount(app)
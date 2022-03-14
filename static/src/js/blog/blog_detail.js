import { createApp, ref } from 'vue'
import BlogDetail from '../../views/blog/BlogDetail.vue'

import { Quasar, Notify } from 'quasar'
import quasarUserOptions from '../quasar-user-options'

import 'animate.css';




const app = document.getElementById('app')


const userIsAuthenticated = ref(false)

if (app.dataset.userIsAuthenticated == 'True') {
    userIsAuthenticated.value = true
}

createApp(BlogDetail).provide('user_is_authenticated', userIsAuthenticated.value)
    .use(Quasar, {
        plugins: {
            Notify
        },
    }, quasarUserOptions).mount(app)
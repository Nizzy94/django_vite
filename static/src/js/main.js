// import 'vite/modulepreload-polyfill'

import { createApp, ref } from 'vue'
import Aos from 'aos'
import 'aos/dist/aos.css';
import Home from '../views/Home.vue'

import { Quasar, Meta } from 'quasar'
import quasarUserOptions from './quasar-user-options'

const app = document.getElementById('app')


const userIsAuthenticated = ref(false)

if (app.dataset.userIsAuthenticated == 'True') {
    userIsAuthenticated.value = true
}


Aos.init()


createApp(Home).provide('user_is_authenticated', userIsAuthenticated.value)
    .use(Quasar, quasarUserOptions, {
        plugins: {
            Meta
        }
    }).mount(app)
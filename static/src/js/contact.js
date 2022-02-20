import { createApp, ref } from 'vue'
import Contact from '../views/Contact.vue'

import { Quasar } from 'quasar'
import quasarUserOptions from './quasar-user-options'


const app = document.getElementById('app')


const userIsAuthenticated = ref(false)

if (app.dataset.userIsAuthenticated == 'True') {
    userIsAuthenticated.value = true
}

createApp(Contact).provide('user_is_authenticated', userIsAuthenticated.value)
    .use(Quasar, quasarUserOptions).mount(app)
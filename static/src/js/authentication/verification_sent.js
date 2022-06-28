import { createApp, ref } from 'vue'
// import Auth from '../../views/authentication/Auth.vue'
import EmailConfirm from '../../views/authentication/VerificationSent.vue'

import { Quasar } from 'quasar'
import quasarUserOptions from '../quasar-user-options'


const app = document.getElementById('app')


const userIsAuthenticated = ref(false)


const messages = app.dataset.messages ? JSON.parse(app.dataset.messages) : ''

if (app.dataset.userIsAuthenticated == 'True') {
    userIsAuthenticated.value = true
}

createApp(EmailConfirm)
    .provide('user_is_authenticated', userIsAuthenticated.value)
    .provide('messages', messages)
    .use(Quasar, quasarUserOptions).mount(app)
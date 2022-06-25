import { createApp, ref } from 'vue'
// import Auth from '../../views/authentication/Auth.vue'
import EmailConfirm from '../../views/authentication/EmailConfirm.vue'

import { Quasar } from 'quasar'
import quasarUserOptions from '../quasar-user-options'


const app = document.getElementById('app')


const userIsAuthenticated = ref(false)

// console.log(app.dataset.confirmation)

const formErrors = app.dataset.formErrors ? JSON.parse(app.dataset.formErrors) : ''
const oldFormData = app.dataset.oldFormData ? JSON.parse(app.dataset.oldFormData) : ''
const messages = app.dataset.messages ? JSON.parse(app.dataset.messages) : ''
const confirmation = app.dataset.confirmation ? JSON.parse(app.dataset.confirmation) : ''

// console.log(oldFormData)
// console.log(emails)
// console.log(formErrors)
// console.log(messages)
// console.log(confirmation)

if (app.dataset.userIsAuthenticated == 'True') {
    userIsAuthenticated.value = true
}

createApp(EmailConfirm)
    .provide('user_is_authenticated', userIsAuthenticated.value)
    .provide('old_form_data', oldFormData)
    .provide('form_errors', formErrors)
    .provide('messages', messages)
    .provide('confirmation', confirmation)
    .use(Quasar, quasarUserOptions).mount(app)
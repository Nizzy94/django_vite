import { createApp, ref } from 'vue'
// import Auth from '../../views/authentication/Auth.vue'
import AccountEmail from '../../views/authentication/AccountEmail.vue'

import { Quasar } from 'quasar'
import quasarUserOptions from '../quasar-user-options'


const app = document.getElementById('app')


const userIsAuthenticated = ref(false)

// console.log(app.dataset.messages)

const formErrors = app.dataset.formErrors ? JSON.parse(app.dataset.formErrors) : ''
const oldFormData = app.dataset.oldFormData ? JSON.parse(app.dataset.oldFormData) : ''
const emails = app.dataset.emails ? JSON.parse(app.dataset.emails) : ''
const messages = app.dataset.messages ? JSON.parse(app.dataset.messages) : ''

// console.log(oldFormData)
console.log(emails)
    // console.log(formErrors)
console.log(messages)

if (app.dataset.userIsAuthenticated == 'True') {
    userIsAuthenticated.value = true
}

createApp(AccountEmail)
    .provide('user_is_authenticated', userIsAuthenticated.value)
    .provide('old_form_data', oldFormData)
    .provide('form_errors', formErrors)
    .provide('emails', emails)
    .provide('messages', messages)
    .use(Quasar, quasarUserOptions).mount(app)
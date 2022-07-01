import { createApp, ref } from 'vue'
// import Auth from '../../views/authentication/Auth.vue'
import Connections from '../../views/authentication/Connections.vue'

import { Quasar } from 'quasar'
import quasarUserOptions from '../quasar-user-options'


const app = document.getElementById('app')


const userIsAuthenticated = ref(false)

console.log(JSON.parse(app.dataset.providers))

const formErrors = app.dataset.formErrors ? JSON.parse(app.dataset.formErrors) : ''
const oldFormData = app.dataset.oldFormData ? JSON.parse(app.dataset.oldFormData) : ''
const messages = app.dataset.messages ? JSON.parse(app.dataset.messages) : ''
const formAccount = app.dataset.formAccount.toLowerCase() == 'true' ? true : false
const providers = app.dataset.providers ? JSON.parse(app.dataset.providers) : ''

// console.log(oldFormData)
// console.log(emails)
// console.log(formErrors)
// console.log(messages)
// console.log(confirmation)

if (app.dataset.userIsAuthenticated == 'True') {
    userIsAuthenticated.value = true
}

createApp(Connections)
    .provide('user_is_authenticated', userIsAuthenticated.value)
    .provide('old_form_data', oldFormData)
    .provide('form_errors', formErrors)
    .provide('messages', messages)
    .provide('form_account', formAccount)
    .provide('providers', providers)
    .use(Quasar, quasarUserOptions).mount(app)
import { createApp, ref } from 'vue'
// import Auth from '../../views/authentication/Auth.vue'
import ConnectAccount from '../../views/authentication/ConnectAccount.vue'

import { Quasar } from 'quasar'
import quasarUserOptions from '../quasar-user-options'


const app = document.getElementById('app')


const userIsAuthenticated = ref(false)

console.log(app.dataset.provider)

const formErrors = app.dataset.formErrors ? JSON.parse(app.dataset.formErrors) : ''
const oldFormData = app.dataset.oldFormData ? JSON.parse(app.dataset.oldFormData) : ''
const messages = app.dataset.messages ? JSON.parse(app.dataset.messages) : ''
    // const formAccount = app.dataset.formAccount.toLowerCase() == 'true' ? true : false
const provider = app.dataset.provider

// console.log(oldFormData)
// console.log(emails)
// console.log(formErrors)
console.log(messages)
    // console.log(confirmation)

if (app.dataset.userIsAuthenticated == 'True') {
    userIsAuthenticated.value = true
}

createApp(ConnectAccount)
    .provide('user_is_authenticated', userIsAuthenticated.value)
    .provide('old_form_data', oldFormData)
    .provide('form_errors', formErrors)
    .provide('messages', messages)
    // .provide('form_account', formAccount)
    .provide('provider', provider)
    .use(Quasar, quasarUserOptions).mount(app)
import { createApp, ref } from 'vue'
// import Auth from '../../views/authentication/Auth.vue'
import Logout from '../../views/authentication/Logout.vue'

import { Quasar } from 'quasar'
import quasarUserOptions from '../quasar-user-options'


const app = document.getElementById('app')


const userIsAuthenticated = ref(false)

// console.log(app.dataset.confirmation)

const formErrors = app.dataset.formErrors ? JSON.parse(app.dataset.formErrors) : ''
const oldFormData = app.dataset.oldFormData ? JSON.parse(app.dataset.oldFormData) : ''
const messages = app.dataset.messages ? JSON.parse(app.dataset.messages) : ''
const redirectField = app.dataset.redirectField ? JSON.parse(app.dataset.redirectField) : ''

// console.log(oldFormData)
// console.log(emails)
// console.log(formErrors)
console.log(messages)
    // console.log(confirmation)
console.log(redirectField)

if (app.dataset.userIsAuthenticated == 'True') {
    userIsAuthenticated.value = true
}

createApp(Logout)
    .provide('user_is_authenticated', userIsAuthenticated.value)
    .provide('old_form_data', oldFormData)
    .provide('form_errors', formErrors)
    .provide('messages', messages)
    .provide('redirect_field', redirectField)
    .use(Quasar, quasarUserOptions).mount(app)
import { createApp, ref } from 'vue'
import PasswordResetFromKey from '../../views/authentication/PasswordResetFromKey.vue'

import { Quasar } from 'quasar'
import quasarUserOptions from '../quasar-user-options'


const app = document.getElementById('app')


const userIsAuthenticated = ref(false)

// console.log(app.dataset.confirmation)

const formErrors = app.dataset.formErrors ? JSON.parse(app.dataset.formErrors) : ''
const oldFormData = app.dataset.oldFormData ? JSON.parse(app.dataset.oldFormData) : ''
const messages = app.dataset.messages ? JSON.parse(app.dataset.messages) : ''
const tokenFail = app.dataset.tokenFail || false
const actionUrl = app.dataset.actionUrl || ''


// console.log(oldFormData)
// console.log(emails)
// console.log(formErrors)
// console.log(messages)
// console.log(confirmation)

if (app.dataset.userIsAuthenticated == 'True') {
    userIsAuthenticated.value = true
}

createApp(PasswordResetFromKey)
    .provide('user_is_authenticated', userIsAuthenticated.value)
    .provide('old_form_data', oldFormData)
    .provide('form_errors', formErrors)
    .provide('messages', messages)
    .provide('token_fail', tokenFail)
    .provide('action_url', actionUrl)
    .use(Quasar, quasarUserOptions).mount(app)
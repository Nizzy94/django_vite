import { createApp, ref } from 'vue'
// import Auth from '../../views/authentication/Auth.vue'
import Login from '../../views/authentication/Login.vue'

import { Quasar } from 'quasar'
import quasarUserOptions from '../quasar-user-options'


const app = document.getElementById('app')

const userIsAuthenticated = ref(false)

const formErrors = JSON.parse(app.dataset.formErrors)
const oldFormData = JSON.parse(app.dataset.oldFormData)

if (app.dataset.userIsAuthenticated == 'True') {
    userIsAuthenticated.value = true
}

createApp(Login)
    .provide('user_is_authenticated', userIsAuthenticated.value)
    .provide('old_form_data', oldFormData)
    .provide('form_errors', formErrors)
    .use(Quasar, quasarUserOptions).mount(app)
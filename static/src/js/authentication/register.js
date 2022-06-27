import { createApp, ref } from 'vue'
// import Auth from '../../views/authentication/Auth.vue'
import Register from '../../views/authentication/Register.vue'

import { Quasar } from 'quasar'
import quasarUserOptions from '../quasar-user-options'
import vue3GoogleLogin from 'vue3-google-login'


const app = document.getElementById('app')


const userIsAuthenticated = ref(false)
const formErrors = JSON.parse(app.dataset.formErrors)
const oldFormData = JSON.parse(app.dataset.oldFormData)

// console.log(oldFormData)
// console.log(formErrors)

if (app.dataset.userIsAuthenticated == 'True') {
    userIsAuthenticated.value = true
}

createApp(Register)
    .provide('user_is_authenticated', userIsAuthenticated.value)
    .provide('old_form_data', oldFormData)
    .provide('form_errors', formErrors)
    .use(vue3GoogleLogin, {
        clientId: import.meta.env.VITE_GOOGLE_AUTH_KEY
    })
    .use(Quasar, quasarUserOptions).mount(app)
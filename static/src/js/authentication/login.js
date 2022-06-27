import { createApp, ref } from 'vue'
// import Auth from '../../views/authentication/Auth.vue'
import Login from '../../views/authentication/Login.vue'

import { Quasar } from 'quasar'
import quasarUserOptions from '../quasar-user-options'
import vue3GoogleLogin from 'vue3-google-login'

const app = document.getElementById('app')

const userIsAuthenticated = ref(false)

const formErrors = JSON.parse(app.dataset.formErrors)
const oldFormData = JSON.parse(app.dataset.oldFormData)

if (app.dataset.userIsAuthenticated == 'True') {
    userIsAuthenticated.value = true
}

const vue3GoogleLoginOptions = {
    clientId: import.meta.env.VITE_GOOGLE_AUTH_KEY,
    // prompt: "concent",
    buttonConfig: {
        theme: "filled_blue",
        text: "continue_with",
    },
    popupType: "token",
    // ux_mode: "redirect",
}
createApp(Login)
    .provide('user_is_authenticated', userIsAuthenticated.value)
    .provide('old_form_data', oldFormData)
    .provide('form_errors', formErrors)
    .use(vue3GoogleLogin, vue3GoogleLoginOptions)
    .use(Quasar, quasarUserOptions).mount(app)
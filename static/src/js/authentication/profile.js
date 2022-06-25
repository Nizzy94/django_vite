import { createApp, ref } from 'vue'
// import Auth from '../../views/authentication/Auth.vue'
import Profile from '../../views/authentication/Profile.vue'

import { Quasar } from 'quasar'
import quasarUserOptions from '../quasar-user-options'


const app = document.getElementById('app')


const userIsAuthenticated = ref(false)

const formErrors = app.dataset.formErrors ? JSON.parse(app.dataset.formErrors) : ''
const oldFormData = app.dataset.oldFormData ? JSON.parse(app.dataset.oldFormData) : ''

// console.log(oldFormData)
// console.log(formErrors)

if (app.dataset.userIsAuthenticated == 'True') {
    userIsAuthenticated.value = true
}

createApp(Profile)
    .provide('user_is_authenticated', userIsAuthenticated.value)
    .provide('old_form_data', oldFormData)
    .provide('form_errors', formErrors)
    .use(Quasar, quasarUserOptions).mount(app)
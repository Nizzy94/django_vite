import { createApp, ref } from 'vue'
// import Auth from '../../views/authentication/Auth.vue'
import Login from '../../views/authentication/Login.vue'

import { Quasar } from 'quasar'
import quasarUserOptions from '../quasar-user-options'



const userIsAuthenticated = ref(false)

if (app.dataset.userIsAuthenticated == 'True') {
    userIsAuthenticated.value = true
}

createApp(Login)
    .provide('user_is_authenticated', userIsAuthenticated.value)
    .use(Quasar, quasarUserOptions).mount('#app')
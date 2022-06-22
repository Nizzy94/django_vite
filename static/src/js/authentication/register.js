import { createApp, ref } from 'vue'
// import Auth from '../../views/authentication/Auth.vue'
import Register from '../../views/authentication/Register.vue'

import { Quasar } from 'quasar'
import quasarUserOptions from '../quasar-user-options'



const userIsAuthenticated = ref(false)

if (app.dataset.userIsAuthenticated == 'True') {
    userIsAuthenticated.value = true
}

createApp(Register)
    .provide('user_is_authenticated', userIsAuthenticated.value)
    .use(Quasar, quasarUserOptions).mount('#app')
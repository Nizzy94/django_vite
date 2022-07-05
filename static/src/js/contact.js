import { createApp, ref } from 'vue'
import Contact from '../views/Contact.vue'

import { Quasar } from 'quasar'
import quasarUserOptions from './quasar-user-options'
// import getAuthUser from '../composables/getAuthUser'


const app = document.getElementById('app')

// const { callAuthUser } = getAuthUser()



const userIsAuthenticated = ref(false)


if (app.dataset.userIsAuthenticated == 'True') {
    userIsAuthenticated.value = true
}

// if (userIsAuthenticated.value) {
//     user.value = await callAuthUser()
// }

createApp(Contact).provide('user_is_authenticated', userIsAuthenticated.value)

.use(Quasar, quasarUserOptions).mount(app)
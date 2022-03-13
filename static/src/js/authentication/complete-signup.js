import { createApp, ref } from 'vue'
import Aos from 'aos'
import 'aos/dist/aos.css';
import CompleteSignup from '../../views/authentication/CompleteSignup.vue'

import { Quasar } from 'quasar'
import quasarUserOptions from '../quasar-user-options'


Aos.init()


const app = document.getElementById('app')


const userIsAuthenticated = ref(false)

if (app.dataset.userIsAuthenticated == 'True') {
    userIsAuthenticated.value = true
}

createApp(CompleteSignup).provide('user_is_authenticated', userIsAuthenticated.value)
    .use(Quasar, quasarUserOptions).mount(app)
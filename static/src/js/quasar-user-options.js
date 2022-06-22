// import '../css/quasar.scss'
import 'quasar/src/css/index.sass'
import { Loading, QSpinnerPie, Cookies } from 'quasar'


// Import icon libraries
// import '@quasar/extras/material-icons/material-icons.css'
// import '@quasar/extras/material-icons-outlined/material-icons-outlined.css'
// import '@quasar/extras/material-icons-round/material-icons-round.css'
// import '@quasar/extras/material-icons-sharp/material-icons-sharp.css'
// import '@quasar/extras/mdi-v6/mdi-v6.css'
// import '@quasar/extras/ionicons-v4/ionicons-v4.css'


export default {
    plugins: {
        Loading,
        Cookies
    }, // import Quasar plugins and add here

    config: {
        // brand: {
        //   // primary: '#e46262',
        //   // ... or all other brand colors
        // },
        // notify: {...}, // default set of options for Notify Quasar plugin
        loading: {
            spinnerSize: 60,
            spinnerColor: 'primary',
            spinner: QSpinnerPie,
            backgroundColor: 'white'
        }, // default set of options for Loading Quasar plugin
        // loadingBar: { ... }, // settings for LoadingBar Quasar plugin
        // ..and many more (check Installation card on each Quasar component/directive/plugin)
    }

}
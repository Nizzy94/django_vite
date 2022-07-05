import vue from '@vitejs/plugin-vue'
import { quasar, transformAssetUrls } from '@quasar/vite-plugin'

const { resolve } = require('path');

module.exports = {
    plugins: [
        vue({
            template: { transformAssetUrls }
        }),
        quasar({
            sassVariables: './static/src/css/quasar.variables.scss'
        })
    ],
    root: resolve(__dirname, './static/src/'),
    // root: './static/src',
    base: '/static/',
    // server: {
    //     host: 'localhost',
    //     port: 3000,
    //     open: false,
    //     watch: {
    //         usePolling: true,
    //         disableGlobbing: false,
    //     },
    // },
    resolve: {
        extensions: ['.js', '.json'],
    },
    build: {
        outDir: resolve('./static/dist'),
        assetsDir: '',
        manifest: true,
        emptyOutDir: true,
        target: 'es2015',
        rollupOptions: {
            input: {
                // third party
                // home: resolve('./static/src/js/main.js'),

                // main
                home: resolve('./static/src/js/main.js'),
                about: resolve('./static/src/js/about.js'),
                contact: resolve('./static/src/js/contact.js'),
                search: resolve('./static/src/js/search.js'),

                // blog
                blog: resolve('./static/src/js/blog/blog.js'),
                blog_detail: resolve('./static/src/js/blog/blog_detail.js'),

                // auth
                account_email: resolve('./static/src/js/authentication/account_email.js'),
                complete_signup: resolve('./static/src/js/authentication/complete_signup.js'),
                connect_social_account: resolve('./static/src/js/authentication/connect_social_account.js'),
                connections: resolve('./static/src/js/authentication/connections.js'),
                email_confirm: resolve('./static/src/js/authentication/email_confirm.js'),
                login: resolve('./static/src/js/authentication/login.js'),
                logout: resolve('./static/src/js/authentication/logout.js'),
                password_change: resolve('./static/src/js/authentication/password_change.js'),
                password_reset_done: resolve('./static/src/js/authentication/password_reset_done.js'),
                password_reset_from_key_done: resolve('./static/src/js/authentication/password_reset_from_key_done.js'),
                password_reset_from_key: resolve('./static/src/js/authentication/password_reset_from_key.js'),
                password_reset: resolve('./static/src/js/authentication/password_reset.js'),
                password_set: resolve('./static/src/js/authentication/password_set.js'),
                profile: resolve('./static/src/js/authentication/profile.js'),
                register: resolve('./static/src/js/authentication/register.js'),
                verification_sent: resolve('./static/src/js/authentication/verification_sent.js'),
            },
            output: {
                chunkFileNames: undefined,
            },
        },
    },
};
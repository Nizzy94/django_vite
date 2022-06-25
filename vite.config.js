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
                home: resolve('./static/src/js/main.js'),
                about: resolve('./static/src/js/about.js'),
                contact: resolve('./static/src/js/contact.js'),
                search: resolve('./static/src/js/search.js'),

                // blog
                blog: resolve('./static/src/js/blog/blog.js'),
                blog_degails: resolve('./static/src/js/blog/blog_degails.js'),

                // auth
                login: resolve('./static/src/js/authentication/login.js'),
                register: resolve('./static/src/js/authentication/register.js'),
                profile: resolve('./static/src/js/authentication/profile.js'),
                account_email: resolve('./static/src/js/authentication/account_email.js'),
            },
            output: {
                chunkFileNames: undefined,
            },
        },
    },
};
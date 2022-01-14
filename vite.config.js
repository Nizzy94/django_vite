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
    root: resolve(__dirname, './static/src'),
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
            },
            output: {
                chunkFileNames: undefined,
            },
        },
    },
};
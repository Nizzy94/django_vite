import axios from 'axios'
import { Cookies } from 'quasar'


const domain = 'https://django-vite-blog.herokuapp.com'
    // const domain =
    //     import.meta.env.VITE_WEBSITE_ORIGIN

axios.defaults.baseURL = window.location.origin
axios.defaults.headers = {
    'Host': import.meta.env.VITE_WEBSITE_ORIGIN
}

const axiosExternal = axios.create({
    baseURL: domain,
    timeout: 50000,
    headers: {
        'X-CSRFToken': Cookies.get('csrftoken')
    },
    withCredentials: true
})
const fetchWithCredentials = axios.create({
    baseURL: `${ domain }/api`,
    timeout: 50000,
    headers: {
        'X-CSRFToken': Cookies.get('csrftoken')
    },
    withCredentials: true
})
const fetchUserWithCredentials = axios.create({
    baseURL: `${domain}/auth/api`,
    timeout: 50000,
    headers: {
        'X-CSRFToken': Cookies.get('csrftoken')
    },
    withCredentials: true
})

const fetchAllowAny = axios.create({
    baseURL: `/api`,
    timeout: 50000,
    headers: {
        'X-CSRFToken': Cookies.get('csrftoken'),
        "Content-Type": "Application/json",
    },
})

const fetchBlogAllowAny = axios.create({
    baseURL: `${domain}/blog/api`,
    timeout: 50000,
    headers: {
        'X-CSRFToken': Cookies.get('csrftoken'),
        "Content-Type": "Application/json",
    },
})
const fetchBlogWithCredentials = axios.create({
    baseURL: `${domain}/blog/api`,
    timeout: 50000,
    headers: {
        'X-CSRFToken': Cookies.get('csrftoken'),
        "Content-Type": "Application/json",
    },
    withCredentials: true
})

const fetchSearchAllowAny = axios.create({
    baseURL: `${domain}/search/api/query`,
    timeout: 50000,
    headers: {
        'X-CSRFToken': Cookies.get('csrftoken'),
        "Content-Type": "Application/json",
    },
})


export {
    axiosExternal,
    fetchWithCredentials,
    fetchAllowAny,
    fetchBlogAllowAny,
    fetchSearchAllowAny,
    fetchBlogWithCredentials,
    fetchUserWithCredentials
}
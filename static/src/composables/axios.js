import axios from 'axios'
import { Cookies } from 'quasar'


const domain = 'http://localhost:8000'

const fetchWithCredentials = axios.create({
    baseURL: `${domain}/api`,
    timeout: 50000,
    headers: {
        'X-CSRFToken': Cookies.get('csrftoken')
    },
    withCredentials: true
})

const fetchAllowAny = axios.create({
    baseURL: `${domain}/api`,
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


export { fetchWithCredentials, fetchAllowAny, fetchBlogAllowAny }
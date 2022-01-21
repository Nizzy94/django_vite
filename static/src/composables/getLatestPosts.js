import { ref } from "vue"
import { fetchBlogAllowAny } from "./axios"

const getLatestPosts = () => {
    const latest_p = ref([])
    const callLatestPosts = async() => {
        const res = await fetchBlogAllowAny.get('/get-latest-posts/')

        if (res.status == 200) {
            latest_p.value = res.data

            console.log(latest_p)
                // latest_p.value = await res.data
        } else {
            console.log(res.value)
        }
    }

    return { callLatestPosts, latest_p }
}

export default getLatestPosts
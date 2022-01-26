import { ref } from "vue"
import { fetchBlogAllowAny } from "./axios"

const getPostDetail = () => {
    const post = ref({})
    const callPostDetail = async() => {

        try {

            const pathArray = window.location.pathname.slice(1, -1).split("/")

            const post_slug = pathArray.pop()

            const res = await fetchBlogAllowAny.get(`/get-post-detail/${post_slug}/`)

            console.log(res)
            post.value = await res.data
        } catch (e) {
            console.log(e.response)
        }




    }

    return { callPostDetail, post }
}

export default getPostDetail
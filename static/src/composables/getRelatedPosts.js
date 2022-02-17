import { ref } from "vue"
import { fetchBlogAllowAny } from "./axios"

const getRelatedPosts = () => {
    const related = ref([])
    const callRelatedPosts = async() => {
        // const res = await fetchBlogAllowAny.get(`/get-blog-by-tag/${tag.value}/`)

        const pathArray = window.location.pathname.slice(1, -1).split("/")

        const blogSlug = pathArray[2]

        try {
            const res = await fetchBlogAllowAny.get(`/get-releted-posts-by-tag/${blogSlug}/`)

            // console.log(res)
            related.value = await res.data

        } catch (e) {
            console.log(e.response)
        }

    }
    return { callRelatedPosts, related }
}

export default getRelatedPosts
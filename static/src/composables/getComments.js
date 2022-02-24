import { ref } from "vue"
import { fetchBlogAllowAny } from "./axios"

const getComments = () => {
    const comments = ref([])
    const callComments = async(id) => {
        const res = await fetchBlogAllowAny.get(`/get-comments/${id}/`)

        console.log(res)
        comments.value = res.data
    }

    return { callComments, comments }
}

export default getComments
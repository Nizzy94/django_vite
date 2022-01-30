import { ref } from "vue"
import { fetchBlogAllowAny } from "./axios"

const getCategories = () => {
    const categories = ref([])
    const callCategories = async() => {
        try {
            const res = await fetchBlogAllowAny.get('/get-all-categories/')

            console.log(res.data)

            categories.value = await res.data
        } catch (e) {
            console.log(e.response)
        }
    }

    return { callCategories, categories }
}

export default getCategories
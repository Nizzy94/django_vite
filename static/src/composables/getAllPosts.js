import { ref } from "vue"
import { fetchBlogAllowAny } from "./axios"

const getAllPosts = () => {

    const blogs = ref([])

    const callAllPosts = async() => {
        const category = ref("")

        const pathArray = window.location.pathname.slice(1, -1).split("/")

        if (pathArray.length >= 2) {
            category.value = pathArray[1]
        } else {
            category.value = 'all'
        }
        const res = await fetchBlogAllowAny.get(`/get-blog-by-category/${category.value}/`)

        // console.log(res.data)

        blogs.value = res.data

    }
    return { callAllPosts, blogs }
}


export default getAllPosts
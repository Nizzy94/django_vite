import { ref } from "vue"
import { fetchBlogAllowAny } from "./axios"

const getAllPosts = () => {

    const blogs = ref([])

    const callAllPosts = async() => {
        const category = ref("")
        const tag = ref("")

        const pathArray = window.location.pathname.slice(1, -1).split("/")

        console.log(pathArray)
        if (pathArray.length >= 2) {
            if (pathArray[1] == 'tag') {
                console.log('tag')
                tag.value = pathArray[2]
            } else {

                category.value = pathArray[1]
            }
        } else {
            category.value = 'all'
        }
        const res = tag.value == "" ? await fetchBlogAllowAny.get(`/get-blog-by-category/${category.value}/`) : await fetchBlogAllowAny.get(`/get-blog-by-tag/${tag.value}/`)

        // console.log(res.data)

        blogs.value = res.data

    }
    return { callAllPosts, blogs }
}


export default getAllPosts
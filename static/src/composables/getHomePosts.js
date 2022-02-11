import { ref } from "vue"
import { fetchBlogAllowAny } from "./axios"

const getHomePosts = () => {
    const latest = ref([])
    const cats = ref([])
    const news_section = ref([])
        // const cat1_blogs = ref([])
        // const cat2_blogs = ref([])

    const callHomePosts = async() => {
        const res = await fetchBlogAllowAny.get('/get-home-posts/')

        console.log(res.data)


        // console.log(JSON.parse(res.data))

        const home_posts = res.data
            // const home_posts = JSON.parse(res.data)

        if (res.status == 200) {
            latest.value = home_posts.latest
            cats.value = home_posts.cats
                // cat1_blogs.value = home_posts.cat1_blogs
                // cat2_blogs.value = home_posts.cat2_blogs
            news_section.value = home_posts.news_section

            // console.log(latest)
            // latest.value = await res.data
        } else {
            console.log(res.data)
        }
    }

    return {
        callHomePosts,
        latest,
        cats,
        news_section
    }
}

export default getHomePosts
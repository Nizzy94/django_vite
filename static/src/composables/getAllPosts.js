import { ref } from "vue"
import { fetchBlogAllowAny } from "./axios"
import { Loading, QSpinnerPie } from "quasar"


const getAllPosts = () => {

        // const data = ref([])
        const data = ref({})

        const callAllPosts = async(page = 0) => {
                const category = ref("")
                const tag = ref("")

                const pathArray = window.location.pathname.slice(1, -1).split("/")

                // console.log(pathArray)
                if (pathArray.length >= 2) {
                    if (pathArray[1] == 'tag') {
                        // console.log('tag')
                        tag.value = pathArray[2]
                    } else {

                        category.value = pathArray[1]
                    }
                } else {
                    category.value = 'all'
                }


                try {
                    Loading.show({
                        spinner: QSpinnerPie
                    })

                    const res = tag.value == "" ?
                        await fetchBlogAllowAny.get(`/get-blog-by-category/${category.value}/${page > 1 ? `?page=${page}` : ``}`) :
                    await fetchBlogAllowAny.get(`/get-blog-by-tag/${tag.value}/${page > 1 ? `?page=${page}` : ``}`)
                    // console.log(res.data)
            
                    data.value = await res.data
                } catch (e) {
                    console.log(e.response)
                }finally {
            setTimeout(() => {
                Loading.hide()
            }, 500);

        }


    }
    return { callAllPosts, data }
}


export default getAllPosts
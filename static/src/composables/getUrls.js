import { ref } from "@vue/runtime-dom"
import { fetchAllowAny } from "./axios"




const getUrls = () => {

    const routes = ref({})

    const callUrls = async() => {
        const res = await fetchAllowAny.get('/get-routes/')


        console.log(res)

        if (res.status == 200) {
            routes.value = res.data
        } else {
            if (res.status == 400) {
                console.log(res.data)
            } else {
                console.log('error')
            }
        }
    }

    return { callUrls, routes }
}

export default getUrls
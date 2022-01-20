import { ref } from "@vue/runtime-dom"
import { Loading, QSpinnerPie } from "quasar"
import { fetchAllowAny } from "./axios"




const getUrls = () => {

    // const $q = useQuasar()

    const routes = ref({})

    const callUrls = async() => {
        Loading.show({
            spinner: QSpinnerPie
        })
        try {
            const res = await fetchAllowAny.get('/get-routes/')
            routes.value = res.data

            // console.log(res)
        } catch (e) {

            console.log(e.response)
        } finally {
            setTimeout(() => {
                Loading.hide()
            }, 1000);

        }



        // if (res.status == 200) {
        // } else {
        //     if (res.status == 400) {
        //     } else {
        //         console.log('error')
        //     }
        // }
    }

    return { callUrls, routes }
}

export default getUrls
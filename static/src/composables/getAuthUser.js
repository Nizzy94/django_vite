import { fetchUserWithCredentials } from "./axios"

const getAuthUser = () => {
    const callAuthUser = async() => {
        try {
            const res = await fetchUserWithCredentials.get(`/user/`)
            if (res.status == 200) {
                return res.data
            }
        } catch (e) {
            console.log(e)
        }

    }

    return { callAuthUser }
}


export default getAuthUser
// import { inject } from "vue";
import { fetchUserWithCredentials } from "./axios";

const postAuthUser = () => {
    const updateAuthUser = async(formData) => {
        try {

            const res = await fetchUserWithCredentials.post(
                `/complete-signup/`,
                formData
            );
            if (res.status == 200) return res

        } catch (e) {
            if (e.response) return e.response
            if (e.request) return e.request
        }

    }

    return { updateAuthUser }
}

export default postAuthUser
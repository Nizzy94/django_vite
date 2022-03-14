// delete-comment

import { fetchBlogWithCredentials } from "./axios"
import moment from "moment"

const deleteComment = () => {
    const removeComment = async(formData) => {
        // console.log(formData)
        try {

            const res = await fetchBlogWithCredentials.post(`/delete-comment/`, formData)
            if (res.status == 200) {
                return res
            }
        } catch (e) {
            if (e.response) {
                if (e.response.status == 400) {
                    console.log(e.response)
                    return e.response
                } else {
                    console.log(e.response)
                    return e.response

                }

            } else if (e.request) {
                console.log(e.request)
            }
        }
    }

    return { removeComment }
}

export default deleteComment
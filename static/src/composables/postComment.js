import { fetchBlogWithCredentials } from "./axios"

const postComment = () => {
    const saveComment = async(formData) => {
        // console.log(formData)
        try {

            const res = await fetchBlogWithCredentials.post(`/post-comment/`, formData)

            // console.log(res.data)
            if (res.status == 200) {

                return res.data
            }
        } catch (e) {
            if (e.response) {
                if (e.response.status == 400) {

                    console.log(e.response)
                } else {
                    console.log(e.response)

                }

            } else if (e.request) {
                console.log(e.request)
            }
        }
    }

    return { saveComment }
}

export default postComment
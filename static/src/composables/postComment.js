import { fetchBlogWithCredentials } from "./axios"

const postComment = () => {
    const saveComment = async(formData) => {
        // console.log(formData)
        const res = await fetchBlogWithCredentials.post(`/post-comment/`, formData)

        console.log(res.data)
        return res.data
    }

    return { saveComment }
}

export default postComment
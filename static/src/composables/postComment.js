import { fetchBlogWithCredentials } from "./axios"
import moment from "moment"

const postComment = () => {
    const saveComment = async(formData) => {
        // console.log(formData)
        try {

            const res = await fetchBlogWithCredentials.post(`/post-comment/`, formData)
            if (res.status == 200) {

                let data = res.data

                // console.log(moment(data.created_at).format("YYYYMMDD"))
                // let formated_date = moment(data.created_at).format("YYYYMMDD")
                data.created_at = moment(data.created_at).fromNow()
                data.updated_at = moment(data.updated_at).fromNow()
                data.children.forEach(child => {
                    let child_formated_date = moment(child.created_at).format("YYYYMMDD")
                    child.created_at = moment(child_formated_date, "YYYYMMDD").fromNow()
                });

                return data
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
import { ref } from "vue"
import { fetchBlogAllowAny } from "./axios"
import moment from "moment"

const getComments = () => {
    const comments = ref([])
    const callComments = async(id) => {
        const res = await fetchBlogAllowAny.get(`/get-comments/${id}/`)

        comments.value = res.data

        comments.value.forEach(comment => {
            let formated_date = moment(comment.created_at).format("YYYYMMDD")

            comment.created_at = moment(comment.created_at).fromNow()
            comment.updated_at = moment(comment.updated_at).fromNow()
            comment.children.forEach(child => {
                child.created_at = moment(child.created_at).fromNow()
            });
        });

    }

    return { callComments, comments }
}

export default getComments
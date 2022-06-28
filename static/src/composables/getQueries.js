import { ref } from "vue";

const getQueries = () => {
    const getRedirectUrl = () => {
        const query = ref(window.location.search);
        const queries = ref(new URLSearchParams(query.value));
        // const redirect_url = queries.value.get("next");
        const redirect_url = `${window.location.origin}${queries.value.get("next")}`;

        return redirect_url
    }

    return { getRedirectUrl }
}

export default getQueries
import { ref } from "vue";

const getQueries = () => {
    const query = ref(window.location.search);
    const queries = ref(new URLSearchParams(query.value));

    const getRedirectUrl = () => {
        // const redirect_url = queries.value.get("next");
        const nextUrl = queries.value.has("next") ? queries.value.get("next") : ''
        const redirect_url = `${window.location.origin}${nextUrl}`;

        // const redirect_url = `${window.location.origin}${queries.value.get("next")}`;

        return redirect_url ? redirect_url : ''
    }

    const getQueryValue = (query_key) => {
        return queries.value.get(query_key)
    }

    return { getRedirectUrl, getQueryValue }
}

export default getQueries
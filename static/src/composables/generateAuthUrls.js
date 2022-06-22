import { ref, watchEffect } from "vue";

const generateAuthUrls = () => {
    const redirect_url = ref(window.location.pathname);
    const redirect_query = ref("");

    const generateLink = async(routes, next_url) => {
        const isAuthPage = ref(false);

        watchEffect(() => {
            if (Object.keys(routes.value).length) {
                // console.log(routes.value.auth_routes.account_login);
                // console.log(window.location.href.split("?")[0]);

                const authUrls = ref(Object.values(routes.value.auth_routes));
                const full_next_url = `${window.location.origin}${next_url}`;

                // console.log(authUrls.value.includes(full_next_url));
                // console.log(authUrls);

                isAuthPage.value = authUrls.value.includes(full_next_url);

                if (!next_url) {
                    // console.log("not next_url");
                    if (!authUrls.value.includes(window.location.href)) {
                        // console.log("not auth p");
                        redirect_query.value = `?next=${redirect_url.value}`;
                    }
                } else {
                    console.log(`${window.location.origin}${next_url}`);

                    if (!isAuthPage.value) {
                        // console.log("not auth p2");
                        redirect_query.value = `?next=${next_url}`;
                    }
                }
            }
        });
    }

    return { generateLink, redirect_query }

}

export default generateAuthUrls
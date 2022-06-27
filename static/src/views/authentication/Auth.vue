<template>
    <Base ref="base">
        <template #page_content>
            <div class="row justify-center q-pa-lg">
                <q-card class="form-card__complete-signup q-pb-lg">
                    <q-card-section class="text-center">
                        <span class="text-primary text-h5">
                            {{ formTitle }}
                        </span>
                    </q-card-section>

                    <q-separator size="1.5px" />

                    <q-card-section class="row justify-center q-mt-lg">
                        <!-- <div id="buttonDiv"></div> -->

                        <!-- <GoogleLogin :callback="googleCallback" prompt /> -->
                        <!-- <q-btn
                                label="Login with Google"
                                no-caps
                                icon="img:https://cdn.cdnlogo.com/logos/g/35/google-icon.svg"
                                class="my-4 font-semibold text-gray-700"
                            /> -->
                        <!-- </GoogleLogin> -->

                        <q-btn
                            label="Continue with Google"
                            @click="googleCallback"
                            color="google_blue"
                            icon="img:https://cdn.cdnlogo.com/logos/g/35/google-icon.svg"
                            class="my-4 font-bold text-grey-10 bg-google_blue"
                        />

                        <!-- <q-btn
                            label="Continue with Google"
                            icon="img:https://cdn.cdnlogo.com/logos/g/35/google-icon.svg"
                            class="my-4 font-bold"
                            type="a"
                            href="https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=http://localhost:8000/accounts/login/&prompt=consent&response_type=code&client_id=418220639690-agli0obvctmdkttgshfo3j74k23fkuo4.apps.googleusercontent.com&scope=openid%20email%20profile&access_type=offline"
                        /> -->
                    </q-card-section>

                    <div class="row q-px-lg justify-around">
                        <div class="col">
                            <q-separator spaced />
                        </div>
                        <div class="col text-center">
                            <span class="text-bold">OR</span>
                        </div>
                        <div class="col">
                            <q-separator spaced />
                        </div>
                    </div>

                    <q-form
                        :action="`${
                            formTitle.toLowerCase() == 'sign up'
                                ? routes?.auth_routes?.account_signup
                                : routes?.auth_routes?.account_login
                        }${redirect_query}`"
                        method="post"
                    >
                        <q-card-section
                            v-if="formErrors?.non_field_errors"
                            class="text-negative"
                        >
                            <p v-for="error in formErrors.non_field_errors">
                                {{ error.message }}
                            </p>
                        </q-card-section>
                        <CSRFToken />
                        <!-- <input
                            name="csrfmiddlewaretoken"
                            type="hidden"
                            :value="$q.cookies.get('csrftoken')"
                        /> -->
                        <slot name="form_controls" />

                        <q-card-section class="q-px-lg">
                            <p v-if="formTitle.toLowerCase() == 'sign in'">
                                Not having an account?
                                <q-btn
                                    label="Sign Up"
                                    dense
                                    flat
                                    color="primary"
                                    no-caps
                                    type="a"
                                    :href="`/signup/auth/${redirect_query}`"
                                />
                                here.
                            </p>
                            <p v-else-if="formTitle.toLowerCase() == 'sign up'">
                                Already having an account?
                                <q-btn
                                    label="Sign In"
                                    dense
                                    flat
                                    color="primary"
                                    no-caps
                                    type="a"
                                    :href="`/login/auth/${redirect_query}`"
                                />
                                here
                            </p>
                        </q-card-section>

                        <q-card-actions class="row justify-center">
                            <q-btn
                                color="secondary"
                                text-color="dark"
                                :label="formTitle"
                                @click="submitAuth"
                                type="submit"
                                no-caps
                                size="md"
                            />
                        </q-card-actions>
                    </q-form>
                </q-card>
            </div>
        </template>
    </Base>
</template>

<script async setup>
import { ref, toRefs } from "vue";
import Base from "../../components/layouts/Base.vue";
import CSRFToken from "../../components/CSRFToken.vue";
import getUrls from "../../composables/getUrls";
import generateAuthUrls from "../../composables/generateAuthUrls";
import {
    inject,
    onBeforeMount,
    onMounted,
    reactive,
    watch,
} from "@vue/runtime-core";
import { googleTokenLogin, googleOneTap } from "vue3-google-login";
import axios from "axios";
import {
    axiosExternal,
    fetchUserWithCredentials,
} from "../../composables/axios";
import { Cookies } from "quasar";

const props = defineProps({
    formTitle: {
        type: String,
        required: true,
    },
});

const { formTitle } = toRefs(props);

const { callUrls, routes } = getUrls();
const { generateLink, redirect_query } = generateAuthUrls();
const client_id = import.meta.env.VITE_GOOGLE_AUTH_KEY;

const query = ref(window.location.search);
const queries = ref(new URLSearchParams(query.value));
const redirect_url = queries.value.get("next");
// const redirect_q = ref("");

onBeforeMount(async () => {
    await callUrls();

    await generateLink(routes, redirect_url);
});

const emit = defineEmits(["signIn", "signUp"]);

const submitAuth = () => {
    formTitle.value.toLowerCase() == "sign in"
        ? emit("signIn")
        : emit("signUp");
};

const form_errors = inject("form_errors");
console.log(form_errors.__all__);

const formErrors = reactive({
    non_field_errors: form_errors.__all__ ?? "",
});

// googleOneTap()
//     .then((response) => {
//         // This promise is resolved when user selects an account from the the One Tap prompt
//         console.log("Handle the response", response);
//     })
//     .catch((error) => {
//         console.log("Handle the error", error);
//     });

const googleCallback = async () => {
    // console.log(routes.value?.auth_routes?.google_login_validate);
    // console.log("Encoded JWT ID token: ", response);

    const tokeResponse = await googleTokenLogin();

    const urls = await callUrls();
    console.log(urls?.auth_routes?.google_login_validate);
    // // const userData = decodeCredential(response.credential);
    // console.log("tokenResponse: ", tokeResponse);
    // console.log("routes: ", routes.value?.auth_routes?.google_login);

    const validatedToken = await axios.post(
        urls?.auth_routes?.google_login,
        {
            access_token: tokeResponse.access_token,
        },
        {
            headers: {
                "X-CSRFToken": Cookies.get("csrftoken"),
            },
            withCreditions: true,
        }
    );
    console.log(validatedToken);
    if (validatedToken.status == 200) {
        window.location.href = `${window.location.origin}${queries.value.get(
            "next"
        )}`;
    }
    // https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=<CALLBACK_URL_YOU_SET_ON_GOOGLE>&prompt=consent&response_type=code&client_id=<YOUR CLIENT ID>&scope=openid%20email%20profile&access_type=offline
};
// onMounted(() => {
//     window.onload = () => {
//         console.log(window.google);
//         console.log(routes.value?.auth_routes?.google_login_validate);

//         google.accounts.id.initialize({
//             client_id: client_id,
//             // ux_mode: "redirect",
//             callback: googleCallback,
//             // login_uri: Object.keys(routes.value).length
//             //     ? routes.value?.auth_routes?.account_login
//             //     : "",
//         });
//         google.accounts.id.renderButton(
//             document.getElementById("buttonDiv"),
//             { theme: "outline", size: "large" } // customization attributes
//         );
//         google.accounts.id.prompt(); // also display the One Tap dialog
//     };
// });
</script>

<style lang="sass">
.form-card__complete-signup
    margin-top: 70px
    width: 100%
</style>
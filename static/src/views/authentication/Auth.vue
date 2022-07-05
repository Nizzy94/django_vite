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
                        <q-btn
                            label="Continue with Google"
                            @click="googleCallback"
                            text-color="grey-10"
                            icon="img:https://cdn.cdnlogo.com/logos/g/35/google-icon.svg"
                            class="q-my-md q-py-sm font-bold"
                        />
                    </q-card-section>

                    <q-card-section class="row justify-around">
                        <!-- <div class="row q-px-lg justify-around"> -->
                        <div class="col">
                            <q-separator spaced />
                        </div>
                        <div class="col text-center">
                            <span class="text-bold">OR</span>
                        </div>
                        <div class="col">
                            <q-separator spaced />
                        </div>
                        <!-- </div> -->
                    </q-card-section>
                    <q-card-section>
                        <div>
                            <span class="text-negative">{{
                                non_field_errors
                            }}</span>
                        </div>
                    </q-card-section>

                    <q-form
                        id="auth_form"
                        :action="`${
                            formTitle.toLowerCase() == 'sign up'
                                ? routes?.auth_routes?.account_signup
                                : routes?.auth_routes?.account_login
                        }${redirect_query}`"
                        @submit.prevent="submitAuth"
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
                                :loading="submiting"
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
import { googleTokenLogin } from "vue3-google-login";
// import { googleSdkLoaded } from "vue3-google-login"
import axios from "axios";

import { Cookies } from "quasar";

const props = defineProps({
    formTitle: {
        type: String,
        required: true,
    },
    non_field_errors: {
        type: String,
        required: true,
    },
    submiting: {
        type: Boolean,
        required: false,
        default: false,
    },
});

const { formTitle } = toRefs(props);

const { callUrls, routes } = getUrls();
const { generateLink, redirect_query } = generateAuthUrls();
const client_id = import.meta.env.VITE_GOOGLE_AUTH_KEY;

const query = ref(window.location.search);
const queries = ref(new URLSearchParams(query.value));
const redirect_url = queries.value.get("next");

onBeforeMount(async () => {
    await callUrls();

    await generateLink(routes, redirect_url);
});

const emit = defineEmits(["signIn", "signUp"]);

const submitAuth = async () => {
    formTitle.value.toLowerCase() == "sign in"
        ? emit("signIn", routes.value)
        : emit("signUp", routes.value);
};

const form_errors = inject("form_errors");
console.log(form_errors.__all__);

const formErrors = reactive({
    non_field_errors: form_errors.__all__ ?? "",
});

const googleCallback = async () => {
    const tokeResponse = await googleTokenLogin();

    const urls = await callUrls();
    console.log(urls?.auth_routes?.google_login_validate);

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
};
</script>

<style lang="sass">
.google-btn
    background-color: $primary
    // width: 100%
.form-card__complete-signup
    margin-top: 70px
    width: 100%
</style>
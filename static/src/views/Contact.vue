<template>
    <Base>
        <template #page_content="{ routes }">
            <div
                class="q-mx-auto q-px-md q-mt-lg"
                :class="{
                    'row q-col-gutter-lg': $q.screen.gt.xs,
                    column: $q.screen.lt.sm,
                }"
            >
                <div class="col-sm-6 col-xs-12 q-mb-lg">
                    <div class="text-h4 text-primary q-mb-md">
                        Have anything to tell us?
                    </div>
                    <div class="text-body1">Send us a message below.</div>
                    <div id="contact_form__container">
                        <div
                            class="row q-mt-md"
                            :class="{ 'q-col-gutter-md': $q.screen.gt.sm }"
                        >
                            <div class="col-md-6 col-xs-12">
                                <q-input
                                    v-model="contactFormData.name"
                                    hint="Enter full name"
                                    hide-hint
                                    label="Name"
                                    :error="contactFormErrors.name != ''"
                                    :error-message="contactFormErrors.name"
                                />
                            </div>
                            <div class="col-md-6 col-xs-12">
                                <q-input
                                    v-model="contactFormData.email"
                                    type="email"
                                    hint="Enter email address"
                                    hide-hint
                                    label="Email"
                                    :error="contactFormErrors.email != ''"
                                    :error-message="contactFormErrors.email"
                                />
                            </div>
                        </div>
                        <div class="q-mb-lg">
                            <q-input
                                v-model="contactFormData.subject"
                                label="Subject"
                                hint="Give subject to your message"
                                hide-hint
                                :error="contactFormErrors.subject != ''"
                                :error-message="contactFormErrors.subject"
                            />
                        </div>
                        <div class="">
                            <q-input
                                v-model="contactFormData.message"
                                counter
                                maxlength="500"
                                outlined
                                autogrow
                                label="Message"
                                hint="Give message in details"
                                hide-hint
                                :error="contactFormErrors.message != ''"
                                :error-message="contactFormErrors.message"
                            />
                        </div>
                        <div class="flex justify-center">
                            <q-btn
                                label="Send"
                                color="secondary"
                                :loading="sending"
                                text-color="dark"
                                @click="submitContactForm(routes)"
                            />
                        </div>
                    </div>
                </div>
                <div class="col" v-if="$q.screen.lt.sm">
                    <q-separator spaced="26px" />
                </div>
                <div class="col-sm-6 col-xs-12 q-mb-lg">
                    <div id="subscription_form__container">
                        <div class="text-h4 text-primary">
                            Subscribe to our newsletter
                        </div>
                        <div style="margin-top: 57px">
                            <subscription-form :authUser="authUser" />
                        </div>
                    </div>
                </div>
            </div>
        </template>
    </Base>
</template>

<script setup>
import { reactive, ref } from "@vue/reactivity";
import Base from "../components/layouts/Base.vue";
import SubscriptionForm from "../components/blog/SubscriptionForm.vue";
import { useMeta } from "quasar";
import axios from "axios";
import { inject, onBeforeMount } from "@vue/runtime-core";
import { Cookies } from "quasar";
import getAuthUser from "../composables/getAuthUser";

const contactFormData = reactive({
    name: "",
    email: "",
    subject: "",
    message: "",
});
const contactFormErrors = reactive({
    name: "",
    email: "",
    subject: "",
    message: "",
});

const sending = ref(false);
const userIsAuthenticated = inject("user_is_authenticated");
const authUser = ref({});

const { callAuthUser } = getAuthUser();

onBeforeMount(async () => {
    if (userIsAuthenticated) {
        authUser.value = await callAuthUser();
    }
});

const submitContactForm = async (routes) => {
    sending.value = true;
    axios
        .post(routes.contact_api, contactFormData, {
            headers: {
                "X-CSRFToken": Cookies.get("csrftoken"),
            },
            withCredentials: true,
        })
        .then((res) => {
            console.log(res);
        })
        .catch((e) => {
            if (e.response) {
                console.log(e.response.data.email);
                let errors = e.response.data;
                contactFormErrors.name = errors.name ? errors.name[0] : "";
                contactFormErrors.email = errors.email ? errors.email[0] : "";
                contactFormErrors.subject = errors.subject
                    ? errors.subject[0]
                    : "";
                contactFormErrors.message = errors.message
                    ? errors.message[0]
                    : "";
            } else if (e.request) {
                console.log(e.request);
            } else {
                console.log(e);
            }
            // console.log(e);
        })
        .finally(() => {
            sending.value = false;
        });
};

const metaData = {
    // sets document title
    title: "Contact Us",
    // optional; sets final title as "Index Page - ${import.meta.env.VITE_WEBSITE_NAME}", useful for multiple level meta
    titleTemplate: (title) => `${title} - ${import.meta.env.VITE_WEBSITE_NAME}`,

    // meta tags
    meta: {
        description: {
            name: "description",
            content: "Contact us page",
        },
        keywords: {
            name: "keywords",
            content: "Quasar website blog django articles",
        },
        equiv: {
            "http-equiv": "Content-Type",
            content: "text/html; charset=UTF-8",
        },
        // note: for Open Graph type metadata you will need to use SSR, to ensure page is rendered by the server
        ogTitle: {
            property: "og:title",
            // optional; similar to titleTemplate, but allows templating with other meta properties
            template(ogTitle) {
                return `${ogTitle} - ${import.meta.env.VITE_WEBSITE_NAME}`;
            },
        },
    },

    // <noscript> tags
    noscript: {
        default: "This is content for browsers with no JS (or disabled JS)",
    },
};

useMeta(metaData);
</script>

<style lang="sass">
#contact_form__container, #subscription_form__container
    @media (min-width: $breakpoint-md-min)
        padding-right: 50px
</style>
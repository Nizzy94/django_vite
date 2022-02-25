<template>
    <Base>
        <template #page_content>
            <div
                class="row q-mx-auto q-px-md q-mt-lg"
                :class="{ 'q-col-gutter-lg': $q.screen.gt.xs }"
            >
                <div class="col-sm-6 col-xs-12 q-mb-lg">
                    <div class="text-h4 text-primary">
                        Have anything to tell us?
                    </div>
                    <div class="text-body1">Send us a message below.</div>
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
                            />
                        </div>
                        <div class="col-md-6 col-xs-12">
                            <q-input
                                v-model="contactFormData.email"
                                type="email"
                                hint="Enter email address"
                                hide-hint
                                label="Email"
                            />
                        </div>
                    </div>
                    <div class="">
                        <q-input
                            v-model="contactFormData.subject"
                            label="Subject"
                            hint="Give subject to your message"
                            hide-hint
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
                        />
                    </div>
                    <div class="flex justify-center">
                        <q-btn
                            label="Send"
                            color="secondary"
                            text-color="dark"
                        />
                    </div>
                </div>
                <div class="col-sm-6 col-xs-12 q-mb-lg">
                    <div class="text-h4 text-primary">
                        Subscribe to our newsletter
                    </div>
                    <div style="margin-top: 57px">
                        <subscription-form />
                    </div>
                </div>
            </div>
        </template>
    </Base>
</template>

<script setup>
import { reactive } from "@vue/reactivity";
import Base from "../components/layouts/Base.vue";
import SubscriptionForm from "../components/blog/SubscriptionForm.vue";

const contactFormData = reactive({
    name: "",
    email: "",
    subject: "",
    message: "",
});

const metaData = {
    // sets document title
    title: "Contact Us",
    // optional; sets final title as "Index Page - My Website", useful for multiple level meta
    titleTemplate: (title) => `${title} - My Website`,

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
                return `${ogTitle} - My Website`;
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

<style>
</style>
<template>
    <Base>
        <template #page_content>
            <section>
                <about-blog />
            </section>
            <section
                class="q-py-xl"
                style="padding-bottom: 200px; padding-top: 200px"
            >
                <mission-vision />
            </section>
            <section class="" style="padding-bottom: 50px">
                <author />
            </section>
        </template>
    </Base>
</template>

<script setup>
import AboutBlog from "../components/About/AboutBlog.vue";
import Author from "../components/About/Author.vue";
import MissionVision from "../components/About/MissionVision.vue";
import Base from "../components/layouts/Base.vue";
import { useMeta } from "quasar";

const metaData = {
    // sets document title
    title: "About Us",
    // optional; sets final title as "Index Page - My Website", useful for multiple level meta
    titleTemplate: (title) => `${title} - ${import.meta.env.VITE_WEBSITE_NAME}`,

    // meta tags
    meta: {
        description: {
            name: "description",
            content: `About ${import.meta.env.VITE_WEBSITE_NAME}`,
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

<style>
</style>
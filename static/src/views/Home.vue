<template>
    <Layout>
        <template #page_content>
            <section class="">
                <div class="window-height">
                    <hero :latest="latest" />
                </div>
            </section>
            <section class="q-my-xl">
                <category-section />
            </section>
            <!-- <section
                style="margin-top: 150px; margin-bottom: 150px"
                class="column justify-center"
            >
                <latest-section :latest="latest" />
            </section> -->
            <section
                style="margin-top: 150px; margin-bottom: 150px"
                class="justify-center"
            >
                <news-section :cats="cats" :news_section="news_section" />
            </section>
            <section style="padding-top: 100px">
                <Author />
            </section>
            <!-- <section style=" padding-bottom:100px"  >
          <Author />
        </section> -->
        </template>
    </Layout>
</template>
        

<script setup>
import Layout from "../components/layouts/Base.vue";
import Hero from "../components/Home/Hero2.vue";
import CategorySection from "../components/Home/CategorySection.vue";
import LatestSection from "../components/Home/LatestSection.vue";
import NewsSection from "../components/Home/NewsSection.vue";
import Author from "../components/Home/Author.vue";
import getHomePosts from "../composables/getHomePosts";
import { onBeforeMount } from "@vue/runtime-core";
import { useMeta } from "quasar";

const { callHomePosts, latest, cats, news_section } = getHomePosts();

onBeforeMount(async () => {
    await callHomePosts();
    // console.log(latest.value);
});

const metaData = {
    // sets document title
    title: "Blog Website",
    // optional; sets final title as "Index Page - My Website", useful for multiple level meta
    titleTemplate: (title) => `${title} - My Website`,

    // meta tags
    meta: {
        description: {
            name: "description",
            content: "Blog Website landing page. Latest news here",
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
  
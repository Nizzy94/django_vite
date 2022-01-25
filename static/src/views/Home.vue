<template>
    <Layout>
        <template #page_content>
            <section class="">
                <div class="window-height">
                    <hero />
                </div>
            </section>
            <section class="q-my-xl">
                <category-section />
            </section>
            <section
                style="margin-top: 150px; margin-bottom: 150px"
                class="column justify-center"
            >
                <latest-section :latest="latest" />
            </section>
            <section
                style="margin-top: 150px; margin-bottom: 150px"
                class="justify-center"
            >
                <news-section
                    :cats="cats"
                    :cat1_blogs="cat1_blogs"
                    :cat2_blogs="cat2_blogs"
                />
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

const { callHomePosts, latest, cats, cat1_blogs, cat2_blogs } = getHomePosts();

onBeforeMount(async () => {
    await callHomePosts();
    // console.log(latest.value);
});
</script>


<style>
</style>
  
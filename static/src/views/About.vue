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
</script>

<style>
</style>
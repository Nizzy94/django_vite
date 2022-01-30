<template>
    <div class="">
        <div class="row justify-center q-mb-lg">
            <h1 class="text-h2 text-primary">Related</h1>
        </div>
        <div class="row q-col-gutter-md justify-center">
            <div
                class="col-xs-12 col-sm-6 col-md-3"
                v-for="(blog, i) in related"
                :key="blog.id"
            >
                <news-card
                    :title="blog.title"
                    :body="blog.body"
                    :imageSrc="blog.image"
                    subtitle="By John Doe"
                    :url="blog.url"
                />
                <!-- </div> -->
            </div>
        </div>
    </div>
</template>

<script setup>
import NewsCard from "../NewsCard.vue";
import getRelatedPosts from "../../composables/getRelatedPosts";

const { callRelatedPosts, related } = getRelatedPosts();

callRelatedPosts();
</script>

<style>
</style>
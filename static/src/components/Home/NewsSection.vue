<template>
    <div class="row q-px-md q-col-gutter-lg-md">
        <div class="col-xs-12 col-md-6">
            <div class="category_title_container">
                <a :href="cats[0]?.url" class="text-h5">{{ cats[0]?.name }}</a>
            </div>
            <div class="row q-col-gutter-sm">
                <div id="big_side1" class="col-xs-12 col-sm-6">
                    <a
                        :href="cat1_blogs[0]?.url"
                        class="big_blog_link"
                        v-if="cat1_blogs.length"
                    >
                        <news-card
                            v-if="cat1_blogs.length"
                            :title="cat1_blogs[0]?.title"
                            :body="cat1_blogs[0]?.body"
                            :subtitle="'by John Doe'"
                            :imageSrc="cat1_blogs[0]?.image"
                        />
                    </a>
                </div>
                <div id="small_side1" class="col-xs-12 col-sm-6">
                    <a
                        :href="blog.url"
                        v-if="cat1_blogs.length"
                        class="q-mb-sm small_blog_link"
                        v-for="(blog, i) in cat1_blogs.slice(1)"
                        :key="i"
                    >
                        <news-card
                            :title="blog.title"
                            :body="blog.body"
                            :subtitle="'by John Doe'"
                            horizontal
                            :imageSrc="blog.image"
                        />
                    </a>
                </div>
            </div>
        </div>
        <div
            class="col-xs-12 col-md-6"
            :class="{
                'q-mt-lg': $q.screen.lt.md,
                'q-mt-none': $q.screen.gt.sm,
            }"
        >
            <div class="category_title_container">
                <a :href="cats[1]?.url" class="text-h5">{{ cats[1]?.name }}</a>
            </div>
            <div class="row q-col-gutter-sm">
                <div id="big_side2" class="col-xs-12 col-sm-6">
                    <a
                        :href="cat2_blogs[0]?.url"
                        class="big_blog_link"
                        v-if="cat2_blogs.length"
                    >
                        <news-card
                            :title="cat2_blogs[0]?.title"
                            :body="cat2_blogs[0]?.body"
                            :subtitle="'by John Doe'"
                            :imageSrc="cat2_blogs[0]?.image"
                        />
                    </a>
                </div>
                <div id="small_side2" class="col-xs-12 col-sm-6">
                    <a
                        v-if="cat2_blogs.length"
                        :href="blog.url"
                        class="q-mb-sm small_blog_link"
                        v-for="(blog, i) in cat2_blogs.slice(1)"
                        :key="i"
                    >
                        <news-card
                            :title="blog.title"
                            :body="blog.body"
                            :subtitle="'by John Doe'"
                            horizontal
                            :imageSrc="blog.image"
                        />
                    </a>
                </div>
            </div>
        </div>
    </div>
    <div class="q-mt-xl flex justify-center">
        <q-btn
            label="Read More"
            color="secondary"
            text-color="dark"
            type="a"
            :href="routes?.blog?.all"
        />
    </div>
</template>

<script setup>
import NewsCard from "../NewsCard.vue";
import getHomePosts from "../../composables/getHomePosts";
import { computed, ref, toRefs } from "@vue/reactivity";
import { inject } from "@vue/runtime-core";

const props = defineProps({
    cats: {
        type: Array,
    },
    cat1_blogs: {
        type: Array,
    },
    cat2_blogs: {
        type: Array,
    },
});
const { cats, cat1_blogs, cat2_blogs } = toRefs(props);

const routes = computed(() => inject("routes").value);
</script>

<style lang="sass">
.category_title_container
    width: 98%
    color: #fff
    margin-bottom: 20px
    border-bottom: 2px $primary solid

    a.text-h5
        display: block
        color: #fff
        text-decoration: none
        padding-left: 10px
        padding-right: 10px
        padding-top: 2px
        padding-bottom: 2px
        width: fit-content
        background-color: $primary
        margin-bottom: 0

        &:hover
            background-color: $primary_hover

.small_blog_link, .big_blog_link
    display: block
    text-decoration: none
</style>
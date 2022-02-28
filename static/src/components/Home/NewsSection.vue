<template>
    <div class="row q-px-md q-col-gutter-lg-md">
        <div
            class="col-xs-12 col-md-6 q-mb-xl"
            v-for="(sect, i) in news_section"
            :key="i"
        >
            <div class="category_title_container">
                <a :href="sect.cat?.url" class="text-h5">{{
                    sect.cat?.name
                }}</a>
            </div>
            <div class="row q-col-gutter-sm">
                <div id="big_side1" class="col-xs-12 col-sm-6">
                    <!-- <a :href="cat1_blogs[0]?.url" class="card_link"> -->
                    <!-- ${sect.blogs[0]?.user.first_name} ${sect.blogs[0]?.user.last_name} -->
                    <news-card
                        v-if="sect.blogs.length"
                        :title="sect.blogs[0]?.title"
                        :excerpt="sect.blogs[0]?.excerpt"
                        :author="`by ${sect.blogs[0]?.author.first_name} ${sect.blogs[0]?.author.last_name}`"
                        :imageSrc="sect.blogs[0]?.image"
                        :url="sect.blogs[0]?.url"
                    />
                    <!-- </a> -->
                </div>
                <div id="small_side1" class="col-xs-12 col-sm-6">
                    <div
                        v-if="sect.blogs.length"
                        class="q-mb-sm"
                        v-for="(blog, i) in sect.blogs.slice(1)"
                        :key="i"
                    >
                        <news-card
                            :title="blog.title"
                            :excerpt="blog.excerpt"
                            :author="`by ${blog?.author.first_name} ${blog?.author.last_name}`"
                            horizontal
                            :imageSrc="blog.image"
                            :url="blog.url"
                        />
                    </div>
                </div>
            </div>
        </div>
        <!-- <div
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
                  
                    <news-card
                        v-if="cat2_blogs.length"
                        :title="cat2_blogs[0]?.title"
                        :body="cat2_blogs[0]?.body"
                        :subtitle="'by John Doe'"
                        :imageSrc="cat2_blogs[0]?.image"
                        :url="cat2_blogs[0]?.url"
                    />
                </div>
                <div id="small_side2" class="col-xs-12 col-sm-6">
                    <div
                        v-if="cat2_blogs.length"
                        class="q-mb-sm"
                        v-for="(blog, i) in cat2_blogs.slice(1)"
                        :key="i"
                    >
                        <news-card
                            :title="blog.title"
                            :body="blog.body"
                            :subtitle="'by John Doe'"
                            horizontal
                            :imageSrc="blog.image"
                            :url="blog.url"
                        />
                    </div>
                </div>
            </div>
        </div> -->
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
import { inject, watch } from "@vue/runtime-core";

const props = defineProps({
    cats: {
        type: Array,
    },
    news_section: {
        type: Array,
    },
    // cat2_blogs: {
    //     type: Array,
    // },
});
const { cats, news_section } = toRefs(props);

watch(news_section, () => {
    if (news_section.value.length) {
        console.log(news_section.value);
    }
});

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

// .card_link, .card_link
//     display: block
//     text-decoration: none
</style>
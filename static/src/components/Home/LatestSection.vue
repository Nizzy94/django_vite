<template>
    <div class="column">
        <div class="row justify-center q-mb-lg">
            <div class="text-h2 text-center">Latest</div>
        </div>
        <div class="row q-col-gutter-md q-px-xl justify-center">
            <div
                class="col-xs-12 col-sm-6 col-md-3"
                v-for="(news, i) in latest_p"
                :key="news.id"
            >
                <!-- <div class="" style="height:300px"> -->

                <news-card
                    :title="news.title"
                    :body="news.body"
                    subtitle="By John Doe"
                    :imageSrc="`${news.image}`"
                />
                <!-- </div> -->
            </div>
        </div>
    </div>
</template>

<script setup>
import NewsCard from "../NewsCard.vue";
import getLatestPosts from "../../composables/getLatestPosts";
import { computed, inject, onBeforeMount } from "@vue/runtime-core";

const { callLatestPosts, latest_p } = getLatestPosts();

onBeforeMount(async () => {
    await callLatestPosts();
    console.log(latest_p.value);
});

// const domain = computed(() => inject("domain"));

const latest = [
    {
        id: 1,
        title: "General Title",
        body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua consectetur adipiscing elit,.",
    },
    {
        id: 2,
        title: "Sports Title",
        body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    },
    {
        id: 3,
        title: "Politics Title",
        body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    },
    {
        id: 4,
        title: "Entertainment Titlesd",
        body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    },
    {
        id: 5,
        title: "General Title",
        body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua consectetur adipiscing elit,.",
    },
    {
        id: 6,
        title: "Sports Title",
        body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    },
    // {
    //     id:7,
    //     title: 'Politics Title',
    //     body: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    // },
    // {
    //     id:8,
    //     title: 'Entertainment Titlesd',
    //     body: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    // },
];
</script>

<style>
</style>
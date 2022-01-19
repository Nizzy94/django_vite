<template>
    <Base>
        <template #page_content>
            <section class="row justify-center q-my-lg">
                <q-pagination
                    dense
                    boundary-numbers
                    :max-pages="6"
                    :direction-links="$q.screen.gt.xs"
                    :boundary-links="$q.screen.gt.xs"
                    :size="$q.screen.lt.md ? '12px' : 'md'"
                    v-model="currentPage"
                    :max="24"
                    icon-first="skip_previous"
                    icon-last="skip_next"
                    icon-prev="fast_rewind"
                    icon-next="fast_forward"
                />
            </section>
            <section
                class="row q-mx-auto q-px-lg q-col-gutter-md q-my-xl"
                style="max-width: 1440px"
            >
                <div
                    class="col-xs-12 col-sm-6 col-md-3"
                    v-for="(news, i) in blogs"
                    :key="news.id"
                >
                    <news-card
                        :title="news.title"
                        :body="news.body"
                        subtitle="By John Doe"
                    />
                </div>
            </section>
            <section class="row justify-center q-my-lg">
                <q-pagination
                    dense
                    boundary-numbers
                    :max-pages="6"
                    :direction-links="$q.screen.gt.xs"
                    :boundary-links="$q.screen.gt.xs"
                    :size="$q.screen.lt.md ? '12px' : 'md'"
                    v-model="currentPage"
                    :max="24"
                    icon-first="skip_previous"
                    icon-last="skip_next"
                    icon-prev="fast_rewind"
                    icon-next="fast_forward"
                />
            </section>
        </template>
    </Base>
</template>

<script setup>
import { ref } from "@vue/reactivity";
import Base from "../../components/layouts/Base.vue";
import NewsCard from "../../components/NewsCard.vue";

const currentPage = ref(2);

const blogs = [
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
    {
        id: 7,
        title: "Politics Title",
        body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    },
    {
        id: 8,
        title: "Entertainment Titlesd",
        body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    },
    {
        id: 9,
        title: "General Title",
        body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua consectetur adipiscing elit,.",
    },
    {
        id: 10,
        title: "Sports Title",
        body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    },
    {
        id: 11,
        title: "Politics Title",
        body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    },
    {
        id: 12,
        title: "Entertainment Titlesd",
        body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    },
    {
        id: 13,
        title: "General Title",
        body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua consectetur adipiscing elit,.",
    },
    {
        id: 14,
        title: "Sports Title",
        body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    },
    {
        id: 15,
        title: "Politics Title",
        body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    },
    {
        id: 16,
        title: "Entertainment Titlesd",
        body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    },
    {
        id: 17,
        title: "General Title",
        body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua consectetur adipiscing elit,.",
    },
    {
        id: 18,
        title: "Sports Title",
        body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    },
    {
        id: 19,
        title: "Politics Title",
        body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    },
    {
        id: 20,
        title: "Entertainment Titlesd",
        body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    },
    {
        id: 21,
        title: "General Title",
        body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua consectetur adipiscing elit,.",
    },
    {
        id: 22,
        title: "Sports Title",
        body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    },
    {
        id: 23,
        title: "Politics Title",
        body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    },
    {
        id: 24,
        title: "Entertainment Titlesd",
        body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    },
];
</script>

<style>
</style>
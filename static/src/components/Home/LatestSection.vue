<template>
    <div class="column">
        <div class="row justify-center q-mb-lg">
            <div class="text-h2 text-center text-primary q-mb-xl">Latest</div>
        </div>
        <div class="row q-col-gutter-md q-px-md justify-center">
            <div
                class="col-xs-12 col-sm-6 col-md-3"
                v-for="(news, i) in latest"
                :key="news.id"
            >
                <!-- <div class="" style="height:300px"> -->

                <news-card
                    :title="news.title"
                    :body="news.body"
                    subtitle="By John Doe"
                    :imageSrc="`${news.image}`"
                    :url="news.url"
                />
                <!-- </div> -->
            </div>
        </div>
    </div>
</template>

<script setup>
import NewsCard from "../NewsCard.vue";
import { computed, inject, onBeforeMount, toRefs } from "@vue/runtime-core";

const props = defineProps({
    latest: Array,
});

const { latest } = toRefs(props);
</script>

<style>
</style>
<template>
    <q-card class="news-card" tag="a" :href="url" square v-if="horizontal">
        <q-card-section horizontal>
            <q-img
                class="col-5"
                :src="imageSrc"
                fit="cover"
                height="100px"
                width="100px"
            />
            <!-- <q-card-section class="q-pa-none"> -->
            <q-card-section class="q-pt-none">
                <div class="text-body2 ellipsis-3-lines">{{ title }}</div>
                <small class="text-grey-6">{{ subtitle }}</small>
            </q-card-section>

            <!-- <q-card-section class="ellipsis q-pt-none">
            {{ body }}
            </q-card-section> -->
            <!-- </q-card-section> -->
        </q-card-section>
    </q-card>

    <q-card class="news-card" tag="a" :href="url" square v-else>
        <q-img :src="imageSrc" fit="cover" height="250px" />

        <q-card-section>
            <div class="text-h6 text-capitalize ellipsis-3-lines">
                {{ title }}
            </div>
            <div class="text-subtitle2">{{ subtitle }}</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
            <div class="ellipsis-3-lines" v-html="body"></div>
            <!-- {{ body }} -->
        </q-card-section>
    </q-card>
</template>

<script setup>
import { toRefs } from "@vue/reactivity";

const props = defineProps({
    title: {
        type: String,
        required: true,
    },
    body: {
        type: String,
        required: true,
    },
    subtitle: {
        type: String,
        required: false,
    },
    horizontal: {
        type: Boolean,
        default: false,
    },
    imageSrc: {
        type: String,
        required: true,
    },
    url: {
        type: String,
    },
});

const { title, body, subtitle, horizontal, imageSrc, url } = toRefs(props);
</script>

<style lang="sass" scope>
a.news-card
    text-decoration: none
    color: $dark

    &:hover
        .text-h6
            color: $primary
        .text-body2
            color: $primary
</style>
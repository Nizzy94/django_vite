<template>
    <q-card class="news-card" tag="a" href="#" square>
        <img src="https://cdn.quasar.dev/img/mountains.jpg">

        <q-card-section>
            <div class="text-h6">{{ title }}</div>
            <div class="text-subtitle2">{{ subtitle }}</div>
        </q-card-section>

        <q-card-section class="q-pt-none ellipsis">
            {{ body }}
        </q-card-section>
    </q-card>
</template>

<script setup>
import { toRefs } from "@vue/reactivity"


const props = defineProps({
    title: {
        type: String,
        required: true
    },
    body: {
        type: String,
        required: true
    },
    subtitle: {
        type: String,
        required: false
    }
})

const {title, body, subtitle} = toRefs(props)

</script>

<style lang="sass" scope>
a.news-card
    text-decoration: none
    color: $dark

    &:hover
        .text-h6
            color: $primary
</style>
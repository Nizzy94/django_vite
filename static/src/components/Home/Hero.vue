<template>
    <q-carousel
        arrows
        animated
        v-model="slide"
        style="z-index: 1"
        height="95.5vh"
        autoplay
        infinite
        navigation
        navigation-position="top"
    >
        <q-carousel-slide
            name="first"
            img-src="https://cdn.quasar.dev/img/mountains.jpg"
        >
            <div class="absolute-bottom custom-caption">
                <div class="text-h2">First stop</div>
                <div class="text-subtitle1">Mountains</div>
            </div>
        </q-carousel-slide>
        <q-carousel-slide
            name="second"
            img-src="https://cdn.quasar.dev/img/parallax1.jpg"
        >
            <div class="absolute-bottom custom-caption">
                <div class="text-h2">Second stop</div>
                <div class="text-subtitle1">Famous City</div>
            </div>
        </q-carousel-slide>
        <q-carousel-slide
            name="third"
            img-src="https://cdn.quasar.dev/img/parallax2.jpg"
        >
            <div class="absolute-bottom custom-caption">
                <div class="text-h2">Third stop</div>
                <div class="text-subtitle1">Famous Bridge</div>
            </div>
        </q-carousel-slide>
    </q-carousel>
</template>

<script setup>
import { ref } from "vue";
const slide = ref("first");
</script>

<style lang="sass" scoped>
.custom-caption
    text-align: center
    padding: 12px
    color: white
    background-color: rgba(0, 0, 0, .3)
</style>
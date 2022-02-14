<template>
    <q-carousel
        animated
        v-model="slide"
        style="z-index: 1"
        height="95.5vh"
        infinite
        :autoplay="10000"
        navigation
        :navigation-position="$q.screen.gt.sm ? 'right' : 'bottom'"
        transition-next="jump-up"
        transition-prev="jump-down"
        vertical
    >
        <q-carousel-slide
            :name="i"
            class="row"
            v-for="(news, i) in latest"
            :key="news.id"
        >
            <carousel-slide
                :header="news.title"
                :subtitle="news.body"
                :imageSrc="news.image"
            />
        </q-carousel-slide>
        <!-- <q-carousel-slide name="second" class="row">
            <carousel-slide
                :header="'Second Stop'"
                :subtitle="'Subtitle for second stop'"
                imageSrc="https://cdn.quasar.dev/img/parallax1.jpg"
            />
        </q-carousel-slide>
        <q-carousel-slide name="third" class="row">
            <carousel-slide
                :header="'Third Stop'"
                :subtitle="'Subtitle for third stop'"
                imageSrc="https://cdn.quasar.dev/img/parallax2.jpg"
            />
        </q-carousel-slide> -->
    </q-carousel>
</template>

<script setup>
import { ref, toRefs } from "vue";
import CarouselSlide from "./CarouselSlide.vue";

const props = defineProps({
    latest: {
        type: Array,
    },
});

const { latest } = toRefs(props);

const slide = ref(0);
</script>

<style lang="sass" scoped>
// .caption__div_1
//     background: rgba(38, 166, 154, 0.9)
//     width: 10%

//     @media (min-width: $breakpoint-sm-min)
//         background: rgba(255, 255, 255, 0.7)
//         width: 25%
// .caption__div
//     // background: rgba(38, 166, 154, 0.7)
//     // width: 25%

//     @media (min-width: $breakpoint-sm-min)
//         background: rgba(255, 255, 255, 0.7)
//         width: 25%

.q-carousel__slide
    // padding-top: 0 !important
    padding: 0 !important
.custom-caption
    text-align: center
</style>
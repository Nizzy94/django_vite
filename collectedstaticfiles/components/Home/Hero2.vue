<template>
    <q-carousel
        animated
        v-model="slide"
        style="z-index: 1"
        height="95.5vh"
        infinite
        autoplay="10000"
        navigation
        navigation-position="right"
        transition-next="jump-up"
        transition-prev="jump-down"
        vertical
    >
        <q-carousel-slide name="first" class="row">
            <div class="custom-caption col" v-if="$q.screen.gt.xs">
                <div class="column justify-center full-height">
                    <div>
                        <div class="text-h2 text-primary">First stop</div>
                        <div class="text-subtitle1">Mountains</div>
                    </div>
                </div>
            </div>
            <q-intersection
                :transition="$q.screen.gt.xs ? 'slide-down' : ''"
                transition-duration="1500"
                class="custom-caption col-sm-6 col-xs-12"
            >
                <q-img
                    height="95vh"
                    src="https://cdn.quasar.dev/img/mountains.jpg"
                >
                    <div
                        class="
                            absolute-full
                            text-subtitle2
                            flex flex-center
                            caption__div
                        "
                    >
                        <div v-if="$q.screen.lt.sm">
                            <div class="text-h2">First stop</div>
                            <div class="text-subtitle1">Mountains</div>
                        </div>
                    </div>
                </q-img>
            </q-intersection>
        </q-carousel-slide>
        <q-carousel-slide name="second" class="row">
            <div class="custom-caption col">
                <div class="column justify-center full-height">
                    <div>
                        <div class="text-h2 text-primary">Second stop</div>
                        <div class="text-subtitle1">Mountains</div>
                    </div>
                </div>
            </div>
            <q-intersection
                :transition="$q.screen.gt.xs ? 'slide-down' : ''"
                transition-duration="1500"
                class="custom-caption col-sm-6 col-xs-12"
            >
                <q-img
                    height="95vh"
                    src="https://cdn.quasar.dev/img/parallax1.jpg"
                >
                    <div
                        class="
                            absolute-full
                            text-subtitle2
                            flex flex-center
                            caption__div
                        "
                    >
                        <div v-if="$q.screen.lt.sm">
                            <div class="text-h2">First stop</div>
                            <div class="text-subtitle1">Mountains</div>
                        </div>
                    </div>
                </q-img>
            </q-intersection>
        </q-carousel-slide>
        <q-carousel-slide name="third" class="row">
            <div class="custom-caption col">
                <div class="column justify-center full-height">
                    <div>
                        <div class="text-h2 text-primary">Third stop</div>
                        <div class="text-subtitle1">Mountains</div>
                    </div>
                </div>
            </div>
            <q-intersection
                :transition="$q.screen.gt.xs ? 'slide-down' : ''"
                transition-duration="1500"
                class="custom-caption col-sm-6 col-xs-12"
            >
                <q-img
                    height="95vh"
                    src="https://cdn.quasar.dev/img/parallax2.jpg"
                >
                    <div
                        class="
                            absolute-full
                            text-subtitle2
                            flex flex-center
                            caption__div
                        "
                    >
                        <div v-if="$q.screen.lt.sm">
                            <div class="text-h2">First stop</div>
                            <div class="text-subtitle1">Mountains</div>
                        </div>
                    </div>
                </q-img>
            </q-intersection>
        </q-carousel-slide>
        <!-- <q-carousel-slide
            name="second"
            img-src="https://cdn.quasar.dev/img/parallax1.jpg"
        >
            <div class="absolute-left custom-caption">
                <div class="text-h2">Second stop</div>
                <div class="text-subtitle1">Famous City</div>
            </div>
        </q-carousel-slide>
        <q-carousel-slide
            name="third"
            img-src="https://cdn.quasar.dev/img/parallax2.jpg"
        >
            <div class="absolute-left custom-caption">
                <div class="text-h2">Third stop</div>
                <div class="text-subtitle1">Famous Bridge</div>
            </div>
        </q-carousel-slide> -->
    </q-carousel>
</template>

<script setup>
import { ref } from "vue";
const slide = ref("first");
</script>

<style lang="sass" scoped>
.caption__div
    background: rgba(38, 166, 154, 0.7)
.q-carousel__slide
    // padding-top: 0 !important
    padding: 0 !important
.custom-caption
    text-align: center
    // padding: 12px
    // color: white
    // background-color: rgba(0, 0, 0, .3)
</style>
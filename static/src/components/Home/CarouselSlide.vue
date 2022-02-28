<template>
    <div class="custom-caption col-xs-12 col-md-5" v-if="$q.screen.gt.sm">
        <div class="column justify-center full-height">
            <a class="carousel_link q-pa-xl" :href="url">
                <div class="text-h4 text-primary q-mb-md">{{ header }}</div>
                <!-- <div class="text-subtitle1">{{ subtitle }}</div> -->
                <div class="text-body1" v-html="subtitle"></div>
                <!-- <div
                    class="text-body1"
                    v-html="subtitle.substring(0, 500).concat('...')"
                ></div> -->
            </a>
        </div>
    </div>
    <q-intersection
        :transition="$q.screen.gt.sm ? 'slide-down' : ''"
        transition-duration="1500"
        class="custom-caption col-xs-12 col-md-7"
    >
        <q-img height="95vh" :src="imageSrc">
            <div
                v-if="$q.screen.lt.md"
                class="text-subtitle2 flex flex-center"
                :class="{
                    'absolute-full': $q.screen.lt.md,
                    //'absolute-left': $q.screen.gt.xs,
                }"
            >
                <div v-if="$q.screen.lt.md">
                    <div class="text-h5 q-mb-md">{{ header }}</div>

                    <div class="text-subtitle1" v-html="subtitle"></div>
                    <!-- <div
                        class="text-subtitle1"
                        v-html="subtitle.substring(0, 500).concat('...')"
                    ></div> -->
                </div>
            </div>
        </q-img>
    </q-intersection>
</template>

<script setup>
import { toRefs } from "@vue/reactivity";

const props = defineProps({
    header: {
        type: String,
        // required: true,
    },
    subtitle: {
        type: String,
    },
    imageSrc: {
        type: String,
    },
    url: {
        type: String,
    },
});

const { header, subtitle, imageSrc, url } = toRefs(props);
</script>

<style lang="sass">
.carousel_link
    display: block
    text-decoration: none
    color: $dark
.custom-caption
    text-align: center
</style>
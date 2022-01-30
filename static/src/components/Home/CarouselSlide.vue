<template>
    <div class="custom-caption col-xs-12 col-sm-6" v-if="$q.screen.gt.xs">
        <div class="column justify-center full-height">
            <div>
                <div class="text-h2 text-primary">{{ header }}</div>
                <div class="text-subtitle1">{{ subtitle }}</div>
            </div>
        </div>
    </div>
    <q-intersection
        :transition="$q.screen.gt.xs ? 'slide-down' : ''"
        transition-duration="1500"
        class="custom-caption col-xs-12 col-sm-6"
    >
        <q-img height="95vh" :src="imageSrc">
            <div
                v-if="$q.screen.lt.sm"
                class="text-subtitle2 flex flex-center"
                :class="{
                    'absolute-full': $q.screen.lt.sm,
                    //'absolute-left': $q.screen.gt.xs,
                }"
            >
                <div v-if="$q.screen.lt.sm">
                    <div class="text-h2">{{ header }}</div>
                    <div class="text-subtitle1">{{ subtitle }}</div>
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
});

const { header, subtitle, imageSrc } = toRefs(props);
</script>

<style lang="sass">
.custom-caption
    text-align: center
</style>
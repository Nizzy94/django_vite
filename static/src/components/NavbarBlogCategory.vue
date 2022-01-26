<template>
    <q-list>
        <q-item
            tag="a"
            :href="routes?.blog?.all"
            :class="{ 'text-primary': currentRoute == routes?.blog?.all }"
        >
            <q-item-section>All</q-item-section>
        </q-item>
        <q-item
            v-for="cat in routes?.blog?.categories"
            :key="cat.url"
            clickable
            v-close-popup
            tag="a"
            :href="cat?.url"
            :class="{ 'text-primary': currentRoute == cat?.url }"
        >
            <!-- {{ currentRoute == cat?.url }} -->
            <!-- <q-item-section avatar>
                <q-avatar
                    icon="mdi-folder"
                    color="secondary"
                    text-color="white"
                />
            </q-item-section> -->
            <q-item-section>
                <q-item-label>{{ cat.name }}</q-item-label>
                <!-- <q-item-label caption>February 22, 2016</q-item-label> -->
            </q-item-section>
        </q-item>
    </q-list>
</template>

<script setup>
import { computed, inject, ref, toRefs, watch } from "@vue/runtime-core";

const routes = inject("routes");
const currentRoute = ref(window.location.href);

// watch(routes, () => {
//     console.log(routes.value);
//     if (Object.keys(routes.value).length) {
//         currentRouteIsBlog.value = Object.values(routes.value.blog).includes(
//             currentRoute.value
//         );
//     }
// });
</script>

<style>
</style>
<template>
    <q-list>
        <q-item
            v-for="cat in routes?.blog?.categories"
            :key="cat.url"
            clickable
            v-close-popup
            tag="a"
            :href="cat.url"
        >
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
import { computed, inject, ref } from "@vue/runtime-core";

const routes = computed(() => inject("routes").value);
const currentRoute = ref(window.location.href);
</script>

<style>
</style>
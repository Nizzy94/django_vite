<template>
    <q-dialog v-model="search_d" position="top">
        <q-card style="min-width: 350px" class="q-px-sm">
            <!-- <q-card-section>
          <div class="text-h6">Search</div>
        </q-card-section> -->

            <q-card-section class="q-pt-md">
                <q-input
                    v-model="search_term"
                    label="Search"
                    autofocus
                    @keyup.enter="searchQuery"
                />
                <!-- <slot name=input_field /> -->
            </q-card-section>

            <q-card-actions align="right" class="text-primary">
                <q-btn flat label="Cancel" v-close-popup />
                <q-btn flat label="Search" @click="searchQuery" />
            </q-card-actions>
        </q-card>
    </q-dialog>
</template>

<script setup>
import { inject, ref } from "vue";

const routes = inject("routes");

const search_term = ref("");
const search_d = ref(false);

const searchQuery = () => {
    if (search_term.value == "") {
        search_d.value = false;
        return;
    }

    // console.log(search_term.value);

    window.location.href = `${routes.value.search}?q=${search_term.value}`;
};

const openSearch = () => (search_d.value = true);

defineExpose({
    openSearch,
});
</script>

<style>
</style>
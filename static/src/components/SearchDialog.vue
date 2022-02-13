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
                    clearable
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
import { inject, ref, watch } from "vue";

const routes = inject("routes");

const search_term = ref("");
const search_d = ref(false);
const query_string = ref();
// watch(search_term, () => {
//     query_string.value = encodeURIComponent(search_term.value);
// });

const query = ref(window.location.search);
const queries = ref(new URLSearchParams(query.value));

if (queries.value.has("q")) {
    search_term.value = queries.value.get("q");
}

const searchQuery = () => {
    if (search_term.value == "") {
        search_d.value = false;
        return;
    }

    query_string.value = search_term.value.replace(/ /g, "+");

    window.location.href = `${routes.value.search}?q=${query_string.value}`;
};

const openSearch = () => (search_d.value = true);

defineExpose({
    openSearch,
});
</script>

<style>
</style>
<template>
    <q-dialog v-model="search_d" position="top">
        <q-card style="max-width: 600px; max-hegiht: 700px" class="q-px-sm">
            <!-- <q-card-section>
          <div class="text-h6">Search</div>
        </q-card-section> -->

            <q-card-section class="q-pt-md">
                <q-input
                    v-model="search_term"
                    label="Search"
                    autofocus
                    debounce="300"
                    @update:model-value="onRequest"
                    clearable
                    @keyup.enter="searchQuery"
                />
                <!-- <slot name=input_field /> -->
            </q-card-section>

            <q-card-actions align="right" class="text-primary">
                <q-btn flat label="Cancel" v-close-popup />
                <q-btn flat label="Search" @click="searchQuery" />
            </q-card-actions>

            <q-card-section class="q-pt-md" style="">
                {{ results.height }}
                <q-scroll-area :style="results.style">
                    <div
                        class="q-mb-sm"
                        v-for="res in results.data"
                        :key="res.id"
                    >
                        <news-card
                            :title="res.title"
                            :body="res.body"
                            :subtitle="'by John Doe'"
                            horizontal
                            :imageSrc="res.image"
                            :url="res.url"
                        />
                    </div>
                </q-scroll-area>
            </q-card-section>
        </q-card>
    </q-dialog>
</template>

<script setup>
import { inject, ref, watch } from "vue";
import getAllPosts from "../composables/getAllPosts";
import NewsCard from "../components/NewsCard.vue";

const routes = inject("routes");

const search_term = ref("");
const search_d = ref(false);
const query_string = ref();
const results = ref({
    data: [],
    style: {
        height: "0px",
        maxWidth: "600px",
    },
});

const query = ref(window.location.search);
const queries = ref(new URLSearchParams(query.value));

if (queries.value.has("q")) {
    search_term.value = queries.value.get("q");
}

const openSearch = () => (search_d.value = true);

const { callAllPosts, data } = getAllPosts();

const searchQuery = () => {
    if (search_term.value == "") {
        search_d.value = false;
        return;
    }

    query_string.value = search_term.value.replace(/ /g, "+");

    window.location.href = `${routes.value.search}?q=${query_string.value}`;
};

const onRequest = async () => {
    // let query = ref(window.location.search); // get query string

    // let queries = ref(new URLSearchParams(query.value)); //get all query params
    // // console.log(queries.value.get("q"));
    // let q_param = queries.value.has("q") ? queries.value.get("q") : "";
    if (search_term.value == "") {
        results.value.data = [];
        results.value.style.height = "0px";
        return;
    }

    await callAllPosts({ query: search_term.value });

    console.log(data.value);
    results.value.data = data.value.results;
    results.value.style.height = "500px";
};

// watch(data, () => {
// if (Object.keys(data.value).length) {
//     blogs.value = data.value.results;
//     pagination.value.totalNumberOfPages = parseInt(data.value.num_pages);
// }
// console.log(data.value);
// });

defineExpose({
    openSearch,
});
</script>

<style>
</style>
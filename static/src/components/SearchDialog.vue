<template>
    <q-dialog v-model="search_d" position="top">
        <q-card class="q-px-sm search_card">
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
                <q-scroll-area :style="results.style">
                    <transition
                        appear
                        enter-active-class="animated fadeIn"
                        leave-active-class="animated fadeOut"
                    >
                        <div v-show="results.data.length">
                            <div
                                class="q-mb-sm"
                                v-for="res in results.data"
                                :key="res.id"
                            >
                                <news-card
                                    :title="res.title"
                                    :excerpt="res.excerpt"
                                    :subtitle="'by John Doe'"
                                    horizontal
                                    :inSearchDialog="true"
                                    :imageSrc="res.image"
                                    :url="res.url"
                                />
                            </div>
                        </div>
                    </transition>
                </q-scroll-area>
                <q-inner-loading :showing="results.loading">
                    <q-spinner-pie size="50px" color="primary" />
                </q-inner-loading>
            </q-card-section>
        </q-card>
    </q-dialog>
</template>

<script setup>
import { inject, ref, watch } from "vue";
import getAllPosts from "../composables/getAllPosts";
import NewsCard from "../components/NewsCard.vue";
import { useQuasar } from "quasar";
import removeDuplicates from "../composables/removeDuplicate";
const routes = inject("routes");
const $q = useQuasar();

const search_term = ref("");
const search_d = ref(false);
const query_string = ref();
const searchCardStyle = ref({
    minWidth: "300px",
    maxHeight: "700px",
});
const results = ref({
    data: [],
    style: {
        height: "0px",
    },
    loading: false,
});

const query = ref(window.location.search);
const queries = ref(new URLSearchParams(query.value));

// console.log(queries.value.get("q"));

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

    // query_string.value = search_term.value.replace(/[ \/:?]/g, "+");
    query_string.value = search_term.value.replace(/[ \/:?;,@\&=\+\$]/g, "+");
    query_string.value = removeDuplicates(query_string.value);
    console.log(query_string.value);

    window.location.href = `${routes.value.search}?q=${query_string.value}`;
    // window.location.replace(`${routes.value.search}?q=${query_string.value}`);
};

const onRequest = async () => {
    query_string.value = encodeURIComponent(search_term.value);

    results.value.loading = true;
    if (search_term.value == "") {
        results.value.loading = false;
    } else {
        await callAllPosts({ query: search_term.value });
    }

    if (!data.value.results?.length || search_term.value == "") {
        results.value.data = [];
        results.value.style.height = "0px";
        return;
    }

    if (data.value.results.length) {
        // console.log(data.value);
        results.value.style.height = "500px";
        results.value.data = await data.value.results;
        results.value.loading = false;
    }
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

<style lang="sass">
.search_card
    min-width: 300px
    max-height: 600px

    @media (min-width: $breakpoint-sm-min)
        min-width: 500px
</style>
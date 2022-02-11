<template>
    <Base>
        <template #page_content>
            <section class="row justify-center q-my-lg">
                <!-- {{ data.num_pages }} -->
                <q-pagination
                    dense
                    boundary-numbers
                    :max-pages="6"
                    :direction-links="$q.screen.gt.xs"
                    :boundary-links="$q.screen.gt.xs"
                    :size="$q.screen.lt.md ? '12px' : 'md'"
                    v-model="pagination.page"
                    @update:model-value="onRequest"
                    :max="pagination.totalNumberOfPages"
                    icon-first="skip_previous"
                    icon-last="skip_next"
                    icon-prev="fast_rewind"
                    icon-next="fast_forward"
                />
            </section>
            <section
                class="row q-mx-auto q-px-md q-col-gutter-md q-my-xl"
                style="max-width: 1440px"
            >
                <div class="col-xs-12 col-md-9 col-lg-10">
                    <div class="row q-col-gutter-sm">
                        <div
                            class="col-xs-12 col-sm-6 col-md-4 col-lg-3"
                            v-for="blog in blogs"
                            :key="blog.id"
                        >
                            <!-- <a :href="blog.url" class="card_link"> -->
                            <news-card
                                :title="blog.title"
                                :body="blog.body"
                                :imageSrc="blog.image"
                                subtitle="By John Doe"
                                :url="blog.url"
                            />
                            <!-- </a> -->
                        </div>
                    </div>
                </div>
                <div class="col-xs-12 col-md-3 col-lg-2">
                    <div class="side_bar">
                        <sidebar />
                    </div>
                </div>
            </section>
            <section class="row justify-center q-my-lg">
                <q-pagination
                    dense
                    boundary-numbers
                    :max-pages="6"
                    :direction-links="$q.screen.gt.xs"
                    :boundary-links="$q.screen.gt.xs"
                    :size="$q.screen.lt.md ? '12px' : 'md'"
                    v-model="pagination.page"
                    @update:model-value="onRequest"
                    :max="pagination.totalNumberOfPages"
                    icon-first="skip_previous"
                    icon-last="skip_next"
                    icon-prev="fast_rewind"
                    icon-next="fast_forward"
                />
            </section>
        </template>
    </Base>
</template>

<script setup>
import { ref } from "@vue/reactivity";
import { onBeforeMount, onMounted, watch } from "@vue/runtime-core";
import Base from "../../components/layouts/Base.vue";
import NewsCard from "../../components/NewsCard.vue";
import getAllPosts from "../../composables/getAllPosts";
import Sidebar from "../../components/blog/Sidebar.vue";
import { useQuasar } from "quasar";

const $q = useQuasar();

const pagination = ref({
    sortBy: "created_at",
    // descending: true,
    page: 1,
    // rowsPerPage: 2,
    rowsNumber: 0,
    totalNumberOfPages: 0,
});

const currentPage = ref(2);

const { callAllPosts, data } = getAllPosts();
const blogs = ref([]);

watch(data, () => {
    if (Object.keys(data.value).length) {
        blogs.value = data.value.results;
        pagination.value.totalNumberOfPages = parseInt(data.value.num_pages);
    }
});
onBeforeMount(async () => {
    await callAllPosts();
});

const pageLink = (page) => {
    return `${window.location.href}?page=${page}`;
};

const onRequest = async (props) => {
    await callAllPosts(props);
};
</script>

<style lang="sass">
.side_bar
    position: sticky
    top: 15px
</style>
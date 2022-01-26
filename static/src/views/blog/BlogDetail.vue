<template>
    <Base>
        <template #page_content>
            <div class="q-pa-md">
                <q-btn
                    label="Go back"
                    color="secondary"
                    text-color="dark"
                    type="a"
                    :href="backUrl"
                />
            </div>
            <div class="row q-mx-auto q-col-gutter-md q-px-xl">
                <div class="col-xs-12 col-md-9">
                    <div class="">
                        <section>
                            <h1 class="text-h1">
                                {{ post.title }}
                            </h1>
                        </section>

                        <section>
                            <div>
                                <q-img height="400px" :src="post.image" />
                            </div>
                            <q-separator spaced="16px" />
                            <div class="row q-gutter-md">
                                <q-avatar class="">
                                    <img
                                        src="https://cdn.quasar.dev/img/avatar.png"
                                    />
                                </q-avatar>
                                <div>
                                    <div class="text-body1">
                                        {{ post?.author?.username }}
                                    </div>
                                    <div class="text-caption text-grey-7">
                                        {{ date_created }}
                                    </div>
                                </div>
                            </div>
                            <q-separator spaced="16px" />
                        </section>

                        <section v-html="post.body"></section>
                    </div>
                    <q-separator spaced="16px" />
                    <div>
                        <section>
                            <related />
                        </section>
                    </div>
                </div>
                <div class="col-xs-12 col-md-3">
                    <div class="side_bar">
                        <sidebar />
                    </div>
                </div>
            </div>
        </template>
    </Base>
</template>

<script setup>
import Base from "../../components/layouts/Base.vue";
import Related from "../../components/blog/Related.vue";
import Sidebar from "../../components/blog/Sidebar.vue";
import getPostDetail from "../../composables/getPostDetail";
import { onBeforeMount, ref, watch } from "@vue/runtime-core";
import { date } from "quasar";

const { callPostDetail, post } = getPostDetail();
onBeforeMount(() => {
    callPostDetail();
});

const date_created = ref("");
const date_format = ref("");
const backUrl = document.referrer;

watch(post, () => {
    if (post.value.created_at) {
        date_format.value = new Date(post.value.created_at);

        date_created.value = date.formatDate(
            date_format.value,
            "MMMM Do, YYYY"
        );
    }
});
</script>

<style>
</style>